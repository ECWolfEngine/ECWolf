#
# parse_decorate.py
#
#---------------------------------------------------------------------------
# Copyright 2025 Braden Obrzut
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. The name of the author may not be used to endorse or promote products
#    derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
# NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
# THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#---------------------------------------------------------------------------
#
#

import collections.abc
import itertools
import os
import pathlib
import pygments.token
import sphinx.addnodes
import sphinx.application
import zpygments.decorate

class DecorateActor:
	def __init__(self, name: str, parent: str, source: str, action_functions: list['DecorateAction']):
		self.name = name
		self.parent = parent
		self.source = source
		self.action_functions = {action.name.lower(): action for action in action_functions}

	def resolve_children(self) -> list['DecorateActor']:
		global context

		children = []
		for actor in context.actors.values():
			if actor.parent == self.name:
				children.append(actor)
		return children

	def resolve_inheritance(self) -> list[str]:
		global context

		if self.name == self.parent:
			return [self.name]

		inheritance = [self.parent, self.name]
		while (actor := context.actors[inheritance[0]]).parent != actor.name:
			inheritance.insert(0, actor.parent)
		return inheritance

class DecorateAction:
	def __init__(self, scope: str, prototype: str, tokens: list[tuple[int, pygments.token.Token, str]]):
		self.scope = scope
		self.prototype = prototype
		self.name = ''
		self.parameters = []

		try:
			self._parse_tokens(iter(tokens))
		except StopIteration:
			pass

	def _parse_tokens(self, tokens: collections.abc.Iterable[tuple[int, pygments.token.Token, str]]):
		# Find start of parameters and grab function name
		while True:
			_, token_type, token = next(tokens)
			if token_type == pygments.token.Name.Function:
				self.name = token
			elif token_type == pygments.token.Punctuation and token == '(':
				break

		# Get parameter list
		sublevel = 1
		type_start = -1
		type_end = -1
		default_start = -1
		default_end = -1
		default_tokens = []
		param_name = ''
		while sublevel > 0:
			token_position, token_type, token = next(tokens)
			if type_start == -1: # Start of new parameter type?
				type_start = token_position

			if token_type == pygments.token.Punctuation:
				if sublevel == 1 and (token == ',' or token == ')'):
					if param_name:
						type_name = self.prototype[type_start:type_end]
						default_value = self.prototype[default_start:default_end] if default_start != -1 else None
						self.parameters.append(DecorateActionParameter(type_name, param_name, default_value, default_tokens))

					type_start = -1
					type_end = -1
					default_start = -1
					default_end = -1
					default_tokens = []
					param_name = ''

				if token == '(':
					sublevel += 1
				elif token == ')':
					sublevel -= 1
				elif sublevel == 1 and default_start == -1 and token == '=':
					token_position, token_type, token = next(tokens)
					default_start = token_position
					default_end = token_position+len(token)
					default_tokens.append((token_position-default_start, token_type, token))
			elif len(param_name) == 0 and token_type == pygments.token.Name.Variable:
				param_name = token
			else:
				if default_start != -1:
					default_end = token_position+len(token)
					default_tokens.append((token_position-default_start, token_type, token))
				elif len(param_name) == 0:
					type_end = token_position+len(token)

	def make_parameter_list(self) -> sphinx.addnodes.desc_parameterlist:
		"""
		Converts the pygments token stream into Sphinx signature parameter list
		nodes.
		"""

		param_list = sphinx.addnodes.desc_parameterlist()
		for param in self.parameters:
			param_node = sphinx.addnodes.desc_parameter('', param.name)
			param_node.insert(0, sphinx.addnodes.desc_sig_name('', param.type))
			param_node.insert(1, sphinx.addnodes.desc_sig_space())
			param_list.append(param_node)
			if not param.default:
				continue

			param_node.append(sphinx.addnodes.desc_sig_operator('', '='))
			for _, token_type, token in param.default_tokens:
				match token_type:
					case pygments.token.Operator:
						param_node.append(sphinx.addnodes.desc_sig_operator('', token))
					case pygments.token.Punctuation:
						param_node.append(sphinx.addnodes.desc_sig_punctuation('', token))
					case (pygments.token.Number | pygments.token.Number.Bin |
						pygments.token.Number.Float | pygments.token.Number.Hex |
						pygments.token.Number.Integer | pygments.token.Number.Integer.Long |
						pygments.token.Number.Oct):
						param_node.append(sphinx.addnodes.desc_sig_literal_number('', token))
					case pygments.token.String:
						param_node.append(sphinx.addnodes.desc_sig_literal_string('', token))
					case _:
						param_node.append(sphinx.addnodes.desc_inline('decorate', '', token))

		return param_list

