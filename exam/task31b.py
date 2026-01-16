#Дан csv-файл "students.csv"
# реализуйте функции добавления и удаления записей 
# в файле(там каждая запись типа:имя;возраст;группа)

import csv
def addStudent(name, age, group, filename="students.csv"):
    with open(filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        studentData = [name, age, group]
        writer.writerow(studentData)
    print(f'Студент {name} добавлен')

def removeStudent(name, filename="students.csv"):
    newList = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if row and row[0] != name:
                newList.append(row)
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(newList)


addStudent("Iton", 19, "33b")
removeStudent("Алексей Сидоров")