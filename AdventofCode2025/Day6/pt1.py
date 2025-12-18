import math
elements = []
grandTotal = 0
file_object = open("input.txt", "r")
for line in file_object:
    line = line.strip()
    splitLine = line.split(" ")
    toAdd = []
    for item in splitLine:
        if item != "":
            toAdd.append(item)
    elements.append(toAdd)

for column in range(len(elements[0])):
    sign = elements[len(elements)-1][column]
    # print(sign)
    total = int(elements[0][column])
    print(total)
    for row in range(1, len(elements)-1):
        if sign == "+":
            total = total + int(elements[row][column])
        elif sign == "*":
            total = total * int(elements[row][column])
    grandTotal += total
print(grandTotal)