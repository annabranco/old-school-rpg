from mechanics.combat.attack import attack
from mechanics.combat.defend import defend
from mechanics.combat.initiative import initiative

def ask_for_action():
	print('What do you do?')
	return input('> ')

def encounter_reaction(enemy):
	action = ask_for_action()
	if action == 'attack':
		print(f'You draw your sword and strike before {enemy["name"]} has a chance to understand what is happening.')
		attack(2, enemy)
	elif action == 'wait':
		print(f'You wait to see the reaction of the {enemy["name"]}. He draws a club and comes to attack you.')
		initiative(0, enemy)
	elif action == 'defend':
		print(f'You put yourseld on a defensive stance while the {enemy["name"]} draws a club and comes to attack you.')
		defend(2, enemy)