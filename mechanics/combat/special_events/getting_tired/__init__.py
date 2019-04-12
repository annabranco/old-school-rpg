from mechanics.combat.combat_rounds.combat_rounds import combat_rounds
from core_elements.characters.Hero import Hero
from core_elements.characters import NPC, Player, Character


def is_character_tired(character: Character, rounds: int) -> bool:
	character_status = character.status.split()[-1]
	if character_status == 'exhausted':
		pass
	elif character_status == 'tired':
		if character.status.split()[-2] == 'very':
			pass
		else:
			pass
	else:
		pass

	if rounds * multiplier > character.resistance:
		return true

def are_characters_tired(Hero: Player, enemy: NPC, rounds: int) -> bool:
	Hero_is_tired = is_character_tired(Hero, rounds)
	enemy_is_tired = is_character_tired(enemy, rounds)


