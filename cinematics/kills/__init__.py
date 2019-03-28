from textwrap import dedent
from core_elements import print_cinematics, cinematics_block
import cinematics
from core_elements.characters.Hero import Hero


# PRINTS CINEMATICS OF KILLS


def victory():
    '''
        It is called when Hero wins a combat.
    '''
    cinematics_block()
    print_cinematics(Hero.declare_status)
    print_cinematics('You win!\n')


def killed_enemy(you, enemy):
    '''
        It is called when Hero kills an enemy on combat.
    '''
    cinematics_block()
    print_cinematics(
        f'You give a mortal thrust of your {you.weapon.name} and {enemy.name} falls dead.\n')
    victory()


def killed_enemy_on_simultaneous_attack(you, enemy):
    '''
        It is called when Hero kills an enemy on combat on a simultaneous attack.
    '''
    cinematics_block()
    print_cinematics(f'''
        You give a heavy blow on {enemy.name} and hear some bones crushing while {enemy.pronom[1]} body falls with a last moan.
        You breath deeply with relief starting to feel the pain of the damage you took.
        ''')
    victory()
