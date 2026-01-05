import math
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

points = []
largestArea = 0
largestPointA = None
largestPointB = None
largestPointC = None
largestPointD = None
xRanges = []
yRanges = []

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

file_object = open("input.txt", "r")
# First path populates points
for line in file_object:
    line = line.strip()
    x, y = map(int, line.split(","))
    newPoint = Point(x, y)
    points.append(newPoint)

polygon = Polygon(points)

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
                pointC = Point(pointA.x, pointB.y)
                pointD = Point(pointB.x, pointA.y)
                testPolygon = Polygon([pointA, pointC, pointB, pointD])
                # print(f"PointC: ({pointC.x}, {pointC.y}), PointD: ({pointD.x}, {pointD.y})")
                # cFound = False
                # dFound = False
                # if ((pointC in points) or polygon.contains(pointC)):
                #     cFound = True
                # if ((pointD in points) or polygon.contains(pointD)):
                #     dFound = True
                if polygon.covers(testPolygon):
                    print(f"New Largest Area Found: {area}")
                    largestArea = area
                    largestPointA = pointA
                    largestPointB = pointB
                    largestPointC = pointC
                    largestPointD = pointD



print(largestArea)
print(f"Largest Points: A({largestPointA.x}, {largestPointA.y}), B({largestPointB.x}, {largestPointB.y})")
print(f"                  C({largestPointC.x}, {largestPointC.y}), D({largestPointD.x}, {largestPointD.y})")


# row ranges between points y dims
# We get p1 and p2 from the for loops above but need to also determine p3 and p4
# and make sure that p3 and p4 are in the ranges of other points to form a valid rectangle
# p3.x = p1.x, p3.y = p2.y