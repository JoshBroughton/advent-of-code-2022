import string

letter_array = list(string.ascii_letters)
letter_dict = {}

for index, letter in enumerate(letter_array):
    letter_dict[letter] = index + 1

with open('data.txt') as inputFile:
    lines = inputFile.readlines()
    score = 0
    for line in lines:
        line = line.strip()
        middle_index = int(len(line)/2)
        compartment_1 = line[0:middle_index]
        compartment_2 = line[middle_index:len(line)]

        for letter in compartment_1:
            if letter in compartment_2:
                score += letter_dict[letter]
                break

    
with open('data.txt') as inputFile:
    lines = inputFile.readlines()
    index = 0
    score = 0
    while index < len(lines):
        line_1 = lines[index]
        line_2 = lines[index + 1]
        line_3 = lines[index + 2]

        for letter in line_1:
            if letter in line_2 and letter in line_3:
                score += letter_dict[letter]
                break
        
        index += 3

    print(score)
            