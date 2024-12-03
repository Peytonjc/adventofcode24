import os
# Import the input file
script_dir = os.path.dirname(__file__)
input = open(script_dir + "/input.txt")
inputArray = input.readlines()

ansCount = 0
for line in inputArray:
    line = line.removesuffix('\n')
    levelList = line.split(' ')
    valid = True
    increasing = None
    val1 = None
    val2 = None
    futureIndex = 1
    for level in levelList:
        if futureIndex > len(levelList) - 1 or  (not valid):
            break
        val1 = int(level)
        val2 = int(levelList[futureIndex])
        futureIndex = futureIndex + 1
        diff = val2 - val1
        if abs(diff) > 3 or abs(diff) < 1:
            valid = False
        if increasing == None:
            if diff > 0:
                increasing = True
            else:
                increasing = False
        else:
            if increasing == True and diff < 0:
                valid = False
            if increasing == False and diff > 0:
                valid = False
    if valid:
        ansCount += 1
            
print(ansCount)