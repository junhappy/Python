import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as la

A = np.array([ [3,2],
               [5,2] ])
w, v = la.eig(A)
print('w:固有値',w)
print('v:固有値ベクトル',v)

a = np.dot(A,v) #行列Aと固有値ベクトルv

#plt.quiver([0,0,v[:,0,v[:,1]], angles = 'xy', scale='xy', scale=1)
#plt.quiver([0,0,2,1], angles = 'xy', scale_units='xy', scale=1)
#plt.draw()
#plt.show()
