A_ReFire
========

.. action:: A_ReFire
	:class: Weapon

	Jumps if the player is holding down the fire button and the player still has ammo.

	:param hold: State to jump to. The default value will pick the Hold state if it's defined, otherwise use the Fire state. If so, jumps to the Hold/AltHold state if defined, otherwise jumps to the Fire/AltFire state.
