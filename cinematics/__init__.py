from core.config import print_cinematics
from mechanics import actions
from db.hero import Hero

def start_encounter(enemy):
    print_cinematics(f'You see {enemy["name"]}.\n')
    declare_enemy_status(enemy)
    actions.encounter_reaction(enemy)

def declare_enemy_status(enemy):
    print_cinematics(f'{enemy["name"]} looks {enemy["status"][0]}.')

def declare_hero_status():
    print_cinematics(f'You are {Hero["status"][0]}.')

