.. index:: LANGUAGE

.. _LANGUAGE:

LANGUAGE
========

The language lump provides various text strings for use in game. Multiple translations can be provided in order to localize your mod.

Syntax
------

To begin you must select a language by placing it's three letter code in brackets (for example English is enu). If this is the primary translation for your strings you may also provide the default keyword. Other languages which may not provide a translation for your string will fall back to the default.

After the header you provide a list of strings by using the following format: ``LOGICALNAME = "Translation";``

Examples
--------

.. code:: ini

	[enu default]

	WL_EPISODE1 = "Episode 1\nEscape from Wolfenstein";
	WL_EPISODE2 = "Episode 2\nOperation: Eisenfaust";
	WL_EPISODE3 = "Episode 3\nDie, Fuhrer, Die!";
	WL_EPISODE4 = "Episode 4\nA Dark Secret";
	WL_EPISODE5 = "Episode 5\nTrail of the Madman";
	WL_EPISODE6 = "Episode 6\nConfrontation";

	[spa]

	WL_EPISODE1 = "Episodio 1\nFuga desde Wolfenstein";
	WL_EPISODE2 = "Episodio 2\nOperacion Eisenfaust";
	WL_EPISODE3 = "Episodio 3\nMuere, Fuhrer, Muere!";
	WL_EPISODE4 = "Episodio 4\nUn Negro Secreto";
	WL_EPISODE5 = "Episodio 5\nHuellas del Loco";
	WL_EPISODE6 = "Episodio 6\nConfrontacion";
