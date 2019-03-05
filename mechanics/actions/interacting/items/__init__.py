from core.elements import Item
from core.scenario import Scenario
from core.characters.Hero import Hero
from typing import Union
from core.elements import Element, Item, Container

def take(object: str, scenario: Scenario):
	_object:str = object.replace(' ', '_').lower()

	if _object in scenario.ambient:
			print(
				f'There\'s no point in doing it.')
	elif _object in scenario.far_away:
			print(
            f'Even if you could take it, it is too far away.')
	elif hasattr(scenario.floor, _object):
				this_object: Item = getattr(scenario.floor, _object)
				Hero.get_item(this_object)
				delattr(scenario.floor,_object)
	elif hasattr(scenario, _object):
			this_object: Element = getattr(scenario, _object)
			if type(this_object) == Container:
					print(
							f'You cannot take it.')
			elif this_object.weight >= Hero.carrying_capacity:
				print(f'It is too much for you to carry.')
			else:
				Hero.get_item(this_object)
				delattr(scenario,_object)
	else:
			print(
					f'You don\'t see any {object} nearby to take it.')