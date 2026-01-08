# ---------------- ADVENT OF CODE 2025 ---------------- #

# ---------------- DAY 7 PART 1 ---------------- #
import numpy as np


with open("input_7.txt") as file:
    manifold = file.readlines()

beams = [[manifold[0].find("S")]] # add starting beam marked as "S"
print("Position of starting beam: ", beams[0][0])

max_layer = len(manifold)
splits = 0
i = 0 # layer

for layer in range(max_layer):
    beams.append([])
    beams[layer] = list(set(beams[layer])) # unique
    # print(f"\nBeams going into layer {i} at positions {beams[i]}")

    for beam in beams[layer]:
        if manifold[layer][beam] == "^":
            # print(f"beam split in layer {i} at position {beam}")
            beams[layer+1].append(beam-1)
            beams[layer+1].append(beam+1)
            splits += 1
        else:
            beams[layer+1].append(beam)
            # print(f"beam continues in layer {i} at position {beam}")
    
print(f"The tachyon beam was split {splits} times while travelling though the manifold")



# ---------------- DAY 7 PART 2 ---------------- #
max_layer = len(manifold)
layer_len = len(manifold[0])
beams = np.zeros((max_layer+1, layer_len)).astype(int) # zero array 

start = manifold[0].index("S") # starting beam marked "S"
beams[0][start] = 1

print("Position of starting beam: ", *np.where(beams[0] == 1)[0])


for layer in range(max_layer):
    row = beams[layer]

    # Split-mask
    mask = np.array(list(manifold[layer])) == "^"

    # Split beams
    split = row * mask
    beams[layer+1, 1:] += split[:-1]   # right shift
    beams[layer+1, :-1] += split[1:]   # left shift

    # Continue straight
    cont  = row * ~mask # = not splits
    beams[layer+1] += cont


print(f"There are {beams[max_layer].sum()} active timelines after {max_layer} layers")

