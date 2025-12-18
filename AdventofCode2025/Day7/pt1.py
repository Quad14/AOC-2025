import math
matrix = []
newMatrix = []
previousLine = ""
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
    elif previousLine != "":
        newRow = ""
        index = 0
        while index < len(row):
            if row[index] == "." and previousLine[index] == "|":
                newRow += "|"
            elif row[index] == "^" and previousLine[index] == "|":
                if newRow[index - 1] == ".":
                    newRow = newRow[:-1]  # remove last character
                    newRow += "|^|"
                    index += 1  # skip next character
                else:
                    newRow += "^|"
                    index += 1  # skip next character
                grandTotal += 1
            else:
                newRow += row[index]
            index += 1
        row = newRow


    previousLine = row
    newMatrix.append(row)

for row in newMatrix:
    print(row)
print(grandTotal)