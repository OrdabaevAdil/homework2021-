from itertools import product
N = int(input('Кол-во бросков:'))
M = int(input('Кол-во сторон на кубике(ДО 30):'))

L = []
o = 0
n = 1
while o < M:
     n=str(n)
     L.append(n)
     n=int(n)
     n += 1
     o += 1


Amin=1*N
print('Amin',Amin)
Amax= M*N
print('Amax',Amax)

res = ["".join(i) for i in product(L, repeat = N)]
def Sum(Amin):
    m = 0  # Число благоприятных событий
    for i in range(0, len(res)):
        string = res[i]
        s = 0
        for j in range(0, N):
            s += int(string[j])
        if Amin <= s <= Amin:
            m += 1

    n = (M ** N)  # Число всевозможных событий
    P = m / n  # Общая вероятность
    print(P * 100, '%')

while Amin<=Amax:
    print('Сумма',Amin,'равна:')
    print(Sum(Amin))
    Amin+=1