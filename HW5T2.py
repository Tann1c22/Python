def summa(a, b):
    a += 1
    b -= 1
    if b > 0:
        return summa(a, b)
    else:
        return a
 
print("Введите первое число: ") 
a = int(input())
print("Введите второе число: ")
b = int(input())
print (summa(a, b))