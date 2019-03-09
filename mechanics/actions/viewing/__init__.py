from core.config import *
from core.scenario import Scenario
from core.characters.Hero import Hero
# DETERMINES THE MECHANICS RELATED TO VIEWING THINGS


# look
'''
    It is called when the Hero looks at something.
'''
def look(element: str, scenario: Scenario):
    __element = element.replace(' ', '_').lower()

    print('has', Hero.has_item(__element))
    if __element == '' or __element == 'around':
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

    else:
        print_cinematics(
            f'There is nothing to be seen.')


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
    else:
        print_cinematics(
            f'There is nothing to be found.')
