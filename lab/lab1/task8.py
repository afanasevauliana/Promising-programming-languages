import re

print("Введите текст: ", end="")
text = input()
words = re.split(r'[ ,.!?;:1234567890\s]+', text)

count = 0
print("\nСлова, содержащие три буквы 'c':")

for word in words:
    lower_word = word.lower()  # приводим к нижнему регистру
    cnt = 0
    for letter in lower_word:
        if (letter == 'с' or letter == 'c'):
            cnt += 1
    if cnt == 3:
        count += 1
        print(f"'{word}' - содержит {cnt} буквы 'с'")

print(f"\nОбщее количество таких слов: {count}")