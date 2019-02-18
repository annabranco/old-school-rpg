import cinematics
from db.enemies import ugly_monster, strong_monster
from db import enemies
from db.hero import hero
from sys import argv
from core.config import print

argv = argv[1:]
if len(argv) == 0:
    enemy = ugly_monster
else:
    enemy_called = argv[0]
    enemy = getattr(enemies, enemy_called, ugly_monster)

cinematics.start_encounter(enemy)
