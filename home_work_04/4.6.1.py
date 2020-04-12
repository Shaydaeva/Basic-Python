from itertools import count
from itertools import cycle

# итератор, генерирующий целые числа, начиная с указанного
for i in count(105):
    if i > 113:
        break
    print(i)

# итератор, повторяющий элементы некоторого списка, определенного заранее
l = ['spring', 'summer', 'autumn', 'winter']

c = 0
for i in cycle(l):
    if c >= 7:
        break
    print(i)
    c += 1
