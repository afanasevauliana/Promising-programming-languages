import csv

def find_bachelors(filename="students_bachelors.csv"):
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)
        for row in reader:
            if row[3] == 'bachelors':
                print(f"{row[0]} {row[1]}")
    return 0

find_bachelors()