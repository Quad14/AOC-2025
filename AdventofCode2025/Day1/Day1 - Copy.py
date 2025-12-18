import math
index = 50
zeroCounter = 0

file_object = open("day1input.txt", "r")
for line in file_object:
    line = line.strip()
    RL = line[0]
    turns = int(line[1:])
    print(f"index before move: {index}")
    print(f"Direction: {RL}, Turns: {turns}")
    # zeroCounter += math.floor(turns / 100)
    remainder = turns % 100
    if RL == "R":
        index += remainder
    else:
        index -= remainder
    if index < 0:
        index += 100
    if index >= 100:
        index -= 100

    if index == 0:
        zeroCounter += 1
    print(f"index after move: {index}")
print(f"0s Passed: {zeroCounter}")
print(f"Final Index: {index}")
