from core.config import print_cinematics, cinematics_block
from core.characters.Hero import Hero
from core.characters import Character
# Prints cinematics of the actions.


# cause_damage
'''
    It is called in combat situations when a character inflicts
    damage upon another one
'''

def cause_damage(attacker: Character, defendant: Character, severity: int):
    cinematics_block()

    if attacker == Hero:
        print_cinematics(
            f'You strike a blow on {defendant.name}, causing some blood to spill.\n')
    else:
        print_cinematics(
            f'{attacker.name} hit you causing a painful bruise.\n')

    cinematics_block()
