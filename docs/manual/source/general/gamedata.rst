.. _Game data:

Game data
=========

|project| requires base game data from the original games in order to play. For convienance this data is referred to as the IWAD since it is the equivalent to those files in Doom.

Supported data/IWADs
--------------------

Below are the data sets supported by |project|. Each table contains the specific list of files needed as well as their md5 checksums. On macOS and Linux the md5sum tool can be used to generate a hash for your files. For Windows `HashCheck <https://code.kliu.org/hashcheck/>`_ or one of the many other tools can be used. Older version of Wolfenstein 3D can be patched using the utility on the `ECWolf downloads page <https://maniacsvault.net/ecwolf/download.php>`_.

In addition to the below the games *Wolfstone 3D* and *Elite Hans: Die Neue Ordnung* are supported and must be extracted from *Wolfenstein II* and *Wolfenstein: Youngblood* respectively. The tool for extracting these games, WolfstoneExtract, can also be found on the downloads page.

.. csv-table:: Super 3D Noah's Ark
	:header: MD5, \*.n3d

	9c7e08401faf9c7d64e7ee7bceb6c9b8, audiohed.n3d
	8b40a14de58cf8578bb3a783dcb4f7bb, audiot.n3d
	d35ce2257a4fb56f61529df5f7f77adb, gamemaps.n3d
	2eaab4dd50856abeaebe75a8bcbbab42, maphead.n3d
	fb3d87a2e265d87e720ac011b7301b23, vgadict.n3d
	58d67ea6f4a9d5c7a788b7406e50dda3, vgagraph.n3d
	fe26baf052f03e92019e221bc106dfec, vgahead.n3d
	8c61a9b3bb38a598990ccb743d2679fa, vswap.n3d

.. csv-table:: Spear of Destiny
	:header: MD5, \*.sod

	6e914d15335125872737718470061ad8, audiohed.sod
	10020fce0f04d21bd07b1b5b951c360a, audiot.sod
	04f16534235b4b57fc379d5709f88f4a, gamemaps.sod
	276c79a4a6419db6b23e7699e41cb9fa, maphead.sod
	30b11372b9ec6bc06289eb3e9b2ef0b9, vgadict.sod
	3b85f170098fb48d91d8bedd0cac4e0d, vgagraph.sod
	fb75007a1167bba05c4acadf90bc30d8, vgahead.sod
	b1dac0a8786c7cdbb09331a4eba00652, vswap.sod

.. csv-table:: Spear of Destiny Demo
	:header: MD5, \*.sdm

	f0022742f86c214872bd72f03aaf1529, audiohed.sdm
	fcde1333c941229f4dd6ca099fcfe616, audiot.sdm
	4eb2f538aab6e4061dadbc3b73837762, gamemaps.sdm
	40fa03caf7a1a4dbd22da4321c6e10d4, maphead.sdm
	2f85b6763a582df19e6a35dd9634c736, vgadict.sdm
	1cc5ceb8e43c0c0030cf552fc8ae9d0d, vgagraph.sdm
	18c03cb401ed274bc0b659e951140e64, vgahead.sdm
	35afda760bea840b547d686a930322dc, vswap.sdm

.. csv-table:: Wolfenstein 3D
	:header: MD5, \*.wl6

	a41af25a2f193e7d4afbcc4301b3d1ce, audiohed.wl6
	2385b488b18f8721633e5b2bdf054853, audiot.wl6
	a4e73706e100dc0cadfb02d23de46481, gamemaps.wl6
	b8d2a78bc7c50da7ec9ab1d94f7975e1, maphead.wl6
	dec8939cff5a4ec27ae7b43e8f52ec28, vgadict.wl6
	8b40b5b785f898e229bf1c2f2e3ee003, vgagraph.wl6
	8e75e3ffb842ed3d08abe6ffea97b231, vgahead.wl6
	b8ff4997461bafa5ef2a94c11f9de001, vswap.wl6

.. csv-table:: Wolfenstein 3D Shareware
	:header: MD5, \*.wl1

	58aa1b9892d5adfa725fab343d9446f8, audiohed.wl1
	4b6109e957b584e4ad7f376961f3887e, audiot.wl1
	30fecd7cce6bc70402651ec922d2da3d, gamemaps.wl1
	7b6dd4e55c33c33a41d1600be5df3228, maphead.wl1
	76a6128f3c0dd9b77939ce8313992746, vgadict.wl1
	74decb641b1a4faed173e10ab744bff0, vgagraph.wl1
	61bf1616e78367853c91f2c04e2c1cb7, vgahead.wl1
	6efa079414b817c97db779cecfb081c9, vswap.wl1

.. csv-table:: Mission 2: Return to Danger
	:header: MD5, \*.sd2

	fa5752c5b1e25ee5c4a9ec0e9d4013a9, gamemaps.sd2
	d55508cd58e2e61076ac81b98aeb9269, maphead.sd2
	25d92ac0ba012a1e9335c747eb4ab177, vswap.sd2

.. csv-table:: Mission 3: Ultimate Challenge
	:header: MD5, \*.sd3

	4219d83568d770b1c6ac9c2d4d1dfb9e, gamemaps.sd3
	52fd50245a77e61dc1df91110c186195, maphead.sd3
	e3e87518f51414872c454b7d72a45af6, vswap.sd3

.. csv-table:: Mission 3: Ultimate Challenge (Alternate UAC version)
	:header: MD5, \*.sd3

	29860b87c31348e163e10f8aa6f19295, gamemaps.sd3
	a8b24dd3d3271e0b7fc6f2f995915f27, maphead.sd3
	94aeef7980ef640c448087f92be16d83, vswap.sd3

