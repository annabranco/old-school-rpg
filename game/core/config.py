import sys
import time
from random import randint

# This function overwrites basic "print" so the texts are print like they were being typed
def print(text):
    for letter in text:
        if letter == '.':
            write_to_screen(letter)
            write_to_screen(' ')
            time.sleep(0.5)
        elif letter == '?' or letter == '!':
            write_to_screen(letter)
            write_to_screen(' ')
            time.sleep(0.8)
        elif letter == ',':
            write_to_screen(letter)
            time.sleep(0.3)
        elif letter == ' ':
            write_to_screen(letter)
        else:
            time.sleep(0.05)
            write_to_screen(letter)
    write_to_screen('\n')

def roll_dices(dices_number, difficult, reason):
		print(str(difficult))
		i = 1
		rolls = []
		rolled_results = []
		decisive = 0
		critical = 0
		success = 0
		fail = 0
		while i <= dices_number:
				rolls.append(randint(1, 10))
				i += 1
		for roll in rolls:
				if roll == 10:
						rolled_results.append({roll: '❕ decisive success'})
						decisive += 1
						success += 1
				elif roll == 1:
						rolled_results.append({roll: '❗️ critical fail'})
						critical += 1
				elif roll >= difficult:
						rolled_results.append({roll: '✔️ success'})
						success += 1
				else:
						rolled_results.append({roll: '✖️ fail'})
						fail += 1
		decisiveMinusCritical = decisive - critical
		print(f'decisiveMinusCritical: {decisiveMinusCritical}')
		final_result = success + decisiveMinusCritical
		print_rolls(difficult, rolls, rolled_results, final_result, reason)

def print_rolls(difficult, rolls, rolled_results, final_result, reason):
		print('==========================')
		time.sleep(0.01)
		print(f'{reason}')
		print(f'Dices to roll: {len(rolled_results)}')
		print(str(rolled_results))
		print(f'Difficult: {difficult}')
		print('\n')
		index = 0
		for roll in rolled_results:
				result_num = rolls[index]
				result_txt = rolled_results[index].rolls[index]
				time.sleep(1.2)
				write_to_screen(f'{result_num} ')
				time.sleep(0.8)
				write_to_screen(f'{result_txt}\n')
		print('\n')

		print(f'Result: {difficult}')
		print('==========================')


def write_to_screen(letter):
    sys.stdout.write(letter)
    sys.stdout.flush()

roll_dices(4,6, 'Attacking the enemy')