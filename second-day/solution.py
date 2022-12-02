key = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

# A < B < C < A

# X < Y < Z < X
def determine_winner(enemy, me):
    outcome = None
    # loss
    if me == 'X':
        if enemy == 'A':
            me = 'C'
        elif enemy == 'B':
            me = 'A'
        elif enemy == 'C':
            me = 'B'
    # draw
    elif me == 'Y':
        me = enemy
    # win
    elif me == 'Z':
        if enemy == 'A':
            me = 'B'
        elif enemy == 'B':
            me = 'C'
        elif enemy == 'C':
            me = 'A'


    if enemy == me:
        outcome = 'draw'
    elif enemy == 'A':
        if me == 'B':
            outcome = 'win'
        elif me == 'C':
            outcome = 'loss'
    elif enemy == 'B':
        if me == 'A':
            outcome = 'loss'
        elif me == 'C':
            outcome = 'win'
    elif enemy == 'C':
        if me == 'A':
            outcome = 'win'
        elif me == 'B':
            outcome = 'loss'

    return {'outcome': outcome, 'me': me}


with open('data.txt') as inputFile:
    lines = inputFile.readlines()
    score = 0
    for line in lines:
        enemy = line[0]
        me = line[2]
        result = determine_winner(enemy, me)
        if result['outcome'] == 'draw':
            score += 3
        elif result['outcome'] == 'win':
            score += 6
        
        if result['me'] == 'A':
            score += 1
        elif result['me'] == 'B':
            score += 2
        elif result['me'] == 'C':
            score += 3
    
    print(score)






            
