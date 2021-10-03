def check_user_input(input):
    try:
        # Convert it into integer
        val = int(input)
        print("Введенное число N -целое. N = ", val)
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
            print("Введенное число N -с плавающей запятой. N = ", val)
        except ValueError:
            print("Введенные данные не являются числом")


def is_prime(x) -> bool:
    sq = int(x ** 0.5)
    for i in range(2, sq + 1):
        if x % i == 0:
            return False
    return True


while True:
    try:
        N = int(input("Введите целое число N: "))
        check_user_input(N)
        if N < 2:
            print('Вводимое число должно быть больше 2!')
        primes = [x for x in range(2, N) if is_prime(x)]
        print("Простые числа от 2 до N:", *primes)
        exit(0)
    except (TypeError, ValueError) as e:
        print("Упс, что-то пошло не так, попробуйте снова ввести целое число!")
input()