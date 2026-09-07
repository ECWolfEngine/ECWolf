.. index:: Art screens

.. _Art screens:

Art screens
===========

Art screens are used to provide an in game manual as well as provide story elements between clusters. They are simply specifically formatted text and do not have any specific naming convention, although the Read This screen is HELPART.

.. important:: Every art screen should start with a ``^P`` command to start the first page. If you don’t include a ``^P`` for the first page, then flipping back to previous pages might cause crashes or corrupted art screens to appear.

Commands
--------

A command is a letter prefixed with the caret character (``^``) possibly followed by some specific formatting. The following commands are recognized. Commands with *EOL* indicate they must be on a separate line.

**^;**\ <anything> *EOL*
	Comment

**^>**
    Indents the text 160 pixels.

**^B**\ <x> <y> <w> <h> *EOL*
    Create a black rectangle with the specified dimensions.

**^C**\ <index>
    Sets the font to a stencil mode with the color specified by palette index. Not recommended for use.

**^C**\ [<textcolor>]
    Sets the font to a color specified in :ref:`TEXTCOLO`. This will retain font shading.

**^E**
    Ends page and the art script.

**^G**\ <y> <x> <index>
    Draws an image by an art index specified in :ref:`TEXTURES`. Not recommended for use.

**^G**\ <y> <x> [<texture>]
    Draws an image in the specified location by texture name.

**^L**\ <y> <x> *EOL*
    Sets the font drawing position in lines.

**^P**
    Ends the current page (if there is one) and starts the next.

**^T**\ <y> <x> <index> *EOL*
    Waits time and then draws an image by index.

**^T**\ <y> <x> [<texture>] EOL
    Waits time and then draws an image by texture name.
