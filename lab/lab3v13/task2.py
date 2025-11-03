def ReplaceDuplicates(lst, repl):
    my_set = set()
    answer = []
    for i in lst:
        if i in my_set:
            answer.append(repl)
        else:
            answer.append(i)
            my_set.add(i)
    return answer
while True:
    try:
        n = int(input("Введите количество элементов списка: "))
        if n > 0:
            lst = []
            for i in range(n):
                element = input(f"Введите элемент {i+1}: ")
                lst.append(element)
            break
        else:
            print("Количество элементов списка должно быть больше 0. Попробуйте снова.")
    except ValueError:
        print("Введите целое число")

print("Исходный список:", lst)
replacement = input("Введите значение для замены дубликатов: ")
new_lst = ReplaceDuplicates(lst, replacement)
print("Список после замены дубликатов:", new_lst)