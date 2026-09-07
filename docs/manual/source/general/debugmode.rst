.. index:: Debug mode, Cheat codes

.. _Debug mode:

Debug mode
==========

The debug mode, or cheat codes as they may be known, can be enabled by pressing shift+alt+backspace during game play. Unlike vanilla, the -goobers or -debugmode parameter is no longer required to access debug mode.

The codes described below are those supported by |project|. Some codes were removed since they are no longer relevant or weren't able to be translated to the new structures. Some of these codes were reassigned for other purposes.

For all of these codes, tab can be substituted with grave (``\```) or backspace. This is needed if you assigned some function, such as automap toggle, to tab.

Commands
--------

.. list-table::
	:stub-columns: 1

	* - tab+b
	  - Changes the status bar border texture to the lump specified.
	* - tab+c
	  - Counts the number of actors present in the level.
	* - tab+d
	  - Toggles the on screen fps counter.
	* - tab+e
	  - Triggers Exit_Normal to exit the level.
	* - tab+f
	  - Gives the coordinates of the player as well as the angle. Full coordinates are given so divide by 64 and truncate to get the tile.
	* - tab+g
	  - Toggles god mode. On second use the red damage flash is disabled.
	* - tab+h
	  - Deals 16 points of damage to the player.
	* - tab+i
	  - Gives all weapons, ammo, full health, and 100,000 points.
	* - tab+k
	  - Gives keys based on the lock number in LOCKDEFS.
	* - tab+l
	  - Prints the level statistics (kill ratio, secret ratio, treasure ratio, time).
	* - tab+m
	  - Enables experimental mouse look.
	* - tab+n
	  - Toggles no clipping.
	* - tab+o
	  - Reveal the full overhead map.
	* - tab+p
	  - Takes a screen shot.
	* - tab+q
	  - Quits the game.
	* - tab+s
	  - Enables slow motion.
	* - tab+t
	  - Disables enemy targeting by sight or sound.
	* - tab+v
	  - Sets the extravbls parameter (which basically makes the engine wait some time before rendering the next frame).
	* - tab+w
	  - Warps to a level based on either the levelnum in MAPINFO or the level marker name (MAP01-MAP60, etc).
	* - tab+x
	  - Gives an Inventory item.
	* - tab+z
	  - Spawns the given actor in front of the player.
