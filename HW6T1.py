n = int(input('Input n ')) #общее кол-во эл-в
x = int(input('Input a[0] '))
d = int(input('Input d ')) #шаг
print(*range(x, x + d * n, d))