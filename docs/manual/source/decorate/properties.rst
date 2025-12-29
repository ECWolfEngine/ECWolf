.. include:: /_templates/roles.rst

Actor properties
================

Properties set various values regarding the behavior of a DECORATE actor. If a property has the same name as a ZDoom property the behavior should be assumed to be similar.

Behavior
--------

.. property:: Damage value

	Specifies the amount of damage the actor will do on impact. If the damage is given in parenthesis the value will be absolute. Otherwise, it will use the :expr:`value*random(1,8)`.

.. property:: GibHealth value

	The negative health threashold before the actor enters its extreme death state.

.. property:: Health value[, skill2 ...]

	Sets the number of hit points the actor has. If multiple health values are given the health will apply to the next successive skill level. Unspecified skills will use the next highest value. (In other words, if only skills 1 and 2 are given skill 3 will use the value for ``skill2``.)

.. property:: PainChance value

	The chance (out of 256, where 256 = Always) the actor will enter the Pain state when damaged.

.. property:: SightTime value[, random]

	The number of function calls (usually :action:`A_Look`) it takes for the actor to react to seeing the player. The random portion is the maximum number of tics to add to the base value.

.. property:: Speed value[, runspeed]

	The amount the actor moves in one Doom tic or one call to :action:`A_Chase`. The speed will be changed to runspeed when the actor sees the player.

Physics
-------

.. property:: Height value

	The height of the actor. This is ignored at the time, but should be set to 64 for all solid actors for forwards compatibility.

.. property:: Radius value

	The radius of the actor.

Attacks
-------

.. property:: MeleeRange value

	Gives the maximum distance from the center of the monster that a melee attack can reach.

.. property:: MinMissileChance value

	Gives the minimum chance (0-256) the monster has of not attacking when attempting to attack. Lower values are more aggressive.

.. property:: MissileFrequency value

	Gives a floating point multiplier for the missile chance curve. Higher values will make the monster attack more frequently over longer distances.

Sound
-----

.. property:: ActiveSound soundname

	Defines the sound to randomly play while the actor is active.

.. property:: AttackSound soundname

	Defines the sound to play when the actor attacks.

.. property:: DeathSound soundname

	Defines the sound to play when :action:`A_Scream` is called.

.. property:: PainSound soundname

	Defines the sound to play when :action:`A_Pain` is called.

.. property:: SecretDeathSound soundname

	Defines the alternative deathsound to play when the level requests it.

.. property:: SeeSound soundname

	Defines the sound to play when the actor sees the player.

Rendering
---------

.. property:: Scale value
              XScale value
              YScale value

	Defines scaling factors for the actor's sprite. Scale sets both xscale and yscale.

Special
-------

.. property:: OverheadIcon tile

	What overhead icon the actor should show on the automap. Typically tile will be a TILE8 lookup in the form of :expr:`"TILE:value".

.. property:: DropItem classname[, probability[, amount]]

	When an actor dies it will drop items based off this property. A probability can be specified (0-255) which indicates the liklihood of the item spawning. Amount is used for ammunition and indicates how much ammo the pickup should give.

.. property:: Points score

	Number of points to give to the target when the actor is killed or picked up.

Additional Properties
=====================

The following properties are restricted to a certain set of actors.

Inventory
---------

.. property:: Inventory.Amount amount

	Amount to give when picking up the inventory item.

.. property:: Inventory.Icon icon

	Icon to show in the players inventory. (Partially implemented)

.. property:: Inventory.InterHubAmount amount

	Amount to keep in the players inventory between hubs.

.. property:: Inventory.MaxAmount amount

	Maximum amount of this item the actor can carry at once.

.. property:: Ammo.BackpackAmount amount

	Amount of the item to be supplied when picking up a backpack.

.. property:: Ammo.BackpackBoostAmount amount

	How much the backpack should boost the item's capacity.

.. property:: Ammo.BackpackMaxAmount amount

	Maximum amount of this item that backpacks can boost it to.

.. property:: Inventory.PickupSound soundname

	Sound to play when picking up the item.

Player
------

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

Weapon
------

.. property:: Weapon.AmmoGive1 amount

	Amount of ammo to give when picking up the weapon.

.. property:: Weapon.AmmoType1 classname

	The ammo type to use for this weapon.

.. property:: Weapon.AmmoUse1 amount

	The amount of ammo to use when firing this weapon.

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

Flag combos
===========

These properties set a series of flags appropriate for a certain kind of actor.

.. property:: MONSTER

	* :flag:`CANUSEWALLS`
	* :flag:`COUNTKILL`
	* :flag:`ISMONSTER`
	* :flag:`SHOOTABLE`
	* :flag:`SOLID`

.. property:: PROJECTILE

	* :flag:`MISSILE`
