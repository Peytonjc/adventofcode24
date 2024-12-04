import os, re
# Import the input file
script_dir = os.path.dirname(__file__)
input = open(script_dir + "/input.txt")
inputArray = input.read().splitlines()

x = 0
y = 0
resultCount = 0
while y < len(inputArray):
    x = 0
    while x < len(inputArray[0]):
        currentChar = inputArray[y][x]
        
        if currentChar == 'A':
            if x < len(inputArray[0]) - 1 and y < len(inputArray) - 1 and x > 0 and y > 0:
                if ((inputArray[y-1][x-1] + currentChar + inputArray[y+1][x+1] == "SAM" or inputArray[y-1][x-1] + currentChar + inputArray[y+1][x+1] == "MAS")
                    and (inputArray[y-1][x+1] + currentChar + inputArray[y+1][x-1] == "SAM" or inputArray[y-1][x+1] + currentChar + inputArray[y+1][x-1] == "MAS")):
                    resultCount += 1
                    #print("location: " + str(x) + ", " + str(y))
        x += 1
    y += 1

print(resultCount)