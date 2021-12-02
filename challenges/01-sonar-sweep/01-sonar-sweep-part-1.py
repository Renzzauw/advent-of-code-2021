import numpy as np

# Load data
data = np.loadtxt('01-sonar-sweep/input.txt', dtype=int)

# Calculate the differences
diffs = np.diff(data)

# Get the ones that have positive difference
has_increased = diffs > 0

# Count their sum
result = np.sum(has_increased)

print(result)
