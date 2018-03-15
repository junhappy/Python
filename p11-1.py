import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as la
n = 1
x = 3 #初期値x0
while True:
    x2 = x - (x**3 - (3/2*x*x) -(3/2*x) + 1)  /( 3*x*x-(3*x)-(3/2))   
    # a = x**3 - (3/2*x**2) -(3/2*x) + 1 #f(x)
    # 計算後の値が誤差の範囲内になったら計算終了
    if abs(x2 - x) < 0.0001:
        break
    # 計算後の値をxとして計算を繰り返す
    x = x2
    n += 1

# 計算結果の表示
print('解:',x)
print('計算回数:',n)
