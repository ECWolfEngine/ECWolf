A_WeaponReady
=============

.. action:: A_WeaponReady
	:class: Weapon

	Makes the weapon idle and ready for firing. This function enables weapon bobbing for the duration of the state and handles player actions.

	:param flags: Modifies the behavior of the function.

		- .. constant:: WRF_ALLOWRELOAD

			Enables checking for the reload key and jumping to the Reload state.

		- .. constant:: WRF_ALLOWZOOM

			Enables checking for the zoom key and jumping to the Zoom state.

		- .. constant:: WRF_DISABLESWITCH

			Cancel weapon switch requests.

		- .. constant:: WRF_NOBOB

			Disables weapon bobbing.

		- .. constant:: WRF_NOFIRE

			Alias for the combination of :const:`WRF_NOPRIMARY` and :const:`WRF_NOSECONDARY`.

		- .. constant:: WRF_NOPRIMARY

			Disables checking for the primary fire button and jumping to the Fire state.

		- .. constant:: WRF_NOSECONDARY

			Disables checking for the secondary fire button and jumping to the AltFire state.

		- .. constant:: WRF_NOSWITCH

			Defer weapon switching until the next call without cancelling.
