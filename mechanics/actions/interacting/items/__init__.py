from core.elements import Item
from core.scenario import Scenario
from core.characters.Hero import Hero
from typing import Union
from core.elements import Element, Item, Container
import gameplay
from core.config import system_name
# DETERMINES THE MECHANICS RELATED TO INTERACTING WITH ITEMS


# take
'''
    It is called when the Hero tries to get something from the Scenario.
'''
def take(object: str, scenario: Scenario):
    __object: str = object.replace(' ', '_').lower()

    if __object in scenario.ambient:
        print('There\'s no point in doing it.')

    elif __object in scenario.far_away:
        print('Even if you could take it, it is too far away.')

    elif any(system_name(__object) == system_name(__item.name) for __item in scenario.floor):
        for __item in scenario.floor:
            if system_name(__object) == system_name(__item.name):
                this_object: Item = __item
        if Hero.has_item(this_object):
            print(f'You already have {object} on your inventory.')
        else:
            if hasattr(this_object, 'on_taking') and this_object.on_taking() != 'keep':
                scenario.floor.remove(this_object)
            Hero.get_item(this_object)

    elif hasattr(scenario, __object):
        this_object: Element = getattr(scenario, __object)
        if type(this_object) == Container:
            print('You cannot take it.')
        elif this_object.weight >= Hero.carrying_capacity:
            print('It is too much for you to carry.')
        elif Hero.has_item(this_object):
                print(f'You already have {object} on your inventory.')
        else:
            Hero.get_item(this_object)
            if not hasattr(this_object, 'on_taking') and this_object.on_taking != 'keep':
                delattr(scenario, __object)

    else:
        print(f'You don\'t see any {object} nearby to take it.')

# take
'''
    Generic function to check if the Hero has an Item in the inventory.
'''
def drop(object: str, scenario: Scenario):
    if not object:
        print('Which item would you like to drop?')
        Hero.declare_inventory()
        which_item = input('> ')
        __object: str = which_item.replace(' ', '_').lower()

    else:
        __object: str = object.replace(' ', '_').lower()

    this_object: Item = Hero.get_item_from_inventory(__object)
    if this_object:
        if this_object not in gameplay.CURRENT_SCENARIO.floor:
            gameplay.CURRENT_SCENARIO.add_to_floor(this_object)
        Hero.drop_item(this_object)
