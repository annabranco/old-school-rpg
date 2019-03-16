from core.characters import NPC
from db.weapons import *
from db.armors import *
from db.shields import *
from db.food import *

# DEFINES DATABASE FOR ALL ENEMIES
'''
    #constructor = NPC(name: str, race: str, gender: str='undefined')
    if enemy has an armor, you should state  the attribute on_taking after assigning the armor
        <NPC>.armor.on_taking = lambda: print(
            f'You remove {<Armor>.name} from the {<NPC>.name}.')
'''

# Ugly Monster
'''
    This is a generic unpleasant monster, for combat testing.
        Normally this guy will be killed by the Hero when figthing.
'''
ugly_monster = NPC('Ugly Monster', 'monster', 'undefined')
ugly_monster.weapon = club
ugly_monster.armor = leather_armor
ugly_monster.shield = small_shield
ugly_monster.armor.on_taking = lambda: print(
    f'You remove {leather_armor.name} from the {ugly_monster.name}.')

ugly_monster.inventory.append(smelly_meat)
smelly_meat.add(10)

ugly_monster.full_hp = ugly_monster.hp = 2
ugly_monster.attack = 2
ugly_monster.defense = 2
ugly_monster.speed = 2
ugly_monster.status = 'angry'

# Strong Monster
'''
    This is a generic stronger monster, for combat testing.
        Normally this guy will kill the Hero when figthing.
'''
strong_monster = NPC('Strong Monster', 'monster')
strong_monster.weapon = heavy_club
strong_monster.inventory = [{'name': 'food', 'quantity': 10}]
strong_monster.attack = 5
strong_monster.defense = 5
strong_monster.full_hp = 20
strong_monster.speed = 2
strong_monster.hp = 20
strong_monster.status = 'very angry'

# ugly_monster = NPC('Ugly Monster', 'monster')
# ugly_monster_stats = {
#     'attack': 1,
#     'defense': 9,
#     'total_hp': 2,
#     'hp': 1,
#     'status': ['angry', 3],
#     'speed': 1,
#     'weapon':  {'name': 'club', 'type': 'blunt', 'bonus': 0}
# }
