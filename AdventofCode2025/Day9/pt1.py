import math

points = []
largestArea = 0

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

file_object = open("input.txt", "r")
for line in file_object:
    line = line.strip()
    x, y = map(int, line.split(","))
    newPoint = Point(x, y)
    points.append(newPoint)


for point in points:
    print(f"Point: ({point.x}, {point.y})")

def calculateSizeOfRectangle(p1, p2):
    length = abs(p1.x - p2.x) + 1
    width = abs(p1.y - p2.y) + 1
    return length * width

for pointA in points:
    for pointB in points:
        if pointA != pointB:
            area = calculateSizeOfRectangle(pointA, pointB)
            if area > largestArea:
                largestArea = area

print(largestArea)