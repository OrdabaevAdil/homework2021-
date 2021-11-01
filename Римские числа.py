s = input('Первое Римское число:')
c=0
a=0

n=0
for i in s:
        c1=c
        if i == 'I': c = 1
        if i == 'V': c = 5
        if i == 'X': c = 10
        if i == 'L': c = 50
        if i == 'C': c = 100
        if i == 'D': c = 500
        if i == 'M': c = 1000
        if c > c1: a = -2 * c1
        n = n + a + c
print(n)

s = input('Второе Римское число:')
h=0
for i in s:
        c1=c
        if i == 'I': c = 1
        if i == 'V': c = 5
        if i == 'X': c = 10
        if i == 'L': c = 50
        if i == 'C': c = 100
        if i == 'D': c = 500
        if i == 'M': c = 1000
        if c > c1: a = -2 * c1
        h = h + a + c
print(h)
D=n/h
print(D)

coding = zip(
  [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1],
  ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
)


def decToRoman(num):
  if num <= 0 or num >= 4000 or int(num) != num:
    raise ValueError('Input should be an integer between 1 and 3999')
  result = []
  for d, r in coding:
    while num >= d:
      result.append(r)
      num -= d
  return ''.join(result)
print(decToRoman(D))