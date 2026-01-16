data = {"Иван": 1923, "Мария": 1995, "Алексей": 1987}
with open("outputtask14.txt", "w", encoding='utf-8') as file:
    for name, year in data.items():
        revName = name[::-1]
        revYear = str(year)[::-1]
        file.write(f"{revYear} {revName}\n")