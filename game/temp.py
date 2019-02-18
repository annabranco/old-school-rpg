import sys
import time
from random import randrange

text = 'Testing printing test'

for letter in text:
    sys.stdout.write(letter)
    sys.stdout.flush()
    seconds = "0." + str(randrange(1, 3, 1))
    seconds = float(seconds)
    time.sleep(seconds)
