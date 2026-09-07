.. decorate-actor-header:: RandomSpawner

Overview
--------

Specifies an actor which randomly spawns one item from the :prop:`DropItem <dropitem>` list. The two parameters for DropItem affect the probability of the thing spawning. The first number gives a chance the actor will spawn, and the second number gives the weight of the actor (essentially the number of times the actor should appear on the list).

Random spawners can spawn other random spawners, but an infinite loop protection will occur at 32 iterations.

.. decorate-actor-footer:: RandomSpawner
