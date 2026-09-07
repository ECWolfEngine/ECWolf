A_GunAttack
===========

.. action:: A_GunAttack
	:class: Weapon

	Performs a standard player attack similar to :action:`A_WolfAttack`. Deals damage to the closest shootable enemy in front of the player in a 9 degree cone.

	:param flags: Modifies the behavior of the function.

		- .. constant:: GAF_MACDAMAGE

			Changes the point blank damage fall off to be half rather than 2/3.

		- .. constant:: GAF_NOAMMO

			Disables drawing from the weapon's ammo.

		- .. constant:: GAF_NORANDOM

			Disables damage randomization.

	:param sound: Sound to play for this attack. The default uses the weapon's :prop:`attack sound <attacksound>`.
	:param snipe: Factor to multiply distance calculations by (smaller values are more accurate).
	:param maxdamage: The amount of damage the attack does. Maximum of 256 without :const:`GAF_NORANDOM`.
	:param blocksize: Size of a map block. This defaults to 128 to account for the scale of Doom 2's Wolf3D maps.
	:param pointblank: Number of blocks for which the damage is done in full. After which the damage is multiplied by 2/3.
	:param longrange: Number of blocks after which accuracy is lost. The attack will have a distance/maxrange chance of failing.
	:param maxrange: Maximum number of blocks an attack can travel.

