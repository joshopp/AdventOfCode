# ---------------- ADVENT OF CODE 2025 ---------------- #

# ---------------- DAY 6 PART 1 ---------------- #

import math

def calculate(nums, op):
    if op == '+':
        return sum(int(x) for x in nums)
    elif op == '*':
        return math.prod(int(x) for x in nums)
    else:
        print(f"ERROR: Invalid Operation: ({op}) with extracted numbers {nums}")
        return 0


grand_total = 0

with open("input_6.txt") as file:
    lines = file.readlines()
problems = [line.split() for line in lines]
problems = list(zip(*problems)) # transpose to get operations in last row -> easy to process

for problem in problems:
    # print("Exercise:", problem)
    solved = calculate(problem[:-1], problem[-1])
    # print("Solution:", solved)
    grand_total += solved

print("Sum of all calculated results:", grand_total)



# ---------------- DAY 6 PART 2 ---------------- #
arr = [line[:-1] for line in lines] # remove "\n" from the end of each line
num_rows = len(arr)
grand_total = 0
problem_length = len(arr[0])
i= 0

while i < problem_length:
    start = i
    while i < problem_length and not all(arr[r][i] == ' ' for r in range(num_rows)): # check if all columns are " " -> end of op
        i += 1

    x=[] # create empty list to store cephalopod numbers
    for digit in range(start, i):
        number = "".join(arr[r][digit] for r in range(num_rows - 1))
        x.append(number)
        # print("Extracted number:", number)

    op = arr[-1][start]
    solved = calculate(x, op)
    # print("Solved operation:", solved, "\n")
    grand_total += solved
    
    i += 1

print("Final sum: ", grand_total)
