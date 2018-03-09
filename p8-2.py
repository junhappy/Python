import numpy as np

a =np.array([ 3,5,6,2,1 ])
b =np.arange( 1,6 )
print (a)
print (b)
for i in range(5):
    print (a[i] + b[i])
print ('')
for i in range(5):
    print (2  *  a[i])

for i in range(5):
    print ( np.sin(0.5)  *  b[i])




