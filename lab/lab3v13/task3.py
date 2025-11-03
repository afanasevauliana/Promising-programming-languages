def GCD(A, B):
    if B == 0:
        return A
    else:
        return GCD(B, A % B)
    
while True:
    try:
        A = int(input("Введите число A: "))
        B = int(input("Введите число B: "))
        break
    except ValueError:
        print("Введите целое число")

divider = GCD(abs(A), abs(B))
print(f"Наибольший общий делитель чисел {A} и {B} равен: {divider}")