
import numpy as np
import matplotlib.pyplot as plt

from math import sqrt, sin, cos


# Задаем функцию
def f(x):
    return sin(x)

# Основа метода
def method(x1, x2, h, eps):
    # Проверка на содержание корня
    if f(x1) * f(x2) > 0:
        return None, None
    else:
        # Проверка на содержание корня в одной из заданных точек
        if f(x1) == 0 or f(x2) == 0:
            if f(x1) == 0:
                xk = x1
                intt = 0
                return xk, intt
            if f(x2) == 0:
                xk = x2
                intt = 0
                return xk, intt

        else:
            # Вычисление кол-ва иттераций и поиск корня
            xk = 0
            intt = 0
            while abs(x1 - x2) > eps:
                x3 = x1 + ((3 - sqrt(5)) / 2) * (x2 - x1)
                x4 = x1 + ((sqrt(5) - 1) / 2) * (x2 - x1)
                if abs(f(x3)) > abs(f(x4)):
                    x1 = x3
                else:
                    x2 = x4
                intt += 1
            xk = x3
            return xk, intt


# Функция для построения таблицы
def table(k, x1, x2, xk, intt, Err):
    print('--------------------------------------------------------\
--------------')
    print('|{0:^7}|{1:^8.4f}|{2:^8.4f}|{3:^8.4f}|{4:^11.4e}|{5:^11}\
|{6:^9}|'.format(k, x1, x2, xk, f(xk), intt, Err))


# Основная функция программы
def main():
    # Ввод значений
    a = float(input('Введите начало отрезка: '))
    b = float(input('Введите конец отрезка: '))
    h = float(input('Введите шаг разбиений: '))
    eps = float(input('Введите точность: '))
    mint = int(input('Введите максимальную итерацию: '))
    print('                       Метод золотого сечения')
    print('--------------------------------------------------------\
--------------')
    print('|   №   |   x1   |   x2   |   xk   |   f(xk)   |\
   itter   |   Err   |')
    # Задаем начальные значения x1 и x2 и списки для построения графика
    x1 = a
    x2 = a + h
    xmas = []
    fmas = []
    k = 1
    # Ставим флаг для того, чтобы убрать ошибку при выводе наложения корней
    flag = 0
    # Ставим флаг для проверки наличия корней
    flag1 = 0
    while x2 <= b:
        if f(x2) == 0:
            flag = 1
        Err = 0
        xk, intt = method(x1, x2, h, eps)
        if xk != None:
            # вывод ошибки
            if intt >= mint:
                Err = 1
            # добавление корней в список и таблицу и проверка на наличие корней
            if not (f(x1) == 0 and flag == 1):
                table(k, x1, x2, xk, intt, Err)
                k += 1
                xmas.append(xk)
                fmas.append(f(xk))
                flag1 = 1
        x1 = x2
        x2 = x1 + h
        if x2 > b and x1 != b:
            x2 = b
    if flag1 == 0:
        print('|                            НЕТ КОРНЕЙ           \
                   |')
    print('------------------------------------------------------\
----------------')
    print('Тип ошибок: ')
    print('0 - ошибок нет ')
    print('1 - превышено число итераций ')
    print('Нажмите enter, чтобы построить график')
    input()
    makeGraph(a, b, xmas, fmas)


# Постройка графика
def makeGraph(a, b, xMas, fMas):
    ls = np.linspace(a, b, num=round(b - a) * 100)
    plt.plot(ls, fLinespace(ls), xMas, fMas, 'ro')
    plt.grid(True)
    plt.show()


def fLinespace(ln):
    mas = []
    for i in ln:
        mas.append(f(i))
    return mas


main()