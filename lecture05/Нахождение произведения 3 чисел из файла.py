from random import randint
f = open('task1.txt')
ABC=[]
for line in f:
    ABC.append(int(line))

Summa=0
while Summa!= 2020:
    x=randint(0,199)
    y=randint(0,199)
    z=randint(0,199)
    a=ABC[x]
    b=ABC[y]
    c=ABC[z]
    Summa=a+b+c
    Proizved=a*b*c
    print(Summa)
else:
    print(a)
    print(b)
    print(c)
    print(Proizved)

a=str(a)
b=str(c)
c=str(c)
Summa=str(Summa)
Proizved=str(Proizved)

file = open('output1.txt','w')
lines = ["Первое число равно:",a, "Второе число равно:",b,\
         "Третье число равно:",c,"Сумма чисел равна:",Summa,\
         "Произведение чисел равно:",Proizved]
with open('output1.txt', "w") as file:
    for  line in lines:
        file.write(line + '\n')