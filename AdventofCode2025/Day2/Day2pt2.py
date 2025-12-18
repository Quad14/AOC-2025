import math
myList = []
invalidCounts = 0
found = False

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
        found = False
        indexString = str(i)
        # print("IndexString: " + str(indexString))
        # print("Length: " + str(len(indexString)//2))
        for j in range(1, len(indexString)//2 + 1):
            snipet = indexString[:j]
            # print("Snipet: " + snipet)
            for k in range(j, len(indexString), j):
                # print("compareSnipet: " + str(indexString[k:k+j]))
                if snipet != indexString[k:k+j]:
                    break
                if k == len(indexString) - j:
                    # print("Found repeating Index: " + indexString)
                    found = True
            if found:
                invalidCounts += i
                break
print(invalidCounts)