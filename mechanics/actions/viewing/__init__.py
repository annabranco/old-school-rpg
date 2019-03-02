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
			f'You look at the {what}, but is too far away see any details.')
	elif what in scenario.has_something:
		looking_place = getattr(scenario, what)
		print_cinematics(
			f'The {what} {looking_place[0].get("description")}.')
	else:
		print_cinematics(
			f'There is nothing to be seen.')
