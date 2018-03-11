import numpy as np
import numpy.linalg as la
#from numpy.linalg import inv


a = np.array([ [1,2],[3,4] ])
b = np.array([ [1,2],[3,4] ])

print(la.det(a))
print(la.inv(a))

#print (a)
#print (inv(a))
#ainv = inv(a)
#np.dot(a, ainv) 
