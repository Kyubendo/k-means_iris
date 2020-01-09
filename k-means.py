import numpy as np
import random


def hcube(data):
    min = data.min()
    max = data.max()
    for i in range(len(data)):
        for j in range(len(data[0])):
            data[i][j] = round(2*((data[i][j]-min)/(max-min))-1, 3)
    return data


def assignment(data, centroids, nearest, dist_arr):
    for i in range(len(data)):
        for j in range(len(centroids)):
            dist = np.linalg.norm(data[i]-centroids[j])
            if dist < nearest[i][1]:
                nearest[i][1] = dist
                for k in range(len(centroids[0])):
                    dist_arr[i][k] = np.linalg.norm(data[i][k]-centroids[j][k])
                nearest[i][0] = j


def calc_centroids(data, centroids, nearest):
    for i in range(len(centroids)):
        mean = np.zeros(4)

        num = 0
        for j in range(len(nearest)):
            if nearest[j][0] == i:
                mean += data[j]
                num += 1
        if num != 0:
            mean /= num
        else:
            mean = centroids[i]
        centroids[i] = mean


d = []
with open('iris.data') as f:
    for i in f:
        i = i.split(',')
        d.append(i[:-1])
d.pop()

d = [[float(x) for x in y] for y in d]
data = np.array(d).T
data = hcube(data)
data = data.T
np.random.shuffle(data)

k = 3
centroids = [[random.uniform(-.5, .5), random.uniform(-.5, .5),
              random.uniform(-.5, .5), random.uniform(-.5, .5)]for i in range(k)]
centroids = np.array(centroids)

nearest = np.full((len(data), 2), np.inf)
dist_arr = np.zeros((150, 4))
for i in range(100):
    assignment(data, centroids, nearest, dist_arr)
    calc_centroids(data, centroids, nearest)

print(centroids, "\n\n")
print(dist_arr, "\n\n")
print(sum(dist_arr))
