import math
P = int(input("Введите произведение чисел"))
S = int(input("Введите сумму чисел"))
x = int()
y = int()
D = S**2 - 4*P
print(D)
if D > 0:
    x1 = (-1 * S - math.sqrt(D))/2
    x = (-1 * S + math.sqrt(D))/2
    print(x, x1)
elif D == 0:
    x = -1 * S / 2
elif D <= 0:
    print("Таких чисел нет, Петя соврал!")
if D > 0:
    print ("Первое число равно", x1 * -1, "  Второе число равно", x * -1)
elif D == 0:
    print ("Оба числа равны", x * -1)