calorie_per_elf = []

with open('data.txt') as inputFile:
    lines = inputFile.readlines()
    elf_total = 0
    for line in lines:
        if line == '\n':
            calorie_per_elf.append(elf_total)
            elf_total = 0
        else:
            calories = line.split('\\')[0]
            elf_total += int(calories)

top_3 = []
for i in range(0, 3):
    max_calories = 0
    for amount in calorie_per_elf:
        if amount > max_calories:
            max_calories = amount
    top_3.append(max_calories)
    calorie_per_elf.remove(max_calories)


print(top_3)
print(sum(top_3))
