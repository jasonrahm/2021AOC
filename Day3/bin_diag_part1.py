"""
Advent of Code - Day 3
Puzzle: Binary Diagnostics Part 1
"""
import pandas as pd

with open('../input/binary_diagnostics_data.txt', 'r') as f:
    binary_digits: list = f.readlines()

for i, num in enumerate(binary_digits):
    binary_digits[i] = [int(x) for x in num.strip()]

gamma_rate = ''
epsilon_rate = ''
df = pd.DataFrame(binary_digits)
for i in range(0, 12):
    gamma_rate += str(df[i].value_counts().idxmax())
    epsilon_rate += str(df[i].value_counts().idxmin())
print(int(gamma_rate, 2) * int(epsilon_rate, 2))
