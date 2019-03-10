from core.characters import Player
from core.elements import Food, Item
# THIS IMPORTS THE PLAYER CLASS, CREATES A PLAYABLE CHARACTER
# AND DETERMINES ITS INITIAL ATTRIBUTES ANS ITEMS

Hero = Player('Hero', 'human')
Hero.weapon = {'name': 'short sword', 'type': 'blade', 'bonus': 0}
food = Food('food', 'dry and untasty meat', 10)
Hero.inventory.append(food)

Hero.attack = 5
Hero.defense = 5
Hero.full_hp = 5
Hero.speed = 5
Hero.hp = 5
Hero.status = 'well'
