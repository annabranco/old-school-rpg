from core.characters import NPC
# DEFINES DATABASE FOR ALL ENEMIES


# Ugly Monster
'''
    This is a generic unpleasant monster, for combat testing.
		Normally this guy will be killed by the Hero when figthing.
'''
ugly_monster = NPC('Ugly Monster', 'monster')
ugly_monster.weapon = {'name': 'club', 'type': 'blunt', 'bonus': 0}
ugly_monster.inventory = [{'name': 'food', 'quantity': 10}]
ugly_monster.attack = 2
ugly_monster.defense = 2
ugly_monster.full_hp = 2
ugly_monster.speed = 2
ugly_monster.hp = 2
ugly_monster.status = 'angry'


# Strong Monster
'''
    This is a generic stronger monster, for combat testing.
		Normally this guy will kill the Hero when figthing.
'''
strong_monster = NPC('Strong Monster', 'monster')
strong_monster.weapon = {'name': 'heavy club', 'type': 'blunt', 'bonus': 0}
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
