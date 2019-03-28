# Core modules
from core_elements import *
from core_elements.characters.Hero import Hero
from core_elements.characters import NPC
from core_elements.scenario import Scenario

# Mechanics modules
from mechanics.combat import initiative
from mechanics.combat import attack
from mechanics.combat import defend
from mechanics.combat.combat_rounds import combat_rounds
from mechanics.actions.viewing import look, search
from mechanics.actions.interacting.items import take, drop, equip
from db.enemies import ugly_monster


# DETERMINES THE MECHANICS RELATED TO GENERIC ACTIONS


def ask_for_action() -> str:
    '''
        It is generically called whenever an action is expected from the Player.
    '''
    print_cinematics('What do you do?')
    return await_for_action()


def await_for_action() -> str:
    return input('\n\t\t> ').lower()


def encounter_reaction(enemy: NPC):
    '''
        It is called every time an encounter starts. Checks if the enemy is aware of the Hero presence.
    '''
    action: str = ask_for_action()
    print('\n')
    if enemy.status == 'unaware' or enemy.status == 'sleeping':
        encounter_reaction_unaware(action, enemy)
    else:
        encounter_reaction_aware(action, enemy)


def encounter_reaction_unaware(action: str, enemy: NPC):
    '''
        It is called to check Player decisions when the enemy IS NOT aware of the Hero.
    '''
    if action.startswith('attack') or action.startswith('kill'):
        print_cinematics(f'{Hero.draw_weapon} and strike before {enemy.name} has a chance to understand what is happening.')
        mechanics_block('SNEAK ATTACK')
        attack.attack(enemy, 2, True)
        combat_rounds.took_action['enemy'] = True
    elif action == 'wait' or action == 'defend':
        print_cinematics(
            f'You stand on your position, but the {enemy.name} just doesn\'t notice you.')
        encounter_reaction(enemy)


def encounter_reaction_aware(action: str, enemy: NPC):
    '''
        It is called to check Player decisions when the enemy IS aware of the Hero.
    '''
    decision_taken = False
    while not decision_taken:

        if action.startswith('attack') or action.startswith('kill'):
            decision_taken = True
            print_cinematics(
                f'{Hero.draw_weapon} and quickly strike {enemy.name}.')
            mechanics_block('COMBAT')
            attack.attack(enemy, 0, False)

        elif action.startswith('wait'):
            decision_taken = True
            print_cinematics(f'You wait to see {enemy.pronom[1]} reaction.')
            print_cinematics(f'{enemy.draw_weapon} and comes to attack you.')
            print_cinematics(f'{Hero.draw_weapon} and prepare to face {enemy.pronom[2]}.')
            initiative.initiative(enemy, 0)

        elif action.startswith('defend'):
            decision_taken = True
            print_cinematics(
                f'{Hero.draw_weapon} and put yourself on a defensive stance while the {enemy.draw_weapon} and comes to attack you.')
            mechanics_block('COMBAT')
            combat_rounds.took_action['Hero'] = True
            defend.defend(enemy, 0, True)

        else:
            print('You can\'t do that.')
            action: str = ask_for_action()



def basic_actions(scenario: Scenario):
    '''
        It is called to check Player decisions related to no-combat actions.
    '''
    print_cinematics('What do you do?')
    while True:
        action = await_for_action()

        if action.startswith('look'):
            what = action.replace('look', '').replace(' at ', '').replace(' the ', '').lstrip()
            look(what, scenario)

        elif action.startswith('search'):
            if action == 'search':
                print('You need to tell where would you like to search.')

            else:
                place: str = action.replace( 'search', '').replace('the', '').lstrip()
                search(place, scenario)

        elif action.startswith('take') or action.startswith('get'):
            what: str = action.replace('take', '').replace('get', '').lstrip()
            take(what, scenario)

        elif 'inventory' in action or 'items' in action:
            Hero.declare_inventory()

        elif 'bad' in action:
            print('$$$', list(__this.name for __this in ugly_monster.inventory))
            print('$$$', list([getattr(ugly_monster.weapon, 'name', None),
                        getattr(ugly_monster.armor, 'name', None), getattr(ugly_monster.shield, 'name', None)]))

        elif 'status' in action in action:
            print_cinematics(Hero.declare_status)

        elif action.startswith('draw'):
            item: str = action.replace('draw', '').replace('weapon', '').lstrip()
            if not Hero.weapon:
                print('You have no weapons.')
            else:
                weapon = Hero.get_equiped_item(item)
                if not weapon:
                    print(f'{item.title()} is not your main weapon.')
                else:
                    print(f'{Hero.draw_weapon}.')

        elif action.startswith('drop'):
            what: str = action.replace('drop', '').lstrip()
            drop(what, scenario)

        elif action.startswith('equip'):
            what: str = action.replace('equip', '').lstrip()
            equip(what)

        else:
            print('You can\'t do that.')
