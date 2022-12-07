def cd(arg, current):
    if arg == '..':
        return files[current]['parent']
    elif arg == '/':
        return '/'
    else:
        return arg
    
#there are naming collisions (nested dirs with same names) need to handle this
# I should just re-approach the problem: dir object with lists of children (
# which are file or dir objects themselves)
# if I used TS could make interfaces
def parse_line(line):
    if line[0] == 'dir':
        if line[1] in files:
            files[line[1]] = {
            'parent': current_dir,
            'children': [],
            'size': 0,
            'type': 'dir',
            }
    else:
        files[line[1]] = {
            'parent': current_dir,
            'size': int(line[0]),
            'type': 'file',
        }

def dir_size(file):
    if files[file]['type'] == 'dir':
        temp = files[file]['children']
        if len(temp) == 0:
            return
        for in_file in temp:
            if files[in_file]['type'] == 'dir':
                dir_size(in_file)
                files[file]['size'] += files[in_file]['size']
            else:
                files[file]['size'] += files[in_file]['size']
        

with open('data.txt') as in_file:
    files = {'/': {
        'children': [],
        'size': 0,
        'type': 'dir',
        }}
    current_dir = '/'
    line = in_file.readline()
    while line != '':
        line = line.strip().split(' ')
        print(line)
        print(current_dir)
        if line[0] == '$':
            if line[1] == 'cd':
                current_dir = cd(line[2], current_dir)
            else:
                line = in_file.readline().strip().split()
                print(line)
                files[current_dir]['children'].append(line[1])
                parse_line(line)
        else:
            files[current_dir]['children'].append(line[1])
            parse_line(line)
        line = in_file.readline()
    
    dir_size('/')
    print(files['/'])
    sum = 0
    for file in files:
        if files[file]['type'] == 'dir' and files[file]['size'] < 100000:
            sum += files[file]['size']
    print(sum)
    

    

