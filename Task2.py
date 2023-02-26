print("Введите число кустов")
N = int(input())
i = int()
sum_1 = N - 1 + 2 * (N - 1) + 3 * (N - 1)
for i in range(N):
    sum_2 = i + 2 * i + 3 * i
    if sum_1 <= sum_2:
        print (sum_2//2)