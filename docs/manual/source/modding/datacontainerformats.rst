.. index:: PK3, WAD

.. _Data container formats:

Data container formats
======================

While data in the vanilla Wolfenstein 3D format can be loaded with the help of :ref:`map files <WL6 maps>`, doing so is not recommended for mods. Other formats are supported which allow management of data with less tedium.

Format comparison
-----------------

There are effectively two container formats recommended for use.

**Zip (PK3)**
	Supports long file names and organization of data into a directory structure. Compression of resources is also supported (including LZMA and BZip2).

**WAD**
	Basic uncompressed container with limited organizational opportunities. This format was used by Rise of the Triad and the Jaugar version of Wolfenstein 3D.

.. note:: A directory containing the same structure that would go in a PK3 can also be used for development and loaded directly. If doing so you should always package up the mod into a PK3 for distribution.

A number of other container formats can also be loaded including 7z (typically used with PK7 extension), Quake PAK, Duke3D GRP, and Blood RFF. The former two are fully capable of being used for mods, but offer little benefit. Using a 7z/PK7 archive does offer higher compression ratios, but this normally comes at the cost of higher resident memory usage.

Namespaces
----------

Various name spaces are used to logically organize data. In WADs in some cases use empty marker lumps (XY_START and XY_END) to signify a change in name space, but may be automatically detected. Below is a table describing the various name spaces used.

.. list-table::
	:header-rows: 1

	* - Directory
	  - WAD Marker
	  - Description
	* - graphics/
	  - *None*
	  - Graphics such as title picture or sign on screens are placed in this directory.
	* - hires/
	  - :zd:`HI <HI_START>`
	  - High resolution textures. The scale factor for the high resolution texture will be determined by the size of the similarly named low resolution texture.
	* - flats/
	  - :zd:`F <F_START>`
	  - Floor and ceiling textures. Lumps here should be of type "Graphic (Flat)" or PNG. "Graphic (Doom)" lumps will not work.
	* - maps/
	  - *None*
	  - Maps stored within WAD files. Maps must contain the data for a single level and the name of the file will be used as the map label.
	* - music/
	  - *None*
	  - Background music.
	* - patches/
	  - *None*
	  - Small textures which are to be referenced by the :ref:`TEXTURES` lump.
	* - sounds/
	  - *None*
	  - Sounds to be referenced by :ref:`SNDINFO`.
	* - sprites/
	  - :zd:`S <S_START>`
	  - Sprites for actors. Sprites may be organized into sub-directories.
	* - textures/
	  - :zd:`TX <TX_START>`
	  - Textures to be used as-is.

In WAD files the Rise of the Triad namespaces are also recognized. There is no reason to use them and they have compatibility behaviors associated with them which may be undesirable if not trying to be compatible with vanilla Rise of the Triad. These namespaces are: ``ANIMSTRT``/``ANIMSTOP``, ``DOORSTRT``/``DOORSTOP``, ``ELEVSTRT``/``ELEVSTOP``, ``EXITSTRT``/``EXITSTOP``, ``SIDESTRT``/``SIDESTOP``, ``SKYSTRT``/``SKYSTOP``, ``UPDNSTRT``/``UPDNSTOP``, and ``WALLSTRT``/``WALLSTOP``. At the moment the support for these exists to permit using ROTT maps as testing samples and behavior and quirks are subject to change.

Packaging vanilla mods
----------------------

If you are building an otherwise vanilla mod, or even a mod for another engine that can be made compatible, you can package it in a way that |project| will automatically be able to load it. If your mod uses game data files with the extension ``xyz``, then create a file called ``ecwolf.xyz`` and include it in your zip archive. Then the Zip archive can be directly used as a mod and any of the ``audiot.xyz``, ``gamemaps.xyz``, ``vgagraph.xyz``, and/or ``vswap.xyz`` files will be loaded followed by ``ecwolf.xyz``.

Although an empty (0 byte) file will serve to enable this behavior, if it's actually a PK3 or WAD file then any resources needed to adapt the mod, including :ref:`WL6 maps`, will be applied.

The WolfstoneExtract program uses this when building the PK3 files for Wolfstone 3D and Elite Hans as those games are mostly in vanilla format with the exception of the sounds and some constructed support resources.

Notes
-----

* In formats which support paths the ``^`` character is sprites is changed to a ``\``. This is a carry over from ZDoom where this was needed in order to be compatible with the arch-vile sprites.
* Although in general the order of lumps should not be relied upon. For formats which support full paths, the lumps are loaded alphabetically.
* Archives with full paths which have duplicated files are malformed and will exhibit undefined behavior. Entries are considered duplicates even if casing doesn't match.
* It is strongly recommended that you do not use the zip/7z extension when using the respective formats since the average user is used to decompressing those files. Use PK3/PK7 instead.

See also
--------

* :zd:`Using ZIPs as WAD replacement`
