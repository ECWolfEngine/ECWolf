A_SpawnItemEx
=============

.. action:: A_SpawnItemEx

	Spawns an actor of type at the location of the calling actor.

	:param type: Actor to spawn.
	:param xoffset: X offset to apply from the caller's position. Relative to the direction the actor is facing.
	:param yoffset: Y offset to apply from the caller's position. Relative to the direction the actor is facing.
	:param zoffset: Z offset to apply from the caller's position. Relative to the direction the actor is facing. Currently ignored and should be kept at 0.
	:param xvel: X velocity to apply to the spawned actor.
	:param yvel: Y velocity to apply to the spawned actor.
	:param zvel: Z velocity to apply to the spawned actor. Currently ignored and should be kept at 0.
	:param angle: Relative angle offset to apply the spawned actor.
	:param flags: Modifies the behavior of the function.

		- .. constant:: SXF_TRANSFERPOINTERS

			Transfers the target from the calling actor to the spawned actor.

	:param failchance: Probability from 0 to 256 that the actor will not spawn.
