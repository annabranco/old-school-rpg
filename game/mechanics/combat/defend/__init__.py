from core.config import *
from db.hero import Hero
from mechanics.global_mechanics.rolls.rolls import roll_dices
from mechanics.combat import combat_mechanics
from mechanics.combat.combat_rounds import combat_rounds
import mechanics.combat

from db import fails


def defend(enemy, bonus=0, focus_on_defense=False):
		combat_rounds.took_action['enemy'] = True

		if focus_on_defense:
				print('Hero stands on a defensive stance.')

		difficult = Hero['defense'] + bonus
		base_attack = enemy['attack']

		results_number, results_text = roll_dices(base_attack, difficult, f'Defending {enemy["name"]}')

		if results_text == 'epic':
				print('Epic success on attack')
				combat_mechanics.damage(results_number, enemy, Hero)
		elif results_text == 'decisive' or results_number > 0:
				combat_mechanics.damage(results_number, enemy, Hero)
		elif results_text == 'critical':
				print('Critical fail on attack')
				fails.disastrous_fail_on_attack(results_number, enemy, Hero)
		elif results_text == 'disastrous':
				print('Disastrous fail on attack')
				fails.disastrous_fail_on_attack(results_number, enemy, Hero)
		else:
				combat_mechanics.missed(enemy, Hero)


				# correct text about damage...