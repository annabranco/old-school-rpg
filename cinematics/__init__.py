from core_elements import print_cinematics
from mechanics import actions
from core_elements.characters.Hero import Hero
from core_elements.characters import NPC

# PRINTS GENERAL CINEMATICS


def start_encounter(enemy: NPC) -> None:
    '''
        It is called when an encounter with a possible enemy starts.
    '''
    print_cinematics(enemy.declare_status)
    actions.encounter_reaction(enemy)
