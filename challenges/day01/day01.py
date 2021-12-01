import numpy as np

# Load data
data = np.loadtxt('day01/day01_input.txt', dtype=int)

# Perform a sliding window summation per 3 elements
# TODO: uncomment for answer of part B
# data = np.convolve(data, np.ones(3, dtype=int), 'valid')

# Calculate the differences
diffs = np.diff(data)

# Get the ones that have positive difference
has_increased = diffs > 0

# Count their sum
result = np.sum(has_increased)

print(result)
