
# Load data
data = open('challenges/02-dive/input.txt', 'r')
lines = data.readlines()

horizontal_pos = 0
aim = 0
depth = 0

# Update depth, aim and horizontal position line by line
for line in lines:
    row = line.rstrip('\n').split(' ')
    val = int(row[1])
    if row[0] == "up":
        aim -= val
    elif row[0] == "down":
        aim += val
    else:
        horizontal_pos += val
        depth += aim * val

result = horizontal_pos * depth

print(result)






