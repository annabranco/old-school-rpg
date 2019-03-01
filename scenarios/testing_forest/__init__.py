from scenarios import Scenario

testing_forest = Scenario('Forest', 'scene01', 'a forest')
testing_forest.description = 'a vast green field full of trees. \
Near you there are some bushes and far away you can see a river flowing from the left \
to the right. The trail you\'ve been following seems to go on until a bridge on the river'
testing_forest.ambient = ['trail', 'field']
testing_forest.far_away = ['river', 'bridge']
testing_forest.has_something = ['bushes', 'trees']
testing_forest.hiding_places = ['bushes']

bushes = [
    {'special': 'You spend a very long time searching the bushes and start to feel tired.', 'status': 'tired'},
    {
        'description': 'are high green bushes full of leaves',
        'name': 'coin',
        'hidden': True,
    }]
trees = [
    {'special': None},
    {
        'description': 'are apple trees full of apples',
        'name': 'apples',
        'hidden': False,
    }]
testing_forest.add('bushes', bushes)
testing_forest.add('trees', trees)

