.. _Version compatibility:

Version compatibility
=====================

One of the main design goals of ECWolf is to allow easy mod authoring in a way that requires little programming knowledge. In turn it is reasonable to expect that future updates to the engine will not break released mods. While this will eventually be the case, **this is not true for the 1.x series**. Starting with ECWolf 2.0 backwards compatibility will be kept, but until then fixing issues takes priority. The main reason for this is because there are certain features that are currently only partially implemented and broken features should not get in the way of normal progress.

Forwards compatibility tips
---------------------------

While this is by no means a complete list, the following items will allow mods to be easily ported from one version to another by following upgrade directions posted here in the future.

* Whenever you are asked to provide a z-coordinate always use 0. Please note that this may not be the default value. Particularly when it comes to projectiles. If a specific value is given for a z-height elsewhere then use that instead.
* When you create a :flag:`SOLID` object, always give it a height of 64. (Again, this is not the default.)
* Inherit from :class:`WolfensteinMonster` when creating monster with Wolfenstein style definitions. (``NOP A_Chase``)

Upgrading mods
--------------

There are three categories of changes for upgrading mods.

**Critical**
	These changes cause ECWolf to reject the mod if not corrected.

**Major**
	These changes cause the mod to behave differently than in the previous version. ECWolf will still start, but gameplay may be drastically different than intended.

**Minor**
	These changes are recommended for best forwards compatibility, but do not cause any change in behavior from the previous version.

Upgrade to 1.4
~~~~~~~~~~~~~~

.. rubric:: Critical

* Additional actors from Macintosh Wolfenstein support or other experimental game support may conflict. Problematic actors will need to be renamed.

.. rubric:: Major

* Editor numbers are deprecated and replaced with using the actor class name in all relevant scripts. 1.4 retains backwards compatibility with editor numbers, but they will be removed in the future. Additionally if editor number overriding warnings produced in previous versions were ignored then there may be differences in behavior.

Upgrade to 1.3
~~~~~~~~~~~~~~

This version is mostly mod and save compatible with 1.2 if the mod followed all recommended practices.

.. rubric:: Critical

* Super 3D Noah's Ark support comes with a number of new actors. There is a chance that a mod may conflict with the actor names chosen and must be renamed.

.. rubric:: Minor

* The ``floornumber`` property for maps was changed to a string. This resulted in the level completed string being changed in :ref:`LANGUAGE`.

Upgrade to 1.2
~~~~~~~~~~~~~~

.. rubric:: Critical

* Due to the new ROTT style trigger system, some :ref:`action specials <Action specials>` have been changed. While this won't technically prevent ECWolf from loading the mod, it will be completely unplayable if a custom :ref:`map translator <Map translator>` was used.

  * :special:`Door_Open` arguments have been changed to (tag, speed, delay, lock, type) from (speed, lock, type).

    * Horizontal/Vertical is no longer determined by activation direction. This would not work right when activated by a switch. Instead the first bit of the type argument is used so 0 = horizontal, 1 = vertical. Obviously higher numbers are still reserved for other types of doors.
    * Delay should be set to 300 to be the same as before and specifies the number of tics the door will hold open.

  * :special:`Pushwall_Move` arguments have been changed to (tag, speed, direction, distance) from (speed, direction, distance)

    * Direction has been modified to include support for diagonal push walls. ECWolf does not yet support diagonal push walls, but this was done in preparation for when it's needed for ROTT support. As a result you need to multiply your direction by 2 (so move away from the activator is 2 instead of 1).

.. rubric:: Major

* Gatling gun pick up is now represented by :class:`GatlingGunUpgrade`. If you are using "replaces :class:`GatlingGun`" just use "replaces :class:`GatlingGunUpgrade`" instead.
* If you replace the :class:`BJRun` actor. It should call :special:`Exit_Victory` now instead of :special:`Exit_Normal` otherwise ECWolf will continue on to MAP10.
* Due to a bug in parsing, the boolean defaults in :action:`A_FireCustomMissile` and :action:`A_CustomPunch` may not have been set properly. This means A_FireCustomMissile uses ammo by default like it should have.
* :action:`A_FireCustomMissile` and :action:`A_CustomPunch` now make noise unless :flag:`WEAPON.NOALERT` is set.
* :prop:`player.viewheight` needs to be set to 32 unless you inherit from :class:`BJPlayer`.
* Palette property in :ref:`intermission definition <Intermission definition>` has been replaced with ZDoom compatible parameters in the background property.

.. rubric:: Minor (1.2.3 only)

* If inheriting from :class:`WolfensteinMonster` the :flag:`OLDRANDOMCHASE` flag has been set. This should be more or less harmless but the flag can be unset for the old behavior which uses a much better random number generator.

Upgrade to 1.1
~~~~~~~~~~~~~~

.. rubric:: Major

* If you define your monsters in Wolfenstein style (that's: ``NOP A_Chase``) then you will probably want to inherit from :class:`WolfensteinMonster`. There's nothing special about this actor other than it sets the defaults for these kind of monsters. If you don't either change your actor to reflect that actor, or inherit from it, your monster will change significantly in aggressiveness.
* If you inherited directly from :class:`Weapon` your weapon will now have Doom like bobbing. To fix add :flag:`WEAPON.DONTBOB`. (You can also inherit from :class:`WolfWeapon`, but this will carry other effects.)
* If you have a custom player class not inheriting from :class:`BJPlayer` it will also have movement bob. Add :prop:`player.movebob` 0 to correct.
* :prop:`Meleerange <meleerange>` now default to 44 if you don't inherit from :class:`WolfensteinMonster` (where it will be 42). This may seem like a small change, but the old behavior is to have the meleerange equal to the radius (42).
* The missilechance property has been removed. It is the same as :prop:`missilefrequency`, but missilefrequency takes a floating point value that is 0.005*missilechance.

.. rubric:: Minor

* Rename :const:`WAF_NORANDOM` to :const:`GAF_NORANDOM` if used with :class:`A_GunAttack`.
