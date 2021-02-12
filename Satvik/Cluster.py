import math


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



# Used for getting random clusters around the intially found centroid 
def getClusters(k,initial: tuple):
    clusters =[]
    for i in range(k):
        
        angle = (i*((2*math.pi)/k))
        clusters.append(Cluster(initial[0] + math.cos(angle),initial[1]+math.sin(angle)))
    return clusters