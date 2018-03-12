import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation as ani

plt.figure(figsize=(10,10))
n=10
xmin = 0
xmax = 8
ymin = 0
ymax = 8

A = [[ 3, 2],
     [5,2]]
for i in range(n):
    for j in range(n):
        x=j
        y=i
        a = np.dot(A, [x, y])
        #plt.scatter(x,  y,  facecolor="b", edgecolors='none', alpha=.7, s=20)
        plt.scatter(a[i], a[i], facecolor="r", edgecolors='none', alpha=.7)

        #plt.plot([xmin,xmax],[0,0],"k", linewidth=1)
        #plt.plot([0,0],[ymin,ymax],"k", linewidth=1)
        plt.xlim(xmin, xmax)
        plt.ylim(ymin, ymax)
plt.show()
