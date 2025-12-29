import docutils.transforms
import docutils.nodes
import docutils.parsers.rst
import re
import sphinx.addnodes
import sphinx.builders
import sphinx.directives
import sphinx.domains
import sphinx.environment
import sphinx.roles
import sphinx.util.nodes
import typing
import zdirective.parse_decorate

def identifier_to_target(name: str) -> str:
	return name.lower().replace('_','-')

class DecorateActionFunctionObject(sphinx.directives.ObjectDescription[str]):
	doc_field_types = [
		sphinx.util.docfields.TypedField(
			'parameter',
			label='Parameters',
			names=('param',),
			typerolename='class',
			typenames=('type',),
			can_collapse=True
		)
	]

	option_spec = {
		**sphinx.directives.ObjectDescription[str].option_spec,
		'class': docutils.parsers.rst.directives.unchanged,
	}

	def _lookup_action_function(self, name: str) -> zdirective.parse_decorate.DecorateAction|None:
		if cls := zdirective.parse_decorate.get_class(self.options.get('class', 'Actor')):
			return cls.action_functions.get(name.lower())
		return None

	def add_target_and_index(self, name: str, sig: str, signode: docutils.nodes.TextElement):
		target = identifier_to_target(name)
		if target not in self.state.document.ids:
			signode['ids'].append(target)
			self.state.document.note_explicit_target(signode)

		domain = typing.cast(DecorateDomain, self.env.get_domain('decorate'))
		domain.note_object('action', name, self.env.docname, target)

		self.indexnode['entries'].append(('single', f'Action functions; {name}', target, '', None))

	def transform_content(self, content_node: sphinx.addnodes.desc_content):
		cls_name = self.options.get('class', 'Actor')
		# Add restriction note if applicable
		if cls_name != 'Actor':
			nodes = self.parse_text_to_nodes(f'This action function is restricted to :class:`{cls_name}` and derived classes.')
			print(f'nodes[{type(nodes)}] = {nodes}')
			content_node += nodes

		# Auto populate the types of parameters from the parsed prototype
		field_list_index = content_node.first_child_matching_class(docutils.nodes.field_list)
		if field_list_index is None:
			return
		field_list = content_node.children[field_list_index]

		cls = zdirective.parse_decorate.get_class(cls_name)
		action = self._lookup_action_function(self.names[0])
		if not action:
			return

		for param in action.parameters:
			field = docutils.nodes.field()
			field.append(docutils.nodes.field_name('', f'type {param.name}'))
			field.append(docutils.nodes.field_body('', docutils.nodes.paragraph('', param.type)))
			field_list.insert(0, field)

	def handle_signature(self, sig: str, signode: docutils.nodes.TextElement) -> str:
		signode.append(sphinx.addnodes.desc_name(sig, sig))

		if action := self._lookup_action_function(sig):
			signode.append(action.make_parameter_list())

		return sig

class DecorateConstantObject(sphinx.directives.ObjectDescription[str]):
	def add_target_and_index(self, name: str, sig: str, signode: docutils.nodes.TextElement):
		target = f'const:{identifier_to_target(name)}'
		if target not in self.state.document.ids:
			signode['ids'].append(target)
			self.state.document.note_explicit_target(signode)

		domain = typing.cast(DecorateDomain, self.env.get_domain('decorate'))
		domain.note_object('const', name, self.env.docname, target)

		self.indexnode['entries'].append(('single', f'Constants; {name}', target, '', None))

	def handle_signature(self, sig: str, signode: docutils.nodes.TextElement) -> str:
		signode.append(sphinx.addnodes.desc_name(sig, sig))
		return sig

class DecorateFlagObject(sphinx.directives.ObjectDescription[str]):
	def add_target_and_index(self, name: str, sig: str, signode: docutils.nodes.TextElement):
		target = f'flag:{identifier_to_target(name)}'
		if target not in self.state.document.ids:
			signode['ids'].append(target)
			self.state.document.note_explicit_target(signode)

		domain = typing.cast(DecorateDomain, self.env.get_domain('decorate'))
		domain.note_object('flag', name, self.env.docname, target)

		self.indexnode['entries'].append(('single', f'Actor flags; {name}', target, '', None))

	def handle_signature(self, sig: str, signode: docutils.nodes.TextElement) -> str:
		signode.append(sphinx.addnodes.desc_name(sig, sig))
		return sig

# Subclass so markup extension/module can detect the property parameter list
class DecoratePropertyParameterList(sphinx.addnodes.desc_parameterlist):
	pass

