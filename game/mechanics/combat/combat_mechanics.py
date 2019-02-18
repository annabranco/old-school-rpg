from mechanics.global_mechanics import modifiers
from random import randint
from db.hero import hero

def dispatch_attack(difficult, base_attack, attacker, defendant):
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
		epic_fail(successes, attacker)
	elif successes > 1:
		cause_damage(successes, attacker, defendant)
	else:
		missed(attacker, defendant)

def epic_fail(successes, attacker):
	if attacker == hero:
		print('You lose your balance and fall on the ground.')
	else:
		print(f'{attacker["name"]} loses the balance and falls on the ground.')

def cause_damage(successes, attacker, defendant):
	hp = defendant['hp']
	print(defendant, hp)
	new_hp = hp - successes
	print(defendant, ' - hp: ', new_hp)
	if new_hp <= 0:
		defendant['status'] = ['dead', 0]
		if defendant == hero:
			death_by_combat(defendant, attacker)
		else:
			killed_enemy(defendant)

	elif new_hp <= hp / 3:
		defendant['hp'] = new_hp
		defendant['status'] = ['severily wounded', 1]
		print(f'You slash your sword causing a great damage on {defendant["name"]}. It is badly hurt.')
	else:
		defendant['hp'] = new_hp
		defendant['hp'] = ['wounded', 2]

	print('xxx')
	# next_round(defendant)

def next_round(enemy):
	cinematics.declare_enemy_status(enemy)
	actions.encounter_reaction(enemy)

def missed(enemy):
	print(f'You miss your blow on {enemy["name"]}.')

def death_by_combat(hero, enemy):
	print(f'You feel an intense pain with the blow of {enemy["name"]} seconds after everything turns black and your body falls without life on the ground.')
	print('That\'s the end of your adventure...')
	exit(1)

def killed_enemy(enemy):
	print(f'You give a mortal thrust of your blade and {enemy["name"]} falls dead.')
	print('You win!')
	exit(0)

def cause_wound(defendant, attacker, severity):
		print(f'You strike a blow on {enemy["name"]}, causing some blood to spill.')
