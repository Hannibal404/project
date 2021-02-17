import math
import numpy as np

import matplotlib.pyplot as plot


def removearray(L, arr):
    ind = 0
    size = len(L)
    while ind != size and not np.array_equal(L[ind], arr):
        ind += 1
    if ind != size:
        L.pop(ind)
    else:
        raise ValueError('array not found in list.')


class Cluster:
    def __init__(self, a: int, b: int):
        self.centroid = np.array([a, b], dtype="int64")
        self.members = []

    def getCentroid(self):
        return self.centroid

    def setCentroid(self, newCentroid):
        self.centroid = newCentroid

    def getMembers(self):
        return self.members

    def addMember(self, newMember):
        self.members.append(newMember)

    def removeMember(self, member):
        removearray(self.members, member)

    def getLength(self):
        return len(self.members)


def distance(a: np.array, b: np.array):
    return abs(np.linalg.norm(a - b))


file = open("Pradyumn/SKFR dataset 8 clusters.txt")
points = []

outfile = open("Pradyumn/output.out", "w")

lines = file.readlines()

for line in lines:
    points.append(
        np.array(list(map(lambda x: x, map(int, line.split()))), dtype="int64"))
nDim = len(points[0])
x = np.array([0 for i in range(nDim)], dtype="int64")
k = 4
s = 2
for point in points:
    x = x + point
n = len(points)
totalCentroid = x/n
diffSq = 0

for point in points:
    diffSq += abs(np.linalg.norm(point - totalCentroid))

variance = diffSq / n
std = math.sqrt(variance)

clusters = []

for i in range(k):
    angle = i * ((2*math.pi)/k)
    clusters.append(
        Cluster(totalCentroid[0] + (std * math.cos(angle)), totalCentroid[1] + (std * math.sin(angle))))

for point in points:
    group = clusters[0]
    dist = distance(point, clusters[0].getCentroid())
    for cluster in clusters:
        tdist = distance(point, cluster.getCentroid())
        if tdist < dist:
            dist = tdist
            group = cluster
    group.addMember(point)

for cluster in clusters:
    x = np.array([0, 0], dtype="int64")
    members = cluster.getMembers()
    for member in members:
        x += member

    n = len(cluster.getMembers())
    if n != 0:
        cluster.setCentroid(x/n)
    # print(cluster.getCentroid())

# for cluster in clusters:
#     print(len(cluster.getMembers()))
z = 1


outfile.write(f"z = {z}: ")
for cluster in clusters:
    outfile.write(f"({len(cluster.getMembers())} , {cluster.getCentroid()}), ")
outfile.write("\n")


change = True
while change == True and z < 10:
    print(z)
    z += 1
    change = False
    for cluster in clusters:
        centroid = cluster.getCentroid()
        members = cluster.getMembers()
        for member in members:
            dist = distance(centroid, member)
            group = cluster
            for cluster2 in clusters:
                tdist = distance(member, cluster2.getCentroid())
                if tdist < dist:
                    dist = tdist
                    group = cluster2
            if group == cluster:
                continue
            else:
                change = True
                cluster.removeMember(member)
                cluster2.addMember(member)
    for cluster in clusters:
        x = np.array([0, 0], dtype="int64")
        members = cluster.getMembers()
        for member in members:
            # print(f"x ={x}, element ={member}")
            # if x[1] < 0:
            #     print(f"x: {x}, current element = {member}")
            #     exit()
            x = x + member
        n = len(cluster.getMembers())
        if n != 0:
            cluster.setCentroid(x/n)
    outfile.write(f"z = {z}: ")
    for cluster in clusters:
        outfile.write(
            f"({len(cluster.getMembers())} , {cluster.getCentroid()}), ")
    outfile.write("\n")

# for cluster in clusters:
#     print(cluster.getMembers())
# memberlist = clusters[7].getMembers()
# print(z)
# plot.scatter(*zip(*memberlist))
# plot.show()

if clusters[0].getLength() > 0:
    plot.scatter(*zip(*clusters[0].getMembers()), c="red")
if clusters[1].getLength() > 0:
    plot.scatter(*zip(*clusters[1].getMembers()), c="green")
if clusters[2].getLength() > 0:
    plot.scatter(*zip(*clusters[2].getMembers()), c="blue")
if clusters[3].getLength() > 0:
    plot.scatter(*zip(*clusters[3].getMembers()), c="purple")
# if clusters[4].getLength() > 0:
#     plot.scatter(*zip(*clusters[4].getMembers()), c="yellow")
# if clusters[5].getLength() > 0:
#     plot.scatter(*zip(*clusters[5].getMembers()), c="orange")
# if clusters[6].getLength() > 0:
#     plot.scatter(*zip(*clusters[6].getMembers()), c="cyan")
# if clusters[7].getLength() > 0:
#     plot.scatter(*zip(*clusters[7].getMembers()), c="black")
plot.show()
