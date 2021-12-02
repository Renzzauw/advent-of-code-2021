# Load data
data = open('challenges/02-dive/input.txt', 'r')
lines = data.readlines()

horizontal_pos = 0
depth = 0

# Update depth and horizontal position line by line
for line in lines:
    row = line.rstrip('\n').split(' ')
    val = int(row[1])
    if row[0] == "up":
        depth -= val
    elif row[0] == "down":
        depth += val
    else:
        horizontal_pos += val

result = horizontal_pos * depth

print(result)






