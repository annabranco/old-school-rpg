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
                if hasattr(gameplay.CURRENT_SCENARIO, system_name):
                    print_cinematics(
                        f'There is a {value.name} on the {self.name}')
                else:
                    gameplay.CURRENT_SCENARIO.add_to_scenario(
                        system_name, value)

         # FUNCTION: on_looking
    '''
    DESCRIPTION: If the place looked upon has visible elements (ej. apples on trees),
    the items are added to the Scenario instance and can now be also interacted to with.
    Hidden elements are only found with on_serching.
    '''

    def on_searching(self, callback=None) -> None:
        for attr, value in self.__dict__.items():
            if type(value) == Item and value.hidden == True:
                value.hidden = False
                print_cinematics(f'You find {value.name}')
                system_name = value.name.replace(' ', '_').lower()
                gameplay.CURRENT_SCENARIO.add_to_scenario(
                    system_name, value)
                # delattr(self, system_name)
                return
        print_cinematics(f'You search the {self.name} but you find nothing.')


class Container(Element):
    def __init__(self, name: str, description: str):
        super(Container, self).__init__(name, description)


class Item(Element):
    def __init__(self, name: str, description: str, weight: int):
        super(Item, self).__init__(name, description)
        self.hidden: bool = False
        self.usable: bool = False
        self.weight: int = weight


class Weapon(Item):
    def __init__(self, name: str, description: str):
        super(Weapon, self).__init__(name, description)
        self.type: str = ''
        self.bonus: int = 0


class Shield(Item):
    def __init__(self, name: str, description: str):
        super(Shield, self).__init__(name, description)
        self.type: str = ''
        self.bonus: int = 0


class Armor(Item):
    def __init__(self, name: str, description: str):
        super(Armor, self).__init__(name, description)
        self.type: str = ''
        self.bonus: int = 0


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
