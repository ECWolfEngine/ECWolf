#
# __init__.py
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

import docutils.nodes
import sphinx.application
import sphinx.directives.code
import sphinx.util.docutils

import zdirective.domain
import zdirective.parse_decorate

class DecorateActorDirective(sphinx.util.docutils.SphinxDirective):
	"""
	Produces the source definition for a DECORATE actor.
	"""

	has_content = True
	required_arguments = 1

	def run(self) -> list[docutils.nodes.Node]:
		actor = zdirective.parse_decorate.get_class(self.arguments[0])
		code_block = sphinx.directives.code.CodeBlock('code', ['DECORATE'], {}, actor.source.splitlines(), self.lineno, self.content_offset, self.block_text, self.state, self.state_machine)
		return code_block.run()

class DecorateActorHeaderDirective(sphinx.util.docutils.SphinxDirective):
	"""
	Produces the common header for all actor pages.
	"""

	has_content = True
	required_arguments = 1

	def run(self) -> list[docutils.nodes.Node]:
		actor = zdirective.parse_decorate.get_class(self.arguments[0])

		children_list = '.. rst-class:: inheritance-tree\n\n'
		if actor.name != actor.parent:
			children_list += '\n'.join(f'- :class:`{actor.name}`' for actor in sorted(actor.resolve_children(), key=lambda actor: actor.name))
		else:
			children_list += '- All other actor classes'

		inheritance = ' → '.join(f':class:`{name}`' for name in actor.resolve_inheritance())

		content = (
			f':orphan:\n'
			f'\n'
			f'.. index::\n'
			f'	single: Classes; {actor.name}\n'
			f'\n'
			f'Classes:{actor.name}\n'
			f'========{'=' * len(actor.name)}\n'
			f'\n'
			f'.. include:: /_templates/class-header.rst\n'
			f'\n'
			f'{inheritance}\n\n'
			f'{children_list}\n'
			f'\n'
		)

		return self.parse_text_to_nodes(content, allow_section_headings=True)


class DecorateActorFooterDirective(sphinx.util.docutils.SphinxDirective):
	"""
	Produces the common footer for all actor pages.
	"""

	has_content = True
	required_arguments = 1

	def run(self) -> list[docutils.nodes.Node]:
		class_name = self.arguments[0]
		content = (
			f'DECORATE definition\n'
			f'-------------------\n'
			f'\n'
			f'.. decorate-actor:: {class_name}\n'
			f'\n'
		)

		return self.parse_text_to_nodes(content, allow_section_headings=True)

def setup(app: sphinx.application.Sphinx):
	app.add_domain(domain.DecorateDomain)

	app.add_transform(domain.AutoXRefTransform)

	app.add_directive('decorate-actor', DecorateActorDirective)
	app.add_directive('decorate-actor-footer', DecorateActorFooterDirective)
	app.add_directive('decorate-actor-header', DecorateActorHeaderDirective)

	app.connect('builder-inited', zdirective.parse_decorate.builder_inited)
