
with open('.\Day 2\day2 Input.txt') as file:
    rounds = file.readlines()
    file.close()

play_results = {
    'X' : {
        'A': 3,
        'B': 0,
        'C': 6
    },
    'Y': {
        'A':6,
        'B': 3,
        'C':0
    },
    'Z': {
        'A':0,
        'B':6,
        'C':3
    }
}

play_scores = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

player_score = 0

for round in rounds:
    opponent_play = round[0]
    your_play = round[2]
    player_score += play_results[your_play][opponent_play]
    player_score += play_scores.get(your_play,0)

print(player_score)