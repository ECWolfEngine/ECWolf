A_WolfAttack
============

.. action:: A_WolfAttack

	Executes a standard long range attack. There is no spread since the damage is dealt directly to the target actor after an accuracy roll and adjustments based on distance and velocity.

	:param flags: Modifies the behavor of the function.

		- .. constant:: WAF_NORANDOM

			Changes maxdamage to a constant damage.

	:param sound: Sound to play during the attack. The default value indicates the :prop:`attack sound <attacksound>` should be used.
	:param snipe: Multiplies the effective distance for calculations (smaller values are more accurate).
	:param maxdamage: The maximum damage this call can do (limited to 256 by technical limitations).
	:param blocksize: The number of half map pixels that are considered a block. This is accounting for ZDoom's scale which is based off Doom 2's oversized Wolf3D maps.
	:param pointblank: The number of blocks where the attack deals full damage. After which, the damage is halved.
	:param longrange: The number of blocks after which the damage is divided again.
	:param runspeed: Target speed after which accuracy is reduced.
