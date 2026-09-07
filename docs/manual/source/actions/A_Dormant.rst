A_Dormant
=========

.. action:: A_Dormant

	Jumps to a given state if there are no actors currently occupying the calling actor's position. When the jump happens, it sets the :flag:`AMBUSH`, :flag:`SHOOTABLE`, and :flag:`SOLID` flags while losing the target.

	:param frame: State to jump to.
	:param flags: Modifies the behavior of the function.

		.. constant:: DF_REVIVE

			Restores the actor's :prop:`health` when the jump occurs.
