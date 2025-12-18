import math
freshIds = []
IdtoCheck = []
beforeSplit = True
total = 0
file_object = open("input.txt", "r")
for line in file_object:
    if line == "\n":
        beforeSplit = False
    else:
        line = line.strip()
        if beforeSplit:
            freshIds.append(line)
        else:
            IdtoCheck.append(int(line))

for Id in IdtoCheck:
    for freshId in freshIds:
            firstindex, lastindex = freshId.split("-")
            firstIndex = int(firstindex)
            lastIndex = int(lastindex)
            if Id >= firstIndex and Id <= lastIndex:
                total += 1
                break

print(total)