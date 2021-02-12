import math
import random

import matplotlib.pyplot as plot
import scipy


class Cluster:
    def __init__(self, a: int, b: int):
        self.centroid = (a, b)
        self.members = []

    def getCentroid(self):
        return self.centroid

    def setCentroid(self, newCentroid: tuple):
        self.centroid = newCentroid

    def getMembers(self):
        return self.members

    def addMember(self, newMember: tuple):
        self.members.append(newMember)

    def removeMember(self, member: tuple):
        self.members.remove(member)


def distance(a: tuple, b: tuple):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)


file = open("SKFR dataset 8 clusters.txt")
points = []

lines = file.readlines()

for line in lines:
    points.append(tuple(map(int, line.split())))
x, y = 0, 0
k = 8
for point in points:
    x += point[0]
    y += point[1]
n = len(points)
totalCentroid = (x/n, y/n)

clusters = []

for i in range(k):
    angle = (i * ((2*math.pi)/k)) #+ math.pi/8
    clusters.append(
        Cluster(totalCentroid[0] + math.cos(angle), totalCentroid[1] + math.sin(angle)))

# for cluster in clusters:
#     cluster.setCentroid(points[int(random.random()*n)])

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
    x, y = 0, 0
    members = cluster.getMembers()
    for member in members:
        x += member[0]
        y += member[1]
    n = len(cluster.getMembers())
    if n != 0:
        cluster.setCentroid((x/n, y/n))
    print(cluster.getCentroid())

for cluster in clusters:
    print(len(cluster.getMembers()))
z = 1
change = True
while change == True and z <= 50:
    z += 1
    # change = False
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
        x, y = 0, 0
        members = cluster.getMembers()
        for member in members:
            x += member[0]
            y += member[1]
        n = len(cluster.getMembers())
        if n != 0:
            cluster.setCentroid((x/n, y/n))
        # print(cluster.getCentroid())
for cluster in clusters:
    print(len(cluster.getMembers()))

memberlist = clusters[0].getMembers()
# print(x)
plot.scatter(*zip(*memberlist),c='blue')

memberlist = clusters[1].getMembers()
# print(x)
plot.scatter(*zip(*memberlist),c='orange')

memberlist = clusters[2].getMembers()
# print(x)
plot.scatter(*zip(*memberlist),c='yellow')

memberlist = clusters[3].getMembers()
# print(x)
plot.scatter(*zip(*memberlist),c='green')

memberlist = clusters[4].getMembers()
# print(x)
plot.scatter(*zip(*memberlist),c='indigo')

memberlist = clusters[5].getMembers()
# print(x)
plot.scatter(*zip(*memberlist),c='violet')

memberlist = clusters[6].getMembers()
# print(x)
plot.scatter(*zip(*memberlist),c='purple')

memberlist = clusters[7].getMembers()
# print(x)
plot.scatter(*zip(*memberlist),c='red')
plot.show()

# for cluster in clusters:
#     plot.scatter(*zip(*cluster.getMembers()))
#     plot.show()