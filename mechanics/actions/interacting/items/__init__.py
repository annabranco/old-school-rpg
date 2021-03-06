from core_elements.elements import Item
from core_elements.scenario import Scenario
from core_elements.characters.Hero import Hero
from core_elements.characters import NPC
from typing import Union
from core_elements.elements import Element, Item, Container
import gameplay
import copy
from core_elements import system_name

# DETERMINES THE MECHANICS RELATED TO INTERACTING WITH ITEMS


def take(element: str, scenario: Scenario) -> None:
    '''
        Function fired when the Player wants the Hero to take something from the Scenario.
    '''
    Hero.update_weigth()
    element = system_name(element)
    if any(__item.endswith(element) for __item in scenario.ambient):
        print('There\'s no point in doing it.')

    elif any(__item.endswith(element) for __item in scenario.far_away):
        print('Even if you could take it, it is too far away.')

    elif any(system_name(__item.name).endswith(element) for __item in scenario.floor) or \
            element.startswith('body'):

        for __item in scenario.floor:
            __item: Union[Item, NPC]
            if system_name(__item.name).startswith('body') and system_name(element).startswith('body') or \
                    system_name(__item.name).endswith(element) and system_name(__item.name).startswith('body'):

                __item.update_weigth()
                if Hero.carrying_weigth + __item.weight > Hero.weigth_capacity:
                    print('It is too much for you to carry.')
                else:
                    moving_body(__item, scenario)
                    Hero.take_item(__item)
                    scenario.floor.remove(__item)

            elif system_name(__item.name).endswith(element):

                if Hero.carrying_weigth + __item.weight > Hero.weigth_capacity:
                    print('It is too much for you to carry.')
                else:
                    if Hero.has_item(__item):
                        owned_item = Hero.get_item_from_inventory(__item)
                        owned_item.change_quantity(__item.quantity)
                        Item_name_in_singular = owned_item.name[:-1]
                        print(
                            f'You get another {Item_name_in_singular}.')
                    else:
                        if hasattr(__item, 'on_taking') and __item.on_taking() == 'keep':
                            __item = copy.copy(__item)
                        else:
                            scenario.floor.remove(__item)
                    Hero.take_item(__item)

    elif any(system_name(__item.name).endswith(element) for __item in scenario.elements):
        this_element: Element = scenario.get_element(element)

        if type(this_element) == Container:
            print('You cannot take it.')

        elif Hero.carrying_weigth + this_element.weight > Hero.weigth_capacity:
            print('It is too much for you to carry.')

        elif Hero.has_item(this_element):
            owned_item = Hero.get_item_from_inventory(this_element)
            owned_item.add(this_element.quantity)
            Item_name_in_singular = owned_item.name[:-1]
            print(
                f'You get another {Item_name_in_singular}.')

        else:
            Hero.take_item(this_element)
            if not hasattr(this_element, 'on_taking') or this_element.on_taking() != 'keep':
                scenario.elements.remove(this_element)

    elif element.endswith('armor') and \
        any(type(__thing) == NPC and
            __thing.armor.container != None for __thing in scenario.floor):
        for __thing in scenario.floor:
            if type(__thing) == NPC:
                if __thing.armor != None:
                    __thing.armor.on_taking()
                    __thing.armor.container = None
                    Hero.take_item(__thing.armor)
                    __thing.armor = None

    else:
        print(f'You don\'t see any {element} nearby to take it.')


def moving_body(body: NPC, scenario: Scenario) -> None:
    droped_items = body.drop_item()
    Hero.appearance = 'all bloodstained'
    if len(droped_items) > 0:
        print(
            f'When you move the body, its \
            {" and ".join(item.name for item in droped_items)} \
            fall{"s" if len(droped_items) == 1 else ""} on the ground.')
    for item in droped_items:
        scenario.add_to_floor(item)


def drop(element: Union[str, NPC], scenario: Scenario) -> None:
    '''
        Function fired when the Player wants the Hero to drop something.
    '''
    if not element:
        print('Which item would you like to drop?')
        Hero.declare_inventory()
        which_item = input('> ')
        __element: str = system_name(which_item)

    else:
        __element: str = system_name(element)

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


def equip(item: str) -> None:
    '''
        Function fired when the Player wants the Hero to equip a weapon, shield or armor.
    '''
    Hero.equip(item)
