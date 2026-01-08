import numpy as np
# ---------------- ADVENT OF CODE 2025 ---------------- #

# ---------------- DAY 3 PART 1 ---------------- #

joltage_total = 0

with open("input_3.txt") as file:
    lines = file.readlines()

for bank in lines:
    batteries = list(map(int, list(bank.strip())))
    # print("Batteries in bank:", batteries)

    max_1 = max(batteries[:-1])
    position = batteries.index(max_1)
    # print(f"Max battery in bank: {max_1} at position {position}")
    
    rest_bank = batteries[position + 1:]
    max_2 = max(rest_bank)
    # position_2 = rest_bank.index(max_2) + position + 1
    # print(f"Max battery in bank: {max_2} at position {position_2}")
    joltage = 10*max_1 + max_2
    joltage_total += joltage

print("Total joltage from selected batteries:", joltage_total)




# ---------------- DAY 3 PART 2 ---------------- #

joltage_total = 0
digits = 12

for bank in lines:
    batteries = list(map(int, bank.strip()))
    # print("Batteries in bank:", batteries)
    joltage = 0

    max_batteries = np.zeros(digits, dtype =int)
    positions = np.zeros(digits+1, dtype =int)

    for i in range(digits):
        remaining = digits-1-i # batteries left to select after this one

        # Slice batteries to only consider valid options
        if remaining == 0:
            current_slice = batteries[positions[i]:]
        else:
            current_slice = batteries[positions[i]:-(remaining)]
        # print(f"possible range: {current_slice}")

        max_batteries[i] = np.max(current_slice)
        positions[i+1] = np.argmax(current_slice) + positions[i] + 1

        # print(f"Max battery {i+1} is: {max_batteries[i]} at position {positions[i+1]}")
        joltage += 10 ** (remaining) * max_batteries[i]

    # print(f"Joltage for this bank: {joltage}\n")
    joltage_total += joltage

print("Total joltage from selected batteries:", joltage_total)