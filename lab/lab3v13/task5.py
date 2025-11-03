list1 = [6, 5, 3, 9]
list2 = [0, 1, 7, 7]
answer = list(map(lambda x, y: (x + y, x * y), list1, list2))
print("Первый список:", list1)
print("Второй список:", list2)
print("Результат:", answer)