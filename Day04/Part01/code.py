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

        #Horizontal
        if x < len(inputArray[0]) - 3:
            if (currentChar + inputArray[y][x+1] + inputArray[y][x+2] + inputArray[y][x+3] == "XMAS" 
            or currentChar + inputArray[y][x+1] + inputArray[y][x+2] + inputArray[y][x+3] == "SAMX"):
                resultCount += 1
                #print("location: " + str(x) + ", " + str(y))

        #Vertical
        if y < len(inputArray) - 3:
            if (currentChar + inputArray[y+1][x] + inputArray[y+2][x] + inputArray[y+3][x] == "XMAS"
            or currentChar + inputArray[y+1][x] + inputArray[y+2][x] + inputArray[y+3][x] == "SAMX"):
                resultCount += 1

        #Right Diagonal
        if (x < len(inputArray[0]) - 3) and (y < len(inputArray) - 3):
            if (currentChar + inputArray[y+1][x+1] + inputArray[y+2][x+2] + inputArray[y+3][x+3] == "XMAS"
            or currentChar + inputArray[y+1][x+1] + inputArray[y+2][x+2] + inputArray[y+3][x+3] == "SAMX"):
                resultCount += 1
        
        #Left Diagonal
        if (x > 2) and (y < len(inputArray) - 3):
            if (currentChar + inputArray[y+1][x-1] + inputArray[y+2][x-2] + inputArray[y+3][x-3] == "XMAS"
            or currentChar + inputArray[y+1][x-1] + inputArray[y+2][x-2] + inputArray[y+3][x-3] == "SAMX"):
                resultCount += 1

        x += 1
    y += 1

print(resultCount)