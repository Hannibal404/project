from Cluster import Cluster, distance, getClusters

def SKFR1(points,k):
    x,y = 0,0
    for point in points:
        x += point[0]
        y += point[1]
    n = len(points)
    totalCentroid = (x/n,y/n)
    clusters = getClusters(k,totalCentroid)
    for point in points:
        group = clusters[0]
        dist = distance(point,clusters[0].getCentroid())
        for cluster in clusters:
            tdist = distance(point, cluster.getCentroid())
            if tdist<dist:
                dist = tdist
                group = cluster
        group.addMember(point)
    for cluster in clusters:
        x,y = 0,0
        members = cluster.getMembers()
        for member in members:
            x += member[0]
            y += member[1]
        n = len(cluster.getMembers())
        if n!=0:
            cluster.setCentroid((x/n,y/n))
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
    return clusters