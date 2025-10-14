while True:
    try:
        N = int(input("Введите количество элементов массива: "))
        if N > 0:
            break
        else:
            print("Количество элементов должно быть больше 0!")
    except ValueError:
        print("Ошибка! Введите целое число.")

array = []
for i in range(N):
    while True:
        try:
            a = int(input(f"Введите {i+1} элемент: "))
            array.append(a)
            break
        except ValueError:
            print("Ошибка! Введите целое число.")

minim = min(array)
ind = array.index(minim)
print(f"Введенный массив: {array}")
print(f"Минимальный элемент массива: {minim}")
print(f"Индекс минимального элемента: {ind}")