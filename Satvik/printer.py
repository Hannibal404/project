from Cluster import Cluster
import matplotlib.pyplot as plot
import numpy as np

def printer(clusters):
    l = len(clusters)
    for i in range(l):
        memberlist = clusters[i].getMembers()
        rgb = np.random.rand(3,)
        plot.scatter(*zip(*memberlist), color=rgb)
    plot.show()