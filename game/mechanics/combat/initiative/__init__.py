from core.config import *
from mechanics.combat.combat_rounds import combat_rounds
from db.hero import Hero
from random import randint
from mechanics.combat import attack
from mechanics.combat import defend

def initiative(enemy, bonus=0):
		print('An initiative should be rolled to know who strikes first.')
		combat_rounds.took_action['Hero'] = False
		combat_rounds.took_action['enemy'] = False
		initiative_difficulty = 6

		Hero_initiative = 0
		Hero_rolls = []
		h = 0
		while h < Hero['speed'] + bonus:
				Hero_rolls.append(randint(1, 10))
				h += 1
		print(str(Hero_rolls))
		for roll in Hero_rolls:
				if roll >= initiative_difficulty:
						Hero_initiative += 1
		print(str(Hero_initiative))

		enemy_initiative = 0
		enemy_rolls = []
		e = 0
		while e < enemy['speed']:
				enemy_rolls.append(randint(1, 10))
				e += 1
		print(str(enemy_rolls))
		for roll in enemy_rolls:
				if roll >= initiative_difficulty:
						enemy_initiative += 1
		print(str(enemy_initiative))

		compare_initiatives(Hero_initiative, enemy_initiative, enemy)


def compare_initiatives(Hero_initiative, enemy_initiative, enemy):
		if Hero_initiative > enemy_initiative:
				print('You strike first.')
				combat_rounds.took_action['Hero'] = True
				attack.attack(enemy, 0, False)

		elif Hero_initiative < enemy_initiative:
				print(f'{enemy["name"]} strikes first.')
				combat_rounds.took_action['enemy'] = True
				defend.defend(enemy, 1, False)

		else:
				print('Simultaneous attack.')
				combat_rounds.took_action['Hero'] = True
				combat_rounds.took_action['enemy'] = True