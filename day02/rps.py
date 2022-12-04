winners = {'A':'Y', 'B':'Z', 'C':'X'}
ties = {'A':'X', 'B':'Y', 'C':'Z'}

with open('rps.txt') as f:
    score = 0
    for line in f.readlines():
        choices = line.split()
        opponent, player = choices[0], choices[1]
        if winners[opponent] == player:
            score += 6
        elif ties[opponent] == player:
            score += 3
        score += ord(player) - ord('X') + 1
print(f'Score: {score}')