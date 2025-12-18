import math
elements = []
grandTotal = 0
file_object = open("input.txt", "r")
for line in file_object:
    elements.append(line.rstrip('\n'))

totalProblem = []
for column in range(len(elements[0])-1, -1, -1):
    digit = ""
    for row in range(len(elements)-1):
        digit += elements[row][column]
    if digit.strip() != "":
        totalProblem.append(int(digit.strip()))

    if elements[len(elements)-1][column] == "+":
        tempTotal = 0
        print("adding")
        print(totalProblem)
        for item in totalProblem:
            tempTotal += item
        print(tempTotal)
        grandTotal += tempTotal
        totalProblem = []
    elif elements[len(elements)-1][column] == "*":
        tempTotal = 1
        print("multiplying")
        print(totalProblem)
        for item in totalProblem:
            tempTotal *= item
        print(tempTotal)
        grandTotal += tempTotal
        totalProblem = []

print(grandTotal)