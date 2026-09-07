.. decorate-actor-header:: BJRun

Overview
--------

Special actor spawned by the :special:`Exit_VictorySpin` action special. The actor has no special behavior in itself, but is formatted to work with the victory spin action.

Specifically the spawn state causes the actor to move forwards in the direction it is facing. When the victory spin detects the actor bumping into the player, it will be turned into a projectile with the run speed as the velocity and play the Death state. Ultimately the actor triggers the actual exit special.

.. decorate-actor-footer:: BJRun
