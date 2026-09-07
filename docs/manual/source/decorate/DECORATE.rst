.. index:: DECORATE

.. _DECORATE:

DECORATE
========

DECORATE is a text actor defintion language based upon the language from ZDoom. DECORATE allows you to define many things such as monsters, decorations, key, and weapons.

Syntax
------

The general format of a DECORATE script looks like this:

.. parsed-literal::

	**actor** name [: parent] [**replaces** otheractor] [ednum]
	{
		:ref:`properties <Actor properties>`
		+/-:ref:`flags <Actor flags>`
		**states**
		{
			:ref:`states <Actor states syntax>`
		}
	}

Refer to the :ref:`actor states <Actor states>` page for the syntax for the states block.

The *ednum* field is deprecated as all places where they were used previously have been changed to accept the actor names directly. They will appear in code fragments in this documentation, as backwards compatibility for old mods has not yet been removed, but new mods should always omit them.

Inheritance
-----------

Inheritance is a concept in DECORATE whereby a new :class:`actor <Actor>` - the child - may inherit its behaviour from another actor, the parent. When a child inherits from a parent it takes all of the defined :ref:`states <Actor states>`, :ref:`properties <Actor properties>`, and :ref:`flags <Actor flags>` of the parent. These behaviours may then be overridden as required.

In order to inherit from a parent, the child actor defines its DECORATE definition in the following way:

.. code:: DECORATE

	actor ChildActor : ParentActor
	{
		// ...
	}

Inheritance is used in a number of cases where objects share similar basic behaviours. One example of this is the use of :class:`WolfensteinMonster` as a parent class for all :ref:`Wolfenstein-style enemies <A_Chase calling conventions>` in the game.

Example
~~~~~~~

One example of this might be when we wish to create a new SS enemy that behaves just like the standard SS and uses the same graphics, except that it has twice as many hit points and gives the player twice as many points. This would be done in the following way:

.. code:: DECORATE

	actor NewSS : WolfensteinSS
	{
		points 1000
		health 200
	}

Additional topics
-----------------

.. toctree::

	classes
	flags
	functions
	properties
	states

See also
--------

* :zd:`DECORATE information on the ZDoom wiki <DECORATE>`
