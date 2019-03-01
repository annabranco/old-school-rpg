from core.characters.Hero import Hero
from mechanics.combat import combat_mechanics
from core.config import print_cinematics, cinematics_block

# ATTACK


def disastrous_fail_on_attack(fails, attacker, defendant):
    fail_types = {}
    if attacker.weapon["type"] == 'range':
        if fails >= 3:
            fails = 3
        fail_types = {
            1: [
                f'You miss {defendant.name} by far and your arrow is lost.',
                f'{attacker.name} misses by far and the arrow is lost.'
            ],
            2: [
                'Your arrow gets stuck on the quiver as you try to draw, and as you push it all your arrows slip out to the ground.',
                f'You start laughing as you see {attacker.name} droping all his arrows when trying to reach for one.'
            ],
            3: [
                f'As you stretch the arroy back to attack, the string just splits in half, making the {attacker.weapon["name"]} useless.',
                f'As {attacker.name} pushes the arrow back on its {attacker.weapon["name"]}, his string just splits.',
            ]
        }
    else:
        if fails >= 4:
            fails = 4
        fail_types = {
            1: [
                'You miss your attack, leaving your guard partially opened.',
                f'{attacker.name} misses the attack, leaving the guard partially opened.'
            ],
            2: [
                'You miss your attack very badly and leave your guard completely opened.',
                f'{attacker.name} misses very badly the attack and leaves the guard completely opened.'
            ],
            3: [
                f'Your attack was very predictable and {defendant.name} parres it sending your {attacker.weapon["name"]} to the ground.',
                f'{attacker.name}\'s attack was very predictable you take the opportunity to parry it and send its {defendant.weapon["name"]} to the ground.',
            ],
            4: [
                'As you step forward to attack and misses it, you lose your balance and ungainly fall to the ground.',
                f'{attacker.name} does  a very weird attack, losing its balance and falling ridiculously to the ground.']
        }

    cinematics_block()
    if attacker == Hero:
        print_cinematics(f'{fail_types[fails][0]}\n')
    else:
        print_cinematics(f'{fail_types[fails][1]}\n')
    cinematics_block()

    combat_mechanics.next_round(attacker, defendant)

# DEFEND

# DEXTERITY CHECK

# STRENGTH CHECK

# MENTAL CHECK

# CHARISMA CHECK
