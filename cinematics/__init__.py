from core.config import print_cinematics
from mechanics import actions
from core.characters.Hero import Hero


# PRINTS GENERAL CINEMATICS


def start_encounter(enemy):
    '''
        It is called when an encounter with a possible enemy starts.
    '''
    print_cinematics(enemy.declare_status)
    actions.encounter_reaction(enemy)
