A_MonsterRefire
===============

.. action:: A_MonsterRefire

	Calls :action:`A_FaceTarget` and has a chance of continuing while the target is visible.

	:param chance: Probability 0 to 256 that the actor does not jump to abort.
	:param abort: State to jump to if the chance roll fails.
