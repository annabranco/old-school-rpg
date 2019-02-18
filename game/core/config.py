import sys
import time

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


def write_to_screen(letter):
    sys.stdout.write(letter)
    sys.stdout.flush()
