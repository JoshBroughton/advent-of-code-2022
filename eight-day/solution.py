# naive approach: each line into an array, move left to right
#through array; if a tree is the tallest encountered so far, add one
#to the total. Same right to left. then again top to bottom and bottom 
#to top (by looking at index 0 of each array in turn, index 1, etc)
class Tree: 
    def __init__(self, size, counted=False):
        self.size = size
        self.counted = counted

#EACH TREE CAN ONLY BE COUNTED AS VISIBLE ONCE 
#BUILD AS ARRAY OF TREE OBJECTS WHICH HAVE "COUNTED" ATTRIBUTE
with open('data.txt') as in_file:
    lines = in_file.readlines()
    arrays = []
    for line in lines:
        line = line.strip()
        line = list(line)
        line_array = list()
        for tree in line:
            line_array.append(Tree(int(tree)))
        arrays.append(line_array)

    total = 0
    #left to right
    for i, line in enumerate(arrays):
        temp = -1
        for j, digit in enumerate(line):
            size = digit.size
            # print(f'{arrays[i][j].size}, {digit.size}')
            # print(temp)

            if size > temp and not digit.counted:
                temp = size    
                total += 1
                arrays[i][j].counted = True
            elif size > temp:
                temp = size
    
    for idx, array in enumerate(arrays):
        print(f'line: {idx}')
        for tree in array:
            print(tree.counted)

    #right to left
    for i, line in enumerate(arrays):
        line = line[::-1]
        temp = -1
        for j, digit in enumerate(line):
            size = digit.size
            if size > temp and not digit.counted:
                temp = size
                total += 1
                arrays[i][-j - 1].counted = True
            elif size > temp:
                temp = size

    for idx, array in enumerate(arrays):
        print(f'line: {idx}')
        for tree in array:
            print(tree.counted)
    #top to bottom
    for i in range(0, len(arrays[0])):
        temp = -1
        for j in range(0, len(arrays)):
            #print(arrays[j][i].size)
            if arrays[j][i].size > temp and not arrays[j][i].counted:
                temp = arrays[j][i].size
                total += 1
                arrays[j][i].counted = True
            elif arrays[j][i].size > temp:
                temp = arrays[j][i].size

    #bottom to top
    for i in range(0, len(arrays[0])):
        temp = -1
        for j in range(len(arrays) - 1, -1, -1):
            #print(temp)
            if arrays[j][i].size > temp and not arrays[j][i].counted:
                temp = arrays[j][i].size
                total += 1
                arrays[j][i].counted = True
            elif arrays[j][i].size > temp:
                temp = arrays[j][i].size


    print(total)
    # for array in arrays:
    #     for tree in array:
    #         print(tree.counted)
