A_MeleeAttack
=============

.. action:: A_MeleeAttack

	Performs a melee attack on the target.

	.. note:: This function is different from the deprecated A_MeleeAttack in ZDoom.

	:param damage: Amount of damage to deal. Not multiplied by any factor.
	:param accuracy: Probability from 0.0 to 1.0 that the attack will succeed.
	:param hitsound: Sound that will be played if the attack makes contact.
	:param misssound: Sound that will be played if the attack misses. Will use hitsound if not specified.
