from textwrap import dedent
from core.config import print_cinematics, cinematics_block
import cinematics
from core.characters.Hero import Hero
# Prints cinematics of the actions.


# victory
'''
    It is called when Hero wins a combat.
'''
def victory():
    cinematics_block()
    Hero.declare_status()
    print_cinematics('You win!\n')


# victory
'''
    It is called when Hero kills an enemy on combat.
'''
def killed_enemy(you, enemy):
    cinematics_block()
    print_cinematics(
        f'You give a mortal thrust of your {you.weapon.name} and {enemy.name} falls dead.\n')
    victory()


# victory
'''
    It is called when Hero kills an enemy on combat on a simultaneous attack.
'''
def killed_enemy_on_simultaneous_attack(you, enemy):
    cinematics_block()
    print_cinematics(f'''
        You give a heavy blow on {enemy.name} and hear some bones crushing while its body falls with a last moan.
        You breath deeply with relief starting to feel the pain of the damage you took.
        ''')
    victory()
