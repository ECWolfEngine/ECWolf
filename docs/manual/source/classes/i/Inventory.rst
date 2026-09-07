.. decorate-actor-header:: Inventory

Overview
--------

This is a base class which defines an actor as an inventory item. An inventory item is an actor which can be picked up by or given to the player and may be used for a variety of purposes including implementing counters.

One thing to remember is that all actors can hold inventory items, not just players.

Flags
~~~~~

.. flag:: INVENTORY.ALWAYSPICKUP

	This item is picked up even if the player has no use for it.

.. flag:: INVENTORY.AUTOACTIVATE

	Item is activated automatically when picked up. (Partially implemented)

.. flag:: INVENTORY.INVBAR

	Item is placed into the player's visible inventory when picked up. (Partially implemented)

Properties
~~~~~~~~~~

.. property:: Inventory.Amount amount

	Amount to give when picking up the inventory item.

.. property:: Inventory.Icon icon

	Icon to show in the players inventory. (Partially implemented)

.. property:: Inventory.InterHubAmount amount

	Amount to keep in the players inventory between hubs.

.. property:: Inventory.MaxAmount amount

	Maximum amount of this item the actor can carry at once.

.. property:: Inventory.PickupSound soundname

	Sound to play when picking up the item.

.. decorate-actor-footer:: Inventory
