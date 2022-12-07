
with open('.\Day 2\day2 Input.txt') as file:
    rounds = file.readlines()
    file.close()

play_results = {
    'X' : {
        'A': 3,
        'B': 1,
        'C': 2
    },
    'Y': {
        'A':1,
        'B':2,
        'C':3
    },
    'Z': {
        'A':2,
        'B':3,
        'C':1
    }
}

round_scores = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

player_score = 0

for round in rounds:
    opponent_play = round[0]
    round_outcome = round[2]
    player_score += play_results[round_outcome][opponent_play]
    player_score += round_scores.get(round_outcome,0)

print(player_score)