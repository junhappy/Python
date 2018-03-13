#https://raw.githubusercontent.com/PrinzEugen7/Lesson/master/Python/math/newton_method.py
# 解を求める関数
def f(x):
    return  x**3 - (3/2*x**2) -(3/2*x) + 1 #f(x)
 
# 導関数
def df(x):
    return 0

# ニュートン法
def newton_method(a, eps):
    #for i in range(1000):
    while True :
          # 漸化式
        ah = a - f(a)/df(a)
        # 収束条件(近似解の変化が十分小さい)を満たせば計算終了
        if abs(ah - a) < eps:break
        #　近似解の更新
        a = ah      
    return a
    
    
def main():
    a , i = newton_method(1.0, 0.0001)
    print("解:",a ,"(計算回数:", i+1, ")") # 解: 2.00000... (計算回数: 5 )
    
if __name__ == '__main__':
    main()
