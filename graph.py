import csv
import numpy as np
from scipy.spatial.distance import euclidean
import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt

from fastdtw import fastdtw

# CSVファイルを読み込んでdataという配列に格納する
with open('kazuma/l_knee.csv') as f:
    kazumaLKnee = f.read().split(',')

with open('kazuma/r_knee.csv') as f:
    kazumaRKnee = f.read().split(',')

with open('kazuma/l_elbow.csv') as f:
    kazumaLElbow = f.read().split(',')

with open('kazuma/r_elbow.csv') as f:
    kazumaRElbow = f.read().split(',')


with open('taisuke/l_knee.csv') as f:
    taisukeLKnee = f.read().split(',')

with open('taisuke/r_knee.csv') as f:
    taisukeRKnee = f.read().split(',')

with open('taisuke/l_elbow.csv') as f:
    taisukeLElbow = f.read().split(',')

with open('taisuke/r_elbow.csv') as f:
    taisukeRElbow = f.read().split(',')

# 配列内の要素の型をint型に変換する
kazumaLKnee = [float(i) for i in kazumaLKnee]
kazumaRKnee = [float(i) for i in kazumaRKnee]
kazumaLElbow = [float(i) for i in kazumaLElbow]
kazumaRElbow = [float(i) for i in kazumaRElbow]

taisukeLKnee = [float(i) for i in taisukeLKnee]
taisukeRKnee = [float(i) for i in taisukeRKnee]
taisukeLElbow = [float(i) for i in taisukeLElbow]
taisukeRElbow = [float(i) for i in taisukeRElbow]

# def executeDTW(modA, modB):
#     distance, path = fastdtw(modA, modB, dist=euclidean)
#     return distance
#     return path
#     print(distance)
#     print(path)

distance, path = fastdtw(kazumaLElbow, taisukeLElbow, dist=euclidean)

plt.title('Left Elbow Joint Angles')
plt.xlabel('frames')
plt.ylabel('degrees')

plt.plot(kazumaLElbow, label = 'Kazuma')
plt.plot(taisukeLElbow, label = 'Taisuke')

for line in path:
    plt.plot(line, [kazumaLElbow[line[0]], taisukeLElbow[line[1]]], linewidth=0.2, c="gray")

plt.grid()
plt.legend(loc = 'upper left')

plt.show()