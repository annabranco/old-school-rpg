from textwrap import dedent
from core.config import print_cinematics, cinematics_block
import cinematics
from core.characters.Hero import Hero


def victory():
    cinematics_block()
    Hero.declare_status()
    print_cinematics('You win!\n')
    exit(0)


def killed_enemy(you, enemy):
    cinematics_block()
    print_cinematics(
        f'You give a mortal thrust of your {you.weapon["name"]} and {enemy.name} falls dead.\n')
    victory()


def killed_enemy_on_simultaneous_attack(you, enemy):
    cinematics_block()
    print_cinematics(f'''
		You give a heavy blow on {enemy.name} and hear some bones crushing while its body falls with a last moan.
		You breath deeply with relief starting to feel the pain of the damage you took.
		''')
    victory()
