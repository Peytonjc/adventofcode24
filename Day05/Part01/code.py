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
for pair in pairs:
    afterDict[pair[0]].append(pair[1])
    beforeDict[pair[1]].append(pair[0])
ans = 0
for line in updateList:
    index = 0
    goodLine = True
    while index < len(line):
        leftSide = line[:index]
        rightSide = line[index+1:]
        if any(item in afterDict[line[index]] for item in leftSide):
            goodLine = False
        if any(item in beforeDict[line[index]] for item in rightSide):
            goodLine = False
        index += 1
    if goodLine:
        ans += line[len(line)//2]
    


print(ans)






    