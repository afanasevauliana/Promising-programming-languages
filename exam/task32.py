import csv

with open('students_bachelors.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)
    for row in reader:
        if int(row[2]) < 22:
            print(row)
