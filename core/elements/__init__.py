import gameplay
from core.config import *


class Element(object):
		def __init__(self, name, description):
				self.name: str = name
				self.description: str = description
				self.scenario: str = ''
				self.looking_effect: str = None
				self.searching_effect: str = None
				self.on_hearing = None
				self.hearing_effect: str = None
				self.on_touching = None
				self.touching_effect: str = None
				self.on_tasting = None
				self.tasting_effect: str = None

		# FUNCTION: on_looking
		'''
		DESCRIPTION: If the place looked upon has visible elements (ej. apples on trees),
		the items are added to the Scenario instance and can now be also interacted to with.
		Hidden elements are only found with on_serching.
		'''

		def on_looking(self, callback=None) -> None:
				for attr, value in self.__dict__.items():
						if type(value) == Item and value.hidden == False:
								system_name = value.name.replace(' ', '_').lower()
								gameplay.CURRENT_SCENARIO.add_to_scenario(
										system_name, value)

	 # FUNCTION: on_looking
		'''
		DESCRIPTION: If the place looked upon has visible elements (ej. apples on trees),
		the items are added to the Scenario instance and can now be also interacted to with.
		Hidden elements are only found with on_serching.
		'''

		def on_searching(self, callback=None) -> None:
				print(f'searching {self.name}')
				for attr, value in self.__dict__.items():
						if type(value) == Item and value.hidden == True:
								value.hidden == False
								print_cinematics(f'You find {value.name}')
								system_name = value.name.replace(' ', '_').lower()
								gameplay.CURRENT_SCENARIO.add_to_scenario(
										system_name, value)


class Container(Element):
		def __init__(self, name, description):
				super(Container, self).__init__(name, description)


class Item(Element):
		def __init__(self, name, description):
				super(Item, self).__init__(name, description)
				self.hidden = False
				self.usable = False


class Weapon(Item):
		def __init__(self, name, description):
				super(Weapon, self).__init__(name, description)
				self.type = ''
				self.bonus = 0


class Shield(Item):
		def __init__(self, name, description):
				super(Shield, self).__init__(name, description)
				self.type = ''
				self.bonus = 0


class Armor(Item):
		def __init__(self, name, description):
				super(Armor, self).__init__(name, description)
				self.type = ''
				self.bonus = 0


'''
	class Element(object):
	def __init__(self, name, description):
		self.name = name
		self.description = description

		on_looking =
		'looking_effect': 'tired'

		'on_searching': 'You spend a very long time searching the bushes and start to feel tired.',
		'searching_effect': 'tired'

'''
