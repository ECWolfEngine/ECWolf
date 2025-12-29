#
# __init__.py
#
#---------------------------------------------------------------------------
# Copyright 2023 Braden Obrzut
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
# This is an extremely gross hack reaching into all sorts of internal data
# structures and passing objects where they're not supposed to be. Uses a
# similar idea to the sphinx-codeautolink extension where the output from
# pygments is parsed to then insert a cross reference link.
#

from typing import Any
import re

import sphinx.application
import sphinx.builders
import sphinx.environment
import sphinx.errors

import docutils.nodes
import sphinx.addnodes
import sphinx.writers.html5

import docutils
import docutils.utils

pygment_span_re = re.compile(r'<span class="(\w+)">([\w.]+)</span>')

def identifier_to_target(name: str) -> str:
	return name.lower().replace('_','-')

# Intercept generation of HTML for highlighted code and insert xrefs
class HighlighterWrapper:
	app = None

	def __init__(self, builder: sphinx.environment.BuildEnvironment, underlying: sphinx.highlighting.PygmentsBridge, translator):
		self.builder = builder
		self.underlying = underlying
		self.translator = translator

	def _resolve_reference(self, symbol: str, ref_name: str, fromdocname: str) -> docutils.nodes.reference|None:
		node = sphinx.addnodes.pending_xref('', refexplicit=True, reftarget=ref_name)
		contnode = docutils.nodes.inline(symbol, symbol)
		node.append(contnode)

		if ref := self.app.env.domains['decorate'].resolve_xref(self.app.env, fromdocname, self.builder, 'ref', ref_name, node, contnode):
			return ref

		return self.app.env.domains.standard_domain.resolve_xref(self.app.env, fromdocname, self.builder, 'ref', ref_name, node, contnode)

	def highlight_block(self, source: str, lang: str, opts: dict | None = None, force: bool = False, location: Any = None, **kwargs: Any) -> str:
		html_source = self.underlying.highlight_block(source, lang, opts=opts, force=force, location=location, **kwargs)
		if lang not in {'DECORATE'}:
			return html_source

		# Hack in the cross reference links
		fromdocname = self.translator.builder.current_docname
		offset = 0
		for span in pygment_span_re.finditer(html_source):
			symbol_type = span.group(1)
			symbol = span.group(2)

			match symbol_type:
				case 'na':
					ref_name = f'flag:{identifier_to_target(symbol)}'
				case 'nc':
					ref_name = f'classes:{identifier_to_target(symbol)}'
				case 'nf':
					ref_name = identifier_to_target(symbol)
				case 'py':
					ref_name = f'prop:{identifier_to_target(symbol)}'
				case _:
					continue

			# Create refence node to re-use builtin translator to make HTML
			ref_node = self._resolve_reference(symbol, ref_name, fromdocname)
			if not ref_node:
				continue

			# HTML5Translator expects reference elements to have a parent
			parent_node = docutils.nodes.TextElement('', '')
			parent_node.append(ref_node)

			# We need a clone of the HTML5Translator that has an empty state
			translator = sphinx.writers.html5.HTML5Translator(self.translator.document, self.translator.builder)
			# Generate link HTML
			ref_node.walkabout(translator)
			link = ''.join(translator.body)

			# Substitute symbol with link
			html_source = html_source[:span.start(2) + offset] + link + html_source[span.end(2) + offset:]
			offset += len(link) - len(symbol)

		return html_source

# Intercept the code block translating process and insert our xref links
class XrefHTML5Translator(sphinx.writers.html5.HTML5Translator):
	def __init__(self, document, builder: sphinx.builders.Builder) -> None:
		super().__init__(document, builder)

		self.wrapped_highlighter = HighlighterWrapper(builder, self.highlighter, self)

	def visit_literal_block(self, node: docutils.nodes.Element) -> None:
		self.highlighter = self.wrapped_highlighter
		try:
			super().visit_literal_block(node)
			self.highlighter = self.wrapped_highlighter.underlying
			return
		except Exception:
			self.highlighter = self.wrapped_highlighter.underlying
			raise

	def visit_DecoratePropertyParameterList(self, node: docutils.nodes.Element) -> None:
		self._visit_sig_parameter_list(node, sphinx.addnodes.desc_parameter, '', '')
	def depart_DecoratePropertyParameterList(self, node: docutils.nodes.Element) -> None:
		self._depart_sig_parameter_list(node)

def setup(app: sphinx.application.Sphinx) -> None:
	# Let the highlighter interact with the app environment
	HighlighterWrapper.app = app

	# Override the HTML translator
	app.set_translator('html', XrefHTML5Translator, True)