class DecoratePropertyObject(sphinx.directives.ObjectDescription[str]):
	doc_field_types = [
		sphinx.util.docfields.TypedField(
			'parameter',
			label='Parameters',
			names=('param',),
			typerolename='class',
			typenames=('type',),
			can_collapse=True
		)
	]

	def add_target_and_index(self, name: str, sig: str, signode: docutils.nodes.TextElement):
		target = f'prop:{identifier_to_target(name)}'
		if target not in self.state.document.ids:
			signode['ids'].append(target)
			self.state.document.note_explicit_target(signode)

		domain = typing.cast(DecorateDomain, self.env.get_domain('decorate'))
		domain.note_object('prop', name, self.env.docname, target)

		self.indexnode['entries'].append(('single', f'Actor properties; {name}', target, '', None))

	def handle_signature(self, sig: str, signode: docutils.nodes.TextElement) -> str:
		match = re.match(r'([\w.]+)\s*(.*)', sig)
		name = match.group(1)
		signode.append(sphinx.addnodes.desc_name(sig, name))

		if parameter_list_sig := match.group(2):
			parameter_list = DecoratePropertyParameterList(parameter_list_sig, '')
			while req_param := re.match(r'([\w\-]+),?\s*', parameter_list_sig):
				# Consume parameter
				parameter_list_sig = parameter_list_sig[len(req_param.group(0)):]
				parameter_list.append(sphinx.addnodes.desc_parameter(req_param.group(0), req_param.group(1)))

			opt_tail = None
			while opt_param := re.match(r'\[,?\s*([\w\-]+)\s*(.*)\]$', parameter_list_sig):
				parameter_list_sig = opt_param.group(2)
				opt = sphinx.addnodes.desc_optional()
				opt.append(sphinx.addnodes.desc_parameter(opt_param.group(1), opt_param.group(1)))

				if opt_tail:
					opt_tail.append(opt)
				else:
					parameter_list.append(opt)
				opt_tail = opt

			if re.match(r'\[?,?\s*\.\.\.\]?', parameter_list_sig):
				variadic = sphinx.addnodes.desc_sig_punctuation('...', '…')
				if opt_tail:
					opt_tail.append(variadic)
				else:
					parameter_list.append(variadic)

			signode.append(sphinx.addnodes.desc_sig_space())
			signode.append(parameter_list)

		return name

class DecorateXRefRole(sphinx.roles.XRefRole):
	def process_link(self, env: sphinx.environment.BuildEnvironment, refnode: docutils.nodes.Element, has_explicit_title: bool, title: str, target: str) -> tuple[str, str]:
		prefix = refnode['reftype']

		if prefix == 'action':
			return (title, identifier_to_target(target))

		if prefix == 'class':
			prefix = 'classes'
		return (title, f'{prefix}:{identifier_to_target(target)}')

class DecorateDomain(sphinx.domains.Domain):
	name = 'decorate'
	label = 'DECORATE'

	object_types = {
		'action': sphinx.domains.ObjType('action function', 'action'),
		'class': sphinx.domains.ObjType('class', 'class'),
		'const': sphinx.domains.ObjType('constant', 'const'),
		'flag': sphinx.domains.ObjType('flag', 'flag'),
		'func': sphinx.domains.ObjType('function', 'func'),
		'prop': sphinx.domains.ObjType('property', 'prop'),
		'special': sphinx.domains.ObjType('action special', 'special'),
	}

	directives = {
		'action': DecorateActionFunctionObject,
		'constant': DecorateConstantObject,
		'flag': DecorateFlagObject,
		'property': DecoratePropertyObject,
	}

	roles = {
		'action': DecorateXRefRole(),
		'class': DecorateXRefRole(),
		'const': DecorateXRefRole(),
		'flag': DecorateXRefRole(),
		'func': DecorateXRefRole(),
		'prop': DecorateXRefRole(),
		'special': DecorateXRefRole(), # Not really a DECORATE thing, but good place to put this
	}

	initial_data = {
		'objects': {}
	}

	def note_object(self, typ: str, name: str, docname: str, targetid: str):
		self.data['objects'][targetid] = docname

	def resolve_xref(self, env: sphinx.environment.BuildEnvironment, fromdocname: str, builder: sphinx.builders.Builder, typ: str, target: str, node: sphinx.addnodes.pending_xref, contnode: docutils.nodes.Element) -> docutils.nodes.reference|None:
		if not (todocname := self.data['objects'].get(target)):
			return None

		# Don't bother linking to self (will still highlight)
		if todocname == fromdocname:
			return None

		# Last argument is title for tooltip
		return sphinx.util.nodes.make_refnode(builder, fromdocname, todocname, target, contnode, None)

class AutoXRefTransform(docutils.transforms.Transform):
	"""
	Scans for dedicated pages for object types in our domains and builds xref
	targets so roles work automatically.
	"""

	default_priority = 210

	typ_map = {
		'classes': 'class'
	}

	def apply(self):
		docname = self.document.settings.env.docname.split('/')
		if len(docname) < 2:
			return
		typ, name = docname[0], docname[-1]
		if typ not in self.typ_map:
			return

		targetid = f'{typ}:{identifier_to_target(name)}'
		targetnode = docutils.nodes.target('', '', ids=[targetid], names=[targetid])

		insert_index = 0
		while isinstance(self.document[insert_index], docutils.nodes.field_list):
			insert_index += 1

		self.document.note_explicit_target(targetnode)
		self.document.insert(insert_index, targetnode)

		domain = typing.cast(DecorateDomain, self.document.settings.env.get_domain('decorate'))
		domain.note_object(self.typ_map[typ], name, self.document.settings.env.docname, targetid)
