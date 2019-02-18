from random import randint
from mechanics.global_mechanics import modifiers
from db.hero import Hero
import actions
import cinematics
from core.config import print
from mechanics.combat.combat_mechanics import dispatch_attack

# define texts by types of weapons


def attack(enemy, bonus=0, surprise_attack=False):

    if surprise_attack == True:
        difficult = 2
    else:
        difficult = enemy['defense']

    base_attack = Hero['attack'] + bonus
    dispatch_attack(difficult, base_attack, Hero, enemy)
