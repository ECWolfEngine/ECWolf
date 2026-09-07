.. _Engine quirks:

Engine quirks
=============

This article is a place to document interesting oddities and quirks of the Wolfenstein 3D game engine.

General
-------

Enemy pathing
~~~~~~~~~~~~~

The AI generally tries to move in a straight line towards the player, dealing with the limitation of only being able to move to the center of tiles. When the player is out of sight the AI needs to make an attempt to walk around walls. The way this is supposed to be done is by having the enemy move in a "random" direction and then try to get to the player from their new position. At the end of ``SelectChaseDir`` this is done, but regardless of the result of the random number generator the enemy will only ever try to go north, nortwest, or west. If the AI is observed from the other side of a wall one can see triangular movement from the east or south, but wall hugging from the west or north.

*Resolution:* Currently preserved.

Determinism
-----------

The Wolfenstein 3D game engine, not being designed for multiplayer, has many examples of indeterministic code. While indeterminism is a primary reason that multiplayer is not a trivial add to the vanilla engine, the way that the Wolfenstein 3D engine adapts to lower frame rates results in changes in game play with ranging severity.

Adaptive frame rate compensation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to handle frame rate fluctuations without changing the speed of the game play, the Wolfenstein 3D engine calculates the number of 1/70 second moments that have passed in ``CalcTics`` into the variable tics. This value is used as a multiplier in various places. For example in ``T_Projectile`` the movement distance of the projectile is multiplied by this value, or in ``T_Chase`` the chance of something happening is multiplied by this value, or even in the case of ``ghostobj`` in ``MoveObj`` (Pac-Man ghosts or spectres) multiplies damage delt. The former example could in theory manifest itself in collision detection errors since movement collision is only calculated instantaneously rather than as a continuous motion. The latter has a host of implications due to the uneven distribution of the random number generator in addition to changing the number of and order of calls to the RNG.

These issues are to some extent mitigated by a ``MAXTICS`` constant which limits frame rate compensation to 10 tics or 7fps. If the frame rate drops below 7fps the game will slow down instead.

*Resolution:* Similar to how Doom works, the play sim is now rerun for the number of tics that passed rather than multiplied out. What vanilla did was either done because it seemed like an obvious way to do it at the time, or as a deliberate optimization to reduce the number of operations required on slower computers.

Demo playback
~~~~~~~~~~~~~

Demos in Wolfenstein 3D consist of a recording of the state of controller input for each tic of the game. In order for the demo to playback correctly determinism is required, but the engine does not meet this precondition when the frame rate fluctuates. To work around this issue the frame rate is locked, via ``PollControls``, to 17.5fps (70/4) while recording and playback which presumably was determined to be a typically obtainable frame rate.

Due to this it is probably reasonable to believe that the game was designed for the behavior seen around 17.5fps.

*Resolution:* Play sim rate is unlocked from frame rate and set to 70Hz.

Fake Hitler fireballs
~~~~~~~~~~~~~~~~~~~~~

Probably the most well known frame rate dependent quirk in Wolfenstein 3D is the speed of the fake Hitler :class:`fireballs <FireBall>`. In a seemingly contradictory fashion, the fireballs slow down as the frame rate of the game increases (until the 70fps vsync is hit).

This is caused by the adaptive frame rate compensation method combined with a typo whereby ``s_fire1`` and ``s_fire2`` have ``T_Projectile`` as their action function (executed on frame transition) rather than ticker function (executed "every tic"). As the frame rate increases the value of tics, which is used as a multiplier, goes down to a constant value of 1. The result is ``T_Projectile`` is effectively executed a sixth as many times as it is supposed to be.

*Resolution:* Bug is fixed so speed is ``0x1200`` as stated in ``T_FakeFire``. This is the speed that vanilla would have at about 12.6fps or lower and should be fairly similar to the speed at 17.5fps, but doesn't require making up an arbitrary value.

Physics
-------

Enemy positioning
~~~~~~~~~~~~~~~~~

The AI in Wolfenstein 3D is based on tiles. Enemies pick a tile they wish to move to through functions like ``SelectChaseDir`` which look for an unoccupied adjacent tile and claim it as their tilex and tiley. When claimed, the enemy is actually immediately considered in that location for movement collision and the position in which their sprite is located is freed. ``T_Chase`` and similar functions make these calls only when the destination tile is reached, so once a position is selected the enemy is obligated to reach that position even if they pause to shoot at the player.

Due to the freeing of space when a new tile is selected, other enemies are able to choose that space which means that if they stop to shoot multiple enemies can appear to occupy the same space. While this affects the physical location of the actor, shot hit detection is based on the sprite location (viewx), which is based on the actors x and y.

*Resolution:* Behavior is intentionally preserved, although implementation details differ.

Enemy radius
~~~~~~~~~~~~

Enemy AI in Wolfenstein 3D is entirely tile based, and one benefit of this decision is that collision is dramatically simplified to the point where AI movement only need to concern itself with where the player might be. To do this the center of the actor is measured against the center of the player to be no less than ``MINACTORDIST``, which is one full tile (``0x10000``), or 64 pixels. Comparing to the radius of the player given in ``PLAYERSIZE``, aka ``MINDIST``, or 22 pixels (``0x5800``), we see that the radius (perhaps more accurately the apothem) of the enemies is 42 pixels. This makes them larger than a tile so the only reason they can move at all is because there is no collision detection in the AI.

