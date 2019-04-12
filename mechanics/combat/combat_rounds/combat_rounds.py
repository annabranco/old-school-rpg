# GLOBAL COMBAT VARIABLE TO STORE WHO HAD ALREADY ATTACKED INSIDE THE CURRENT ROUND

took_action = {
	'Hero': False,
	'enemy': False
}

num_of_rounds = 0

def reset_rounds():
	global took_action
	took_action = {
		'Hero': False,
		'enemy': False
	}
