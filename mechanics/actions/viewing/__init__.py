from core.config import *
from core.scenario import Scenario
from core.characters.Hero import Hero
from core.elements import Item, Food
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
            message = 'Looking at the floor you see'
            if len(scenario.floor) == 1:
                print_cinematics(
                    f'{message} {scenario.floor[0].article[1]}{scenario.floor[0].name}.')
            else:
                print_cinematics(
                    f'{message} {", ".join(f"{item.article[1]}{item.name}" for item in scenario.floor[: -1])} and {f"{scenario.floor[-1].article[0]}{scenario.floor[-1].name}"}.')

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
            f'The {element} {looking_element.verb} {looking_element.description}.')
        looking_element.on_looking()

    elif Hero.has_item(__element):
        my_item = Hero.get_item_from_inventory(__element)
        enough_for = ''
        if type(my_item) == Food:
            # I consider that 1weight of food is enough for a full day, so multiplying quantity by the food weight returns for how many days one portion of this food is capable of sustaining the Hero.
            enough_for = f', enough for {int(my_item.quantity * my_item.unity_weight)} days'

        print(
            f'The {element} on your inventory {my_item.verb} {my_item.description}{enough_for}.')

    elif __element == 'body':
        for __something in scenario.floor:
            if system_name(__something.name).startswith(__element):
                print(
                    f'The {__something.name} laying on the floor {__something.verb} {__something.description}.')

                if type(__something) == NPC:
                    looking_body(__something, scenario)

    elif any(__something.name.endswith(__element) for __something in scenario.floor) or \
            any(__something.name.startswith(__element) for __something in scenario.floor):
        for __something in scenario.floor:
            if __something.name.startswith(__element) or __something.name.endswith(__element):
                print(
                    f'The {element} laying on the floor {__something.verb} {__something.description}.')
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
    message = []
    if body.armor:
        message.append(f'it is wearing {body.armor.article[0]}{body.armor.name}')
        scenario.add_to_floor(body.armor)
        body.armor = None

    if body.weapon:
        message.append(
            f'{body.weapon.article[0]}{body.weapon.name}')
        scenario.add_to_floor(body.weapon)
        body.weapon = None

    if body.shield:
        message.append(f'{body.shield.article[0]}{body.shield.name}.')
        scenario.add_to_floor(body.shield)
        body.shield = None

    if len(message) == 0:
        return
    elif len(message) == 1:
        print_cinematics(f'You see {message[0]}.')
    else:
        print_cinematics(
            f'You see {", ".join(message[:-1])} and {message[-1]}.')

# search


'''
    It is called when the Hero searched somewhere.
'''


def search(element: str, scenario: Scenario):
    __element = system_name(element)

    if __element in scenario.ambient:
        print_cinematics(f'You search the {element} but you find nothing.')
    elif __element in scenario.far_away:
        print_cinematics(f'It is too far away.')

    elif hasattr(scenario, __element):
        searching_element = getattr(scenario, __element)
        searching_element.on_searching()

    elif __element == 'body':
        for __something in scenario.floor:
            if system_name(__something.name).startswith(__element):
                in_inventory = __something.declare_inventory()
                for __item in __something.inventory:
                    scenario.add_to_floor(__item)
                    __something.inventory.remove(__item)
                searching_body(in_inventory, __something, scenario)

    else:
        print_cinematics(
            f'There is nothing to be found.')


def searching_body(in_inventory: str, body: NPC, scenario: Scenario):
    message = []
    if body.armor:
        message.append(f'it is wearing {body.armor.article[0]}{body.armor.name}')
        scenario.add_to_floor(body.armor)
        body.armor = None

    if body.weapon:
        message.append(
            f'{body.weapon.article[0]}{body.weapon.name}')
        scenario.add_to_floor(body.weapon)
        body.weapon = None

    if body.shield:
        message.append(f'{body.shield.article[0]}{body.shield.name}.')
        scenario.add_to_floor(body.shield)
        body.shield = None

    if len(message) == 0:
        print_cinematics(in_inventory)
    elif len(message) == 1:
        print_cinematics(f'{in_inventory} You also see {message[0]}.')

    else:
        print_cinematics(
            f'{in_inventory}\n\t\tYou also see {", ".join(message[:-1])} and {message[-1]}.')
