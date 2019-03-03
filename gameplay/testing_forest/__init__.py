from core.scenarios import Scenario

# CREATES A SPECIFIC SCENARIO INSTANCE AND ADDS ITS ATTRIBUTES
testing_forest = Scenario('Forest', 'scene01', 'a forest')
testing_forest.description = 'a vast green field full of trees. \
Near you there are some bushes and far away you can see a river flowing from the left \
to the right. The trail you\'ve been following seems to go on until a bridge on the river'
testing_forest.ambient = ['trail', 'field']
testing_forest.far_away = ['river', 'bridge']
testing_forest.hiding_places = ['bushes']



# SPECIFIC ELEMENTS THAT CANNOT BE IMMEDIATELLY INTERACTED WITH.
apples = {
    'name': 'apples',
    'description': 'look juicy red',
}


# GLOBAL ELEMENTS FROM THE SCENARIO THAT CAN BE IMMEDIATELLY INTERACTED WITH.
trees = [
    {
        'description': 'are apple trees full of apples',
        'on_looking': testing_forest.on_looking
    },
    {
        'what': apples,
        'hidden': False
    }]

bushes = [
    {
        'description': 'are 3 feet green bushes full of leaves',
        'on_searching': 'You spend a very long time searching the bushes and start to feel tired.',
        'searching_effect': 'tired'
        },
    {
        'name': 'coin',
        'hidden': True,
    }]


# ADD GLOBAL ELEMENTS TO THE SCENARIO INSTANCE SO THEY CAN BE INTERACTED WITH.
testing_forest.add_to_scenario('bushes', bushes)
testing_forest.add_to_scenario('trees', trees)
