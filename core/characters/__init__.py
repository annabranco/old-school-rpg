from math import ceil
from typing import Dict, List, Union, Tuple
from core.elements import Item, Weapon, Shield, Armor
from core.config import*
import gameplay
# DEFINES BASIC LOGICS FOR CHARACTERS

# Character
'''
    CLASS used for all characters on the game.
'''


class Character(object):

    def __init__(self, name: str, type: str, race: str, gender: str = 'undefined'):
        self.name: str = name
        self.type: str = type
        self.race: str = race
        self.description: str = f'This is {name}'
        self.__weapon: Dict[[str, str], [str, str][str, int]] = None
        self.__shield: Dict[[str, str], [str, str][str, int]] = None
        self.__armor: Dict[[str, str], [str, str][str, int]] = None
        self.inventory: List[str] = []
        self.attack: int = 0
        self.defense: int = 0
        self.full_hp: int = 0
        self.hp: int = 0
        self.speed: int = 0
        self.__status: str = 'unknown'
        self.gender: str = gender
        self.pronom: Tuple[str] = None
        self.appearance = None
        self.set_pronom()
        self.set_appearance()

    def set_pronom(self):
        pronoms_list = {
            'she': ('she', 'her', 'her'),
            'he': ('he', 'his', 'him'),
            'it': ('it', 'its', 'it'),
            'they': ('they', 'their', 'them')
        }

        if self.gender == 'female':
            self.pronom = pronoms_list['she']
        elif self.gender == 'male':
            self.pronom = pronoms_list['he']
        elif self.gender == 'undefined':
            self.pronom = pronoms_list['it']
        elif self.gender == 'non-binary' or self.gender == 'other':
            print('--- Config information needed ---')
            print(f'As your character is identified as {self.gender}, you should state')
            print('which pronom would you like to be used when refering to you?')
            print('eg. she, he, it, they...')
            my_pronom = None
            while not my_pronom:
                my_pronom = input('>> ')
            self.pronom = pronoms_list[my_pronom]
        else:
            self.pronom = pronoms_list['they']

    def set_appearance(self):
        if not self.appearance:
            attributes = (self.attack, self.defense, self.speed)
            better_attribute = max(attributes)
            quality = 'dangerous'
            if attributes.index(better_attribute) == 1:
                quality = 'strong'
            elif attributes.index(better_attribute) == 2:
                quality = 'skillful'
            self.appearance = f'a {quality} {self.gender} {self.race}'

    @property
    def verb(self):
        if self.pronom[0] in ('she', 'he', 'it'):
            return 'is'
        else:
            return 'are'

    @property
    def status(self) -> str:
        return self.__status

    @property
    def declare_status(self) -> None:
        if self.type == 'Player':
            return f'You are {self.__status}.'
        else:
            return f'{self.name} looks {self.__status}.'

    @status.setter
    def status(self, new_status: str=None) -> None:
        self.set_status(new_status)

    def set_status(self, new_status: str=None) -> None:
        if not new_status:
            if self.hp <= 0:
                self.__status = 'dead'
                self.on_dead()
            elif self.hp == self.full_hp:
                self.__status = 'well'
            elif self.hp <= ceil(self.full_hp / 3):
                self.__status = 'severily wounded'
            elif self.hp <= ceil(self.full_hp * 2 / 3):
                self.__status = 'wounded'
            else:
                self.__status = 'lightly wounded'
        else:
            self.__status = new_status

    def declare_hp(self) -> None:
        if self.type == 'Player':
            print(f'Your current HP: {self.hp}')
        else:
            print(f'{self.name}\'s current HP: {self.hp}.')

    def take_damage(self, damage: int) -> None:
        self.hp = self.hp - damage
        if self.type == 'Player':
            print(f'You take {damage} damage.')
        else:
            print(f'{self.name} takes {damage} damage.')
        self.declare_hp()
        self.set_status()

    def declare_inventory(self) -> Union[None, str]:

        if self.type == 'Player':
            searching_result_message = [
                'You have no items on your inventory', 'On your inventory you have']
        else:
            searching_result_message = [
                f'Searching the {self.name} you find nothing worth taking',
                f'Searching the {self.name} you find']

        if len(self.inventory) == 0:
            if self.type == 'Player':
                print_cinematics(f' {searching_result_message[0]}.')
            else:
                return f' {searching_result_message[0]}.'

        elif len(self.inventory) == 1:
            if self.type == 'Player':
                print_cinematics(
                    f'{searching_result_message[1]} {self.inventory[0].article[0]}{self.inventory[0].name}.')
            else:
                return f'{searching_result_message[1]} {self.inventory[0].article[0]}{self.inventory[0].name}.'

        else:
            if self.type == 'Player':
                print_cinematics(
                    f'{searching_result_message[1]} {", ".join(f"{item.article[0]}{item.name}" for item in self.inventory[: -1])} and {f"{self.inventory[-1].article[0]}{self.inventory[-1].name}"}.')
            else:
                return f'{searching_result_message[1]} {", ".join(f"{item.article[0]}{item.name}" for item in self.inventory[: -1])} and {f"{self.inventory[-1].article[0]}{self.inventory[-1].name}"}.'

    def has_item(self, element: Union[str, Item]) -> bool:
        if type(element) == str:
            for __element in self.inventory:
                if __element.name.endswith(element) or \
                    __element.name.startswith('body') and element.startswith('body'):
                        return True
            if self.weapon and self.weapon.name.endswith(element):
                return True
            elif self.shield and self.shield.name.endswith(element):
                return True
            elif self.armor and self.armor.name.endswith(element):
                return True
        else:
            if element in self.inventory:
                return True
            elif self.weapon and self.weapon == element:
                return True
            elif self.shield and self.shield == element:
                return True
            elif self.armor and self.armor == element:
                return True
        return False

    def get_item_from_inventory(self, element: Union[str, Item]) -> Item:
        if self.has_item(element):
            if type(element) == str:
                for __element in self.inventory:
                    if __element.name.endswith(element) or \
                       __element.name.startswith('body') and element.startswith('body'):
                        return __element

            else:
                return element in self.inventory
        else:
            if type(self) == Player:
                print(f'You don\'t have {element} on your inventory.')
            else:
                print(f'{self.name} doesn\'t seem to have {element}')

    @property
    def shield(self) -> Shield:
        if self.__shield:
            return self.__shield

    @shield.setter
    def shield(self, this_shield: Shield) -> None:
        if self.__shield and type(self) == Player:
            self.inventory.append(self.__shield)
        self.__shield = this_shield

    @property
    def armor(self) -> Armor:
        if self.__armor:
            return self.__armor

    @armor.setter
    def armor(self, this_armor: Armor) -> None:
        if self.__armor and type(self) == Player:
            self.inventory.append(self.__armor)
        self.__armor = this_armor

    @property
    def weapon(self) -> Weapon:
        if self.__weapon:
            return self.__weapon

    @weapon.setter
    def weapon(self, this_weapon: Weapon) -> None:
        if self.__weapon and type(self) == Player:
            self.inventory.append(self.__weapon)
        self.__weapon = this_weapon

    def equip(self, item: Item) -> None:
        this_item = self.get_item_from_inventory(item)
        if this_item:
            if type(this_item) == Weapon:
                self.weapon = this_item
                if self.weapon.type == 'blunt':
                    print_cinematics(f'You hang it on your belt.')
                    print_cinematics(f'The {self.weapon.name} is now your main weapon.')
                if self.weapon.type == 'blade':
                    print_cinematics(f'You sheathe it carrefully.')
                    print_cinematics(f'The {self.weapon.name} is now your main weapon.')
                if self.weapon.type == 'range':
                    print_cinematics(f'You place it on your back ready for a quick draw.')
                    print_cinematics(f'The {self.weapon.name} is now your main weapon.')
            elif type(this_item) == Shield:
                self.shield = this_item
                print_cinematics(f'You strap it in your arm.')
                print_cinematics(f'You are now using the {self.shield.name}.')
            elif type(this_item) == Armor:
                old_one = ''
                if self.armor:
                    old_one = f'strip yourself of the {self.armor.name} and '
                print_cinematics(f'You {old_one}wear the {this_item.name}.')
                self.armor = this_item
            else:
                print(f'You can\'t equip {this_item.article[0]}{this_item.name}.')

            self.inventory.remove(this_item)

        else:
                print('You can only equip items that you have on your inventory.')

    def get_equiped_item(self, item: str) -> Union[Weapon, Shield, Armor]:
        if self.weapon and self.weapon.name.lower().endswith(item):
            return self.weapon
        elif self.shield and self.shield.name.lower().endswith(item):
            return self.shield
        elif self.armor and self.armor.name.lower().endswith(item):
            return self.armor
        else:
            return None

    @property
    def draw_weapon(self) -> str:
        if not self.weapon:
            if self.type == 'Player':
                print(f'You have no weapon.')
            else:
                exit(f'{self.name} doesn\'t have a weapon. This is probably a mistake on your code.')
        else:
            action = self.weapon.draw_action
            if self.type == 'Player':
                return f'You {action[0]} your {self.weapon.name}'
            else:
                return f'{self.name} {action[1]} {self.pronom[1]} {self.weapon.name}'

