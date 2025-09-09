import array

size = 12
mas = [[0 for i in range(size)] for j in range(size)]
for i in range(size):
    for j in range(size):
        if j >= i:
            mas[i][j] = j - i + 1
        else:
            mas[i][j] = 0
for row in mas:
    for a in row:
        print(a, " ", end="")
    print()