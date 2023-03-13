print("Введите длину первого множества чисел")
n = int(input())
print("Введите длину второ множества чисел")
m = int(input())
list_1 = []
list_2 = []
for i in range(n):
    print("Введите элемент 1 множества")
    num = int(input())
    list_1.append(num)
for i in range(m):
    print("Введите элемент 2 множества")
    num = int(input())
    list_2.append(num)

list_3 = list_1 + list_2
print("Числа, имеющиеся в обоих множествах:")
for i in set(list_3):
    if list_3.count(i) > 1:
        print(i)