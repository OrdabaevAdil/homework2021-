from random import randint,shuffle

def create_array(size=10,max=100):
    return [randint(0,max) for _ in range(size)]

def is_sorted(a):
    n = len(a)
    for i in range(0, n-1):
        if (a[i] > a[i+1] ):
            return False
    return True

def bogo_sort(a):
    ct=0
    while not is_sorted(a):
        shuffle(a)
        ct+=1
    return ct,a

print('Данная программа перетасовывает введенные вами случайные числа методом BogoSort')
print('Осторожно! При обработке чисел от 5 и больше, из-за большого кол-ва операций, программа может зависнуть!')
N = input('Пожалуйста, введите количество случайных чисел:')
try:
    n=int(N)
except:
    print('Вам нужно ввести натуральное число!')
    input()
    exit()


a = create_array(n,100)
print("Cписок случайных чисел:",a)
ct,s = bogo_sort(a)
print("Перетасованный список:",s)
print("Количество задействованных операций: %d"%ct)
input()