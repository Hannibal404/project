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
        self.centroid = np.array([a, b])
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


def distance(a: np.array, b: np.array):
    return np.linalg.norm(a - b)


file = open("SKFR dataset 8 clusters.txt")
points = []

lines = file.readlines()

for line in lines:
    points.append(np.array(list(map(int, line.split()))))
x = np.array([0, 0])
k = 8
for point in points:
    # print(type(x), type(point))
    x = x + point
n = len(points)
totalCentroid = x/n

clusters = []

for i in range(k):
    angle = i * ((2*math.pi)/k)
    clusters.append(
        Cluster(totalCentroid[0] + math.cos(angle), totalCentroid[1] + math.sin(angle)))

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
    x = np.array([0, 0])
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
change = True
while change == True and z < 10:
    z += 1
    change = False
    for cluster in clusters:
        members = cluster.getMembers()
        for member in members:
            dist = distance(cluster.getCentroid(), member)
            group = cluster
            for cluster2 in clusters:
                tdist = distance(member, cluster2.getCentroid())
                if tdist < dist:
                    dist = tdist
                    group = cluster2
            if cluster2 == cluster:
                continue
            else:
                change = True
                cluster.removeMember(member)
                cluster2.addMember(member)
    for cluster in clusters:
        x = np.array([0, 0])
        members = cluster.getMembers()
        for member in members:
            x += member
        n = len(cluster.getMembers())
        if n != 0:
            cluster.setCentroid(x/n)
for cluster in clusters:
    print(len(cluster.getMembers()))

memberlist = clusters[7].getMembers()
print(z)
plot.scatter(*zip(*memberlist))
plot.show()
