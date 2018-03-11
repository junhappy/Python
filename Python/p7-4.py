#p7-4

a = int(input( ))
if(a < 2):
    print('2以上の任意の整数を入力お願いします')
print('約数は ', end = '')
for num in range(1 , a+1):
    if(a % num ==0):
        print( num,', ' ,end = '') 
print('\n')
