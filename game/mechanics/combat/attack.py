from random import randint
from mechanics.global_mechanics import modifiers
from db.hero import hero
import actions
import cinematics

def attack(bonus, enemy):
	difficult = enemy['defense']
	base_attack = hero['attack'] + bonus
	i = 0
	rolls = []
	while i < base_attack:
		rolls.append(randint(1, 10))
		i += 1
	successes = 0
	print(rolls)
	for roll in rolls:
		if roll >= difficult:
			successes += 1
	print(f'successes: {successes}', end=' ')
	successes = successes - modifiers.manage_critical_fails(rolls) + modifiers.manage_critical_successes(rolls)
	print(f'- total: {successes}')
	if successes < 0:
		epic_fail(successes)
	elif successes > 1:
		cause_damage(successes, enemy)
	else:
		missed(enemy)

def	epic_fail(successes):
	print('You lose your balance and fall on the ground.')

def cause_damage(successes, enemy):
	hp = enemy['hp']
	print(hp)
	new_hp = hp - successes
	print(new_hp)
	if new_hp <= 0:
		enemy['hp'] = ['dead', 0]
		print(f'You give a mortal thrust of your blade and {enemy["name"]} falls dead.')
		print('You win!')
		exit(0)
	elif new_hp <= hp / 3:
		enemy['hp'] = new_hp
		enemy['status'] = ['severily wounded', 1]
		print(f'You slash your sword causing a great damage on {enemy["name"]}. It is badly hurt.')
	else:
		enemy['hp'] = new_hp
		enemy['status'] = ['wounded', 2]
		print(f'You strike a blow on {enemy["name"]}, causing some blood to spill.')
	next_round(enemy)

def next_round(enemy):
	cinematics.declare_enemy_status(enemy)
	actions.encounter_reaction(enemy)

def missed(enemy):
	print(f'You miss your blow on {enemy["name"]}.')
