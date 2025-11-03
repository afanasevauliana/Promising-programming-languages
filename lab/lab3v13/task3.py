def GCD(A, B):
    a, b = abs(A), abs(B)
    if a == b:
        return a
    elif a > b:
        return GCD(a - b, b)
    else:
        return GCD(a, b - a)
    
while True:
    try:
        A = int(input("Введите число A: "))
        B = int(input("Введите число B: "))
        break
    except ValueError:
        print("Введите целое число")

divider = GCD(abs(A), abs(B))
print(f"Наибольший общий делитель чисел {A} и {B} равен: {divider}")