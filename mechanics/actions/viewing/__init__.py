from core.config import *
from core.scenario import Scenario


def look(place: str, scenario: Scenario):
    _place = place.replace(' ', '_').lower()

    if _place == '' or _place == 'around':
        print_cinematics(
            f'You look around and you see {scenario.description}.')
    elif _place in scenario.ambient:
        print_cinematics(
            f'You see nothing special about the {place}.')
    elif _place in scenario.far_away:
        print_cinematics(
            f'You look at the {place}, but is too far away to see any details.')

    elif hasattr(scenario, _place):
        looking_place = getattr(scenario, _place)
        print_cinematics(
            f'The {place} {looking_place.description}.')
        looking_place.on_looking()
    else:
        print_cinematics(
            f'There is nothing to be seen.')


def search(place: str, scenario: Scenario):
    _place = place.replace(' ', '_').lower()

    if place in scenario.ambient:
        print_cinematics(f'You search the {place} but you find nothing.')
    elif place in scenario.far_away:
        print_cinematics(f'It is too far away.')

    elif hasattr(scenario, _place):
        searching_place = getattr(scenario, _place)
        searching_place.on_searching()
    else:
        print_cinematics(
            f'There is nothing to be found.')
