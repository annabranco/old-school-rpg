from db import enemies
import cinematics
from sys import argv

### START OF THE GAME.
# It is currently used for testing purposes related to combat.

'''
This file mught be started as
$python3 start.py [enemy]

[enemy] is an opitional argument, for example strong_monster

If an enemy is passed as argument upon starting the game,
a combat starts agains this enemy.
If no enemy is passed as argument, a combat starts against Ugly Monster.
'''

argv = argv[1:]
if len(argv) == 0:
    enemy = enemies.ugly_monster
else:
    enemy_called = argv[0]
    enemy = getattr(enemies, enemy_called, enemies.ugly_monster)

cinematics.start_encounter(enemy)
