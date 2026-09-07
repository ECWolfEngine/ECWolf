.. include:: /_templates/roles.rst

.. index:: Actor properties

.. _Actor properties:

Actor properties
================

Properties set various values regarding the behavior of a DECORATE actor. If a property has the same name as a ZDoom property the behavior should be assumed to be similar.

Behavior
--------

.. property:: Damage value

	Specifies the amount of damage the actor will do on impact. If the damage is given in parenthesis the value will be absolute. Otherwise, it will use the :expr:`value*random(1,8)`.

.. property:: GibHealth value

	The negative health threashold before the actor enters its extreme death state.

.. property:: Health value[, skill2 ...]

	Sets the number of hit points the actor has. If multiple health values are given the health will apply to the next successive skill level. Unspecified skills will use the next highest value. (In other words, if only skills 1 and 2 are given skill 3 will use the value for ``skill2``.)

.. property:: PainChance value

	The chance (out of 256, where 256 = Always) the actor will enter the Pain state when damaged.

.. property:: SightTime value[, random]

	The number of function calls (usually :action:`A_Look`) it takes for the actor to react to seeing the player. The random portion is the maximum number of tics to add to the base value.

.. property:: Speed value[, runspeed]

	The amount the actor moves in one Doom tic or one call to :action:`A_Chase`. The speed will be changed to runspeed when the actor sees the player.

Physics
-------

.. property:: Height value

	The height of the actor. This is ignored at the time, but should be set to 64 for all solid actors for forwards compatibility.

.. property:: ProjectilePassHeight value

	Height of the actor as it appears to projectiles. Currently this should be set to either the actor's height (default) or 0 to allow projectiles to pass through an otherwise solid actor.

.. property:: Radius value

	The radius of the actor.

Attacks
-------

.. property:: MeleeRange value

	Gives the maximum distance from the center of the monster that a melee attack can reach.

.. property:: MinMissileChance value

	Gives the minimum chance (0-256) the monster has of not attacking when attempting to attack. Lower values are more aggressive.

.. property:: MissileFrequency value

	Gives a floating point multiplier for the missile chance curve. Higher values will make the monster attack more frequently over longer distances.

Sound
-----

.. property:: ActiveSound soundname

	Defines the sound to randomly play while the actor is active.

.. property:: AttackSound soundname

	Defines the sound to play when the actor attacks.

.. property:: DeathSound soundname

	Defines the sound to play when :action:`A_Scream` is called.

.. property:: PainSound soundname

	Defines the sound to play when :action:`A_Pain` is called.

.. property:: SecretDeathSound soundname

	Defines the alternative deathsound to play when the level requests it.

.. property:: SeeSound soundname

	Defines the sound to play when the actor sees the player.

Rendering
---------

.. property:: Scale value
              XScale value
              YScale value

	Defines scaling factors for the actor's sprite. Scale sets both xscale and yscale.

Special
-------

.. property:: ConversationID value

	An ID that is used to bind conversation trees to the actor.

.. property:: OverheadIcon tile

	What overhead icon the actor should show on the automap. Typically tile will be a TILE8 lookup in the form of :expr:`"TILE:value"`.

.. property:: DropItem classname[, probability[, amount]]

	When an actor dies it will drop items based off this property. A probability can be specified (0-255) which indicates the liklihood of the item spawning. Amount is used for ammunition and indicates how much ammo the pickup should give.

.. property:: Points score

	Number of points to give to the target when the actor is killed or picked up.

Additional Properties
=====================

The following actor classes have additional properties available through inheritance.

* :class:`Ammo`
* :class:`Inventory`
* :class:`PlayerPawn`
* :class:`Weapon`

Flag combos
===========

These properties set a series of flags appropriate for a certain kind of actor.

.. property:: MONSTER

	* :flag:`CANUSEWALLS`
	* :flag:`COUNTKILL`
	* :flag:`ISMONSTER`
	* :flag:`SHOOTABLE`
	* :flag:`SOLID`

.. property:: PROJECTILE

	* :flag:`MISSILE`
