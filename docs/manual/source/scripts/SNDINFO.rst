.. index:: SNDINFO

.. _SNDINFO:

SNDINFO
=======

SNDINFO is a lump used to assign certain properties to sounds. Sounds are referenced by their logical name and not their lump name so this lump is primarily used to assign logical names.

Logical names
-------------

To assign a logical name to a sound lump all you need to do is specify the logical name followed by the lump name of the sound. Wolfenstein has three types of sounds. Digital, AdLib, and PC Speaker sounds. If the sound you wish to use is only of the digital type then just specifying the two names will work. Otherwise you must enclose the lumps in braces and in the before mentioned order. ``NULL`` can be used where a sound of that type does not exist. If the PC speaker sound does not exist it may be left out.

.. code:: SNDINFO

	misc/mynewsound    MYSND // This is a digital-only sound
	misc/myadlibsound  { NULL MYALSND } // This sound only has an AdLib form.
	msic/mypcspkrsound { NULL NULL MYPCSND } // This sound only has a PC Speaker form.

Commands
--------

SNDINFO also supports a few commands to create sounds with certain properties.

**$alias** *logicalname* *othersound*
	Creates a logical sound that is indentical to the othersound.

**$random** *logicalname* { *othersound* *...* }
	Creates a logical sound that randomly plays one sound from the list.
