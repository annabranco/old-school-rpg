import cinematics
from core.scenario import Scenario
from core.elements import Item, Container
import gameplay
from db.enemies import ugly_monster
from core.config import *
from db.food import *
from db.valuables import *


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
testing_forest.far_away = ['river', 'bridge']


# ELEMENTS THAT CAN BE USED AS SAFE PLACES FOT THE HERO TO HIDE AND REST.
testing_forest.safe_places = ['bushes']


# EXIT POINTS THAT CONNECT TO OTHER SCENARIOS.


# GLOBAL CONTAINERS FROM THE SCENARIO THAT CAN BE IMMEDIATELLY INTERACTED WITH.
trees = Container('trees', 'are apple trees full of apples')

bushes = Container('bushes', 'are 3 feet green bushes full of leaves')
bushes.searching_effect = ['You spend a very long time searching the bushes and start to feel tired.', 'tired']


# SPECIFIC ITEMS THAT CANNOT BE IMMEDIATELLY INTERACTED WITH.
trees.add_item(apples)
apples.on_taking = lambda: 'keep'

bushes.add_item(golden_coin)
golden_coin.hidden = True


# ADDS GLOBAL CONTAINERS TO THE SCENARIO INSTANCE SO THEY CAN BE INTERACTED WITH.
testing_forest.add_to_scenario('bushes', bushes)
testing_forest.add_to_scenario('trees', trees)


# STARTING CINEMATICS
print_cinematics(f'You are on a large green field. You hear some steps coming from behind a group of trees. ')
print_cinematics(
    f'You see an {ugly_monster.name} coming from behind them. It seems to be looking for something on the ground.')
print_cinematics(
    f'He suddently sees you and grunts unknown words approaching its hand to a heavy club hanging from its belt.')


cinematics.start_encounter(ugly_monster)
