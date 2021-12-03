import pandas as pd

# Load data
data = open('challenges/03-binary-diagnostic/input.txt', 'r')
lines = data.readlines()
df = pd.DataFrame(dtype=int)

for line in lines:
    row = pd.Series([int(c) for c in line.rstrip('\n')])
    df = df.append(row, ignore_index=True)

# Count the most and least common values by grabbing the mode and inverse of the mode respectively
most_common = df.mode(axis=0, numeric_only=True).iloc[0, :]
least_common = most_common.apply(lambda x: 0 if x == 1 else 1)

# Calculate the gamma and epsilon values by converting the binary values to int
gamma = int("".join(str(int(i)) for i in most_common), 2)
epsilon = int("".join(str(int(i)) for i in least_common), 2)
result = gamma * epsilon

print(result)


