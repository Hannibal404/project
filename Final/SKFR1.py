import math
import numpy as np

import matplotlib.pyplot as plot


class Cluster:
    def __init__(self, arr: list):
        self.centroid = np.array(arr)
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
        L = self.members
        ind = 0
        size = len(L)
        while ind != size and not np.array_equal(L[ind], member):
            ind += 1
        if ind != size:
            L.pop(ind)
        else:
            raise ValueError('array not found in list.')

    def getLength(self):
        return len(self.members)



def distance(a: np.array, b: np.array):
    return np.linalg.norm(a - b)


file = open("SKFR dataset 8 clusters.txt")
points = []

lines = file.readlines()

for line in lines:
    points.append(np.array(list(map(int, line.split()))))
nDim = len(points[0])
x = np.array([0 for i in range(nDim)])
k = 8
s = 2
for point in points:
    x = x + point
n = len(points)

totalCentroid = x/n     # Initial totalCentroid 

clusters = []

for i in range(k):      # set of clusters around the initial total Centroid
    randSign = np.random(10)
    randMag = np.random(1.0)
    clusters.append(totalCentroid[i]+((-1)**randSign)*randMag for i in range (nDim))



for point in points:    # Assigning data sets to the nearest cluster in the previous formed set
    group = clusters[0]
    dist = distance(point, clusters[0].getCentroid())
    for cluster in clusters:
        tdist = distance(point, cluster.getCentroid())
        if tdist < dist:
            dist = tdist
            group = cluster
    group.addMember(point)

# beginning of the clustering process
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
    featureRanks = []

    for l in range(nDim):
        dl = 0
        for cluster in clusters:
            dl += cluster.getLength() * (cluster.getCentroid()[l] ** 2)
        featureRanks.append((l, dl))
    
    # Sorting the feature ranks in decending order of ranks of each feature 
    featureRanks.sort(key=lambda x: x[1], reverse=True)
    # Selecting the features with rank less than s
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
