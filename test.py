import math

x = 5

A = x-  ( ((1/math.e**x/2) - 1/math.e**x )/(-1/math.e**x/2 + x*(-1/2)*1/math.e**x/2) )


a =((1/math.e**x/2) - 1/math.e**x ) 
b = (-1/math.e**x/2 + x*(-1/2)*1/math.e**x/2)
c = a/b
d = x - c 
#x2 = x - ( x * (1/math.e**x/2) - 1/math.e**x ) / (-1/math.e**x/2 + x*(-1/2)*1/math.e**x/2)
print(A)
