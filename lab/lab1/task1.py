m = []
for i in range(12):
    row = []
    for j in range(12):
        if j < i:
            row.append(0)
        else:
            row.append(j-i+1)
    m.append(row)
for row in m:
    print(' '.join(f'{num:2d}' for num in row))