#p8-3

import numpy as np
import matplotlib.pyplot as plt
import math
#x = np.arange(0,1,0.01) 
#y = x**2
#plt.plot(x,y)
#plt.show()
pi = math.pi

#x = np.linspace(0 , 2*pi , 100)
#y = np.sin(x)
x = np.linspace(-2*pi , 2*pi , 100)
y = np.cos(x)

plt.plot(x,y)
plt.show()
