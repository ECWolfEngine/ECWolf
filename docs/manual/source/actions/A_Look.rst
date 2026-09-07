A_Look
======

.. action:: A_Look

	Causes the monster to check its field of vision for any targets.

	:param flags: Unused at the moment. Should be set to 0.
	:param minseedist: Minimum distance (in map pixels) the target must be from the actor in order for it to be seen.
	:param maxseedist: Maximum distance (in map pixels) the target can be from the actor for it to be able to see it.
	:param maxheardist: Maximum distance (in map pixels) the target can be from the actor and still be able to hear gun fire.
	:param fov: The field of vision for this call in degrees. Default is 180 degrees.

.. action:: A_LookEx

	Implemented as an alias of :action:`A_Look`. This alias can be used if compatibility with ZDoom is desired.
