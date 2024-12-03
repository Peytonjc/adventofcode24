import os
# Import the input file
script_dir = os.path.dirname(__file__)
input = open(script_dir + "/input.txt")
inputArray = input.readlines()

leftNums = []
rightNums = []
# Get inputs into two seperate lists
for line in inputArray:
    line = line.removesuffix('\n')
    nums = list(filter(None, line.split(' ')))
    leftNums.append(int(nums[0]))
    rightNums.append(int(nums[1]))
# Order lists and start calculating distances
leftNums.sort()
rightNums.sort()
ansList = []
for x in range(len(leftNums)):
    freq = rightNums.count(leftNums[x])
    if freq == '':
        freq = 0
    ansList.append(leftNums[x] * freq)
print(sum(ansList))
#print(inputArray)