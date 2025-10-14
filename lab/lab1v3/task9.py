symbol = input("Введите один символ: ")
kod = ord(symbol)
dvoichniy = bin(kod)[2:].zfill(8)

# cчитаем позиции единиц СПРАВА НАЛЕВО
pozitsii = []
for i in range(8):
    if dvoichniy[7-i] == '1':
        pozitsii.append(i + 1)

print(f"Символ: {symbol}")
print(f"Двоичный код: {dvoichniy}")
print(f"Единицы в позициях: {pozitsii}")