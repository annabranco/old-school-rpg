from core.config import *

def manage_critical_fails(rolls):
		critical_fails = 0
		for roll in rolls:
				if roll == 1:
						critical_fails += 1
		print('critical_fails', critical_fails, end=' ')
		return critical_fails

def manage_critical_successes(rolls):
		critical_successes = 0
		for roll in rolls:
				if roll == 10:
						critical_successes += 1
		print('critical_successes',critical_successes)
		return critical_successes

	# critical fail should cancel 1 success, even if it is decisive
