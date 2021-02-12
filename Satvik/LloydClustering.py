from Cluster import distance, Cluster, getClusters
import math

def lloydClusters(points,k):
    x,y = 0,0
    for point in points:
        x += point[0]
        y += point[1]
    n = len(points)
    totalCentroid = (x/n, y/n)

    clusters = getClusters(k,totalCentroid)

    #initialize points to a cluster 
    for point in points:
        group = clusters[0]
        dist = distance(point, clusters[0].getCentroid())
        for cluster in clusters:
            tdist = distance(point, cluster.getCentroid())
            if tdist < dist:
                dist = tdist
                group = cluster
        group.addMember(point)

    #update clusters
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

    z = 1
    change = True
    while change == True:
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
            x, y = 0, 0
            members = cluster.getMembers()
            for member in members:
                x += member[0]
                y += member[1]
            n = len(cluster.getMembers())
            if n != 0:
                cluster.setCentroid((x/n, y/n))