# Core modules
from core.config import *
from core.characters.Hero import Hero
from core.characters import NPC
from core.scenario import Scenario

# Mechanics modules
from mechanics.combat import initiative
from mechanics.combat import attack
from mechanics.combat import defend
from mechanics.combat.combat_rounds import combat_rounds
from mechanics.actions.viewing import look, search
from mechanics.actions.interacting.items import take, drop
# DETERMINES THE MECHANICS RELATED TO GENERIC ACTIONS

# ask_for_action
'''
    It is generically called whenever an action is expected from the Player.
'''


def ask_for_action() -> str:
    print_cinematics('What do you do?')
    return await_for_action()


def await_for_action() -> str:
    return input('\n\t\t> ')

# encounter_reaction


'''
    It is called every time an encounter starts. Checks if the enemy is aware of the Hero presence.
'''


def encounter_reaction(enemy: NPC):
    action: str = ask_for_action()
    print('\n')
    if enemy.status == 'unaware' or enemy.status == 'sleeping':
        encounter_reaction_unaware(action, enemy)
    else:
        encounter_reaction_aware(action, enemy)

# encounter_reaction_unaware


'''
    It is called to check Player decisions when the enemy IS NOT aware of the Hero.
'''


def encounter_reaction_unaware(action: str, enemy: NPC):
    if action.startswith('attack') or action.startswith('kill'):
        print_cinematics(
            f'You draw your {Hero.weapon["name"]} and strike before {enemy.name} has a chance to understand what is happening.')
        mechanics_block('SNEAK ATTACK')
        attack.attack(enemy, 2, True)
        combat_rounds.took_action['enemy'] = True
    elif action == 'wait' or action == 'defend':
        print_cinematics(
            f'You stand on your position, but {enemy.name} just doesn\'t notice you.')
        encounter_reaction(enemy)

# encounter_reaction_unaware


'''
    It is called to check Player decisions when the enemy IS aware of the Hero.
'''


def encounter_reaction_aware(action: str, enemy: NPC):
    decision_taken = False
    while not decision_taken:

        if action.startswith('attack') or action.startswith('kill'):
            decision_taken = True
            print_cinematics(
                f'You draw your {Hero.weapon.name} and quickly strike {enemy.name}.')
            mechanics_block('COMBAT')
            attack.attack(enemy, 0, False)

        elif action.startswith('wait'):
            decision_taken = True
            print_cinematics(
                f'You wait to see the reaction of {enemy.name}. He draws a {enemy.weapon.name} and comes to attack you.')
            print_cinematics(
                f'You draw your {Hero.weapon.name} and prepare to face him.')
            initiative.initiative(enemy, 0)

        elif action.startswith('defend'):
            decision_taken = True
            print_cinematics(
                f'You draw your {Hero.weapon.name} and put yourself on a defensive stance while the {enemy.name} draws a {enemy.weapon.name} and comes to attack you.')
            mechanics_block('COMBAT')
            combat_rounds.took_action['Hero'] = True
            defend.defend(enemy, 0, True)

        else:
            print('You can\'t do that.')
            action: str = ask_for_action()

# basic_actions


'''
    It is called to check Player decisions related to no-combat actions.
'''


def basic_actions(scenario: Scenario):
    print_cinematics('What do you do?')
    while True:
        action = await_for_action()

        if action.startswith('look'):
            what = action.replace('look', '').lstrip()
            look(what, scenario)

        elif action.startswith('search'):
            if action == 'search':
                print('Where would you like to search?')
                place = input('> ')
            else:
                place: str = action.replace('search', '').lstrip()
            search(place, scenario)

        elif action.startswith('take') or action.startswith('get'):
            what: str = action.replace('take', '').replace('get', '').lstrip()
            take(what, scenario)

        elif 'inventory' in action or 'items' in action:
            Hero.declare_inventory()

        elif 'status' in action in action:
            Hero.declare_status()

        elif action.startswith('drop'):
            what: str = action.replace('drop', '').lstrip()
            drop(what, scenario)

        else:
            print('You can\'t do that.')
