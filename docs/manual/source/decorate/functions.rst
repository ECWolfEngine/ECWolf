.. index:: Action functions

.. _Action functions:

Action functions
================

.. This toctree includes the action functions as while it would be possible to generate a toctree for each actor, there's not a great way to handle cases where one file resolves multiple action functions.

.. toctree::
	:hidden:
	:glob:

	/actions/*

The following are code pointers for use within :ref:`DECORATE`. If the name of a function below matches one found in ZDoom the behavior should be similar.

Monster AI
----------

* :action:`A_AlertMonsters`
* :action:`A_Chase`
* :action:`A_FaceTarget`
* :action:`A_Look`/:action:`A_LookEx`
* :action:`A_Wander`

Generic monster attacks
-----------------------

* :action:`A_CustomMissile`
* :action:`A_Explode`
* :action:`A_MeleeAttack`
* :action:`A_MonsterRefire`
* :action:`A_WolfAttack`

Sound functions
---------------

* :action:`A_ActiveSound`
* :action:`A_Pain`
* :action:`A_PlaySound`
* :action:`A_Scream`

Special actions
---------------

* :action:`A_BossDeath`

Spawn functions
---------------

* :action:`A_SpawnItem`
* :action:`A_SpawnItemEx`

State jumps
-----------

* :action:`A_Jump`
* :action:`A_JumpIf`
* :action:`A_JumpIfCloser`
* :action:`A_JumpIfInventory`

Status changes
--------------

* :action:`A_ChangeFlag`
* :action:`A_ChangeVelocity`
* :action:`A_Dormant`
* :action:`A_Fall`
* :action:`A_ScaleVelocity`
* :action:`A_SetTics`

Inventory functions
-------------------

* :action:`A_GiveExtraMan`
* :action:`A_GiveInventory`
* :action:`A_TakeInventory`

Custom inventory functions
--------------------------

* :action:`A_Succeed`
* :action:`A_WeaponGrin`

Missile movement
----------------

* :action:`A_Stop`

Weapon functions
----------------

* :action:`A_GunFlash`
* :action:`A_Light`/:action:`A_Light0`/:action:`A_Light1`/:action:`A_Light2`
* :action:`A_Lower`
* :action:`A_Raise`
* :action:`A_ReFire`
* :action:`A_WeaponReady`
* :action:`A_ZoomFactor`

Weapon attack functions
-----------------------

* :action:`A_CustomPunch`
* :action:`A_FireCustomMissile`
* :action:`A_GunAttack`
