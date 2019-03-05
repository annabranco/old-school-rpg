from core.scenario import Scenario
from core.elements import Item, Container
import gameplay

# CREATES A SPECIFIC SCENARIO INSTANCE AND ADDS ITS ATTRIBUTES
testing_forest = Scenario('testing_forest', 'scene01', 'a forest')
testing_forest.description = 'a vast green field full of trees. \
Near you there are some bushes and far away you can see a river flowing from the left \
to the right. The trail you\'ve been following seems to go on until a bridge on the river'
testing_forest.ambient = ['trail', 'field']
testing_forest.far_away = ['river', 'bridge']
testing_forest.hiding_places = ['bushes']
gameplay.CURRENT_SCENARIO = testing_forest

# SPECIFIC ELEMENTS THAT CANNOT BE IMMEDIATELLY INTERACTED WITH.
apples = Item('apples', 'look juicy red', 'apples')

# GLOBAL ELEMENTS FROM THE SCENARIO THAT CAN BE IMMEDIATELLY INTERACTED WITH.
trees = Container('trees', 'are apple trees full of apples', 'trees')
trees.apples = apples

golden_coin = Item('golden coin', 'a very old coin made of gold', 'coin')
golden_coin.hidden = True

bushes = Container('bushes', 'are 3 feet green bushes full of leaves', 'bushes')
bushes.searching_effect = ['You spend a very long time searching the bushes and start to feel tired.', 'tired']
bushes.golden_coin = golden_coin


# ADD GLOBAL ELEMENTS TO THE SCENARIO INSTANCE SO THEY CAN BE INTERACTED WITH.
testing_forest.add_to_scenario('bushes', bushes)
testing_forest.add_to_scenario('trees', trees)
