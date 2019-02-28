from db.fails import disastrous_fail_on_attack
from core.characters.Hero import Hero
from db.enemies import ugly_monster

# ugly_monster.weapon = {'name': 'short bow', 'type': 'range'}

disastrous_fail_on_attack(5, ugly_monster, Hero)
