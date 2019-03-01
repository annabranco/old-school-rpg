from mechanics.combat import initiative
from mechanics.combat import attack
from mechanics.combat import defend
from mechanics.combat.combat_rounds import combat_rounds
from core.characters.Hero import Hero
from core.config import *
import scenarios

def ask_for_action():
    print_cinematics('What do you do?')
    return input('\n\t\t> ')


def encounter_reaction(enemy):
    action = ask_for_action()
    print('\n')
    if enemy.status == 'unaware' or enemy.status == 'sleeping':
        encounter_reaction_unaware(action, enemy)
    else:
        encounter_reaction_aware(action, enemy)


def encounter_reaction_unaware(action, enemy):
    if action == 'attack':
        print_cinematics(
            f'You draw your {Hero.weapon["name"]} and strike before {enemy.name} has a chance to understand what is happening.')
        mechanics_block('SNEAK ATTACK')
        attack.attack(enemy, 2, True)
        combat_rounds.took_action['enemy'] = True
    elif action == 'wait' or action == 'defend':
        print_cinematics(
            f'You stand on your position, but {enemy.name} just doesn\'t notice you.')
        encounter_reaction(enemy)


def encounter_reaction_aware(action, enemy):
    if action == 'attack':
        print_cinematics(
            f'You draw your {Hero.weapon["name"]} and quickly strike {enemy.name}.')
        mechanics_block('COMBAT')
        attack.attack(enemy, 0, False)

    elif action == 'wait':
        print_cinematics(
            f'You wait to see the reaction of {enemy.name}. He draws a {enemy.weapon["name"]} and comes to attack you.')
        print_cinematics(
            f'You draw your {Hero.weapon["name"]} and prepare to face him.')
        initiative.initiative(enemy, 0)

    elif action == 'defend':
        print_cinematics(
            f'You draw your {Hero.weapon["name"]} and put yourself on a defensive stance while the {enemy.name} draws a {enemy.weapon["name"]} and comes to attack you.')
        mechanics_block('COMBAT')
        combat_rounds.took_action['Hero'] = True
        defend.defend(enemy, 0, True)

def where(place):
    return getattr(scenarios, place)

def basic_actions():
        place = ask_for_action()

    # if action == 'look around' or action == 'look':
    #     print_cinematics(
    #         f'You look around and you see {scenario.description}.')

    # elif action == 'search':
    #     print('Where would you like to search?')
    #     place = input('> ')
        if place in scenarios.ambient:
            print_cinematics(f'You search the {place} but you find nothing.')
        elif place in scenarios.far_away:
            print_cinematics(f'It is too far away.')
        elif place in scenarios.has_something:
            if where(place)[0]["special"] != None:
                print(where(place)[0]["special"])
                Hero.change_status('tired')
                Hero.declare_status()
            if len(where(place)) > 1:
                print('You\'ve found:')
                for item in where(place):
                    if item.get("name") != None:
                        print(f'- {item.get("name")}')


            # if not getattr(scenarios, place["special"]):
            #     print(getattr(scenarios, place["special"])
            # else:
            #     print(f'You\'ve found {getattr(scenarios, place["special"]}')

        # for place in scenarios.ambient:
        #     if place == search_where:
        #         print_cinematics(f'You search {place} but you find nothing.')

