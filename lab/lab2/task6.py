with open('fortask6.txt', 'r', encoding='utf-8') as file:
    A = []
    while True:
        line = file.readline()
        if line == '':
            break
        line = line.strip()
        if line:
            A.append(int(line))

arithmetic_mean = sum(A) / len(A)
max_chain = 1
cnt = 1
for i in range(1, len(A)):
    if A[i] == A[i-1]:
        cnt += 1
        if cnt > max_chain:
            max_chain = cnt
    else:
        cnt = 1
print(f"Среднее арифметическое: {arithmetic_mean}")
print(f"Длина самой длинной цепочки: {max_chain}")
with open('output.txt', 'w', encoding='utf-8') as file_output:
    file_output.write(f"Среднее арифметическое: {arithmetic_mean}\n")
    file_output.write(f"Длина самой длинной цепочки одинаковых чисел: {max_chain}")