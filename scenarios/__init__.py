class Scenario(object):
    def __init__(self, name, scene, short_description):
        self.scene = scene
        self.name = name
        self.short_description = 'desert'
        self.description = 'a dull boring vast desert full of sand'
        self.encounter_rate = 0
        self.encounters = []
        self.hiding_places = []
        self.status_on_entering = ''
        self.ambient = ['sand']
        self.has_something = []
        self.far_away = []
        self.floor = []
        self.exits = []
        self.special_death = []
        self.special_kill = []

    def add(self, field, value):
        setattr(self, field, value)

