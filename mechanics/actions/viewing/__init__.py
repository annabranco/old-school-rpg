from core.config import *
from core.scenario import Scenario


def look(what: str, scenario: Scenario):

	if what == '' or what == 'around':
		print_cinematics(
				f'You look around and you see {scenario.description}.')
	elif what in scenario.ambient:
		print_cinematics(
				f'You see nothing special about the {what}.')
	elif what in scenario.far_away:
		print_cinematics(
				f'You look at the {what}, but is too far away to see any details.')

	elif hasattr(scenario, what):
		looking_place = getattr(scenario, what)
		looking_place.on_looking()
		print_cinematics(
				f'The {what} {looking_place.description}.')
	else:
		print_cinematics(
				f'There is nothing to be seen.')


def search(place: str, scenario: Scenario):

	if place in scenario.ambient:
			print_cinematics(f'You search the {place} but you find nothing.')
	elif place in scenario.far_away:
			print_cinematics(f'It is too far away.')

	elif hasattr(scenario, place):
			searching_place = getattr(scenario, place)
			searching_place.on_searching()
	else:
			print_cinematics(
					f'There is nothing to be found.')
