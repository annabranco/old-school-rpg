from mechanics.combat import initiative
from mechanics.combat import attack
from mechanics.combat import defend
from mechanics.combat.combat_rounds import combat_rounds
from core.config import *


def ask_for_action():
		print_cinematics('What do you do?')
		return input('\n\t\t> ')

def encounter_reaction(enemy):
		action = ask_for_action()
		print('\n')
		if enemy['status'][0] == 'unaware' or enemy['status'][0] == 'sleeping':
			encounter_reaction_unaware(action, enemy)
		else:
			encounter_reaction_aware(action, enemy)

def encounter_reaction_unaware(action, enemy):
		if action == 'attack':
			print_cinematics(
					f'You draw your sword and strike before {enemy["name"]} has a chance to understand what is happening.')
			mechanics_block('SNEAK ATTACK')
			attack.attack(enemy, 2, True)
			combat_rounds.took_action['enemy'] = True
		elif action == 'wait' or action == 'defend':
			print_cinematics(
					f'You stand on your position, but {enemy["name"]} just doesn\'t notice you.')
			encounter_reaction(enemy)

def encounter_reaction_aware(action, enemy):
		if action == 'attack':
				print_cinematics(
						f'You draw your sword and quickly strike {enemy["name"]}.')
				mechanics_block('COMBAT')
				attack.attack(enemy, 0, False)

		elif action == 'wait':
				print_cinematics(
						f'You wait to see the reaction of the {enemy["name"]}. He draws a club and comes to attack you.')
				print_cinematics('You draw your sword and prepare to face him.')
				initiative.initiative(enemy, 0)
		elif action == 'defend':
				print_cinematics(
						f'You put yourself on a defensive stance while the {enemy["name"]} draws a club and comes to attack you.')
				mechanics_block('COMBAT')
				combat_rounds.took_action['Hero'] = True
				defend.defend(enemy, 0, True)