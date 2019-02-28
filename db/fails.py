from core.characters.Hero import Hero
from mechanics.combat import combat_mechanics
from core.config import print_cinematics, cinematics_block

# ATTACK


def disastrous_fail_on_attack(successes, attacker, defendant):
    cinematics_block()
    if attacker == Hero:
        print_cinematics('You lose your balance and fall on the ground.\n')
    else:
        print_cinematics(
            f'{attacker.name} loses the balance and falls on the ground.\n')
    cinematics_block()
    combat_mechanics.next_round(attacker, defendant)

# DEFEND

# DEXTERITY CHECK

# STRENGTH CHECK

# MENTAL CHECK

# CHARISMA CHECK
