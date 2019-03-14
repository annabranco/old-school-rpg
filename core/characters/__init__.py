from math import ceil
from typing import Dict, List, Union
from core.elements import Item, Weapon, Shield, Armor
from core.config import*
import gameplay
# DEFINES BASIC LOGICS FOR CHARACTERS

# Character
'''
    CLASS used for all characters on the game.
'''


class Character(object):

    def __init__(self, name: str, type: str, race: str):
        self.name: str = name
        self.type: str = type
        self.race: str = race
        self.description: str = f'This is the {name}'
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

    @property
    def status(self) -> str:
        return self.__status

    @property
    def declare_status(self) -> None:
        if self.type == 'Player':
            return f'You are {self.__status}'
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
                'You have no items on your inventory.', 'On your inventory you have']
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
            if self.shield and self.shield.name.endswith(element):
                return True
            if self.armor and self.armor.name.endswith(element):
                return True
        else:
            if element in self.inventory:
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
        if self.__shield:
            self.inventory.append(self.__shield)
        self.__shield = this_shield

    @property
    def armor(self) -> Armor:
        if self.__armor:
            return self.__armor

    @armor.setter
    def armor(self, this_armor: Armor) -> None:
        if self.__armor:
            self.inventory.append(self.__armor)
        self.__armor = this_armor

    @property
    def weapon(self) -> Weapon:
        if self.__weapon:
            return self.__weapon

    @weapon.setter
    def weapon(self, this_weapon: Weapon) -> None:
        if self.__weapon:
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

    def draw_weapon(self) -> None:
        if not self.weapon["name"]:
            if self.type == 'Player':
                print(f'You have no weapon.')
            else:
                exit(
                    f'{self.name} doesn\'t have a weapon. This is probably a mistake on your code.')
        else:
            if self.weapon["type"] == 'blade':
                action = ['unsheathe', 'unsheathes']
            elif self.weapon["type"] == 'range':
                action = ['place an arrow on', 'places an arrow on']
            elif self.weapon["type"] == 'blunt':
                action = ['draw', 'draws']

            if self.type == 'Player':
                print(f'You {action[0]} your {self.weapon["name"]}.')
            else:
                print(f'{self.name} {action[1]} a {self.weapon["name"]}.')

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

    def drop_item(self, item: Item = None):
        if self.has_item(item):
            print(f'{self.name} drops drop {item.name}.')
            self.inventory.remove(item)
            return item
        else:
            print(f'You don\'t have {item} on your inventory.')

# Player


'''
    CLASS used exclusivelly for the Hero (controlled by the player).
'''


class Player(Character):

    def __init__(self, name='Hero', race='human'):
        super(Player, self).__init__(name, 'Player', race)
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

    def __init__(self, name: str='Ugly Monster', race: str='humanoid', pronom: str='it'):
        super(NPC, self).__init__(name, 'NPC', race)
        self.weight: int = 8
        self.__pronom = pronom

    @property
    def pronom(self):
        if self.__pronom == 'she':
            return ('she', 'her', 'her')
        elif self.__pronom == 'he':
            return ('he', 'his', 'him')
        elif self.__pronom == 'it':
            return ('it', 'its', 'it')
        else:
            return ('they', 'their', 'them')

    @property
    def verb(self):
        if self.__pronom in ('she', 'he', 'it'):
            return 'is'
        else:
            return 'are'

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
