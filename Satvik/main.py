import math
import random
from lloydCluster import lloydClusters
import matplotlib.pyplot as plot
from printer import printer

file = open("Dataset.txt")
points = []

lines = file.readlines()

for line in lines:
    points.append(tuple(map(int, line.split())))
x, y = 0, 0
k = 8

clusters = lloydClusters(points, k)
printer(clusters)
