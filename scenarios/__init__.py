class Scenario(object):
    def __init__(self, name, scene):
        self.scene = scene
        self.name = name
        self.description = 'a dull boring vast desert full of sand'
        self.encounter_rate = 0
        self.hiding_places = []
        self.status_on_entering = ''
        self.ambient = ['sand']
        self.has_something = []
        self.far_away = []
        self.floor = []
        self.exits = []
