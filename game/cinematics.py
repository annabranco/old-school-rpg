import actions
from core.config import print


def start_encounter(enemy):
    print(f'You see {enemy["name"]}.\n')
    declare_enemy_status(enemy)
    actions.encounter_reaction(enemy)


def declare_enemy_status(enemy):
    print(f'{enemy["name"]} looks {enemy["status"][0]}.')
