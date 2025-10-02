while True:
    try:
        N = int(input("Введите количество элементов массива: "))
        if N > 0:
            break
        else:
            print("Нужно ввести значение больше 0")
    except ValueError:
        print("Ошибка! Введите целое число.")
array1 = []
array2 = []
array3 = []
for i in range(N):
    while True:
        try:
            element = int(input(f"Введите {i+1} элемент: "))
            array1.append(element)
            break
        except ValueError:
            print("Ошибка! Введите целое число.")
for num in array1:
    if num > 0:
        array2.append(num)
    else:
        array3.append(num)
print(f"Исходный массив: {array1}")
print(f"Массив положительных элементов: {array2}")
print(f"Массив остальных элементов: {array3}")