import random
print("Вывод случайного числа при помощи использования random.random()")
N = input('Введите N=натуральное число - количество повторений')
try:
    n=int(N)
except:
    print('Пожалуйста, введите N=НАТУРАЛЬНОЕ ЧИСЛО!!')
    input()
    exit()
k = 0
while k<n:
    print(random.random())
    k+=1

input()