from core.config import *
from db.hero import Hero
from db import cinematics
from mechanics.combat.combat_rounds import combat_rounds
from mechanics.combat import initiative
from mechanics.combat import attack
from mechanics.combat import defend

# combat_rounds.took_action = {
# 		'Hero': False,
# 		'enemy': False
# }

def damage(successes, attacker, defendant):
		hp = defendant['hp']
		print(f' {defendant["name"]}\'s HP before attack:')
		print(str(hp))

		new_hp = hp - successes
		print(f' {defendant["name"]}\'s current HP:')
		print(str(new_hp))
		defendant['hp'] = new_hp

		if new_hp <= 0:
				defendant['status'] = ['dead', 0]
				if defendant == Hero:
						death_by_combat(defendant, attacker)
				else:
						killed_enemy(defendant)

		elif new_hp <= hp / 3:
				defendant['status'] = ['severily wounded', 1]
				if defendant == Hero:
						print(f'{attacker["name"]} strikes you causing great pain and damage. You feel badly hurt.\n')
				else:
						print(f'You slash your sword causing a great damage on {defendant["name"]}. It is badly hurt.\n')
		else:
				defendant['status'] = ['wounded', 2]
				cause_wound(attacker, defendant, successes)

		print('\nStart next round.\n')
		next_round(attacker, defendant)


def next_round(attacker, defendant):
		print(combat_rounds.took_action)
		if defendant == Hero and combat_rounds.took_action['Hero'] and combat_rounds.took_action['enemy']:
				initiative.initiative(attacker, 0)
		elif combat_rounds.took_action['Hero'] and combat_rounds.took_action['enemy']:
				initiative.initiative(defendant, 0)
		elif defendant == Hero and combat_rounds.took_action['enemy']:
				cinematics.declare_enemy_status(attacker)
				cinematics.declare_hero_status(defendant)
				attack.attack(attacker, 0, False)
		elif attacker == Hero and combat_rounds.took_action['Hero']:
				cinematics.declare_enemy_status(defendant)
				cinematics.declare_hero_status(attacker)
				defend.defend(defendant, 0, False)
		else:
				print('something went wrong')

def missed(attacker, defendant):
		if attacker == Hero:
				print(f'You miss your blow on {defendant["name"]}.\n')
		else:
				print(f'{attacker["name"]} misses the attack against you.\n')
		next_round(attacker, defendant)



def death_by_combat(Hero, enemy):
		print(
				f'You feel an intense pain with the blow of {enemy["name"]} seconds after everything turns black and your body falls without life on the ground.\n')
		print('That\'s the end of your adventure...\n\n')
		exit(1)


def killed_enemy(enemy):
		print(
				f'You give a mortal thrust of your blade and {enemy["name"]} falls dead.\n')
		print('You win!\n')
		exit(0)


def cause_wound(attacker, defendant, severity):
		print(
				f'You strike a blow on {defendant["name"]}, causing some blood to spill.\n')
