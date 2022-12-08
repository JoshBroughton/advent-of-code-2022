# naive approach: each line into an array, move left to right
#through array; if a tree is the tallest encountered so far, add one
#to the total. Same right to left. then again top to bottom and bottom 
#to top (by looking at index 0 of each array in turn, index 1, etc)
class Tree: 
    def __init__(self, size, counted=False):
        self.size = size
        self.counted = counted
        self.scenic_score = 1

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

    for i in range(0, len(arrays)):
        for j in range(0, len(arrays[i])):
            #walk up
            up_score = 0
            k = i - 1
            while k >= 0:
                up_score += 1
                if arrays[k][j].size >= arrays[i][j].size:
                    break
                k -= 1
            
            #down
            down_score = 0
            k = i + 1
            while k < len(arrays):
                #print(arrays[k][j].size)
                down_score += 1
                if arrays[k][j].size >= arrays[i][j].size:
                    break
                k += 1

            #right
            right_score = 0
            k = j + 1
            while k < len(arrays[i]):
                right_score += 1
                if arrays[i][k].size >= arrays[i][j].size:
                    break
                k += 1

            #left
            left_score = 0
            k = j - 1
            while k >= 0:
                left_score += 1
                if arrays[i][k].size >= arrays[i][j].size:
                    break
                k -= 1
            
            arrays[i][j].scenic_score = up_score * down_score * right_score * left_score
            if i == 0 or j == 0 or i == (len(arrays)-1) or j == (len(arrays[i])-1):
                arrays[i][j].scenic_score = 0
    
    # for row in arrays:
    #     print('LINE BREAK')
    #     for tree in row:
    #         print(tree.scenic_score)

    high_score = 0
    for row in arrays:
        for tree in row:
            if tree.scenic_score > high_score:
                high_score = tree.scenic_score

    print(high_score)
