# ---------------- ADVENT OF CODE 2025 ---------------- #

# ---------------- DAY 2 PART 1 ---------------- #

id_sum_1 = 0

with open("input_2.txt") as file:
    ranges = file.read().split(",")

for r in ranges:
    # print("Checking range:", r)
    start_str, end_str = r.split("-")
    start, end = int(start_str), int(end_str)

    for n in range(start, end):
        if len(str(n)) % 2 == 1: # uneven length, cannot repeat itself
            continue
        mid = len(str(n)) // 2
        left = str(n)[mid:]
        right = str(n)[:mid]
        if left == right:
            id_sum_1 += int(n)
            # print("invalid id found:", n)

print("Sum of all invalid IDs:", id_sum_1)

# ---------------- DAY 2 PART 1 ---------------- #

id_sum_2 = 0

for r in ranges:
    # print("Checking range:", r)
    start, end = r.split("-")

    for i in range(int(start), int(end)):
        s = str(i)
        max_digits = len(s)

        for num_digits in range(1, max_digits//2 + 1):
            if max_digits % num_digits != 0:
                continue

            num_splits = max_digits // num_digits
            matching = True
            comp = s[0:num_digits]

            for j in range(num_splits):
                if comp != s[j * num_digits : (j + 1) * num_digits]:
                    matching = False
                    break
                
            if matching:
                id_sum_2 += i
                # print("invalid id found:", i)
                break

print("Sum of all invalid IDs:", id_sum_2)