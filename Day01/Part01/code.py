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
    leftNums.append(nums[0])
    rightNums.append(nums[1])
# Order lists and start calculating distances
leftNums.sort()
rightNums.sort()
distList = []
for x in range(len(leftNums)):
    distList.append(abs(int(leftNums[x])-int(rightNums[x])))
print(sum(distList))
#print(inputArray)