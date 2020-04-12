from itertools import cycle
from itertools import zip_longest


# Принимает в себя список и количество повторений
def func(a, b):
    l = []
    for i in cycle(a):
        if b <= 0:
            break
        l.append(i)
        b -= 1
    return l


l = ['spring', 'summer', 'autumn', 'winter']
n = range(100, 107)

word = func(l, 7)
num = func(n, 10)

print(word)
print(num)

for i in zip_longest(func(l, 7), func(n, 10), fillvalue=''):
    print(i)
