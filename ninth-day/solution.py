knots = []
count = 0
while count < 10:
    count += 1
    knots.append({
    'x': 0,
    'y': 0,
    })
    
tail_positions = [[0, 0]]

def move_tail(head, tail):
    #same row
    if knots[head]['y'] == knots[tail]['y']:
        if knots[head]['x'] - knots[tail]['x'] > 1:
            knots[tail]['x'] += 1
            
        elif knots[tail]['x'] - knots[head]['x'] > 1:
            knots[tail]['x'] -= 1
    #same column
    elif knots[head]['x'] == knots[tail]['x']:
        if knots[head]['y'] - knots[tail]['y'] > 1:
            knots[tail]['y'] += 1
        elif knots[tail]['y'] - knots[head]['y'] > 1:
            knots[tail]['y'] -= 1
    #double diagonal
    #up right
    elif knots[head]['x'] - knots[tail]['x'] > 1 and knots[head]['y'] - knots[tail]['y'] > 1:
        knots[tail]['x'] += 1
        knots[tail]['y'] += 1
    #down right
    elif knots[head]['x'] - knots[tail]['x'] > 1 and knots[tail]['y'] - knots[head]['y'] > 1:
        knots[tail]['x'] += 1
        knots[tail]['y'] -= 1
    #up left
    elif knots[tail]['x'] - knots[head]['x'] > 1 and knots[head]['y'] - knots[tail]['y'] > 1:
        knots[tail]['x'] -= 1
        knots[tail]['y'] += 1
    #down left
    elif knots[tail]['x'] - knots[head]['x'] > 1 and knots[tail]['y'] - knots[head]['y'] > 1:
        knots[tail]['x'] -= 1
        knots[tail]['y'] -= 1
    
    #diagonal
    elif knots[head]['x'] - knots[tail]['x'] > 1:
        knots[tail]['x'] += 1
        knots[tail]['y'] = knots[head]['y'] 
    elif knots[tail]['x'] - knots[head]['x'] > 1:
        knots[tail]['x'] -= 1
        knots[tail]['y'] = knots[head]['y'] 
    elif knots[head]['y'] - knots[tail]['y'] > 1:
        knots[tail]['y'] += 1
        knots[tail]['x'] = knots[head]['x']   
    elif knots[tail]['y'] - knots[head]['y'] > 1:
        knots[tail]['y'] -= 1
        knots[tail]['x'] = knots[head]['x']
        


def move(command):
    count = 0
    while count < int(command[1]):
        count += 1
        if command[0] == 'R':
            knots[0]['x'] += 1
        elif command[0] == 'L':
            knots[0]['x'] -= 1
        elif command[0] == 'U':
            knots[0]['y'] += 1
        elif command[0] == 'D':
            knots[0]['y'] -= 1

        for i in range (0, 9):
            move_tail(i, i + 1)
        if [knots[9]['x'], knots[9]['y']] not in tail_positions:
            tail_positions.append([knots[9]['x'], knots[9]['y']])
        
    
with open('data.txt') as in_file:
    commands = in_file.readlines()
    for command in commands:
        command = command.strip().split(' ')
        move(command)
    
    print(len(tail_positions))
