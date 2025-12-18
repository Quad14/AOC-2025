import math
freshIds = []
IdtoCheck = []
beforeSplit = True
total = 0
file_object = open("input.txt", "r")
for line in file_object:
    if line == "\n":
        break
    else:
        line = line.strip()
        firstindex, lastindex = line.split("-")
        firstindex = int(firstindex)
        lastindex = int(lastindex)
        freshIds.append((firstindex, lastindex))

freshIds.sort()
index = 1
while index < len(freshIds):
    if index != 0:
        currentRange = freshIds[index]
        prevRange = freshIds[index - 1]
        if currentRange[0] <= prevRange[1]:
            freshIds[index - 1] = (prevRange[0], max(prevRange[1], currentRange[1]))
            freshIds.pop(index)
            index -= 1
    index += 1
    
for id in freshIds:
    total += id[1] - id[0] + 1

print(total)