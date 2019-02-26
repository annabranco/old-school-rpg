from math import ceil


class Character(object):
    def __init__(self, name, type, race):
        self.name = name
        self.type = type
        self.race = ''
        self.weapon = {'name': '', 'bonus': 0}
        self.shield = {'name': '', 'bonus': 0}
        self.armor = {'name': '', 'bonus': 0}
        self.inventory = []
        self.attack = 0
        self.defense = 0
        self.full_hp = 0
        self.hp = 0
        self.status = ''

    def change_status(self):
        if self.hp <= 0:
            self.status = 'dead'
        elif self.hp == self.full_hp:
            self.status = 'well'
        elif self.hp <= ceil(self.full_hp / 3):
            self.status = 'severily wounded'
        elif self.hp <= ceil(self.full_hp * 2 / 3):
            self.status = 'wounded'
        else:
            self.status = 'lightly wounded'

    def take_damage(self, damage):
        self.hp = self.hp - damage
        self.change_status()

    def get_status(self):
        print(f'You are {self.status}')

    def get_hp(self):
        print(f'{self.name}\'s current HP: {self.hp}')


class Player(Character):

    def __init__(self, name='Hero', race='human'):
        super(Player, self).__init__(name, 'Player', race)
        self.status = 'well'

    def get_item(self, item):
        self.inventory.append(item)


Hero = Player('Anna', 'elf')
Hero.full_hp = Hero.hp = 6
Hero.get_item('sword')
long_sword = {'name': 'Long sword', 'bonus': 2}
Hero.get_item(long_sword)
Hero.take_damage(6)
Hero.get_hp()
Hero.get_status()
