f = open('task1.txt','r')
a = f.readlines()
def proizv(a):
  for el1 in a:
    for el2 in a:
      if int(el1)+int(el2)<2020:
        for el3 in a:
          if int(el1)+int(el2)+int(el3)==2020:
            print(el1, el2, el3)
            return (int(el1)*int(el2)*int(el3))
b=proizv(a)
print(b)
b=str(b)
k = open('output1.txt', 'w')
k.write(b)