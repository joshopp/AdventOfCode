# ---------------- ADVENT OF CODE 2025 ---------------- #

# ---------------- DAY 5 PART 1 ---------------- #

with open("input_5.txt") as file:
    lines = file.readlines()

split = lines.index("\n")
id_ranges = lines[:split]
item_ids = lines[split+1:]

fresh_ids_start = []
fresh_ids_end = []
num_fresh = 0

for r in id_ranges:
    # print("Checking range:", r)
    start, end = r.split("-")
    fresh_ids_start.append(int(start))
    fresh_ids_end.append(int(end))
    print("Added range of fresh IDs:", (start, end))
num_ranges = len(fresh_ids_start)
print("number of fresh ID ranges:", num_ranges)

for i in item_ids:
    for j in range(num_ranges):
        if fresh_ids_start[j] <= int(i.strip()) <= fresh_ids_end[j]:
            num_fresh += 1
            print("Found fresh item ID:", i.strip())
            break

print("Number of fresh item IDs found:", num_fresh)


# ---------------- DAY 5 PART 2 ---------------- #
sorted_list = sorted(zip(fresh_ids_start, fresh_ids_end))
# print(sorted_list)

for i in range(1, num_ranges):
    if sorted_list[i-1][1] <  sorted_list[i][0]:
        continue
    print("i = ", i, ", Merging ranges:", sorted_list[i-1], "and", sorted_list[i])
    merge = min(sorted_list[i-1][1], sorted_list[i][0])
    max_val = max(sorted_list[i-1][1], sorted_list[i][1])
    sorted_list[i-1] = (sorted_list[i-1][0], merge)
    sorted_list[i] = (merge + 1, max_val)
    print("After merging:", sorted_list[i-1], "and", sorted_list[i])

fresh_ids_start, fresh_ids_end = zip(*sorted_list)
num_fresh_ids = sum(fresh_ids_end) - sum(fresh_ids_start) + num_ranges
print("Total number of fresh item IDs available:", num_fresh_ids)