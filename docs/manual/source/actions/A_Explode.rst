A_Explode
=========

.. action:: A_Explode

	Deals damage to all actors within a given radius of the caller. Damage drops off linearly.

	:param damage: Amount of damage to deal.
	:param radius: Radius of the explosion.
	:param flags: Modifies the behavior of the function based on the following:

		- .. constant:: XF_HURTSOURCE

			Allows the explosion to damage the actor that is the source of the explosion. This would be the actor that fired the projectile and not the caller.

	:param alert: Allows the explosion to wake up nearby enemies.
	:param fulldamageradius: Radius in which to deal the full damage amount before linear fall off applies.
