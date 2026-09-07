.. decorate-actor-header:: WeaponGiver

Overview
--------

This is a base class for defining alternative weapon pickups. Only the spawn state is needed since the weapon specified by :prop:`DropItem <dropitem>` will be given instead. The first weapon on the list is considered the primary weapon and will determine what kind of ammo is given. Any other weapons in the DropItem list will be given as well, but not for ammo.

.. decorate-actor-footer:: WeaponGiver
