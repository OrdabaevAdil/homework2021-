from random import randint

f = open('task1.txt')

def Summa(f): #Задаю функцию
    for line in f:
        x=randint(1,200) #Беру случайные числа,которые будут соответствовать номеру строки в файле
        y=randint(1,200)
        z=randint(1,200)
        a=line(x)
        b=line(y)
        c=line(z)
        S=a+b+c #Сумма трех аргументов
        D=a*b*c #Произведение трех аргументов

S=0
while S!=2020: #До тех пор, пока сумма не станет равной 2020, после будет вычисленно произведение
    Summa(f)
else:
    print(D)