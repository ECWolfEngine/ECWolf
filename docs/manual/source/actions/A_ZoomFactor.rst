A_ZoomFactor
============

.. action:: A_ZoomFactor
	:class: Weapon

	Changes the field of view for the player relative to their normal field of view.

	:param zoom: Percentage change for field of view.
	:param flags: Modifies the behavior of the function.

		- .. constant:: ZOOM_INSTANT

			Disables fov interpolation.

		- .. constant:: ZOOM_NOSCALETURNING

			Disables rescaling of mouse sensitivity while zoomed.
