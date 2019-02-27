from core.characters.Hero import Hero
from mechanics.global_mechanics.rolls import roll_dices
from mechanics.combat import combat_mechanics
from mechanics.combat.combat_rounds import combat_rounds
from db import fails
from mechanics.combat import initiative
from core.config import *


# define texts by types of weapons


def attack(enemy, bonus=0, surprise_attack=False):
    combat_rounds.took_action['Hero'] = True

    if surprise_attack == True:
        difficult = 2
    else:
        difficult = enemy.defense

    base_attack = Hero.attack + bonus
    results_number, results_text = roll_dices(
        base_attack, difficult, f'Attacking {enemy.name}')

    if results_text == 'epic':
        combat_mechanics.damage(results_number, Hero, enemy)
    elif results_text == 'decisive' or results_number > 0:
        combat_mechanics.damage(results_number, Hero, enemy)
    elif results_text == 'critical':
        fails.disastrous_fail_on_attack(results_number, Hero, enemy)
    elif results_text == 'disastrous':
        fails.disastrous_fail_on_attack(results_number, Hero, enemy)
    else:
        combat_mechanics.missed(Hero, enemy)


def simultaneous_attack(enemy):
    results_number_hero, results_text_hero = roll_dices(
        Hero.attack, enemy.defense, f'Attacking {enemy.name}')
    results_number_enemy, results_text_enemy = roll_dices(
        enemy.attack, Hero.defense, f'{enemy.name}\'s attack')

    if (results_number_hero <= 0 and results_number_enemy <= 0):
        mechanics_block()
        print_cinematics(
            f'You and {enemy.name} attack at the same time and your blows block each other.')
        initiative.initiative(enemy, 0)
    else:
        combat_mechanics.simultaneous_damage(
            results_number_hero, Hero, results_number_enemy, enemy)
