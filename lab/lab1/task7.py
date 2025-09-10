import re

print("Введите текст: ", end="")
text = input()
words = re.split(r'[ ,.!?;:1234567890\s]+', text)

count = 0
print("\nСлова, которые начинаются и заканчиваются на одинаковую букву:")
for word in words:
    lower_word = word.lower() #приводим к нижнему регистру для сравнения
    if lower_word[0] == lower_word[-1]:
        count += 1
        print(f"  '{word}' - начинается и заканчивается на '{word[0]}'")

print(f"\nОбщее количество таких слов: {count}")