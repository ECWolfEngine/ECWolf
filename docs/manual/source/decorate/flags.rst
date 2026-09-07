.. index:: Actor flags

.. _Actor flags:

Actor flags
===========

The following flags will modify the behavior of DECORATE actors in certain ways. If the flag name matches one in ZDoom it is generally safe to assume that the behavior will be similar to that flag in ZDoom.

Physics
-------

.. flag:: DONTRIP

	Ripping projectiles upon hitting this actor will act like a non-ripping projectile and die.

.. flag:: SHOOTABLE

	The actor can be damaged by attacks.

.. flag:: SOLID

	The actor is solid and should block other actors from moving through it.

Behavior
--------

.. flag:: AMBUSH

	The actor does not respond to sounds and instead waits for the player to come in line of sight.

.. flag:: DROPBASEDONTARGET

    Instead of dropping every item in the dropitem list, drop one item based on if the item is present in the target's inventory.

.. flag:: OLDRANDOMCHASE

	Modifies :action:`A_Chase` to use the old random number generator table. This flag was added since the number of times a typical Wolfenstein monster calls :action:`A_Chase` will frequently cycle through the 256-entry random table causing a noticeable difference in aggressiveness at long distances. In general it is preferable to use the new random number generator.

(In)abilities
-------------

.. flag:: CANUSEWALLS

	The monster can active doors. Unlike ZDoom, monsters can open locked doors by default.

.. flag:: REQUIREKEYS

	The monster needs to have keys in their inventory to open a locked door.

Appearance
----------

.. flag:: BILLBOARD

	Disables sprite billboarding. The flag name is backwards. Also known as "directional 3D sprites."

.. flag:: BRIGHT

	Treats all states as having the bright flag set.

.. flag:: RANDOMIZE

	For monsters this will randomize the first frame to any duration up to what is specified. For projectiles this randomizes the death frame as well with both randomizations cutting up to 3 tics.

Projectile
----------

.. flag:: MISSILE

	The actor is a projectile. The actor will move based on its speed automatically, die on collision, etc.

.. flag:: RIPPER

	Projectile can rip through actors.

Miscellaneous
-------------

.. flag:: ALWAYSFAST

	A monster with this flag will always attempt to attack when :action:`A_Chase` is called instead of taking a random number of steps.

.. flag:: COUNTITEM

	The actor is tallied for treasure.

.. flag:: COUNTKILL

	The actor counts as a kill.

.. flag:: COUNTSECRET

	The actor should be consider a secret tally.

.. flag:: ISMONSTER

	The actor should be considered a monster.

.. flag:: PICKUP

	The actor can pick up inventory items by walking over them.

.. flag:: PLOTONAUTOMAP

	The actor is shown on the automap without needing the debug function.

Additional flags
================

The following actor classes have additional flags available through inheritance.

* :class:`Inventory`
* :class:`Weapon`
