import numpy as np
import numpy.linalg as la
#from numpy.linalg import inv   

A = np.array([ [1,2,3],
               [4,5,6],
               [7,8,9]])
#b = np.array ( [7,8,5]  )
#x = la.solve(A,b)
#print(x)
b = np.array([7, 6, 8])
x = la.solve(A, b)
print(x)
