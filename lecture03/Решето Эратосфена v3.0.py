print("Здравствуйте. Данная программа высчитывает все простые числа методом Решета Эратосфена "
      "от 2 до N.Где N= вводимый вами крайний член числовой последовательности, до которой будут вычисляться все простые числа")
N = input("Пожалуйста, введите натуральное число N=")

try:
    n = int(N)
except:
    print('ОШИБКА!!Неверно введенные данные!Пожалуйста введите натуральное число!')
    input()
    exit()
P = int(N)

if P >= 2:
    pass
else:
    print('Введенные данные меньше 2, и не находятся в области вычислений!')
    input()
    exit()

numbers = []
flags = []
i = 2
while i <= P:
    numbers.append(i)
    flags.append(False)
    i += 1

idx = 0

while idx < P // 2:
    n = numbers[idx]
    i = idx + n
    while i < len(numbers):
        flags[i] = True
        i += n

    idx += 1
    while idx < len(flags) and flags[idx]:
        idx += 1
n = numbers[0]
i = 0

print("Простые числа от 2 до N=")
while i < len(numbers):
    if flags[i]:
        i += 1
        continue
    print(numbers[i])
    i += 1

input()
exit()