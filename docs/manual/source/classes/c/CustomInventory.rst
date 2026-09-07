.. include:: /_templates/roles.rst

.. decorate-actor-header:: CustomInventory

Overview
--------

Defines an :class:`Inventory` item which has custom behavior given by DECORATE state sequences. Currently only the Pickup state is supported. This state is executed by the player when the item is picked up.

Note that executed states are only used for their action pointers. The delay and sprite are ignored so it is recommended that you use :state:`TNT1 A 0` for each.

.. decorate-actor-footer:: CustomInventory
