import sys
import time
from textwrap import dedent

# DEFINES BASIC CONFIG FOR ALL OTHER MODULES


# This function overwrites basic "print" so the texts are print like they were being typed
# def print(text: str) -> None:
# 		for letter in text:
# 				if letter == '.':
# 						write_to_screen(letter)
# 						write_to_screen(' ')
# 						time.sleep(0.5)
# 				elif letter == '?' or letter == '!':
# 						write_to_screen(letter)
# 						write_to_screen(' ')
# 						time.sleep(0.8)
# 				elif letter == ',':
# 						write_to_screen(letter)
# 						time.sleep(0.3)
# 				elif letter == ' ':
# 						write_to_screen(letter)
# 				elif letter == '>':
# 						time.sleep(0.01)
# 						write_to_screen(letter)
# 				else:
# 						time.sleep(0.05)
# 						write_to_screen(letter)
# 		write_to_screen('\n')


def print_cinematics(text: str) -> None:
    write_to_screen('\t\t')
    print(text)


def write_to_screen(letter: str) -> None:
    sys.stdout.write(letter)
    sys.stdout.flush()


def mechanics_block(action: str) -> None:
    write_to_screen('\n\n\n')
    write_to_screen('----------------------------- ')
    write_to_screen(action)
    write_to_screen(' -----------------------------')
    write_to_screen('\n')


def cinematics_block() -> None:
    write_to_screen('\n')
    write_to_screen(
        '----------------------------------------------------------')
    write_to_screen('\n\n')


def action_block() -> None:
    print('\n\t\t---\n')

def system_name(name: str) -> str:
    if name.endswith('sses'):
        name = name[:-3]
    elif name.endswith('ves'):
        name = name[:-3] + 'f'
    elif name.endswith('ies'):
        name = name[:-3] + 'y'
    elif name.endswith('ses') or name.endswith('shes') or name.endswith('ches') \
         or name.endswith('xes') or name.endswith('zes') or name.endswith('oes'):
        name = name[:-2]
    elif name.endswith('ses'):
        name = name[:-2]
    elif name.endswith('s'):
        name = name[:-1]
    return name.lower()

def system_name_with_article(name: str) -> str:
    __name = system_name(name)
    if __name.startswith(('a', 'e', 'i', 'o', 'u', 'y')):
        return f'an {__name}'
    else:
        return f'a {__name}'