class DecorateActionParameter:
	def __init__(self, type: str, name: str, default: str|None, default_tokens: list[tuple[int, pygments.token.Token, str]]):
		self.type = type
		self.name = name
		self.default = default
		self.default_tokens = default_tokens

class DecorateContext:
	"""
	Builds lookup tables for relevant parts of DECORATE code based on the
    pygments token stream.
	"""

	lexer = zpygments.decorate.DecorateLexer()

	def __init__(self, root: str, file_name: str):
		self.root = pathlib.PurePath(root)
		self.file_name = pathlib.PurePath(os.path.relpath(os.path.normpath(os.path.join('/', file_name)), start='/'))

		self.actors = {}

		try:
			with open(self.root / self.file_name) as f:
				self.content = f.read()
				[self.tokens] = itertools.tee(filter(lambda tuple: tuple[1] != pygments.token.Whitespace, self.lexer.get_tokens_unprocessed(self.content)), 1)

				self.parse()
		except FileNotFoundError as e:
			print(f'Could not read DECORATE source file: {e}')

	def merge(self, subcontext: 'DecorateContext'):
		self.actors.update(subcontext.actors)

	def next_string(self):
		[tokens] = itertools.tee(self.tokens, 1)
		_, token_type, token = next(tokens)
		assert token_type == pygments.token.String and token == '"'

		result = ""
		try:
			while True:
				prev = tokens
				_, token_type, token = next(tokens)
				if token_type != pygments.token.String:
					tokens = prev
					break
				if token == '"':
					break
				result += token
		except StopIteration:
			pass

		self.tokens = tokens
		return result

	def parse(self):
		while True:
			try:
				token_position, token_type, token = next(self.tokens)
			except StopIteration:
				break

			if token_type == pygments.token.Comment.Preproc and token == '#include':
				include_file_name = self.next_string()
				subcontext = DecorateContext(self.root, self.file_name.parent / include_file_name)
				self.merge(subcontext)
				continue

			if token_type == pygments.token.Keyword and token == 'const':
				self.parse_constant()
				continue

			if token_type == pygments.token.Keyword and token == 'actor':
				self.parse_actor(token_position)
				continue

	def parse_actor(self, start_position: int):
		_, token_type, token = next(self.tokens)
		assert token_type == pygments.token.Name.Class
		actor_name = token
		parent_name = 'Actor'

		action_functions = []

		sublevel = 0
		while True:
			token_position, token_type, token = next(self.tokens)
			if token_type == pygments.token.Punctuation:
				if token == '{':
					sublevel += 1
				elif token == '}':
					sublevel -= 1
					if sublevel == 0:
						break

				# Find parent
				if sublevel == 0 and token == ':':
					token_position, token_type, token = next(self.tokens)
					if token_type == pygments.token.Name.Class:
						parent_name = token

			# Find action functions
			if sublevel == 1 and token_type == pygments.token.Keyword and token == 'action':
				action_prototype_start = token_position
				action_tokens = [(token_position-action_prototype_start, token_type, token)]
				while True:
					token_position, token_type, token = next(self.tokens)
					action_tokens.append((token_position-action_prototype_start, token_type, token))
					if token_type == pygments.token.Punctuation and token == ';':
						break
				action_prototype = self.content[action_prototype_start:token_position+1]
				action_functions.append(DecorateAction(actor_name, action_prototype, action_tokens))

		self.actors[actor_name] = DecorateActor(actor_name, parent_name, self.content[start_position:token_position+1], action_functions)

	def parse_constant(self):
		while True:
			_, token_type, token = next(self.tokens)
			if token_type == pygments.token.Punctuation and token == ';':
				return

def builder_inited(app: sphinx.application.Sphinx):
	global context

	try:
		context = DecorateContext('../../wadsrc/static', 'decorate.txt')
	except FileNotFoundError as e:
		print(f'Could not read DECORATE source file: {e}')

	# Ensure every actor class has a doc file
	for actor in context.actors.values():
		doc_file_name = f'source/classes/{actor.name[0].lower()}/{actor.name}.rst'
		pathlib.Path(doc_file_name).parent.mkdir(parents=True, exist_ok=True)
		if not os.path.exists(doc_file_name):
			with open(doc_file_name, 'w') as f:
				f.write(f'.. decorate-actor-header:: {actor.name}\n\n.. decorate-actor-footer:: {actor.name}\n')

def get_class(name: str) -> DecorateActor:
	return context.actors[name]
