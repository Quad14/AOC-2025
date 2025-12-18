import math
myList = []
invalidCounts = 0

file_object = open("day2input.txt", "r")
for line in file_object:
    line = line.strip()
    line = line.split(",")
    for item in line:
        myList.append(item)

for item in myList:
    firstindex, lastindex = item.split("-")
    firstIndex = int(firstindex)
    lastIndex = int(lastindex)
    for i in range(firstIndex, lastIndex + 1):
        indexString = str(i)
        firstHalf = indexString[:len(indexString)//2]
        secondHalf = indexString[len(indexString)//2:]
        if firstHalf == secondHalf:
            invalidCounts += i
    
print(invalidCounts)