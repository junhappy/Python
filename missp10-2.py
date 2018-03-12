import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as la

A = np.array([ [3,2],
               [5,2] ])
w, v = la.eig(A)
#print('w:固有値',w)                                                                                                    #print('v:固有値ベクトル',v)                                                                                            
#print (A[1])                                                                                                              
#print (v[:,0])                                                                                                         
#x = np.dot(A , v[:,0])
#y = np.dot(A , v[:,1])
#print(la.eig(A))
a = 0
b = 0
x  = np.array([])
y  = np.array([])
c = (3,4)
#print (A[0])
A = np.append(A,c)
#print ([A[0] ,A[1]])
#plt.plot(A[4],A[5],'ro')
#plt.show()
K = np.array([])

for i in range(10):
    for j in range(10):
        plt.plot([0.1*i], [0.1*j], "r.",markersize= 0.8)       

#for p in np.arange(0,102,1):
   # print (p)
    #plt.plot( (K[0+p:2+p] )   #スライス
    #plt.plot([K) 
#print (A[2:4])
#for i in range(11):
    #for j in range(11):
        #y = np.array( [0.1*i],[ 0.1*j]) 
        #x = np.append(x,y)
        #plt.plot([0.1*i], [0.1*j], 'ro')
        #plt.show()
        #print (x)
#plt.plot(5, 5, "ro") 
#plt.quiver(a,b,v[0],v[1], angles = 'xy',scale_units = 'xy', scale = 1,color = 'red')
#plt.quiver(a,b,y[0],y[1], angles = 'xy',scale_units = 'xy', scale = 1,color = 'blue')
#plt.quiver(a,b,x[0],x[1], angles = 'xy',scale_units = 'xy', scale = 1,color = 'blue')
plt.xlim([0,8])
plt.ylim([0,8])
#plt.grid()
#plt.draw()                                                                                                             
#plt.savefig('p10-1.png')
plt.show()
