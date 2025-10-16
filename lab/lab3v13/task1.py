def IsLeapYear(y):
    return (y % 4 == 0) and (y % 100 != 0 or y % 400 == 0)

while True:
    try:
        Y = int(input("Введите год для проверки: "))
        if Y > 0:
            if IsLeapYear(Y):
                print(f"{Y} - високосный год")
            else:
                print(f"{Y} - не високосный год")
            break
        else:
            print("Год должен быть положительным числом. Попробуйте снова:")
    except ValueError:
        print("Введите целое число")