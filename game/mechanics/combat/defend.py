from random import randint
from mechanics.global_mechanics import modifiers
from db.hero import Hero
import actions
import cinematics
from mechanics.combat.combat_mechanics import dispatch_attack
from core.config import print


def defend(enemy, bonus=0, focus_on_defense=False):

    if focus_on_defense:
        print('Hero stands on a defensive stance.')

    difficult = Hero['defense'] + bonus
    base_attack = enemy['attack']
    dispatch_attack(difficult, base_attack, enemy, Hero)
