from Cluster import distance, Cluster, getClusters


def updateClusterCentroid(cluster):
    members = cluster.getMembers()
    l = len(members)
    if l == 0:
        return
    else:
        x, y = 0, 0
        for member in members:
            x += member[0]
            y += member[1]
        cluster.setCentroid(x/l, y/l)
        return cluster.getCentroid()


def changeInClusters(clusters, k):
    change = True
    for cluster in clusters:
        initial = cluster.getCentroid()
        final = updateClusterCentroid(cluster)
        if (initial == final):
            change = False
    return change

def lloydClusters(points, k):
    x, y = 0, 0
    for point in points:
        x += point[0]
        y += point[1]
    n = len(points)
    # intial centroid with all points
    totalCentroid = (x/n, y/n)
    # random cluster centroids around the intial point
    clusters = getClusters(k, totalCentroid)
    # assigning the points to the cluster
   
    for point in points:
        for cluster in clusters:
            group = cluster
            dist = distance(point, group.getCentroid())
            # finding the cluster which is closest to the data entry
            for cluster1 in clusters:
                tempCluster = cluster1
                tempDistance = distance(point,tempCluster.getCentroid())
                if (tempDistance < dist):
                    dist = tempDistance
                    minDistCluster = tempCluster
            minDistCluster.addMember(point)
            t = changeInClusters(clusters,k)
            if (t==False):
                break
    # for point in points:
    #     group = clusters[0]
    #     dist = distance(point,clusters[0].getCentroid())
    #     for cluster in clusters:
    #         tdist = distance(point, cluster.getCentroid())
    #         if tdist<dist:
    #             dist = tdist
    #             group = cluster
    #     group.addMember(point)

    # # update centroids
    # for cluster in clusters:
    #     x,y = 0,0
    #     members = cluster.getMembers()
    #     for member in members:
    #         x += member[0]
    #         y += member[1]
    #     n = len(cluster.getMembers())
    #     if n!=0:
    #         cluster.setCentroid((x/n,y/n))
    #     print(cluster.getCentroid())

    # z = 1
    # change = True
    # while change == True and z <= 50:
    #     z += 1
    #     # change = False
    #     for point in points:
    #         group = clusters[0]
    #         dist = distance(point, clusters[0].getCentroid())
    #         for cluster in clusters:
    #             tdist = distance(point, cluster.getCentroid())
    #             if tdist < dist:
    #                 dist = tdist
    #                 group = cluster
    #         group.addMember(point)

    #     for cluster in clusters:
    #         x, y = 0, 0
    #         members = cluster.getMembers()
    #         for member in members:
    #             x += member[0]
    #             y += member[1]
    #         n = len(cluster.getMembers())
    #         if n != 0:
    #             cluster.setCentroid((x/n, y/n))
    #         # print(cluster.getCentroid())

    return clusters
