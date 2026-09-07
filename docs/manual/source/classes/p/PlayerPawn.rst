.. decorate-actor-header:: PlayerPawn

Overview
--------

Base class for defining a player class. To add a custom player class to the menu it needs to be specified in :ref:`MAPINFO`. In addition the player class must have a unique :prop:`player.displayname`.

Properties
~~~~~~~~~~

.. property:: Player.DamageScreenColor color

	Color which will be used when player takes damage. Darker shade of it is used with fizzle fade death type.

	.. versionadded:: 1.4

.. property:: Player.DisplayName name

	Name to show on the class selection screen. Must be unique.

.. property:: Player.ForwardMove scale[, run-scale]

	Scales the forward/backward movement speed. Moving backwards will still be scaled by 2/3.

.. property:: Player.MaxHealth amount

	Maximum health the class has.

.. property:: Player.MoveBob factor

	Multiplies the strength of the movement bob by the given factor.

.. property:: Player.SideMove scale[, run-scale]

	Scales the strafe speed for the player.

.. property:: Player.StartItem classname[, amount]

	Specifies an inventory item to give to the player initially. For ammo an amount can also be specified.

.. property:: Player.ViewHeight height

	Sets the player's viewheight relative to the ground.

.. property:: Player.WeaponSlot slotnum, classname[, ...]

	Sets the default weapon slot assignment for the class.

.. decorate-actor-footer:: PlayerPawn
