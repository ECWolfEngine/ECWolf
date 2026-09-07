.. include:: /_templates/roles.rst

.. index:: Actor states

.. _Actor states:

Actor states
============

Actor states are the frames of animation used to define the behavior of an actor in :ref:`DECORATE`.

.. _Actor states syntax:

Usage
-----

The states are defined in the states block. Each state has the following syntax.

.. code::

	[StateLabel:]
		sprite frames duration [attributes] [action [ticker]]
		[control flow]

StateLabel
	A state label is name given to the state immediately following. These are used to define jump points in the animation. Some labels are used for various purposes within the engine. Multiple state labels may be assigned to a single state.

sprite
	Four character code that corresponds to the sprite to display for the state. ``TNT1`` can be used if no sprite is desired.

frames
	Frame letter to use for the state. As a shortcut, multiple frames can be specified. They will be expanded to consecutive states differing only in the frame letter.

duration
	How many tics (1/35th of a second) the state should be held. Half durations are allowed since Wolfenstein has a 70hz tic rate. A duration of -1 is defined as infinite.

	Durations can also be specified in the form of :expr:`random(min, max)` in which case the duration will vary between the specified values. Although this looks like the random function available in expressions, min and max here must be literal constant values.

attributes
	Optional modifiers.

	- **Bright**
		Specifies the frame should be rendered as full bright.

	- **Offset**\ (x, y)
		Gives the state an offset. Used by weapon player sprites. Note that values of 0 for either argument is interpreted as "keep previous offset."

action and ticker
	Code pointers to execute. The action function is executed at the start of the state (before it is displayed). The ticker function is executed at the end of every tic (will not be executed on states with a 0 duration). If only the ticker function is desired then ``NOP`` can be used in place of the action function.

	These code pointers can either be :ref:`action functions <Action functions>` or :ref:`action specials <Action specials>`.

Control flow
~~~~~~~~~~~~

By default each state continues on to the state immediately following. This can be changed to any of the following:

**goto** StateLabel[+offset]
	Jumps to the specified state label with an optional offset. Note that this is resolved statically so if the label is redefined in a child actor, this will still goto the label in this actor (not the child). :action:`A_Jump` can be used if dynamic resolution is desired.

**loop**
	Jumps to the last defined state label.

**wait**
	Repeats the previously defined state indefinitely. Used for functions like :action:`A_Raise` where they are expected to jump after a certain period of time. Note that if multiple frames are given this will wait at the last frame.

**stop**
	Removes the actor from the game. Additionally a state label immediately followed by stop undefines that label.

States
------

The following state labels are automatically used for various purposes by the engine.

**Spawn**
	The initial state for all actors entering the game.

**Path**
	Used in place of the Spawn state when the actor is set to follow a path.

**See**
	Used when the actor should be chasing its target (usually the player).

**Melee**
	Defines a melee range attack.

**Missile**
	Defines a long range attack.

**Pain**
	Randomly used when an actor is attacked based on the PainChance.

**Death**
	Jumped to when the actor reaches 0 health or when a projectile hits a wall.

**XDeath**
	Jumped to when an actor reaches a significantly negative amount of health or when a projectile hits an actor.

See also
--------

* :zd:`Actor states` on the ZDoom wiki.
