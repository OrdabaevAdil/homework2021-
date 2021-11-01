from itertools import product
N = int(input('Кол-во бросков:'))
M = int(input('Кол-во сторон на кубике(ДО 30):'))

K = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16",\
     "17","18","19","20","21","22","23","24","25","26","27","28","29","30"]
L = K[0:M]
l=len(L)
Amin=1*N
print('Amin',Amin)
Amax=l*N
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

    n = (l ** N)  # Число всевозможных событий
    P = m / n  # Общая вероятность
    print(P * 100, '%')

while Amin<=Amax:
    print('Сумма',Amin,'равна:')
    print(Sum(Amin))
    Amin+=1