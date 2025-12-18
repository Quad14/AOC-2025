import math
matrix = []
newMatrix = []
previousLine = ""
previousWays = [0] * 1000
grandTotal = 0
file_object = open("input.txt", "r")
for line in file_object:
    line = line.strip()
    matrix.append(line)

# Condition are:
# Contains S then replace with |
# If previous line was | and current line is . then replace with |
# if ^ and previous line in that column is | them replace with |^|
for row in matrix:
    if "S" in row:
        row = row.replace("S", "|")

        previousWays[int((len(row)-1) /2)] = 1
    elif previousLine != "":
        newRow = ""
        newWays = [0] * len(row)
        index = 0
        while index < len(row):
            if row[index] == "." and previousLine[index] == "|":
                newRow += "|"
                newWays[index] += previousWays[index]
            elif row[index] == "^" and previousLine[index] == "|":
                if newRow[index - 1] == ".":
                    newRow = newRow[:-1]  # remove last character
                    newRow += "|^|"
                    newWays[index - 1] = previousWays[index]
                    newWays[index +1] = previousWays[index]
                    newWays[index +1] += previousWays[index+1]
                    index += 1  # skip next character
                    
                else:
                    newRow += "^|"
                    newWays[index - 1] += previousWays[index]
                    newWays[index +1] = previousWays[index]
                    newWays[index +1] += previousWays[index+1]
                    index += 1  # skip next character
            else:
                newRow += row[index]
                newWays[index] = 0
            index += 1
        print(newRow)
        print(newWays)
        
        row = newRow
        previousWays = newWays
    tempTotal = 0
    for item in previousWays:
        tempTotal += item
    print(tempTotal)
    previousLine = row
    newMatrix.append(row)

for item in previousWays:
    grandTotal += item
print(grandTotal)