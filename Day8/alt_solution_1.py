# NOT MINE - Steven Braun shared on RealPython AoC Channel

from collections import Counter

with open("test_data.txt") as f:
    data = [x.strip().split("|") for x in f.readlines()]

ideal_map = "abcefg cf acdeg acdfg bdcf abdfg abdefg acf abcdefg abcdfg"
ideal_mapping = Counter(ideal_map)
map_key = {
    sum([*map(ideal_mapping.get, nums)]): i
    for i, nums in zip(range(10), ideal_map.split())
}

part1 = 0
part2 = 0
for first, second in data:
    part1 += len([x for x in second.split() if len(x) in (2, 3, 4, 7)])
    this_mapping = Counter(first)
    part2 += int("".join([str(map_key[sum([*map(this_mapping.get, nums)])]) for nums in second.split()]))


print(f"Part 1: {part1}")
print(f"Part 2: {part2}")