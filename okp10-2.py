import numpy as np
import matplotlib.pyplot as plt

#plt.figure(figsize = (10,10))
n = 10

A = ( [3,2],
      [5,2] )
for i in range(n):
    for j in range(n):
        
        x = i
        y = j
        
        a = np.dot(A , [0.1*x,0.1*y])
        
        print (a)
        plt.scatter(a[0],a[1],  facecolor="b", edgecolors='none', alpha=.7, s=10)
        plt.scatter(0.1*x, 0.1* y,  facecolor="r", edgecolors='none', alpha=.7, s=10)
       # plt.scatter(a[0], a[1],  facecolor="r", edgecolors='none', alpha=.7, s=10)

        plt.xlim(0,8)
        plt.ylim(0,8)

#print (a[0])
#print (a[1])
plt.savefig("p10-2.png")
plt.show()

#plt.savefig("p10-2.png")
