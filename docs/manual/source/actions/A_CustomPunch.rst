A_CustomPunch
=============

.. action:: A_CustomPunch
	:class: Weapon

	Performs a player melee attack.

	:param damage: The amount of damage the attack will deal.
	:param norandom: If true the damage will not be multiplied by a random factor. By default it is multiplied by some number 1-8.
	:param flags: Changes the behavior of the function.

		- .. constant:: CPF_USEAMMO

			Draw from the weapon's ammo supply.

		- .. constant:: CPF_ALWAYSPLAYSOUND

			Play the :prop:`attack sound <attacksound>` even if nothing is hit.

	:param pufftype: Ignored for now. Will eventually default to BulletPuff.
	:param range: The range of the attack in map pixels.
	:param lifesteal: The factor of the amount of damage to give back to the calling actor.
