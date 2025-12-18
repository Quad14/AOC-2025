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
            foundFailure = False
            cardinalDirections = []
            failureString = "@@@@"
            upClear = rowIndex - 5 >= 0
            rClear = colIndex + 5 <= len(row)
            dClear = rowIndex + 5 <= len(matrix)
            lClear = colIndex - 4 >= 0
            
            # North
            if upClear:
                cardinalDirections.append("".join([matrix[rowIndex-1][colIndex], matrix[rowIndex-2][colIndex], matrix[rowIndex-3][colIndex], matrix[rowIndex-4][colIndex]]))
            
            # NorthEast
            if upClear and rClear:
                cardinalDirections.append("".join([matrix[rowIndex-1][colIndex+1], matrix[rowIndex-2][colIndex+2], matrix[rowIndex-3][colIndex+3], matrix[rowIndex-4][colIndex+4]]))

            # # East
            if rClear:
                cardinalDirections.append(row[colIndex+1:colIndex+5])

            # # SouthEast
            if rClear and dClear:
                cardinalDirections.append("".join([matrix[rowIndex+1][colIndex+1], matrix[rowIndex+2][colIndex+2], matrix[rowIndex+3][colIndex+3], matrix[rowIndex+4][colIndex+4]]))
            
            # # South
            if dClear:
                cardinalDirections.append("".join([matrix[rowIndex+1][colIndex], matrix[rowIndex+2][colIndex], matrix[rowIndex+3][colIndex], matrix[rowIndex+4][colIndex]]))
            
            # # SouthWest
            if dClear and lClear:
                cardinalDirections.append("".join([matrix[rowIndex+1][colIndex-1], matrix[rowIndex+2][colIndex-2], matrix[rowIndex+3][colIndex-3], matrix[rowIndex+4][colIndex-4]]))
            
            # # West
            if lClear:
                cardinalDirections.append(row[colIndex-4:colIndex])
             
            # # NorthWest
            if upClear and lClear:
                cardinalDirections.append("".join([matrix[rowIndex-1][colIndex-1], matrix[rowIndex-2][colIndex-2], matrix[rowIndex-3][colIndex-3], matrix[rowIndex-4][colIndex-4]]))

            for direction in cardinalDirections:
                if failureString in direction:
                    foundFailure = True
                    # print(direction)
                    # print(f"Failure found at {rowIndex}, {colIndex}")
                    break
            if not foundFailure:
                # print(f"Safe at {rowIndex}, {colIndex}")
                total += 1
                newMatrix[rowIndex] = newMatrix[rowIndex][:colIndex] + "X" + newMatrix[rowIndex][colIndex+1:]
print(total)
for row in newMatrix:
    print(row)
