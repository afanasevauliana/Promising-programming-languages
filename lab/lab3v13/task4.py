while True:
    try:
        input_str = input("Введите числа через пробел: ")
        mus = list(map(int, input_str.split()))
        break
    except ValueError:
        print("Ошибка ввода.")
print("Исходный массив:", mus)
sorted_mus = sorted(mus, key=lambda x: (x < 0, x))
print("Массив после сортировки:", sorted_mus)