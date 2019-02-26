class Character(object):
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.race = ''
        self.weapon = {name: '', bonus: 0}
        self.shield = {name: '', bonus: 0}
        self.armor = {name: '', bonus: 0}
        self.inventory = []
        self.attack = 0
        self.defense = 0
        self.full_hp = 0
        self.hp = 0
        self.status = []

        def take_damage(self, damage):
            self.hp = self.hp - damage
            if self.hp <= 0:
                change_status('dead')
            elif self.hp == full_hp:
                change_status('well')
            elif self.hp <= full_hp / 3:
                change_status('severily wounded')
            elif self.hp <= full_hp * 2 / 3:
                change_status('wounded')
            else:
                change_status('lightly wounded')

        def change_status(self, new_status):

        def declare_status(self):
            print(f'You are {self.status[0]}')
