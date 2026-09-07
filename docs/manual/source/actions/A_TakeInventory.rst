A_TakeInventory
===============

.. action:: A_TakeInventory

	Removes a given amount of the an :class:`inventory <Inventory>` item from the calling actor's inventory. Use :action:`A_GiveInventory` to give items.

	:param type: Item to take.
	:param amount: The maximum amount of the item to take (can be less if the caller isn't holding enough).
