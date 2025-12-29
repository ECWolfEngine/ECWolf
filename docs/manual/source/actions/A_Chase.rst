A_Chase
=======

.. action:: A_Chase

	Standard monster AI function. Moves the monster according to the speed property.

	:param melee: If set the monster will jump to the specified state when within the melee range of the target. Default is Melee.
	:param ranged: If set the monster will have a chance of jumping to the specified state to perform a ranged attack. Default is Missile.
	:param flags: Modifies the behavior of the function based on the following:

		- .. constant:: CHF_BACKOFF

			Causes the actor to run away from the player if it gets too close.

		- .. constant:: CHF_DONTDODGE

			Forces the actor to move orthogonally.

		- .. constant:: CHF_NOPLAYACTIVE

			Disables the random change of playing the active sound.

		- .. constant:: CHF_NOSIGHTCHECK

			Do not look for new targets.

Calling conventions
-------------------

This function is used in two different ways: Either as a ticker function or as an action function. These are known as Wolfenstein-style and Doom-style respectively. When used as a ticker function the monster will be far more aggressive and move faster, but will move more smoothly. It is recommended, but not required, that you inherit from :class:`WolfensteinMonster` if you use this method.

Wolfenstein style
~~~~~~~~~~~~~~~~~

.. code:: DECORATE

	actor ExampleGuard : WolfensteinMonster
	{
		speed 3
		states
		{
			/* ... snip ... */
			See:
				GARD ABCD 6 NOP A_Chase
				loop
		}
	}

Doom style
~~~~~~~~~~

.. code:: DECORATE

	actor ExampleGuard
	{
		speed 8
		states
		{
			/* ... snip ... */
			See:
				GARD AABBCCDD 3 A_Chase
				loop
		}
	}
