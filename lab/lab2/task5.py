text = input("Введите текст: ")
words = text.split()
dictionary = {}
A = []
for word in words:
    if word in dictionary:
        A.append(dictionary[word])
        dictionary[word] += 1
    else:
        A.append(0)
        dictionary[word] = 1
print("Результат:")
for i, count in enumerate(A):
    print(f"'{words[i]}' - {count}")