.. include:: /_templates/roles.rst

A_ActiveSound
=============

.. action:: A_ActiveSound

	Plays the calling actor's :prop:`active sound <activesound>`.

	:param chance: Gives the probability of the sound being played (0-256). By default the sound will always play.

		- .. constant:: ASP_CHASE

			Emulates the probability of :action:`A_Chase`. This is useful for Wolfenstein style monsters as the active sound would otherwised be played far more often than it should.

			:state:`GARD A 5 A_ActiveSound(ASP_CHASE) A_Chase("*", "*", CHF_NOPLAYACTIVE)`
