.. decorate-actor-header:: Weapon

Overview
--------

This is the base class for all weapons.

Flags
~~~~~

.. flag:: WEAPON.ALWAYSGRIN

	By default the grin will only happen the first time a weapon is picked up. This flag forces the grin.

.. flag:: WEAPON.DONTBOB

	Disables weapon bobing for this weapon. (Note that this does not disable view movement bob.)

.. flag:: WEAPON.NOALERT

	Prevents weapon attacks from alerting the monsters.

.. flag:: WEAPON.NOAUTOFIRE

	The weapon will not fire when :action:`A_WeaponReady` is reached and the fire key is held down.

.. flag:: WEAPON.NOGRIN

	Disables the grin animation when picking up this weapon.

Properties
~~~~~~~~~~

.. property:: Weapon.AmmoGive1 amount

	Amount of primary ammo to give when picking up the weapon.

.. property:: Weapon.AmmoGive2 amount

	Amount of secondary ammo to give when picking up the weapon.

.. property:: Weapon.AmmoType1 classname

	The primary ammo type to use for this weapon.

.. property:: Weapon.AmmoType2 classname

	The secondary ammo type to use for this weapon.

.. property:: Weapon.AmmoUse1 amount

	The amount of ammo to use when firing this weapon.

.. property:: Weapon.AmmoUse2 amount

	The amount of ammo to use when alternate firing this weapon.

.. property:: Weapon.BobRangeX amount

	Range multiplier for horizontal bobbing. Default is 1.0.

.. property:: Weapon.BobRangeY amount

	Range multiplier for vertical bobbing. Default is 1.0.

.. property:: Weapon.BobSpeed amount

	Bobbing speed multiplier. Affects how quickly the bobbing motion occurs. Default is 1.0.

.. property:: Weapon.BobStyle style

	The type of bobbing to use. Possible values include Normal, Inverse, Alpha, InverseAlpha, Smooth, and InverseSmooth.

	* Normal is the default value and corresponds to the bobbing motion used in all old Doom-engine games.
	* Alpha is the bobbing motion used in the alpha versions of Doom. The weapon sprites are raised when bobbing, not lowered, so they might get cut off if they do not extend enough past the screen.
	* Smooth is a smoother version of the normal style.
	* Inverse\* types mirror the motion vertically compared to the non-inverse version. InverseAlpha lowers the weapon sprite while bobbing; the others raise it.

.. property:: Weapon.SelectionOrder value

	The priority of this weapon when performing auto selections when running out of ammo. Lower numbers are higher priority.

.. property:: Weapon.SlotNumber slotnum

	Assigns this weapon to a slot for all classes.

.. property:: Weapon.SlotPriority value

	Decimal value which specifies where to place the weapon in the slot. 0 for the beginning, 1 for the end.

.. property:: Weapon.YAdjust amount

	Amount of shift the weapon sprite when the hud is off. Positive values shift the sprite down.

.. decorate-actor-footer:: Weapon