# TODO: change threat level when drawn. tired when drawn for a while. not draw twice. def put away

    def on_dead(self):
        if type(self) == Player and gameplay.CURRENT_SCENARIO.special_death:
            print('This scenario has a special death cinematics')
        elif type(self) == NPC and gameplay.CURRENT_SCENARIO.special_kill:
            print('This scenario has a special kill cinematics')
        else:
            self.name = f'body of {self.name}' if type(
                self) == Player else f'body of the {self.name}'
            self.description = 'soaked in blood'
            gameplay.CURRENT_SCENARIO.add_to_floor(self)
        if self.armor:
            self.armor.bonus = self.armor.bonus - 1
            if self.armor.bonus == 0:
                self.armor.name = f'destroyed {self.armor.name}'
            else:
                self.armor.name = f'damaged {self.armor.name}'

    def drop_item(self, item: Item = None) -> Union[Item, List[Item]]:
        if item and self.has_item(item):
            equiped_item = self.get_equiped_item(item)
            if equiped_item:
                if type(equiped_item) == Weapon:
                    self.weapon = None
                    print(f'You place your {equiped_item.name} on the ground.')
                    print(f'You are now unarmed.') # TODO status change

                if type(equiped_item) == Shield:
                    self.shield = None
                    print(f'You unstrap your {equiped_item.name} and drop it.')
                    if self.armor == None:
                        print(f'You are now unprotected.')  # TODO status change

                if type(equiped_item) == Armor:
                    self.armor = None
                    print(f'You strip your {equiped_item.name} off and drop it to the ground.')
                    if self.shield == None:
                        print(f'You are now unprotected.')  # TODO status change

            elif item in self.inventory:
                if type(self) == Player:
                    print(f'You drop the {item.name}.')
                else:
                    print(f'{self.name} drops the {item.name} to the ground.')
                self.inventory.remove(item)
                return item

        elif item == None: # This is only called when a body is moved and drops the items it was holding
            print(f'$$$ {self.weapon.name},  {self.armor.name},  {self.shield.name}')
            items_body_has_equiped = []
            if self.weapon:
                items_body_has_equiped.append(self.weapon)
                self.weapon = None
            if self.shield:
                items_body_has_equiped.append(self.shield)
                self.shield = None
            return items_body_has_equiped

        else:
            print(f'You don\'t have {item.name} on your inventory.')

