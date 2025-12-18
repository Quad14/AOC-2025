import math
total = 0

file_object = open("input.txt", "r")
for line in file_object:
    line = line.strip()
    myList = []
    firstBig = 1
    firstBigIndex = 0
    secondBig = 1
    for item in line:
        myList.append(int(item))
    for i in range(0, len(myList)-1):
        if myList[i] > firstBig:
            firstBig = myList[i]
            firstBigIndex = i
    for i in range(firstBigIndex + 1, len(myList)):
        if myList[i] > secondBig:
            secondBig = myList[i]
    total += int(str(firstBig) + str(secondBig))
    # print(myList)
    # print(int(str(firstBig) + str(secondBig)))
print(total)


# file_object = open("input.txt", "r")
# for line in file_object:
#     line = line.strip()
#     myList = []
#     for item in line:
#         myList.append(item)
#     myList.sort(reverse=True)
#     print(myList[0] + myList[1])
#     total += int(myList[0] + myList[1])