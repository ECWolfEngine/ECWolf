A_CustomMissile
===============

.. action:: A_CustomMissile

	Spawns the specified monster projectile aimed towards the target. Note that this function does not automatically call :action:`A_FaceTarget`, so the monster may face a different direction than the projectile is fired.

	:param missiletype: Actor to spawn.
	:param spawnheight: The height from the ground to spawn the projectile. This is currently ignored and should always be 32.
	:param spawnoffset: The horizontal offset that the projectile is fired from.
	:param angle: The relative angle in which to fire.
	:param aimflags: Changes the behavor of the function.

		- .. constant:: CMF_AIMOFFSET

			The projectile is aimed as if it had an offset of 0. Useful for firing projectiles to multiple locations.
