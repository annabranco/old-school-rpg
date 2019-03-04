from core.config import *

def look(what, scenario):

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
		if type(getattr(scenario, what)) == list:
			looking_place = getattr(scenario, what)[0]
		else:
			looking_place = getattr(scenario, what)

		if getattr(looking_place, 'on_looking'):
			looking_place.on_looking('trees')
		print_cinematics(
			f'The {what} {looking_place.get("description")}.')
	else:
		print_cinematics(
			f'There is nothing to be seen.')
