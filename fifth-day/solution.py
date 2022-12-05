def build_stacks(input):
    stacks = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
    }

    for line in input:
        count = 0
        while count < 9:
            if line[(count * 4) + 1] != ' ':
                stacks[count + 1].append(line[(count * 4) + 1])
            count += 1

    return stacks

def move(num, source, dest):
    if len(source) > 0 and num == 1:
        dest.insert(0, source.pop(0))
    elif len(source) >= num and num > 0:
        temp = []
        count = 1
        while count <= num:
            temp.insert(0, source.pop(0))
            count += 1
        for elem in temp:
            dest.insert(0, elem)


with open('data.txt') as input_file:
    lines = input_file.readlines()
    stacks = build_stacks(lines[0:8])
    command_lines = lines[10:]
    commands = []
    for line in command_lines:
        command = line.strip().split(' ')
        commands.append(command)
    
    for command in commands:
        move(int(command[1]), stacks[int(command[3])], stacks[int(command[5])])

    for key, value in stacks.items():
        print(value[0])