# Player


'''
    CLASS used exclusivelly for the Hero (controlled by the player).
'''


class Player(Character):

    def __init__(self, name: str = 'Hero', race: str = 'human', gender: str = 'non-binary'):
        super(Player, self).__init__(name, 'Player', race, gender)
        self.status = 'well'
        self.carrying_capacity = 10

    def get_item(self, item: Union[Item, str]) -> None:
        print(f'You get the {item.name}.')
        self.inventory.append(item)

    def drop_item(self, item: Item):
        if self.has_item(item):
            print(f'You drop {item.name}.')
            self.inventory.remove(item)
        else:
            print(f'You don\'t have {item} on your inventory.')

# NPC


'''
    CLASS used exclusively for Non Player Characters.
'''


class NPC(Character):

    def __init__(self, name: str='Thing', race: str='humanoid', gender: str = 'undefined'):
        super(NPC, self).__init__(name, 'NPC', race, gender)
        self.weight: int = 8

    @property
    def article(self) -> str:
        if self.name.endswith('s') or self.name.endswith('food'):
            first_time = ''
        elif self.name.startswith(('a', 'e', 'i', 'o', 'u', 'y')):
            first_time = 'an '
        else:
            first_time = 'a '
        return (first_time, 'the ')

    def set_name(self, new_name):
        self.name = new_name
        print(f'The {self.race} tells you {self.pronom[1]} name is {self.name}.')

    def declare_action(self, action):
        print(f'{self.name} {self.verb} {action}.')
