from itertools import product
N = int(input('Кол-во бросков:'))
a,b = map(int,input('Поиск суммы кубов от a до b:').split())
M = ["1","2","3","4"] #Кол-во сторон
m = 0 #Число благоприятных событий

res = ["".join(i) for i in product(M, repeat = N)]
for i in range(0,len(res)):
    string = res[i]
    s = 0
    for j in range(0,N):
        s+=int(string[j])
    if s>=a and s<=b:
        m+=1

n=(6**N) #Число всевозможных событий
P=m/n #Общая вероятность
print(P)
