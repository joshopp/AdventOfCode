# ---------------- ADVENT OF CODE 2025 ---------------- #

# ---------------- DAY 9 PART 1 ---------------- #
import math

with open("input_9.txt") as file:
    lines = file.readlines()

pos = [list(map(int, line.strip().split(","))) for line in lines]

n = len(pos)
max_rect = [0, 0, 0]

for i in range(n):
    for j in range(i+1, n):
        area =  abs(pos[i][0] - pos[j][0])+1 * abs(pos[i][1] - pos[j][1])+1
        if area > max_rect[2]:
            # print(f"new max rectangle found: {rect_size} from points {i} and {j}")
            max_rect = [i, j, area]

print(f"points forming biggest rectangle: {pos[max_rect[0]]}, {pos[max_rect[1]]} with area {max_rect[2]}")


# ---------------- DAY 9 PART 2 ---------------- #

def is_in_polygon(x: int, y: int) -> bool:
    inside = False

    for (x1, y1), (x2, y2) in zip(pos, pos[1:] + [pos[0]]):
        if (x == x1 == x2 and min (y1, y2) <= y <= max(y1, y2) or
           y == y1 == y2 and min (x1, x2) <= x <= max(x1, x2)):
            return True  # point is on edge
        if ((y1 > y) != (y2 > y)) and (x < (x2 - x1) * (y - y1) / (y2 - y1) + x1):
            inside = not inside
    return inside

max_rect = [0, 0, 0]

for i in range(n):
    for j in range(i+1, n):
        area =  abs(pos[i][0] - pos[j][0])+1 * abs(pos[i][1] - pos[j][1])+1
        if area > max_rect[2]:
            if is_in_polygon(pos[i][0], pos[j][1]) and is_in_polygon(pos[j][0], pos[i][1]):
                max_rect = [i, j, area]
                print(f"new max rectangle found: {area} from points {i} and {j}")
            

print(f"points forming biggest rectangle: {pos[max_rect[0]]}, {pos[max_rect[1]]} with area {max_rect[2]}")
