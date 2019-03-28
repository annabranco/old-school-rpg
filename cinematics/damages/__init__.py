from core_elements import print_cinematics, cinematics_block
from core_elements.characters.Hero import Hero
from core_elements.characters import Character

# PRINTS CINEMATICS OF DAMAGES

# TODO: Internationalization

def cause_damage(attacker: Character, defendant: Character, severity: int):
    '''
        It is called in combat situations when a character inflicts
        damage upon another one
    '''
    cinematics_block()
    if attacker == Hero:
        print_cinematics(
            f'You strike a blow on {defendant.name}, causing some blood to spill.\n')
    else:
        print_cinematics(
            f'{attacker.name} hits you causing a painful bruise.\n')

    cinematics_block()
