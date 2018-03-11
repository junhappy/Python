import numpy as np
import numpy.linalg as la
#from numpy.linalg import inv                                                                                       


a = np.array([ [1,2],[3,4] ])
b = np.array([ [5,6],[7,8] ])

for i in np.arange(1,2):
   # print (a[i-1 , :  ])
    c = (a[i-1 , :  ])
#print(c)
print(np.dot(c,b) )
print('')
print(np.dot(b,c) )
