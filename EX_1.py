def bubble_sort(alist):
    for i in range(len(alist) - 1, 0, -1):
        no_swap = True
        for j in range(0, i):
            if alist[j + 1] < alist[j]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
                no_swap = False
        if no_swap:
            return

import random

print("Вывод случайного числа при помощи использования random.random()")
N = input('Введите N=натуральное число - количество повторений')
try:
    n=int(N)
except:
    print('Пожалуйста, введите N=НАТУРАЛЬНОЕ ЧИСЛО!!')
    input()
    exit()
k = 1
a = random.random()
b = a
while k<n:
    a = random.random()
    b = zip (a, b)
    k+=1
print(b)

input()

