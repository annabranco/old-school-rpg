from core.config import print_cinematics
from mechanics import actions
from core.characters.Hero import Hero
# Prints cinematics of the actions.


# start_encounter
'''
    It is called when an encounter with a possible enemy starts.
'''
def start_encounter(enemy):
    print_cinematics(f'You see {enemy.name}.\n')
    print_cinematics(enemy.declare_status())
    actions.encounter_reaction(enemy)