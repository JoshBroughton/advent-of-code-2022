def cd(arg, current):
    if arg == '..':
        return current['parent']
    elif arg == '/':
        return file['/']
    else:
        return current['children'][arg]

def parse_line(line):
    #print(line)
    if line[0] == 'dir':
            return {
            'parent': current_dir,
            'children': {},
            'size': 0,
            'type': 'dir',
            }
    else:
        return {
            'parent': current_dir,
            'size': int(line[0]),
            'type': 'file',
        }

def sum(dir):
    total = 0
    for file in dir['children'].values():
        if file['size'] < 100000 and file['type'] == 'dir':
            total += file['size']
            total += sum(file)
        elif file['type'] == 'dir':
            total += sum(file)

    return total

def to_array(dir):
    for file in dir['children'].values():
        if file['type'] == 'dir' and file['size'] > 2143088:
            dir_array.append(file)
            to_array(file)


def dir_size(file):
    if file['type'] == 'dir':
        temp = file['children']
        if len(temp) == 0:
            return
        for in_file in temp.values():
            #print(in_file)
            if in_file['type'] == 'dir':
                dir_size(in_file)
                file['size'] += in_file['size']
            else:
                file['size'] += in_file['size']
        return file['size']


with open('data.txt') as in_file:
    files = {'/': {
        'children': {},
        'size': 0,
        'type': 'dir',
        }}
    line = in_file.readline()
    current_dir = files['/']
    while line != '':
        line = line.strip().split(' ')
        #print(line)
        if line[0] == '$':
            if line[1] == 'cd':
                #print(current_dir['children'])
                current_dir = cd(line[2], current_dir)
        else:
            #print(current_dir)
            current_dir['children'][line[1]] = parse_line(line)
        line = in_file.readline()

    dir_size(files['/'])
    print(30000000 - (70000000 - files['/']['size']))
    #need closest database at least this size
    space_to_free = 30000000 - (70000000 - files['/']['size'])
    dir_array = []
    to_array(files['/'])
    #print(dir_array)
    current_size = 70000000
    for dir in dir_array:
        if dir['size'] < current_size:
            current_size = dir['size']
    print(current_size)
