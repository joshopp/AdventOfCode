# ---------------- ADVENT OF CODE 2025 ---------------- #

# ---------------- DAY 1 PART 1 ---------------- #
dial = 50 # starting position
password = 0

with open("input_1.txt") as file:
    lines = file.readlines()

for line in lines:
    # line format: "L829", "R3", ...
    direction = line[0]
    value = int(line[1:])
    # print(f"\nDirection: {direction}, Value: {value}")

    if direction == "L":
        dial -= value
        dial = dial % 100
    elif direction == "R":
        dial += value
        dial = dial % 100
    # print(f"Current dial position: {dial}")
    if dial == 0:
        password += 1

print(f"Final password: {password}")

# ---------------- DAY 1 PART 2 ---------------- #
dial = 50 # starting position
password = 0

for line in lines:
    # line format: "L829", "R3", ...
    direction = line[0]
    value = int(line[1:])
    print(f"\nDirection: {direction}, Value: {value}")

    if direction == "L":
        if dial == 0: # already counted as wrap around
            password -= 1
        
        dial -= value
        # print(f"Dial after counterclockwise move: {dial}")
        if dial > 0: # no wrap around
            pass
        else:
            password += - int(dial / 100) + 1 # times dial has wrapped around counterclockwise
        dial = dial % 100

    elif direction == "R":
        dial += value
        # print(f"Dial after clockwise move: {dial}")
        password += int(dial / 100) # times dial has wrapped around clockwise
        dial = dial % 100

    print(f"Current password: {password}")

print(f"Final password using method 0x434C49434B: {password}")