In some instances this means that the player can feel for enemies around corners as a guard flanking an opening will stop the player from moving if they happen to be tracing that side.

*Resolution:* Behavior is intentionally preserved.

Item pickup
~~~~~~~~~~~

In Wolfenstein 3D, the player can not pick up items while moving backwards. This is because the check for pickup collision is done while rendering the 3D scene. ``DrawScaleds`` calls out to ``TransformTile`` which calculates scaling information for the sprite, but also determines if the sprite is within "getting distance." This happens to be defined as within a tile in front of the player and a half tile to either side, but the important part is that only objects which are visible will ever have this check performed.

*Resolution:* While this was fixed in Wolf4SDL by changing how ``TransformTile`` handles off screen items, the check has been moved out of the renderer to actor movement.

Player hit detection
~~~~~~~~~~~~~~~~~~~~

Player weapons use the function GunAttack to deal damage. The way this works is actually done via feedback from the 3D renderer. Objects that are visible on screen are flagged with ``FL_VISIBLE`` and those that are ``FL_SHOOTABLE`` are compared to find the closest shootable actor using the distance calculated during rendition in transx.

While using rendering information for play sim is bad for determinism, the interesting part of this is that the horizontal range or spread is determined by ``shootdelta`` which is compared against the on screen center X coordinate of the sprites viewx. The value of the shootdelta global as set by ``SetViewSize`` is a tenth of the ``viewwidth`` which is the width of the 3D view port. The 3D view port has a horizontal field of view of 90 degrees which is setup in ``CalcProjection``, making the shootable space a cone of approximately +/- 9 degrees from center which due to round off varies slightly by screen size.

Since the center of the target sprite needs to be in that cone, there is an interesting side effect in that enemies become harder to hit the closer they are to the player. This even applies to ``KnifeAttack``.

*Resolution:* To prevent indeterminism the search is changed to an actual +/- 9 degree range rather than using renderer information. Otherwise behavior is preserved.

Projectile radius
~~~~~~~~~~~~~~~~~

Given the limited scope of Wolfenstein 3D the engine was designed with a limited concept of object radius. Furthermore, being designed for single player and without player weapons firing projectiles the engine is only concerned about collision with walls (for the purposes of this discussion, this includes statics) and the player. Confusingly there are two similarly named constants for the size of a projectile. For walls ``PROJSIZE`` (``0x2000``) is used and for the player ``PROJECTILESIZE`` (``0xc000``) is used. The former is the minimum distance from the center of the projectile to the wall, about 8 pixels.

The latter is the minimum distance between the center of the projectile to the center of the player, about 48 pixels. From other instances of player collision in ``TryMove`` we see that a player must be ``PLAYERSIZE``, aka ``MINDIST``, from a wall (``0x5800`` or 22 pixels). Based on this we see that for player collisions the a projectile has a radius of 26 pixels.

*Resolution:* Currently an arbitrary size between the two is picked, but this may be preserved to some extent in a future version.

Pushwalls move three spaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~

There is a typo in ``MovePWalls`` that results in pushwalls sometimes moving up to three spaces instead of only up to two. The likelihood of this event happening increases with frame rate and always occurs if 70fps is reached. The issue is that the counter used to measure pushwall movement pwallstate is supposed to end at 256 (two tiles), but is only checked as the pushwall transitions between two tiles. Since the end condition was written as "greater than 256" instead of "greater than or equal to 256", if the value of ``tics`` is just right and the tile transition happens at exactly 256 the pushwall will move one more tile before the counter is checked again.

This bug is well known so many maps are designed to cope with pushwalls that move either distance, but it could render some maps unwinnable, or in some cases the three space movement is unfortunately depended upon.

*Resolution:* Bug was fixed by Wolf4SDL so the pushwalls always move two spaces. Some vanilla mods took advantage of this bug and a custom :ref:`map translator <Map translator>` can be made to change the pushwall movement range to three spaces.

Data formats
------------

The following quirks have no effect on the player, but have in some way been abused by popular editor developers. These are documented here for the purposes of noting that otherwise valid assumptions can not be made about the game data formats.

Pic table size
~~~~~~~~~~~~~~

The size of the pic table in the VGAGRAPH (which determines the dimensions of 2D graphics) is hard coded as ``NUMPICS`` even though this could be determined by looking at the size of the pic table chunk in the container. For the standard game data and most editors the size is written correctly even though it's unused by the game engine. This is convenient for anyone that want to read VGAGRAPH files generically without predetermined knowledge of the contents. ChaosEdit, however, writes garbage for the size.

*Resolution:* The size of the pic table is determined heuristically by looking for unreasonable image sizes to indicate the end.

Third map plane
~~~~~~~~~~~~~~~

All maps in Wolfenstein 3D consist of three planes of 64x64 16-bit integers. The game, however, only uses the first two. The third is loaded into memory, but not used. For mods it is common to use this plane to assign floor and ceiling textures, and Rise of the Triad used it for meta data (things like triggers and z-axis information). Conveniently this plane is zero filled in the original game data making it only about 10 bytes per level of wasted disk space and most editors follow this convention.

ChaosEdit has other plans though and presumably in an effort to save every byte possible, reuses the pointer for the second plane as the third plane data which effectively means anything that assumes it's safe to use the third map plane at all times will be fed garbage data. It would be possible to reuse a single zero filled plane for every map in a set so this ultimately only saves 10 bytes.

*Resolution:* Maps with shared second and third planes are detected and the third plane is zero filled.
