import os, re
# Import the input file
script_dir = os.path.dirname(__file__)
input = open(script_dir + "/input.txt")
#inputArray = input.readlines()

#print(input.read())
x = []
x = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", input.read())
print(x)
ans = 0
do = True
for val in x:
    if val == 'do()':
        do = True
    elif val == 'don\'t()':
        do = False
    elif do:
        val = val.replace('mul(', '').replace(')', '')
        nums = val.split(',')
        ans += int(nums[0]) * int(nums[1])
print(ans)