Unsupported data
----------------

Tables of md5sums for other Wolfenstein 3D engine games which will be supported by |project| in the future.

.. csv-table:: Corridor 7: Alien Invasion (CD version)
	:header: MD5, \*.co7

	6f41f714f882ea133dd5d1678448dffb, audiohed.co7
	9ed47d8d50a5837af06a941d4d736d8c, audiomus.co7
	c925c5ac9ea51df814d3b6d9c5f2e771, audiot.co7
	6c6df783a32ebf7b1e6053f12010ec54, gfxinfov.co7
	e9a976a8456866d3c2cadd38c9f74662, gfxtiles.co7
	f6f0c4400a8f003713479775823fd821, maptemp.co7
	a80d42f0bb7b10a6318e811c45140aa3, seqfour.co7
	c67824a5bc5d754c00b7ecd99f8018e1, seqone.co7
	3a7b84e6608cef1d7558df824afaaa6d, seqthree.co7
	a0d2b334686bebdd3b1d9e79a91dc5b5, vgadict.co7
	3f6de286010058708110bc7000a2827c, vgagraph.co7
	a186ac0e094d4588c454e4f23c96a002, vgahead.co7

.. csv-table:: Operation Body Count
	:header: MD5, \*.bc

	ccde3d43a536426426c4621d5fe0f370, audiohed.bc
	95489aefee08b0d6262e434bfba1ca62, audiomus.bc
	078b7aaf594ae0d777b7bf72c6a3a700, audiot.bc
	32a17e2d251ac7b1c5f0d094b641836f, f1.bc
	fcd108d98baeeb9e259f3dcd99cc163b, f2.bc
	b08731f5d092c776b9375e5d3422d7d9, f3.bc
	587c1da63bef3d4004e7bfbc5ca67b35, f4.bc
	1f265763b4c686eed0d7e2db826020e6, f5.bc
	fc6e69c5daa0d1acbc675e404d2f3269, f6.bc
	7a2617c6695cd44c494eec4ddf72efb9, f7.bc
	1b501ef167445b37d4b31e84e707da62, gfxinfov.bc
	98cc9d5b4406e70c3affa508adb6a413, gfxtiles.bc
	9c98aeaeb63fc21e66a4fbdb668420df, maphead.bc
	063176ca9fc0b0d8fd2784fab1cb14fb, maptemp.bc
	9942425bb04c5009c7f1ce91234c7ee9, vgadict.bc
	e09be75f20afac2827fa6808ad35f0c7, vgagraph.bc
	f463da1212dc1238730028a21872da72, vgahead.bc

Obtaining game data/IWADs
-------------------------

The two Spear of Destiny mission packs are no longer available for purchase, but the rest of the games can be acquired via most store fronts.

.. rubric:: GOG.com

Get Wolfenstein 3D and Spear of Destiny in a single pack from GOG. Doesn't require a client to install so easily the best way to acquire the games.

* `Super 3D Noah's Ark <https://www.gog.com/en/game/super_3d_noahs_ark>`_
* `Wolfenstein 3D + Spear of Destiny <https://www.gog.com/en/game/wolfenstein_3d>`_
* `Wolfstone 3D <https://www.gog.com/en/game/wolfenstein_ii_the_new_colossus>`_

The unsupported games are also available from GOG.

* `Blake Stone: Aliens of Gold <https://www.gog.com/en/game/blake_stone_aliens_of_gold>`_
* `Blake Stone: Planet Strike <https://www.gog.com/en/game/blake_stone_planet_strike>`_
* `Corridor 7 <https://www.gog.com/en/game/corridor_7_alien_invasion>`_
* `Operation Body Count <https://www.gog.com/en/game/operation_body_count>`_
* `Rise of the Triad: Dark War <https://www.gog.com/en/game/rise_of_the_triad_dark_war>`_
* `Rise of the Triad: Ludicrous Edition <https://www.gog.com/en/game/rise_of_the_triad_ludicrous_edition>`_

.. rubric:: Steam

* `Elite Hans: Die Neue Ordnung <https://store.steampowered.com/app/1056960/Wolfenstein_Youngblood/>`_
* `Super 3D Noah's Ark <https://store.steampowered.com/app/371180/Super_3D_Noahs_Ark/>`_
* `Wolfenstein 3D + Spear of Destiny <https://store.steampowered.com/app/2270/Wolfenstein_3D/>`_
* `Wolfstone 3D <https://store.steampowered.com/app/612880/Wolfenstein_II_The_New_Colossus/>`_

The unsupported games are also available from Steam.

* `The Apogee Throwback Pack <https://store.steampowered.com/app/238050/The_Apogee_Throwback_Pack/>`_

  * `Blake Stone: Aliens of Gold <https://store.steampowered.com/app/358190/Blake_Stone_Aliens_of_Gold/>`_
  * `Blake Stone: Planet Strike <https://store.steampowered.com/app/358310/Blake_Stone_Planet_Strike/>`_
  * `Rise of the Triad: Dark War <https://store.steampowered.com/app/358410/Rise_of_the_Triad_Dark_War/>`_

* `Corridor 7: Alien Invasion <https://store.steampowered.com/app/1341890/Corridor_7_Alien_Invasion/>`_
* `Operation Body Count <https://store.steampowered.com/app/1627120/Operation_Body_Count/>`_
* `Rise of the Triad: Ludicrous Edition <https://store.steampowered.com/app/1421490/Rise_of_the_Triad_Ludicrous_Edition/>`_

.. rubric:: itch.io

* `Super 3D Noah's Ark <https://wisdomtree.itch.io/s3dna>`_
