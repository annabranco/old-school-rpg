from core.config import *
from core.scenario import Scenario
from core.characters.Hero import Hero
from core.elements import Item
from core.characters import NPC

# DETERMINES THE MECHANICS RELATED TO VIEWING THINGS


# look
'''
    It is called when the Hero looks at something.
'''
def look(element: str, scenario: Scenario):
    __element = system_name(element)

    if __element == 'floor':
        if len(scenario.floor) == 0:
            print('There\'s nothing special on the floor.')
        else:
            print_cinematics(
                f'Looking at the floor you find:')
            for __item in scenario.floor:
                if issubclass(type(__item), object) or type(__item) == Item:
                    print(f'\t- {__item.name}',)
                elif type(__item) == dict:
                    print(f'\t- {__item["name"]}',)
                else:
                    print(f'\t- {__item}',)

    elif __element == '' or __element == 'around':
        print_cinematics(
            f'You look around and you see {scenario.description}.')

    elif __element in scenario.ambient:
        print_cinematics(
            f'You see nothing special about the {element}.')

    elif __element in scenario.far_away:
        print_cinematics(
            f'You look at the {element}, but is too far away to see any details.')


    elif hasattr(scenario, __element):
        looking_element = getattr(scenario, __element)
        print_cinematics(
            f'The {element} {looking_element.description}.')
        looking_element.on_looking()

    elif Hero.has_item(__element):
        print(
            f'The {element} on your inventory is {Hero.get_item_from_inventory(__element).description}.')

    elif __element == 'body':
        for __something in scenario.floor:
            if system_name(__something.name).startswith(__element):
                print(
                    f'The {__something.name} laying on the floor is {__something.description}.')

                if type(__something) == NPC:
                    looking_body(__something, scenario)

    elif any(__element == system_name(__something.name) for __something in scenario.floor):
        for __something in scenario.floor:
            if system_name(__something.name) == __element:
                print(
                    f'The {element} laying on the floor is {__something.description}.')
                if type(__something) == NPC:
                    looking_body(__something, scenario)

    else:
        print_cinematics(
            f'There is nothing to be seen.')


# looking_body
'''
    It is called when the Hero look to an enemy dead body.
'''
def looking_body(body: NPC, scenario: Scenario):
    if body.armor:
        print(
            f'It is wearing a {body.armor.name}.')
        scenario.add_to_floor(body.armor)
        body.armor = None

    if body.weapon:
        print(
            f'On the body you you see a {body.weapon.name}.')
        scenario.add_to_floor(body.weapon)
        body.weapon = None

    if body.shield:
        print(
            f' And also a {body.shield.name}.')
        scenario.add_to_floor(body.shield)
        body.shield = None


# search
'''
    It is called when the Hero searched somewhere.
'''
def search(element: str, scenario: Scenario):
    __element = element.replace(' ', '_').lower()

    if element in scenario.ambient:
        print_cinematics(f'You search the {element} but you find nothing.')
    elif element in scenario.far_away:
        print_cinematics(f'It is too far away.')

    elif hasattr(scenario, __element):
        searching_element = getattr(scenario, __element)
        searching_element.on_searching()

    elif __element == 'body':
        for __something in __element.inventory:
            if system_name(__something.name).startswith(__element):
                print(
                    f'The {__something.name} laying on the floor is {__something.description}.')

    else:
        print_cinematics(
            f'There is nothing to be found.')
