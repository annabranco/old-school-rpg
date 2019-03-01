description = 'a vast green field full of trees. \
Near you there are some bushes and far away you can see a river flowing from the left \
to the right. The trail you\'ve been following seems to go on until a bridge on the river'

floor = []
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

ambient = ['trail', 'field']
has_something = ['bushes', 'trees']
far_away = ['river', 'bridge']