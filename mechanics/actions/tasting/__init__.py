# TODO
from core_elements.elements import Food
from core_elements import system_name, print_cinematics,\
    system_name_with_article
from core_elements.scenario import Scenario
from core_elements.characters.Hero import Hero

def eat(element: Food, scenario: Scenario):
    __element = system_name(element)

    if Hero.has_item(__element):
        this_item = Hero.get_item_from_inventory(__element)
        if type(this_item) == Food:
            print(f'You eat {system_name_with_article(this_item.name)}.')
            this_item.remove(1)
            if this_item.quantity == 0:
                print(f'You have no more {this_item.name}s left.')

                Hero.inventory.remove(this_item)

    elif any(system_name(__item.name).split()[-1] == __element for __item in scenario.elements) or \
        any(system_name(__something.name).split()[-1] == __element for __something in scenario.floor):
        print_cinematics('You can only eat things that you have with you.')


    elif any(system_name(__something.name).startswith('body') for __something in scenario.floor) and 'body' in __element:
        for __something in scenario.floor:
            if element.startswith('body') and system_name(__something.name).startswith('body'):
                print(
                  f'You would need to be really starving to death to even think about eathing the {__something.name}.')

        #         print(
        #             f'The {__something.name} laying on the floor {__something.verb} {__something.description}.')
        #         if type(__something) == NPC:
        #             looking_body(__something, scenario)

    else:
        print_cinematics(
            f'You can\'t eat that.')
