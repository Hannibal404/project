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
totalCentroid = x/n

diffSq = 0
for point in points:
    diffSq += abs(np.linalg.norm(point - totalCentroid))

variance = diffSq / n
std = math.sqrt(variance)

clusters = []

for i in range(k):
    angle = i * ((2*math.pi)/k)

    # Seeding initial centroids
    clusters.append(Cluster(
        [totalCentroid[0] + (std * math.cos(angle)), totalCentroid[1] + (std * math.sin(angle))]))

# Initial cluster assignment
for point in points:
    group = clusters[0]
    dist = distance(point, clusters[0].getCentroid())
    for cluster in clusters:
        tdist = distance(point, cluster.getCentroid())
        if tdist < dist:
            dist = tdist
            group = cluster
    group.addMember(point)


z = 1  # Measuring number of iterations
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

        # Feature selection
        featureRanks = []
        for l in range(nDim):
            featureRanks.append(
                (l, cluster.getLength() * (cluster.getCentroid()[l] ** 2)))
        featureRanks.sort(key=lambda x: x[1], reverse=True)

        features = set([featureRanks[i][0] for i in range(s)])
        centroid = cluster.getCentroid()

        # Setting non-informative features to be 0 to assist with implementation
        for l in range(nDim):
            if l not in features:
                centroid[l] = 0
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
            if group == cluster:
                continue
            else:
                change = True
                cluster.removeMember(member)
                group.addMember(member)

num = 0
for cluster in clusters:
    num += cluster.getLength()
    print(cluster.getLength())
print("total =", num)

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
if clusters[4].getLength() > 0:
    plot.scatter(*zip(*clusters[4].getMembers()), c="yellow")
if clusters[5].getLength() > 0:
    plot.scatter(*zip(*clusters[5].getMembers()), c="orange")
if clusters[6].getLength() > 0:
    plot.scatter(*zip(*clusters[6].getMembers()), c="cyan")
if clusters[7].getLength() > 0:
    plot.scatter(*zip(*clusters[7].getMembers()), c="black")
plot.show()
