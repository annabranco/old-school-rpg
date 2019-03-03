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

    def add_to_scenario(self, field, value):
        setattr(self, field, value)

    # TODO: DEF THIS FUNCTION INSIDE CLASS?
    # FUNCTION: on_looking
    '''
    DESCRIPTION: If the place looked upon has visible elements (ej. apples on trees),
    the items are added to the scenario instance and can now be also interacted to with.
    Hidden elements are only found with on_serching.
    '''
    def on_looking(self, where):
        what = getattr(self, where)
        for item in what:
            if item.get('hidden') == False:
                item_to_add = item["what"]
                self.add_to_scenario(item_to_add["name"], item_to_add)

