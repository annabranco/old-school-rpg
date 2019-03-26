from core.characters import Player
from db.food import *
from db.weapons import *

# THIS IMPORTS THE PLAYER CLASS, CREATES A PLAYABLE CHARACTER
# AND DETERMINES ITS INITIAL ATTRIBUTES ANS ITEMS

Hero = Player('Hero', 'human', 'female')
Hero.weapon = short_sword

Hero.inventory.append(leather_meat)
leather_meat.add(10)

Hero.attack = 5
Hero.defense = 5
Hero.full_hp = 5
Hero.speed = 5
Hero.hp = 5
