from random import randint
from db.hero import hero
from core.config import print


def initiative(enemy, bonus=0):
    print('An initiative should be rolled to know who strikes first')

    initiative_difficulty = 6

    hero_initiative = 0
    hero_rolls = []
    h = 0
    while h < hero['speed'] + bonus:
        hero_rolls.append(randint(1, 10))
        h += 1
    print(hero_rolls)
    for roll in hero_rolls:
        if roll >= initiative_difficulty:
            hero_initiative += 1
    print(hero_initiative)

    enemy_initiative = 0
    enemy_rolls = []
    e = 0
    while e < enemy['speed']:
        enemy_rolls.append(randint(1, 10))
        e += 1
    print(enemy_rolls)
    for roll in enemy_rolls:
        if roll >= initiative_difficulty:
            enemy_initiative += 1
    print(enemy_initiative)

    compare_initiatives(hero_initiative, enemy_initiative, enemy)


def compare_initiatives(hero_initiative, enemy_initiative, enemy):
    if hero_initiative > enemy_initiative:
        print('You strike first.')
    elif hero_initiative < enemy_initiative:
        print(f'{enemy["name"]} strikes first.')
    else:
        print('Simultaneous attack')
