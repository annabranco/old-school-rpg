from random import randint
from mechanics.global_mechanics import modifiers
from db.hero import hero
import actions
import cinematics
from mechanics.combat import combat_mechanics
from core.config import print


def defend(enemy, bonus=0, focus_on_defense=False):

    if focus_on_defense:
        print('Hero stands on a defensive stance')

    difficult = hero['defense'] + bonus
    base_attack = enemy['attack']
    combat_mechanics.dispatch_attack(difficult, base_attack, enemy, hero)
