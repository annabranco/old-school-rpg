from cinematics.fails import disastrous_fail_on_attack
from core.characters.Hero import Hero
from db.enemies import ugly_monster
from mechanics.actions import *
from gameplay.testing_forest import testing_forest

# ugly_monster.weapon = {'name': 'short bow', 'type': 'range'}
# Hero.status = 'happy'
# print(Hero.get_status)
# print(Hero.name)
# print(Hero.declare_status())

# print(getattr(testing_forest, 'apples'))
basic_actions(testing_forest)

# disastrous_fail_on_attack(5, ugly_monster, Hero)
