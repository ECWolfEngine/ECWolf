A_SetTics
=========

.. action:: A_SetTics

	Modifies the duration of the calling state. This function allows for more complex expressions to be used to change the duration. For the case of a random duration, using random on the actual state duration is preferred.

	:param duration: Desired duration of calling state. As with all tic durations, this must be a multiple of 0.5 otherwise the behavior of the function is undefined.
