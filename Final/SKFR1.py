import math
import numpy as np

import matplotlib.pyplot as plot


def removearray(L: list, arr: np.array):
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

    def setCentroid(self, newCentroid: np.array):
        self.centroid = newCentroid

    def getMembers(self):
        return self.members

    def addMember(self, newMember: np.array):
        self.members.append(newMember)

    def removeMember(self, member: np.array):
        removearray(self.members, member)

    def getLength(self):
        return len(self.members)


def distance(a: np.array, b: np.array):
    return np.linalg.norm(a - b)


file = open("SKFR dataset 8 clusters.txt")
points = []

lines = file.readlines()

for line in lines:
    points.append(np.array(list(map(int, line.split()))))
x = np.array([0, 0])
k = 8
s = 2
for point in points:
    x = x + point
n = len(points)
totalCentroid = x/n         # Centroid of all data points

nDim = len(points[0])

clusters = []

for i in range(k):          # Getting centroids for clustering around the totalCentroid
    angle = i * ((2*math.pi)/k)
    clusters.append(
        Cluster(totalCentroid[0] + math.cos(angle), totalCentroid[1] + math.sin(angle)))


# Initialization
for point in points:
    group = clusters[0]
    dist = distance(point, clusters[0].getCentroid())
    for cluster in clusters:
        tdist = distance(point, cluster.getCentroid())
        if tdist < dist:
            dist = tdist
            group = cluster
    group.addMember(point)

# updating clusters with the (first) assigned data sets to each cluster
for cluster in clusters:
    x = np.array([0, 0])
    members = cluster.getMembers()
    for member in members:
        x += member

    n = len(cluster.getMembers())
    if n != 0:
        cluster.setCentroid(x/n)

z = 1
change = True
while change == True:
    z += 1
    change = False
    # Centroid calculation for each cluster
    for cluster in clusters:
        x = np.array([0, 0])
        members = cluster.getMembers()
        for member in members:
            x += member

        n = len(cluster.getMembers())
        if n != 0:
            cluster.setCentroid(x/n)

    # Feature ranking
    featureRanks = []

    for l in range(nDim):
        dl = 0
        for cluster in clusters:
            dl += cluster.getLength() * (cluster.getCentroid()[l] ** 2)
        featureRanks.append((l, dl))

    featureRanks.sort(key=lambda x: x[1], reverse=True)

    features = set([featureRanks[i][0] for i in range(s)])

    for cluster in clusters:
        for i in range(nDim):
            centroid = cluster.getCentroid()
            if i not in features:
                centroid[i] = 0
            cluster.setCentroid(centroid)
    # Cluster reassignment
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
    print(len(cluster.getMembers()))

memberlist = clusters[7].getMembers()
print(z)
plot.scatter(*zip(*memberlist))
plot.show()
