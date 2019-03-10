from core.config import print_cinematics, cinematics_block
from core.characters.Hero import Hero
# Prints cinematics of the actions.


# the_end
'''
    It is called when the adventure finishes.
'''
def the_end():
    print_cinematics('That\'s the end of your adventure...\n\n')
    exit(1)


# death_by_combat
'''
    It is called when Hero is killed by an enemy on combat.
'''
def death_by_combat(Hero, enemy):
    cinematics_block()
    print_cinematics(f'''
        You feel an intense pain with the blow of {enemy.name} seconds after everything turns black
        and your body falls without life on the ground.\n
        ''')
    the_end()


# mutual_death_by_combat
'''
    It is called when both Hero and the enemy kill each other simultaneously on combat
'''
def mutual_death_by_combat(enemy):
    cinematics_block()
    print_cinematics(f'''
        Terrifying cries of pain are heard from both sides when you and {enemy.name}\'s weapons crush each others bodies.
        Both of you fall almost simultaneously on the ground to never get up again.
        ''')
    the_end()


# death_by_simultaneous_attack
'''
    It is called when Hero dies on a simultaneous attack, but the enemy survives
'''
def death_by_simultaneous_attack(enemy, results_number_hero):
    cinematics_block()
    if results_number_hero == 0:
        print_cinematics(f'''
        You realize with horror that you missed your attack on {enemy.name} at the same time its {enemy.weapon.name} crushes your head.
        Feeling the most intense pain ever, everything turns black and you feel your dying body falling on the ground.
                ''')
    else:
        print_cinematics(f'''
        You feel a milisecond of joy when your {Hero.weapon.name} pierces the body of {enemy.name}.
        But you have no time to celebrate, as his weapon falls heavily on the top of your head crushing your skull and brains on a bloody mess.
                ''')
    the_end()

# types of weapons
