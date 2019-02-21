from random import randint
from mechanics.global_mechanics import modifiers
from db.hero import Hero
import actions
import cinematics
from core.config import print
from mechanics.global_mechanics.rolls import roll_dices
from mechanics.combat.combat_mechanics import cause_damage, missed
from db.fails import disastrous_fail_on_attack
# define texts by types of weapons


def attack(enemy, bonus=0, surprise_attack=False):

		if surprise_attack == True:
				difficult = 2
		else:
				difficult = enemy['defense']

		base_attack = Hero['attack'] + bonus
		results_number, results_text = roll_dices(base_attack, difficult, f'Attacking {enemy["name"]}')

		if results_text == 'epic':
				print('Epic success on attack')
				cause_damage(results_number, Hero, enemy)
		elif results_text == 'decisive' or results_number > 0:
				cause_damage(results_number, Hero, enemy)
		elif results_text == 'critical':
				print('Critical fail on attack')
				disastrous_fail_on_attack(results_number, Hero, enemy)
		elif results_text == 'disastrous':
				print('Disastrous fail on attack')
				disastrous_fail_on_attack(results_number, Hero, enemy)
		else:
				missed(Hero, enemy)

