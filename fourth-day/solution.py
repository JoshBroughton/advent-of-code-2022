def contains(arr_1, arr_2):
    arrays = shorter_array(arr_1, arr_2)
    for id in arrays['shorter']:
        if id in arrays['longer']:
            return True
    
    return False

def shorter_array(arr_1, arr_2):
    if len(arr_1) < len(arr_2):
        return {'shorter':arr_1, 'longer':arr_2}
    else:
        return {'shorter':arr_2, 'longer':arr_1}

def parse_id(id):
    id = id.split('-')
    array = []
    count = int(id[0])
    while count <= int(id[1]):
        array.append(count)
        count += 1

    return array

with open('data.txt') as input_file:
    lines = input_file.readlines()
    counter = 0
    for line in lines:
        ids = line.split(',')
        parsed_ids = []
        for id in ids:
            parsed_ids.append(parse_id(id))
        if contains(parsed_ids[0], parsed_ids[1]):
            counter += 1
    
    print(counter)
