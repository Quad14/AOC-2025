import math
total = 0

file_object = open("input.txt", "r")
for line in file_object:
    line = line.strip()
    myList = []
    solutionList = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    previousIndex = -1 # Done to make sure we start at 0
    finalAnswer = ""
    for item in line:
        myList.append(int(item))

    for index in range(1, 13):
        for i in range(previousIndex+1, len(myList)-(12 - index)):
            if myList[i] > solutionList[index - 1]:
                solutionList[index - 1] = myList[i]
                previousIndex = i
    print(solutionList)
    for i in range(0, len(solutionList)):
        finalAnswer += str(solutionList[i])
    total += int(finalAnswer)
print(total)