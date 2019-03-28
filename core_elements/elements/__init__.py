import gameplay
from core_elements import *
from typing import List

# DEFINES BASIC LOGICS FOR ELEMENTS AND ITEMS

class Element(object):
    '''
        CLASS used for all interactable elements on the game.
    '''

    def __init__(self, name, description):
        self.name: str = name
        self.description: str = description
        # self.looking_effect: str = None
        # self.searching_effect: List[str] = None
        # self.on_hearing = None
        # self.hearing_effect: str = None
        # self.on_touching = None
        # self.touching_effect: str = None
        # self.on_tasting = None
        # self.tasting_effect: str = None


    @property
    def article(self) -> str:
        if self.name.endswith('s') or self.name.endswith('food'):
            return ('','')
        elif self.name.startswith(('a', 'e', 'i', 'o', 'u', 'y')):
            return ('an ', 'an ')
        else:
            return ('a ', 'a ')

    @property
    def verb(self) -> str:
        if self.name.endswith('s') or self.name.endswith('food'):
            return 'are'
        else:
            return 'is'

    def on_looking(self) -> None:
        '''
            If the place looked upon has visible elements (ej. apples on trees),
            the items are added to the elements List of the Scenario instance and can now be also interacted to with.
            Hidden elements should be on a Container and are only found with on_searching.
        '''
        things_saw: List = []

        for __item in gameplay.CURRENT_SCENARIO.elements:
            if issubclass(type(__item), Item):
                if __item.container == self.name:
                    things_saw.append(__item)

                if len(things_saw) == 1:
                    this_element = things_saw[0]
                    print_cinematics(
                        f'You see {this_element.article[0]}{this_element.name} on the {self.name}')
                elif len(things_saw) > 1:
                    print_cinematics(
                        f'You see \
                        {", ".join(f"{this_element.article[0]}{this_element.name}" for item in things_saw[: -1])} \
                        and {f"{things_saw[-1].article[0]}{things_saw[-1].name}"} on the {self.name}.')

        for property_name, property_value in self.__dict__.items():
            if issubclass(type(property_value), Item) or type(property_value) == Item:
                if property_value.hidden == False:
                    if not property_name in gameplay.CURRENT_SCENARIO.elements:
                        print_cinematics(
                            f'You see {property_value.name} on the {self.name}')
                        gameplay.CURRENT_SCENARIO.add_to_elements(property_value)
                        delattr(self, property_name)
                        break

    def on_taking(self, callback=None):
        '''
        called when Hero takes an item with on_taking attribute.
        '''
        if callback:
            callback()


class Item(Element):
    '''
        CLASS used exclusively for items that can be taken and/or used by the Hero.
    '''

    def __init__(self, name: str, description: str, weight: int, quantity: int = 1):
        super(Item, self).__init__(name, description)
        self.usable: bool = False
        self.container: str = None
        self.hidden: bool = False
        self.unity_weight: int = weight
        self.__quantity: int = quantity
        self.weight: int = weight * quantity

    @property
    def verb(self) -> str:
        if type(self) == Food:
            if self.__quantity <= 1 and not self.name.endswith('food'):
                return 'look'
            else:
                return 'looks'
        else:
            if self.__quantity <= 1:
                return 'is'
            else:
                return 'are'

    def add(self, how_many: int = 'countless') -> int:
        if how_many == 'countless':
            self.on_taking = lambda: 'keep'
            self.name += 's'
            self.__quantity = 1
        else:
            self.__quantity += how_many
            self.update_quantity()
            return (self.__quantity)

    def remove(self, how_many: int):
        self.__quantity -= how_many
        self.update_quantity()
        return (self.__quantity)

    def update_quantity(self):
        self.weight = self.unity_weight * self.__quantity
        if self.__quantity <= 1 and not self.name.endswith('food'):
            if self.name[-1] == 's':
                self.name = self.name[:-1]
        elif self.__quantity > 1 and not self.name.endswith('food'):
            if self.name[-1] != 's':
                self.name = f'{self.name}s'
        self.verb

    @property
    def quantity(self):
        return self.__quantity



class Container(Element):
    '''
        CLASS used exclusively for elements that contain another elements (ej. a chest).
    '''

    def __init__(self, name: str, description: str):
        super(Container, self).__init__(name, description)


    def add_item(self, item: Item, hidden: str = None):
        if hidden == 'hidden':
            item.hidden = True
        setattr(item, 'container', self.name)
        setattr(self, item.name, item)


    def on_searching(self) -> None:
        '''
            If the place looked upon has hidden items,
            they are added to the Scenario instance and can now be also interacted to with.
            Visible items are not found here with on_serching, but seen with on_looking.
        '''
        if getattr(self, 'searching_effect', None):
            print_cinematics(self.searching_effect[0])
            self.searching_effect[1]()

        for property_name, property_value in self.__dict__.items():

            if issubclass(type(property_value), Item) and property_value.hidden == True:
                property_value.hidden = False
                print_cinematics(f'You find {property_value.name}')
                gameplay.CURRENT_SCENARIO.add_to_elements(property_value)
                delattr(self, property_name)
                return
        print_cinematics(
            f'You search the {self.name} but you find nothing special.')


class Food(Item):

    def __init__(self, name: str, description: str, weight: int, quantity: int = 0):
        self.description: str = description
        super(Food, self).__init__(name, self.description, weight, quantity)
        self.usable: bool = True



class Weapon(Item):
    '''
        CLASS used exclusively for Weapons.
    '''

    def __init__(self, name: str, description: str, weight: int, weapon_type: str, bonus: int):
        super(Weapon, self).__init__(name, description, weight)
        self.type: str = weapon_type
        self.bonus: str = bonus

    @property
    def draw_action(self) -> List[str]:
        if self.type == 'blade':
            return ['unsheathe', 'unsheathes']
        elif self.type == 'range':
            return [f'get an arrow and draw', 'gets an arrow and draws']
        elif self.type == 'blunt':
            return ['draw', 'draws']


class Shield(Item):
    '''
        CLASS used exclusively for Shields.
    '''

    def __init__(self, name: str, description: str, weight: int, bonus: int):
        super(Shield, self).__init__(name, description, weight)
        self.bonus: int = bonus


class Armor(Item):
    '''
        CLASS used exclusively for Armors.
    '''

    def __init__(self, name: str, description: str, weight: int, bonus: int):
        super(Armor, self).__init__(name, description, weight)
        self.bonus: int = bonus

    def on_taking(self):
        if self.container:
            print(
                f'You remove the armor from the {self.container}.')


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
