import math
total = 0
matrix = []

file_object = open("input.txt", "r")
for line in file_object:
    line = line.strip()
    matrix.append(line)
newMatrix = matrix.copy()
    
for rowIndex, row in enumerate(matrix):
    for colIndex, item in enumerate(row):
        
        if item == "@":
            foundFailure = 0
            cardinalDirections = []
            failureString = "@"
            upClear = rowIndex - 1 >= 0
            rClear = colIndex + 1 < len(row)
            dClear = rowIndex + 1 < len(matrix)
            lClear = colIndex - 1 >= 0
            
            # North
            if upClear:
                cardinalDirections.append("".join([matrix[rowIndex-1][colIndex]]))
            
            # NorthEast
            if upClear and rClear:
                cardinalDirections.append("".join([matrix[rowIndex-1][colIndex+1]]))

            # # East
            if rClear:
                cardinalDirections.append("".join(row[colIndex+1]))

            # # SouthEast
            if rClear and dClear:
                cardinalDirections.append("".join([matrix[rowIndex+1][colIndex+1]]))
            
            # # South
            if dClear:
                cardinalDirections.append("".join([matrix[rowIndex+1][colIndex]]))
            
            # # SouthWest
            if dClear and lClear:
                cardinalDirections.append("".join([matrix[rowIndex+1][colIndex-1]]))
            
            # # West
            if lClear:
                cardinalDirections.append("".join(row[colIndex-1]))
            
            # # NorthWest
            if upClear and lClear:
                cardinalDirections.append("".join([matrix[rowIndex-1][colIndex-1]]))

            # print(cardinalDirections)
            for direction in cardinalDirections:
                if failureString in direction:
                    foundFailure += 1
            if foundFailure < 4:
                # print(f"Safe at {rowIndex}, {colIndex}")
                total += 1
                newMatrix[rowIndex] = newMatrix[rowIndex][:colIndex] + "X" + newMatrix[rowIndex][colIndex+1:]
print(total)
for row in newMatrix:
    print(row)
