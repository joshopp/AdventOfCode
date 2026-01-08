# ---------------- ADVENT OF CODE 2025 ---------------- #

# ---------------- DAY 4 PART 1 ---------------- #

import numpy as np
from scipy.ndimage import convolve

def numerize_cell(cell):
    if cell == '@':
        return 1
    elif cell == '.':
        return 0
    else:
        print("Unknown cell value:", cell)
        return -1
    

with open("input_4.txt") as file:
    lines = file.readlines()

grid = np.array([list(map(numerize_cell, line.strip())) for line in lines])
# print(grid)

# 3x3 kernel for N8-function
kernel = np.ones((3,3), dtype=int)
# convolute for sum
neighbour_sum = convolve(grid, kernel, mode='constant', cval=0)

num_accessible_1 = np.sum((grid==1) & (neighbour_sum-1<4))

print(num_accessible_1,  " rolls of paper can be accessed by a forklift from the starting grid.")


# ---------------- DAY 4 PART 2 ---------------- #

num_accessible_2 = 0
removed_rolls = 1

while removed_rolls > 0:
    # convolute for sum
    neighbour_sum = convolve(grid, kernel, mode='constant', cval=0)
    accessible = (grid==1) & (neighbour_sum-1<4) # check if roll is accessible
    removed_rolls = np.sum(accessible)
    num_accessible_2 += removed_rolls
    # update grid -> removing accessible rolls
    grid = np.where(accessible, 0, grid)
print(num_accessible_2, " rolls of paper can be removed in total by iteratively removing them.")


