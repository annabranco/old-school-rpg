import cinematics
from db.enemies import ugly_monster, strong_monster
from db import enemies
from db.hero import Hero
from sys import argv
from mechanics.global_mechanics.rolls import roll_dices
from core.config import print

print(roll_dices(4, 6, 'anything'))
