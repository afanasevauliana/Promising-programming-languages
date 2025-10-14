import random

def check_max_value_input(max_value=10):
    while True:
        try:
            value = int(input())
            if value <= 0:
                print("Ошибка. Попробуйте снова. Нужно ввести ПОЛОЖИТЕЛЬНОЕ число <= 10.")
                continue
            if value > max_value:
                print("Ошибка. Попробуйте снова. Нужно ввести число <= 10.")
                continue
            return value
        except ValueError:
            print("Ошибка. Попробуйте снова. Нужно ввести целое число.")

def is_symmetric(row):
    n = len(row)
    for i in range(n // 2):
        if row[i] != row[n - 1 - i]:
            return 0
    return 1

print("Введите количество строк N (N <= 10): ", end="")
N = check_max_value_input()
print("Введите количество столбцов M (M <= 10): ", end="")
M = check_max_value_input()

A = []
for i in range(N):
    row = []
    for j in range(M):
        row.append(random.randint(1, 2))
    A.append(row)

B = []
for i in range(N):
    B.append(is_symmetric(A[i]))

print("\nМатрица A:")
for i in range(N):
    print(A[i])

print("\nМассив B (1 - если строка симметрична, 0 - если не симметрична):")
print(B)
