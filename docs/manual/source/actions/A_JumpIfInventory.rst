A_JumpIfInventory
=================

.. action:: A_JumpIfInventory

	The calling actor jumps to the specified state if the actor is carrying at least amount of the given item.

	:param type: Inventory item to check for.
	:param amount: Minimum amount required.
	:param frame: State to jump to.

Example
-------

.. code:: DECORATE

	// A pistol that reloads every 8 shots.
	// Requires a PistolFired actor derived from Inventory.
	actor ReloadingPistol : Pistol
	{
		states
		{
			Fire:
				PISG A 0 A_JumpIfInventory("PistolFired", 8, "LoadPistol")
				PISG B 3
				PISG C 3 Bright
				PISG D 3 A_GunAttack
				PISG E 3 A_GiveInventory("PistolFired", 1)
				goto ready
			LoadPistol:
				PISG F 3 //Reloading frames
				PISG G 3
				PISG H 3 A_TakeInventory("PistolFired", 8)
				goto ready
		}
	}
