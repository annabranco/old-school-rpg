import cinematics
from core.scenario import Scenario
from core.elements import Item, Container
import gameplay
from db.enemies import ugly_monster
from core.config import *
from db.food import *
from db.valuables import *
from core.characters.Hero import Hero

# A TESTING SCENARIO
# This scenario is just for testing purposes

# CREATES A TESTING SCENARIO INSTANCE AND ADDS ITS ATTRIBUTES
testing_forest = Scenario('testing_forest', 'scene01', 'forest')
gameplay.CURRENT_SCENARIO = testing_forest
testing_forest.description = 'a vast green field full of trees. \
Near you there are some bushes and far away you can see a river flowing from the left \
to the right. The trail you\'ve been following seems to go on until a bridge on the river'

# ELEMENTS THAT CAN BE LIMITEDLY INTERACTED WITH.
testing_forest.ambient = ['trail', 'field']
testing_forest.far_away = ['river', 'old bridge']

# ELEMENTS THAT CAN BE USED AS SAFE PLACES FOT THE HERO TO HIDE AND REST.
testing_forest.safe_places = ['bushes']

# EXIT POINTS THAT CONNECT TO OTHER SCENARIOS.

# GLOBAL CONTAINERS FROM THE SCENARIO THAT CAN BE IMMEDIATELLY INTERACTED WITH.
trees = Container('trees', 'big and very green apple trees')

bushes = Container('bushes', '3 feet green bushes full of leaves')
bushes.searching_effect = [
    'You spend a very long time searching the bushes and start to feel tired.', lambda : Hero.set_status('tired')]
    # TODO: up one degree.. well -> tired -> very tired

# SPECIFIC ITEMS THAT CANNOT BE IMMEDIATELLY INTERACTED WITH.
trees.add_item(apple)
apple.add()
# apple.on_taking = lambda: 'keep'

bushes.add_item(golden_coin, 'hidden')
golden_coin.hidden = True

# ADDS GLOBAL CONTAINERS TO THE SCENARIO INSTANCE SO THEY CAN BE INTERACTED WITH.
testing_forest.add_to_scenario('bushes', bushes)
testing_forest.add_to_scenario('trees', trees)

# ADDS AN ENEMY
npc = ugly_monster

# STARTING CINEMATICS
print_cinematics(
    f'You are on a large green field. You hear some steps coming from behind a group of trees. ')
print_cinematics(
    f'You see {npc.article[0]}{npc.name} coming from behind them. {npc.pronom[0].title()} seems to be looking for something on the ground.')
print_cinematics(
    f'{npc.pronom[0].title()} suddently sees you and grunts unknown words approaching {npc.pronom[1]} hand to {npc.weapon.article[0]}{npc.weapon.name} hanging on {npc.pronom[1]} back.')

cinematics.start_encounter(npc)
