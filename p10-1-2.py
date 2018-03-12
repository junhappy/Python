import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as la


a = [0,-1] #X
b = [0,1]  #Y

plt.quiver(a,b,[1,1],[1,1], angles = 'xy',scale_units = 'xy', scale = 1,color = 'red')

plt.xlim([-3,3])
plt.ylim([-3,3])
plt.grid()

                                                                                                              
plt.savefig('p10-1-2.png')
plt.show()










