from random import randint
 
lo, hi = 3, 8       ##Задаем диапазон
arr = [randint(1, 10) for _ in range(20)]
print("Массив:", arr)
index = [i for i, v in enumerate(arr) if lo <= v <= hi]
print("Индексы:", index)