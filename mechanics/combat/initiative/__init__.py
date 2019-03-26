from core.config import *
from mechanics.combat.combat_rounds import combat_rounds
from core.characters.Hero import Hero
from random import randint
from mechanics.combat import attack
from mechanics.combat import defend
from mechanics.global_mechanics.rolls import roll_dices
from core.characters import NPC


# DETERMINES THE MECHANICS RELATED TO INITIATIVE ON COMBATS
# (DETERMINES WHO WAS QUICKER TO STRIKE FIRST, OR IF IT WAS SIMULTANEOUS)


def initiative(enemy: NPC, bonus: int = 0) -> None:
    '''
        It is called whenever a new round begins and calls roll_dices method.
    '''
    mechanics_block('COMBAT')
    write_to_screen(
        '\tAn initiative should be rolled to know who strikes first.\n')
    write_to_screen(f'YOUR HP: {Hero.hp}, {enemy.name}\'s HP: {enemy.hp}\n')
    action_block()
    combat_rounds.took_action['Hero'] = False
    combat_rounds.took_action['enemy'] = False
    initiative_difficulty = 1

    Initiative_Hero_roll = roll_dices(
        Hero.speed + bonus, initiative_difficulty, 'Hero initiative')
    Initiative_enemy_rolls = roll_dices(
        enemy.speed, initiative_difficulty, 'Enemy initiative')

    Hero_initiative = Initiative_Hero_roll[0]
    enemy_initiative = Initiative_enemy_rolls[0]

    print(f'Your attack speed: {Hero_initiative}')
    print(f'{enemy.name}\'s attack speed: {enemy_initiative}')

    compare_initiatives(Hero_initiative, enemy_initiative, enemy)


def compare_initiatives(Hero_initiative: int, enemy_initiative: int, enemy: NPC) -> None:
    '''
        Compares the results of the rolls obtained in the initiative method.
    '''
    if Hero_initiative > enemy_initiative:
        print('* You strike first.')
        action_block()
        combat_rounds.took_action['Hero'] = True
        attack.attack(enemy, 0, False)

    elif Hero_initiative < enemy_initiative:
        print(f'* {enemy.name} strikes first.')
        action_block()
        combat_rounds.took_action['enemy'] = True
        defend.defend(enemy, 1, False)

    else:
        print('* Simultaneous attack.')
        action_block()
        combat_rounds.took_action['Hero'] = True
        combat_rounds.took_action['enemy'] = True
        attack.simultaneous_attack(enemy)
