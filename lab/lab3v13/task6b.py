a = 'qwerty'
b = 'asdfgh'
c = 'zxcvbn'
words = list(map(lambda x: ''.join(x), zip(a, b, c)))
print("Строка 1:", a)
print("Строка 2:", b) 
print("Строка 3:", c)
print("Список слов:", words)
