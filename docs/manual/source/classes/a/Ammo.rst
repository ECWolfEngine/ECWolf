.. decorate-actor-header:: Ammo

Overview
--------

This actor defines ammo types. Any actor inheriting directly from this class is a new ammo type. Inheriting from that ammo type creates an alternate pickup for that ammo (usually varying capacity).

Properties
~~~~~~~~~~

.. property:: Ammo.BackpackAmount amount

	Amount of the item to be supplied when picking up a backpack.

.. property:: Ammo.BackpackBoostAmount amount

	How much the backpack should boost the item's capacity.

.. property:: Ammo.BackpackMaxAmount amount

	Maximum amount of this item that backpacks can boost it to.

.. decorate-actor-footer:: Ammo
