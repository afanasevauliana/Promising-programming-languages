with open('test_surnames.txt', 'r', encoding='utf-8') as file:
    surnames = []
    for l in file:
        if l[0] in "БВГДЖЗЙКЛМНПРСТФХЦЧШЩ":
            surnames.append(l)
    surnames.sort(reverse=True)

with open("outputtask2.txt", "w", encoding='utf-8') as file:
    file.write(''.join(surnames))