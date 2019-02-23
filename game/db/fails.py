from db.hero import Hero
from mechanics.combat import combat_mechanics
# ATTACK


def disastrous_fail_on_attack(successes, attacker, defendant):
		if attacker == Hero:
				print('You lose your balance and fall on the ground.\n')
		else:
				print(
						f'{attacker["name"]} loses the balance and falls on the ground.\n')
		combat_mechanics.next_round(attacker, defendant)

# DEFEND

# DEXTERITY CHECK

# STRENGTH CHECK

# MENTAL CHECK

# CHARISMA CHECK


