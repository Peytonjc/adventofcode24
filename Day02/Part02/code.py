import os
# Import the input file
script_dir = os.path.dirname(__file__)
input = open(script_dir + "/input.txt")
inputArray = input.readlines()

import os
# Import the input file
script_dir = os.path.dirname(__file__)
input = open(script_dir + "/input.txt")
inputArray = input.readlines()

ansCount = 0
for line in inputArray:
    line = line.removesuffix('\n')
    levelList = line.split(' ')
    levelListCopy = levelList.copy()
    levelListCopy3 = levelList.copy()
    levelListCopyNoFirst = levelList.copy()
    levelListCopyNoFirst.remove(levelListCopyNoFirst[0])
    levelListCopyNoLast = levelList.copy()
    levelListCopyNoLast.pop()

    valid = True
    increasing = None
    val1 = None
    val2 = None
    futureIndex = 1
    tryAgain = False
    for level in levelList:
        if futureIndex > len(levelList) - 1 or  (not valid):
            break
        val1 = int(level)
        val2 = int(levelList[futureIndex])
        futureIndex = futureIndex + 1
        diff = val2 - val1
        if abs(diff) > 3 or abs(diff) < 1:
            valid = False
            levelList.pop(futureIndex - 1)
            levelListCopy.pop(futureIndex - 2)

            break
        if increasing == None:
            if diff > 0:
                increasing = True
            else:
                increasing = False
        else:
            if increasing == True and diff < 0:
                valid = False
                levelList.pop(futureIndex - 1)
                levelListCopy.pop(futureIndex - 2)

                break
            if increasing == False and diff > 0:
                valid = False
                levelList.pop(futureIndex - 1)
                levelListCopy.pop(futureIndex - 2)

                break

    if valid == False:
        valid = True
        increasing = None
        val1 = None
        val2 = None
        futureIndex = 1
        tryAgain = False
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

    if valid == False:
        valid = True
        increasing = None
        val1 = None
        val2 = None
        futureIndex = 1
        tryAgain = False
        for level in levelListCopy:
            if futureIndex > len(levelListCopy) - 1 or  (not valid):
                break
            val1 = int(level)
            val2 = int(levelListCopy[futureIndex])
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

    
    if valid == False:
        valid = True
        increasing = None
        val1 = None
        val2 = None
        futureIndex = 1
        tryAgain = False
        for level in levelListCopyNoFirst:
            if futureIndex > len(levelListCopyNoFirst) - 1 or  (not valid):
                break
            val1 = int(level)
            val2 = int(levelListCopyNoFirst[futureIndex])
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

    if valid == False:
        valid = True
        increasing = None
        val1 = None
        val2 = None
        futureIndex = 1
        tryAgain = False
        for level in levelListCopyNoLast:
            if futureIndex > len(levelListCopyNoLast) - 1 or  (not valid):
                break
            val1 = int(level)
            val2 = int(levelListCopyNoLast[futureIndex])
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