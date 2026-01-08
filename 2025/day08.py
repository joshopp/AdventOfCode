# ---------------- ADVENT OF CODE 2025 ---------------- #

# ---------------- DAY 8 PART 1 ---------------- #
import math
from collections import Counter


def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(i, j):
    root_i, root_j = find(i), find(j)
    if root_i == root_j:
        # print("ERROR: positions in same circuit")
        return False
    if size[root_i] < size[root_j]:
        root_i, root_j = root_j, root_i
    parent[root_j] = root_i
    size[root_i] += size[root_j]
    return True

# parse input
with open("input_8.txt") as file:
    lines = file.readlines()
positions = [list(map(int, line.strip().split(","))) for line in lines]
n = len(positions)

# build and fill distance matrix
distances = []
for i in range(n):
    for j in range(i+1, n):
        d = math.dist(positions[i], positions[j])
        distances.append((d, i, j))

distances.sort(key= lambda x: x[0]) # sort by distance

# Union Find
parent = list(range(n))
size = [1] * n

for d,i,j in distances[:1000]: # for 1000 smallest distances
    union(i,j)

# sort circuits by size
circuits = Counter(find(i) for i in range(n))
sizes = sorted(circuits.values(), reverse=True)

result = sizes[0] * sizes[1] * sizes[2]
print(f"number of biggest three circuits multiplied: {result}")


# ---------------- DAY 8 PART 2 ---------------- #

num_circuits = n
parent = list(range(n))
size = [1] * n

# continue until one circuit remains
for d,i,j in distances:
    if union(i,j):
        num_circuits -= 1
        if num_circuits == 1:
            print(f"\nConnecting the final two circuits at coordinates {positions[i]} and {positions[j]}")
            print(f"Product of the X-coordinates: {positions[i][0] * positions[j][0]}")
            break
