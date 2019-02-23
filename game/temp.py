import cinematics
from db.enemies import ugly_monster, strong_monster
from db import enemies
from db.hero import Hero
from sys import argv
from mechanics.global_mechanics.rolls import roll_dices
from core.config import print
import sys


#print(roll_dices(4, 6, 'anything'))

print(sys.ps1)


from random import randint
from mechanics.global_mechanics import modifiers
from db.hero import Hero
import actions
import db.cinematics
from mechanics.combat.combat_mechanics import damage, missed
from db.fails import disastrous_fail_on_attack
from mechanics.global_mechanics.rolls import roll_dices
from mechanics.combat.initiative import initiative
from mechanics.combat.attack import attack
from mechanics.combat.defend import defend
from mechanics.combat.combat_mechanics import took_action