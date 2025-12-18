import math

connectionsMade = 0
numberOfConnectionstoMake = 10
boxes = []
remainingBoxes = []

class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.name = f"({x}, {y}, {z})"
        self.connections = 0
        self.shortestDistance = 10000000
        self.closestBox = None
        self.nextBox = None
        self.prevBox = None


file_object = open("input.txt", "r")
for line in file_object:
    line = line.strip()
    x, y, z = map(int, line.split(","))
    newBox = Box(x, y, z)
    boxes.append(newBox)

def distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)

def updateClosestBoxes():
    print("Updating closest boxes")
    global boxes
    for box in boxes:
        tempShortestDistance = 10000000
        tempClosestBox = box.closestBox
        if box.connections < 2:
            for secondBox in boxes:
                if secondBox != box and secondBox.connections < 2:
                    newdistance = distance(box.x, box.y, box.z, secondBox.x, secondBox.y, secondBox.z)
                    if newdistance < tempShortestDistance:
                        tempShortestDistance = newdistance
                        tempClosestBox = secondBox
        if tempShortestDistance != box.shortestDistance and tempShortestDistance != 10000000:
            box.shortestDistance = tempShortestDistance
            box.closestBox = tempClosestBox
            print(f"Box({box.x}, {box.y}, {box.z}) closestBox updated to Box({box.closestBox.x}, {box.closestBox.y}, {box.closestBox.z}) at distance {tempShortestDistance}")

    boxes = sorted(boxes, key=lambda box: (box.shortestDistance))
    # for Box in boxes:
    #     print(f"Box({Box.x}, {Box.y}, {Box.z}) closestBox is Box({Box.closestBox.x}, {Box.closestBox.y}, {Box.closestBox.z}) at distance {Box.shortestDistance}")

def makeConnection(box):
    global connectionsMade
    if box.closestBox != box and box.closestBox != box.nextBox and box.closestBox != box.prevBox:
        if box.connections < 2 and box.closestBox.connections < 2:
            box.connections += 1
            box.closestBox.connections += 1
            # order 1 -> 2
            if box.nextBox is None and box.closestBox.prevBox is None:
                box.nextBox = box.closestBox
                box.closestBox.prevBox = box
                connectionsMade += 1
                updateClosestBoxes()
            # order 2 -> 1
            elif box.prevBox is None and box.closestBox.nextBox is None:
                box.prevBox = box.closestBox
                box.closestBox.nextBox = box
                connectionsMade += 1
                updateClosestBoxes()

updateClosestBoxes()

index = 0
while connectionsMade < numberOfConnectionstoMake:
    # print(f"Connecting Box({boxes[i].x}, {boxes[i].y}, {boxes[i].z}) to Box({boxes[i].closestBox.x}, {boxes[i].closestBox.y}, {boxes[i].closestBox.z})")
    makeConnection(boxes[index])
    index += 1

for Box in boxes:
    if Box.prevBox is None and Box.nextBox is not None:
        print(f"Start of circuit at Box({Box.x}, {Box.y}, {Box.z})")
        boxInCircuit = Box
        while boxInCircuit.nextBox is not None:
            print(f"(->{boxInCircuit.nextBox.name})")
            boxInCircuit = boxInCircuit.nextBox

# print(f"Total connections made: {connectionsMade}")
