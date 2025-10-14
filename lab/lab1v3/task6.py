import random

def check_value_input():
    while True:
        try:
            value = int(input())
            if value <= 0:
                print("Ошибка. Попробуйте снова. Нужно ввести ПОЛОЖИТЕЛЬНОЕ число.")
                continue
            return value
        except ValueError:
            print("Ошибка. Попробуйте снова. Нужно ввести целое число.")

print("Введите количество строк: ", end="")
N = check_value_input()
print("Введите количество столбцов: ", end="")
M = check_value_input()

B = []
for i in range(M):
    row = []
    for j in range(N):
        row.append(random.randint(-5, 7))
    B.append(row)

print("\nИсходная матрица B:")
for row in B:
    for a in row:
        print(f"{a:6}", end=" ")
    print()

max_value = B[0][0]
max_i, max_j = 0, 0

for i in range(M):
    for j in range(N):
        if B[i][j] > max_value:
            max_value = B[i][j]
            max_i, max_j = i, j

if max_i != M - 1:
    B[max_i], B[M - 1] = B[M - 1], B[max_i]

if max_j != N - 1:
    for i in range(M):
        B[i][max_j], B[i][N - 1] = B[i][N - 1], B[i][max_j]

print("\nПреобразованная матрица B:")
for row in B:
    for a in row:
        print(f"{a:6}", end=" ")
    print()