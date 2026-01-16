import csv

with open('cities.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    for row in reader:
        if row[2] == 'нет' and row[3] == 'общегражданский':
            print(row)