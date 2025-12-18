import math

connectionsMade = 0
numberOfConnectionstoMake = 1000
numberOfCircuitsMutiplied = 3
boxes = []
circuits = []
remainingBoxes = []
edges = []

class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.name = f"({x}, {y}, {z})"

file_object = open("input.txt", "r")
for line in file_object:
    line = line.strip()
    x, y, z = map(int, line.split(","))
    newBox = Box(x, y, z)
    newCircuit = [newBox]
    circuits.append(newCircuit)
    boxes.append(newBox)


def distance(x1, y1, z1, x2, y2, z2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)  # squared distance for efficiency

def updateClosestBoxes():
    global boxes
    for j in range(0, len(boxes)-1):
        box = boxes[j]
        print(f"Finding edges for Box({box.x}, {box.y}, {box.z})")
        for k in range(j + 1, len(boxes)):
            secondBox = boxes[k]
            if secondBox != box:
                newdistance = distance(box.x, box.y, box.z, secondBox.x, secondBox.y, secondBox.z)
                edge = (box, secondBox, newdistance)
                edges.append(edge)
                    # print(f"Edge added between Box({box.x}, {box.y}, {box.z}) and Box({secondBox.x}, {secondBox.y}, {secondBox.z}) at distance {newdistance}")

    edges.sort(key=lambda edge: edge[2])


def makeConnection(boxA, boxB):
    global connectionsMade
    for circuitA in circuits:
        if boxA in circuitA:
            for circuitB in circuits:
                if boxB in circuitB:
                    # merge circuits
                    if circuitA != circuitB:
                        circuitA.extend(circuitB)
                        circuits.remove(circuitB)
                    connectionsMade += 1
                    return True
                            
updateClosestBoxes()

# for edge in edges:
#     print(f"Edge between Box({edge[0].x}, {edge[0].y}, {edge[0].z}) and Box({edge[1].x}, {edge[1].y}, {edge[1].z}) at distance {edge[2]}")

index = 0
lastEdge = None
for edge in edges:
    if len(circuits) == 1:
        break
    lastEdge = edge
    makeConnection(edge[0], edge[1])

circuits = sorted(circuits, key=lambda circuit: len(circuit), reverse=True)
# print("MAKE CONNECTION")
# for circuit in circuits:
#     if len(circuit) > 1:
#         print("Circuit:")
#         for box in circuit:
#             print(f"  Box({box.x}, {box.y}, {box.z})")
# print(f"Connections made: {connectionsMade}")
firstCircuit = lastEdge[0]
lastCircuit = lastEdge[1]
print(f"First box in Circuit 1 is Box({firstCircuit.x}, {firstCircuit.y}, {firstCircuit.z})")
print(f"Last box in Circuit 1 is Box({lastCircuit.x}, {lastCircuit.y}, {lastCircuit.z})")
total = firstCircuit.x * lastCircuit.x
print(total)