import os
from collections import defaultdict
# Import the input file
script_dir = os.path.dirname(__file__)
input = open(script_dir + "/input.txt")
rules, updateList = input.read().split('\n\n')
# convert updateList vals to ints
updateList = [list(map(int, line.split(','))) for line in updateList.splitlines()]

pairs = [list(map(int, p.split('|'))) for p in rules.splitlines()]

afterDict = defaultdict(list)
beforeDict = defaultdict(list)

def move_left(lst, index):
    if index <= 0:  # Check if the element is already at the beginning
        return lst
    lst[index - 1], lst[index] = lst[index], lst[index - 1]  # Swap the elements
    return lst

def move_right(lst, index):
    if index >= len(lst):  # Check if the element is already at the end
        return lst
    lst[index + 1], lst[index] = lst[index], lst[index + 1]  # Swap the elements
    return lst

def move_super_right(lst, index):
    if index >= len(lst):  # Check if the element is already at the end
        return lst
    lst[index + 2], lst[index] = lst[index], lst[index + 2]  # Swap the elements
    return lst

def testLine(line):
    index = 0
    isGoodLine = True
    moveLeft = False
    while index < len(line):
        leftSide = line[:index]
        rightSide = line[index+1:]
        if any(item in afterDict[line[index]] for item in leftSide):
            isGoodLine = False
            moveLeft = True
            break
        if any(item in beforeDict[line[index]] for item in rightSide):
            isGoodLine = False
            moveLeft = False
            break
        index += 1
    return isGoodLine, moveLeft, index

for pair in pairs:
    afterDict[pair[0]].append(pair[1])
    beforeDict[pair[1]].append(pair[0])
ans = 0
for line in updateList:
    goodLine = True
    index = 0
    goodLine, moveLeft, index = testLine(line)
    if not goodLine:
        print(line)
        runCounter = 0
        while not goodLine:
            for i in range(len(line)):
                for j in range(i +1, len(line)):
                    if [line[j], line[i]] in pairs:
                        line[j], line[i] = line[i], line[j]
            goodLine, moveLeft, index = testLine(line)
            runCounter += 1
        ans += line[len(line)//2]
    


print(ans)