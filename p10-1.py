import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as la

A = np.array([ [3,2],
               [5,2] ])
w, v = la.eig(A)
#print('w:固有値',w)
#print('v:固有値ベクトル',v)

#print (A)
#print (v[:,0])
x = np.dot(A , v[:,0])
y = np.dot(A , v[:,1])
print(la.eig(A))
a = 0
b = 0

plt.quiver(a,b,v[0],v[1], angles = 'xy',scale_units = 'xy', scale = 1,color = 'red')
plt.quiver(a,b,y[0],y[1], angles = 'xy',scale_units = 'xy', scale = 1,color = 'blue')
plt.quiver(a,b,x[0],x[1], angles = 'xy',scale_units = 'xy', scale = 1,color = 'blue')

plt.xlim([-4.8,4.8])
plt.ylim([-4.8,4.8])
plt.grid()
#plt.draw()
plt.savefig('p10-1.png')
plt.show()
