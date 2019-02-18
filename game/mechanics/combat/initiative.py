from random import randint
from db.hero import Hero
from core.config import print


def initiative(enemy, bonus=0):
    print('An initiative should be rolled to know who strikes first.')

    initiative_difficulty = 6

    Hero_initiative = 0
    Hero_rolls = []
    h = 0
    while h < Hero['speed'] + bonus:
        Hero_rolls.append(randint(1, 10))
        h += 1
    print(str(Hero_rolls))
    for roll in Hero_rolls:
        if roll >= initiative_difficulty:
            Hero_initiative += 1
    print(str(Hero_initiative))

    enemy_initiative = 0
    enemy_rolls = []
    e = 0
    while e < enemy['speed']:
        enemy_rolls.append(randint(1, 10))
        e += 1
    print(str(enemy_rolls))
    for roll in enemy_rolls:
        if roll >= initiative_difficulty:
            enemy_initiative += 1
    print(str(enemy_initiative))

    compare_initiatives(Hero_initiative, enemy_initiative, enemy)


def compare_initiatives(Hero_initiative, enemy_initiative, enemy):
    if Hero_initiative > enemy_initiative:
        print('You strike first.')
    elif Hero_initiative < enemy_initiative:
        print(f'{enemy["name"]} strikes first.')
    else:
        print('Simultaneous attack.')
