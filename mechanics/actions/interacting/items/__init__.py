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


def take(element: str, scenario: Scenario):
    __element: str = element.replace(' ', '_').lower()

    if any(__item.endswith(element) for __item in scenario.ambient):
        print('There\'s no point in doing it.')

    elif any(__item.endswith(element) for __item in scenario.far_away):
        print('Even if you could take it, it is too far away.')

    elif any(__item.name.endswith(element) for __item in scenario.floor) or \
        any(__item.name.startswith('body') for __item in scenario.floor):
        for __item in scenario.floor:
            if __item.name.endswith(__element) or __item.name.startswith('body'):
                this_element: Item = __item
        if Hero.has_item(this_element):
            print(f'You already have {element} on your inventory.')
        else:
            if hasattr(this_element, 'on_taking') and this_element.on_taking() == 'keep':
                pass
            else:
                scenario.floor.remove(this_element)
            Hero.get_item(this_element)

    elif any(__item.name.endswith(element) for __item in scenario.elements):
        this_element: Element = scenario.get_element(element)

        if type(this_element) == Container:
            print('You cannot take it.')

        elif this_element.weight >= Hero.carrying_capacity: # TODO
            print('It is too much for you to carry.')

        elif Hero.has_item(this_element): # TODO
                print(f'You already have {element} on your inventory.')

        else:
            Hero.get_item(this_element)
            if not hasattr(this_element, 'on_taking') and this_element.on_taking != 'keep':
                delattr(scenario, __element)

    else:
        print(f'You don\'t see any {element} nearby to take it.')

# take


'''
    Generic function to check if the Hero has an Item in the inventory.
'''


def drop(element: str, scenario: Scenario):
    if not element:
        print('Which item would you like to drop?')
        Hero.declare_inventory()
        which_item = input('> ')
        __element: str = which_item.lower()

    else:
        __element: str = element.lower()

    this_element: Item = Hero.get_item_from_inventory(__element)
    if this_element:
        if this_element not in scenario.floor:
            scenario.add_to_floor(this_element)
        Hero.drop_item(this_element)
    else:
        equiped_item: Item = Hero.get_equiped_item(__element)
        if equiped_item:
            scenario.add_to_floor(equiped_item)
            Hero.drop_item(equiped_item)
        else:
            print('You can\'t drop items that you don\'t have.')

# TODO NOW - items and characters
def equip(item: str):
    Hero.equip(item)
