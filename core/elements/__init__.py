class Element(object):
	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.on_looking = None
		self.looking_effect = None
		self.on_searching = None
		self.searching_effect = None
		self.on_hearing = None
		self.hearing_effect = None
		self.on_touching = None
		self.touching_effect = None
		self.on_tasting = None
		self.tasting_effect = None

class Container(Element):
	def __init__(self, name, description):
		super(Container, self).__init__(name, description)

class Item(Element):
	def __init__(self, name, description):
		self.hidden = False
		self.usable = False

class Weapon(Item):
	def __init__(self, name, description):
		super(Container, self).__init__(name, description)
		self.type = ''
		self.bonus = 0

class Shield(Item):
	def __init__(self, name, description):
		super(Container, self).__init__(name, description)
		self.type = ''
		self.bonus = 0

class Armor(Item):
	def __init__(self, name, description):
		super(Container, self).__init__(name, description)
		self.type = ''
		self.bonus = 0

'''
	class Element(object):
	def __init__(self, name, description):
		self.name = name
		self.description = description

		on_looking =
		'looking_effect': 'tired'

		'on_searching': 'You spend a very long time searching the bushes and start to feel tired.',
		'searching_effect': 'tired'

'''