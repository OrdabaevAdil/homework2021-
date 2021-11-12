from sympy import solveset, symbols, Interval, Min, Max, sqrt, sin, cos, pi
x = symbols('x')
lower_bound = int(input('Введите значение границы области определения функции :'))
upper_bound = int(input('Введите значение границы области определения функции :'))
f = x**2

zeros = solveset(f, x, domain=Interval(lower_bound, upper_bound))
assert zeros.is_FiniteSet
res_min = Min(f.subs(x, lower_bound), f.subs(x, upper_bound), *[f.subs(x, i) for i in zeros])
res_max = Max(f.subs(x, lower_bound), f.subs(x, upper_bound), *[f.subs(x, i) for i in zeros])

print('Экстремум равен=', res_max )
print('Инфимум равен=', res_min )