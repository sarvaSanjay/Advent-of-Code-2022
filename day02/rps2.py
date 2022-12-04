values = {'A':0, 'B':1, 'C':2}

with open('rps.txt') as f:
    score = 0
    for line in f.readlines():
        choices = line.split()
        opponent, outcome = choices[0], choices[1]
        if outcome == 'Y':
            score += 3 + (values[opponent] % 3) + 1
        elif outcome == 'Z':
            score += 6 + ((values[opponent] + 1) % 3) + 1
        else:
            score += ((values[opponent] - 1) % 3) + 1
print(f'Score: {score}')