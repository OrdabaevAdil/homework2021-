from random import randint
f = open('test.txt')
ABC=[]
for line in f:
    ABC.append(line)

Summa=0
while Summa!= 2020:
    x=randint(0,5)
    y=randint(0,5)
    z=randint(0,5)
    a=ABC[x]
    b=ABC[y]
    c=ABC[z]
    Summa=a+b+c
    print(Summa)

else:
    print(Summa)
    exit