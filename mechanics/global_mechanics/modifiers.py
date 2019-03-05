from core.config import *
from typing import List


def manage_critical_fails(rolls: List[int]) -> int:
		critical_fails: int = 0
		for roll in rolls:
				if roll == 1:
						critical_fails += 1
		print('critical_fails', critical_fails, end=' ')
		return critical_fails


def manage_critical_successes(rolls: List[int]) -> int:
		critical_successes: int = 0
		for roll in rolls:
				if roll == 10:
						critical_successes += 1
		print('critical_successes', critical_successes)
		return critical_successes

	# critical fail should cancel 1 success, even if it is decisive
