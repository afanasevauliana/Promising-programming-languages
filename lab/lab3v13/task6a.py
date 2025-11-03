import random
from functools import reduce
a = [random.randint(-100, 100) for x in range(10)]
print("Исходный список:", a)
b = list(filter(lambda x: (x % 2) != 0, a))
b = sorted(b, reverse=True)
print(f"Список из нечетных чисел по убыванию: {b}")
c = reduce(lambda x, y: x * y, b, 1)
print("Произведение нечетных чисел:", c)