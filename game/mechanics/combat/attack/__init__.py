from core.config import *
from db.hero import Hero
from mechanics.global_mechanics.rolls.rolls import roll_dices
from mechanics.combat import combat_mechanics
from mechanics.combat.combat_rounds import combat_rounds
from db import fails

# define texts by types of weapons


def attack(enemy, bonus=0, surprise_attack=False):

		combat_rounds.took_action['Hero'] = True

		if surprise_attack == True:
				difficult = 2
		else:
				difficult = enemy['defense']

		base_attack = Hero['attack'] + bonus
		results_number, results_text = roll_dices(base_attack, difficult, f'Attacking {enemy["name"]}')

		if results_text == 'epic':
				print('Epic success on attack')
				combat_mechanics.damage(results_number, Hero, enemy)
		elif results_text == 'decisive' or results_number > 0:
				combat_mechanics.damage(results_number, Hero, enemy)
		elif results_text == 'critical':
				print('Critical fail on attack')
				fails.disastrous_fail_on_attack(results_number, Hero, enemy)
		elif results_text == 'disastrous':
				print('Disastrous fail on attack')
				fails.disastrous_fail_on_attack(results_number, Hero, enemy)
		else:
				combat_mechanics.missed(Hero, enemy)

