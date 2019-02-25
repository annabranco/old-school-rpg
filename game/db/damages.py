from core.config import *
from db.hero import Hero

def cause_damage(attacker, defendant, severity):
		cinematics_block()

		if attacker == Hero:
				print_cinematics(
				f'You strike a blow on {defendant["name"]}, causing some blood to spill.\n')
		else:
				print_cinematics(
				f'{attacker["name"]} hit you causing a painful bruise.\n')

		cinematics_block()

