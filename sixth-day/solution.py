import re
# part 1
with open('data.txt') as input_file:
    text = list(input_file.readlines()[0].strip())
    final_index = None
    for index, char in enumerate(text):
        if char in text[index + 1:index + 4] or text[index + 1] in text[index + 2: index + 4] or text[index + 2] == text[index + 3]:
            continue
        else:
            final_index = index + 4
            break



def no_repeats_in_list(char_list):
    for char in char_list:
        if char_list.count(char) > 1:
            return False
    
    return True

with open('data.txt') as input_file:
    text = list(input_file.readlines()[0].strip())
    match_index = None
    for index, char in enumerate(text):
        if index < len(text) - 15:
            print(text[index:index + 14])
            if no_repeats_in_list(text[index:index + 14]):
                match_index = index + 14

    print(match_index)


