import actions
from core.config import print
from db.hero import Hero

def start_encounter(enemy):
    print(f'You see {enemy["name"]}.\n')
    declare_enemy_status(enemy)
    actions.encounter_reaction(enemy)


def declare_enemy_status(enemy):
    print(f'{enemy["name"]} looks {enemy["status"][0]}.')

def declare_hero_status(enemy):
    print(f'You are {Hero["status"][0]}.')

