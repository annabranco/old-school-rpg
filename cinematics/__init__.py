from core.config import print_cinematics
from mechanics import actions
from core.characters.Hero import Hero


def start_encounter(enemy):
    print_cinematics(f'You see {enemy.name}.\n')
    print_cinematics(enemy.declare_status())
    actions.encounter_reaction(enemy)


def declare_hero_status():
    print_cinematics(f'You are {Hero["status"][0]}.')
