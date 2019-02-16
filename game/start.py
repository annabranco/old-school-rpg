import cinematics
from db.enemies import ugly_monster, strong_monster
from db import enemies
from db.hero import hero
from sys import argv

# WIP: default value is not working
argv = argv[1:]
if len(argv) == 0:
	enemy = strong_monster
else:
	enemy = enemies.argv[0]

cinematics.start_encounter(enemy)