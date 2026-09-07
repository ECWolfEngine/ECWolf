A_ChangeVelocity
================

.. action:: A_ChangeVelocity

	Adds a given velocity vector to a projectile.

	:param x: X velocity to add.
	:param y: Y velocity to add.
	:param z: Z velocity to add. Currently unsupported and should always be 0.
	:param flags: Modifies the behavior of the function.

		- .. constant:: CVF_RELATIVE

			Specifies velocities relative to the direction of travel.

		- .. constant:: CVF_REPLACE

			Set the absolute velocity instead of relative.
