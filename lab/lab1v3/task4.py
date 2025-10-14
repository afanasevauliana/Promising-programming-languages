print("A B C Результат")
for A in range(2):
    for B in range(2):
        for C in range(2):
            s = (not ((A or B) != C)) or A
            print(A, B, C, "\t", int(s))