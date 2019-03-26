from core.characters import NPC
from db.weapons import *
from db.armors import *
from db.shields import *
from db.food import *

# DEFINES DATABASE FOR ALL ENEMIES
'''
    constructor = NPC(name: str, race: str, gender: str='undefined')
'''

# UGLY MONSTER
'''
    This is a generic unpleasant monster, for combat testing.
    Normally this guy will be killed by the Hero when figthing.
'''
# 0. Identification
ugly_monster = NPC('Ugly Monster', 'monster', 'undefined')
# 1. Basic attributes
ugly_monster.attack = 2
ugly_monster.defense = 2
ugly_monster.speed = 2
ugly_monster.full_hp = ugly_monster.hp = 2
# 2. Weapons
ugly_monster.weapon = club
ugly_monster.armor = leather_armor
ugly_monster.shield = small_shield
# 3. Inventory
ugly_monster.inventory.append(smelly_meat)
smelly_meat.add(10)
# 4. Status
ugly_monster.status = 'angry'

# STRONG MONSTER
'''
    This is a generic stronger monster, for combat testing.
        Normally this guy will kill the Hero when figthing.
'''
# 0. Identification
strong_monster = NPC('Strong Monster', 'monster')
# 1. Basic attributes
strong_monster.attack = 5
strong_monster.defense = 5
strong_monster.full_hp = strong_monster.hp = 20
strong_monster.speed = 2
# 2. Weapons
strong_monster.weapon = heavy_club
# 3. Inventory
strong_monster.inventory = [{'name': 'food', 'quantity': 10}]
# 4. Status
strong_monster.status = 'very angry'
