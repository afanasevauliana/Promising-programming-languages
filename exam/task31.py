# Дан csv-файл "students.csv".
# реализуйте функции добавления и удаления записей в файле
# (там каждая запись типа:имя;возраст;группа)
import csv

def add_student(name, age, group, filename="students.csv"): 
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([name, age, group])
    print(f"Студент {name} добавлен")

def remove_student(name, filename="students.csv"):
    all_students = []
    with open(filename, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')  
        for row in reader:
            if row[0] != name:
                all_students.append(row)

    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(all_students)

add_student("Иван Иванов", 20, "ПИ-101")
add_student("Мария Петрова", 21, "ПИ-102")
remove_student("Анна Смирнова")