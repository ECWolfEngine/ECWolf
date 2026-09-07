.. decorate-actor-header:: FireBall

Overview
--------

The :class:`fake Hitler <FakeHitler>` flamethrower fireball.

Adaptive speed bug
~~~~~~~~~~~~~~~~~~

In the original version of the game this actor was glitched by only performing the movement during the state change. This resulted in the fireball moving up to 6 times slower than it was supposed to. This bug would not have been easily noticed by the developers at the time since computers weren't capable of reaching a high enough frame rate for it to make a significant difference. (The original game accounted for dropped frames in the movement function.)

This bug has been fixed by restoring the intended speed since keeping the original behavior would result in non-deterministic behavior (critical for network/demo sync) or render the game much easier than intended. It is, however, easily possible to set the speed to whatever the user prefers by loading a decorate file with the following contents:

.. code:: DECORATE

	actor SlowFireball : FireBall replaces FireBall
	{
		// Set this to some value between 1.5 to 9 at your preference
		speed 1.5
	}

.. decorate-actor-footer:: FireBall
