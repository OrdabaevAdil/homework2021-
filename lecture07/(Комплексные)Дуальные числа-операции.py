class Operation:

    def plus(self, x, y):
        print(x + y)

    def minus(self, x, y):
        print(x - y)

    def umnoj(self, x, y):
        print(x * y)

    def delenie(self, x, y):
        print(x / y)

    def modul(self, x, y):
        print(abs(7 + 8j))

    def stepen(self, x, y):
        print(pow(x + y, 2))


obj1 = Operation()
x = complex(5, 6)
y = complex(7, 8)
obj1.plus(x, y)
obj1.minus(x, y)
obj1.umnoj(x, y)
obj1.modul(x, y)
obj1.delenie(x, y)
obj1.stepen(x, y)

# возможные исход
class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


z_1 = ComplexNumber(1, -2)
z_2 = ComplexNumber(3, 4)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)