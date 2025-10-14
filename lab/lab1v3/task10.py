import math

while True:
    try:
        N = int(input("Введите натуральное число N: "))
        if N <= 0:
            print("Вы ввели ненатуральное число. Попробуйте снова.")
            continue
        break
    except ValueError:
        print("Вы ввели не число. Попробуйте снова.")
S = 0
for k in range(1, N + 1):
    S += ((-1) ** k) * (math.factorial(2*k + 1))

print(f"S = {S}")