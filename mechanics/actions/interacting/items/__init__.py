from core.elements import Item
from core.scenario import Scenario
from core.characters.Hero import Hero
from typing import Union
from core.elements import Element, Item, Container
# DETERMINES THE MECHANICS RELATED TO INTERACTING WITH ITEMS


# take
'''
    It is called when the Hero tries to get something from the Scenario.
'''
def take(object: str, scenario: Scenario):
	__object: str = object.replace(' ', '_').lower()
	print(Hero.inventory)
	if __object in scenario.ambient:
			print(
				f'There\'s no point in doing it.')
	elif __object in scenario.far_away:
			print(
            f'Even if you could take it, it is too far away.')
	elif hasattr(scenario.floor, __object):
				this_object: Item = getattr(scenario.floor, __object)
				if item_in_inventory(this_object):
					print(
						f'You already have {object} on your inventory.')
				else:
					Hero.get_item(this_object)
					if not hasattr(this_object, 'on_taking') and this_object.on_taking != 'keep':
						delattr(scenario.floor, __object)
	elif hasattr(scenario, __object):
			this_object: Element = getattr(scenario, __object)
			if type(this_object) == Container:
					print(
							f'You cannot take it.')
			elif this_object.weight >= Hero.carrying_capacity:
				print(f'It is too much for you to carry.')
			elif item_in_inventory(this_object):
					print(
						f'You already have {object} on your inventory.')
			else:
				Hero.get_item(this_object)
				if not hasattr(this_object, 'on_taking') and this_object.on_taking != 'keep':
					delattr(scenario, __object)
	else:
			print(
					f'You don\'t see any {object} nearby to take it.')

# take
'''
    Generic function to check if the Hero has an Item in the inventory.
'''
def item_in_inventory(object: Union[str, Item]):
	if type(object) == str:
		for __object in Hero.inventory:
			if type(__object) == Item:
				return __object.name == object
			elif type(__object) == str:
				return __object == object
			else:
				return __object["name"] == object
	else:
		return object in Hero.inventory