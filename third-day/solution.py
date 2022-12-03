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

    print(score)
