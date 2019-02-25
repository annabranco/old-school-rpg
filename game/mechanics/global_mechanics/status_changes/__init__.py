from db.hero import Hero
from db import status

def update_status(character, new_status):
		if character == Hero:
				status_number = status.status_hero[new_status]
				Hero['status'] = [new_status, status_number]
		else:
				status_number = status.status_npc[new_status]
				character['status'] = [new_status, status_number]