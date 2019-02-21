from mechanics.global_mechanics import modifiers
from random import randint
from db.hero import Hero
from core.config import print
import cinematics
import actions

def dispatch_attack(difficult, base_attack, attacker, defendant):
		if successes < 0:
				epic_fail(successes, attacker)
		elif successes > 1:
				cause_damage(successes, attacker, defendant)
		else:
				missed(attacker, defendant)

def cause_damage(successes, attacker, defendant):
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
				defendant['hp'] = ['wounded', 2]

		print('\nStart next round.\n')
		next_round(defendant, attacker)


def next_round(defendant, attacker):
		if defendant == Hero:
			cinematics.declare_enemy_status(attacker)
			cinematics.declare_hero_status(defendant)
			actions.encounter_reaction(attacker)
		else:
			cinematics.declare_enemy_status(defendant)
			cinematics.declare_hero_status(attacker)
			actions.encounter_reaction(defendant)


def missed(attacker, defendant):
		if attacker == Hero:
				print(f'You miss your blow on {defendant["name"]}.\n')
		else:
				print(f'{attacker["name"]} misses the attack against you.\n')


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


def cause_wound(defendant, attacker, severity):
		print(
				f'You strike a blow on {defendant["name"]}, causing some blood to spill.\n')
