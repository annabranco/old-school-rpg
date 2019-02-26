from db import enemies
import cinematics
from sys import argv

argv = argv[1:]
if len(argv) == 0:
    enemy = enemies.ugly_monster
else:
    enemy_called = argv[0]
    enemy = getattr(enemies, enemy_called, enemies.ugly_monster)

cinematics.start_encounter(enemy)
