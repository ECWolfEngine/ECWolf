.. include:: /_templates/roles.rst

A_FireCustomMissile
===================

.. action:: A_FireCustomMissile
	:class: Weapon

	Fire a player projectile, damaging enemies. Will not harm the player.

	:param missiletype: Actor to use as projectile.
	:param angle: Relative angle to fire the projectile in.
	:param useammo: Sets whether the attack uses ammo or not.
	:param spawnoffset: Horizontal offset of the attack.
	:param spawnheight: Vertical offset of the attack. Ignored for now, but should be set to the player class's :expr:`-(height/2 + 8)` in order to keep it spawning at the floor level in future versions.
	:param aim: Currently unimplemented. Keep default value of false.
	:param pitch: Pitch offset. Ignored for now, keep default value of 0.
