while True:
    try:
        input_str = input("Введите числа через пробел: ")
        mus = list(map(int, input_str.split()))
        break
    except ValueError:
        print("Введите целые числа через пробел.")
print("Исходный массив:", mus)
sorted_mus = sorted(mus, key=lambda x: (x < 0, x))
print("Отсортированный массив:", sorted_mus)