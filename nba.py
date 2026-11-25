def sum_ppg(player_one, player_two):
	sum = player_one.get("ppg") + player_two.get('ppg')
	return sum


iverson = {'team': '76ers', 'ppg': 11.2}
jordan = {'team': 'bulls', 'ppg': 20.2}

print(sum_ppg(iverson, jordan))