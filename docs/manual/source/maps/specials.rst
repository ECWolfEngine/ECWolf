.. index:: Action specials

.. _Action specials:

Action specials
===============

Action specials are function which are activated either by :ref:`UWMF trigggers` or :ref:`DECORATE` actions.

General notes:

Tags
	Arbitrary numbers used to link a trigger to the tile that executes it.

Speeds
	Represented in the number of pixels traveled per tic/16. Wolf3D runs at 70 tics per second.

Directions
	Relative to the triggering side or absolute if the 8 is added. **Note that diagonal movement is not supported yet**

	* 0 - Right
	* 1 - Back Right
	* 2 - Back
	* 3 - Back Left
	* 4 - Left
	* 5 - Towards Left
	* 6 - Towards
	* 7 - Towards Right
	* 8 - East
	* 9 - Northeast
	* 10 - North
	* 11 - Northwest
	* 12 - West
	* 13 - Southwest
	* 14 - South
	* 15 - Southeast

List of action specials
-----------------------

.. special:: Door_Open
	:num: 1

	Activates a map spot as a sliding door.

	:param tag: The tag of the map spot which houses the door.
	:param speed: Rate at which door animates. Typical speed for a Wolf3D door is 16.
	:param delay: Tics until the door closes. 300 is normal for a Wolf3D door. -1 means the door will stay open until manually closed.
	:param lock: Lock specifies what keys are needed according to :ref:`LOCKDEFS`. For Wolfenstein 3D: 0 = None, 1 = Gold, 2 = Silver, 101 = Gold + Silver
	:param type: Whether the door is facing east-west (0), north-south (1), east-west double door (2), or north-south double door (3).

.. special:: Pushwall_Move
	:num: 2

	Moves the pushwall in the trigger's map spot.

	:param tag: The tag of the map spot.
	:param speed: Rate at which the wall moves. Typical speed for a Wolf3D pushwall is 8.
	:param direction: The direction to move. See the general notes about how directions are specified.
	:param distance: The distance in tiles to move. A value of 0 means the map tile will move until it is blocked by something.

.. special:: Exit_Normal
	:num: 3

	Exits the level using the standard exit.

	:param pos: Reserved and should be 0.

.. special:: Exit_Secret
	:num: 4

	Exits the level using the secret exit.

	:param pos: Reserved and should be 0.

.. special:: Teleport_NewMap
	:num: 5

	Exits and travels to the specified map by levelnum.

	:param map: The levelnum to travel to.
	:param pos: Reserved and should be 0.
	:param flags: 1 = Keep direction, 2 = Keep position.

.. special:: Exit_VictorySpin
	:num: 6

	Standard exit but does a BJ jump sequence. Normally activated by a pickup. This sequence is partially handled by the :class:`BJRun` actor which is spawned.

.. special:: Exit_Victory
	:num: 7

	Exits the level using the victory exit.

	:param pos: Reserved and should be 0.

.. special:: Trigger_Execute
	:num: 8

	Executes all triggers on a given map spot. Useful for activating something on monster death or having multiple switches do the same thing.

	:param x: The X coordinate of the tile.
	:param y: The Y coordinate of the tile.
	:param z: The Z coordinate of the tile.

.. special:: StartConversation
	:num: 9

	This is an experimental function for starting a :ref:`USDF` dialog. Not very useful with current implementation. Documented here for completeness.

	:param tid: The tag for the thing to converse with.
	:param faceTalker: If set to 1 the player will face the talking actor.

.. special:: Door_Elevator
	:num: 10

	Similar to :special:`Door_Open` in every manner except that the tag should point to the elevator switch.

	:param switchTag: The tag of the elevator switch map spot.
	:param speed: Rate at which door animates.
	:param delay: Tics until the door closes.
	:param lock: Lock specifies what keys are needed.
	:param type: Door direction and style.

.. special:: Elevator_SwitchFloor
	:num: 11

	.. note:: Elevator support is somewhat experimental and may be missing a few features. Changes may occur in order to improve compatibility with Rise of the Triad.

	Triggers the elevator movement. Things in the elevator are moved relative to the switch and the door.

	:param elevTag: The tag of the first switch in the sequence.
	:param doorTag: The tag of the door for this stop.
	:param callSpeed: The time it takes for the elevator to move to or from this floor.
	:param nextTag: The tag for the next switch in the sequence.

.. special:: Pushwall_MoveNoStop
	:num: 12

	The same as :special:`Pushwall_Move` except that the pushwall can not be blocked from moving.

	:param tag: The tag of the map spot.
	:param speed: Rate at which the wall moves.
	:param direction: The direction to move.
	:param distance: The distance in tiles to move.

.. special:: Teleport_Relative
	:num: 13

	Teleports the activator such that their position from the destination spot is the same as the distance to the activated tile. Effectively works the same as :special:`Elevator_SwitchFloor` without the theatrics.

	:param tag: The tag of the map spot to teleport relative to.
	:param angle: Angle offset to apply (0-255).
	:param flags: Modifies the behavior of the special.

		- .. constant:: TELEPORT_NoStop
			:value: 1

			The activator's velocity is preserved after the teleport.

		- .. constant:: TELEPORT_NoFog
			:value: 2

			Disables spawning of the teleport fog effect.

		- .. constant:: TELEPORT_Center
			:value: 4

			Centers the actor to the destination tile.

		- .. constant:: TELEPORT_AbsoluteAngle
			:value: 8

			Treats the angle argument as an absolute value instead of relative.

		- .. constant:: TELEPORT_ActivationAngle
			:value: 16

			Face the actor towards the actviation tile. Typically would be combined with the absolute angle flag.
