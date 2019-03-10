from core.scenario import Scenario
from core.elements import Item, Container
import gameplay
# A TESTING SCENARIO
# This scenario is just for testing purposes


# CREATES A TESTING SCENARIO INSTANCE AND ADDS ITS ATTRIBUTES
testing_forest = Scenario('testing_forest', 'scene01', 'a forest')
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


# SPECIFIC ITEMS THAT CANNOT BE IMMEDIATELLY INTERACTED WITH.
apples = Item('apples', 'look juicy red', 0.2)
apples.on_taking = lambda : 'keep'

golden_coin = Item('golden coin', 'a very old coin made of gold', 0)
golden_coin.hidden = True


# GLOBAL CONTAINERS FROM THE SCENARIO THAT CAN BE IMMEDIATELLY INTERACTED WITH.
trees = Container('trees', 'are apple trees full of apples')
trees.apples = apples

bushes = Container('bushes', 'are 3 feet green bushes full of leaves')
bushes.searching_effect = ['You spend a very long time searching the bushes and start to feel tired.', 'tired']
bushes.golden_coin = golden_coin


# ADDS GLOBAL CONTAINERS TO THE SCENARIO INSTANCE SO THEY CAN BE INTERACTED WITH.
testing_forest.add_to_scenario('bushes', bushes)
testing_forest.add_to_scenario('trees', trees)
