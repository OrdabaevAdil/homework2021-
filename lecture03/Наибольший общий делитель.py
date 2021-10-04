print('Данная программа высчитывает НОД-Наибольший общий делитель двух введенных чисел.')
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

while True:
    try:
        A = int(input("Пожалуйста,введите число A: "))
        B = int(input("Пожалуйста,введите число B: "))
        if gcd(A, B):
            print("Наибольший общий делитель чисел A и B:", gcd(A, B))
            break
        else:
            print("Наибольший общий делитель не найден")
    except (TypeError, ValueError) as e:
        print("ОШИБКА!Пожалуйста,введите целые числа!")
input()