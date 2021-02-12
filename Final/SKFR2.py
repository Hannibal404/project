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


file = open("Dataset.txt")
points = []

lines = file.readlines()

for line in lines:
    points.append(np.array(list(map(int, line.split()))))
x = np.array([0, 0])
k = 8
s = 2
for point in points:
    # print(type(x), type(point))
    x = x + point
n = len(points)
totalCentroid = x/n

# Total no of features
nDim = len(points[0])
clusters = []

# randomly getting the centroids near the initial cluster
for i in range(k):
    angle = i * ((2*math.pi)/k)
    clusters.append(
        Cluster(totalCentroid[0] + math.cos(angle), totalCentroid[1] + math.sin(angle)))

#assigning the initial cluster to each data point.
for point in points:
    group = clusters[0]
    dist = distance(point, clusters[0].getCentroid())
    for cluster in clusters:
        tdist = distance(point, cluster.getCentroid())
        if tdist < dist:
            dist = tdist
            group = cluster
    group.addMember(point)

#updating the cluster centrouds
for cluster in clusters:
    x = np.array([0 for i in range(nDim)])
    members = cluster.getMembers()
    for member in members:
        x += member

    n = len(cluster.getMembers())
    if n != 0:
        cluster.setCentroid(x/n)
    # print(cluster.getCentroid())
""""Uptil now found clusters updated clusters and intialized the process
    now the clustering starts
"""
# for cluster in clusters:
#     print(len(cluster.getMembers()))
z = 1
change = True
while change == True:
    z += 1
    change = False
    # Centroid calculation
    for cluster in clusters:
        x = np.array([0 for i in range(nDim)])
        members = cluster.getMembers()
        for member in members:
            x += member

        n = len(cluster.getMembers())
        if n != 0:
            cluster.setCentroid(x/n)

    # Feature ranking
    # Local ranking 
    j = 0
    for cluster in clusters:
        featureRanks = []
        for l in range(nDim):
            djl = cluster.getLength()*(cluster.getCentroid()[l]**2)
        featureRanks.append((j,l,djl))
        j += 1     



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