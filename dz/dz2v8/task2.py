import xml.etree.ElementTree as ET
import os

def create_xml_file():
    root = ET.Element("videocards")
    tree = ET.ElementTree(root)
    tree.write("videocards.xml", encoding='utf-8', xml_declaration=True)
    print("Создан XML файл: videocards.xml")
if not os.path.exists("videocards.xml"):
    create_xml_file()

def print_menu():
    print("\nВыберите пункт меню:")
    print("1 - Удалить видеокарту (по названию)")
    print("2 - Добавить видеокарту")
    print("3 - Изменить видеокарту")
    print("4 - Получить информацию (по названию)")
    print("5 - Отсортировать видеокарты")
    print("6 - Сохранить в файл и вывести видеокарты с объемом > заданного")
    print("7 - Показать все видеокарты")
    print("0 - Выход")

def input_check(prompt):
    while True:
        user_input = input(prompt)
        
        if not user_input:
            print("Ошибка: поле не может быть пустым.")
            continue
            
        try:
            number = int(user_input)
            if number <= 0:
                print("Ошибка: число должно быть положительным.")
                continue
            return str(number)  # возвращаем как строку для совместимости с XML
        except ValueError:
            print("Ошибка: введите целое число.")

def add_videocard():
    name = input("Введите название видеокарты: ")
    if not name:
        print("Ошибка: название не может быть пустым.")
        return
    memory_size = input_check("Введите объем видеопамяти (ГБ): ")
    memory_type = input("Введите тип видеопамяти (GDDR5/GDDR6/GDDR6X): ")
    gpu_frequency = input_check("Введите частоту графического процессора (МГц): ")
    memory_frequency = input_check("Введите частоту памяти (МГц): ")
    bus_width = input_check("Введите ширину шины (бит): ")

    tree = ET.parse("videocards.xml")
    root = tree.getroot()
    videocard = ET.SubElement(root, "videocard")

    ET.SubElement(videocard, "name").text = name
    ET.SubElement(videocard, "memory_size").text = memory_size
    ET.SubElement(videocard, "memory_type").text = memory_type
    ET.SubElement(videocard, "gpu_frequency").text = gpu_frequency
    ET.SubElement(videocard, "memory_frequency").text = memory_frequency
    ET.SubElement(videocard, "bus_width").text = bus_width

    tree.write("videocards.xml", encoding='utf-8', xml_declaration=True)
    print(f"Видеокарта '{name}' успешно добавлена!")

def print_videocards():
    tree = ET.parse("videocards.xml")
    root = tree.getroot()
    videocards = root.findall("videocard")
    if not videocards:
        print("Видеокарт не найдено!")
        return

    for i, videocard in enumerate(videocards, 1):
        print(f"\nВидеокарта {i}:")
        print(f"Название: {videocard.find('name').text}")
        print(f"Объем видеопамяти: {videocard.find('memory_size').text} ГБ")
        print(f"Тип видеопамяти: {videocard.find('memory_type').text}")
        print(f"Частота ГП: {videocard.find('gpu_frequency').text} МГц")
        print(f"Частота памяти: {videocard.find('memory_frequency').text} МГц")
        print(f"Ширина шины: {videocard.find('bus_width').text} бит")

def delete_videocard():
    name = input("Введите название видеокарты для удаления: ")
    tree = ET.parse("videocards.xml")
    root = tree.getroot()
    found = False
    for videocard in root.findall("videocard"):
        if videocard.find("name").text.lower() == name.lower():
            root.remove(videocard)
            found = True
            break
    if found:
        tree.write("videocards.xml", encoding='utf-8', xml_declaration=True)
        print(f"Видеокарта '{name}' успешно удалена!")
    else:
        print(f"Видеокарта '{name}' не найдена!")

def edit_videocard():
    name = input("Введите название видеокарты для изменения: ")
    tree = ET.parse("videocards.xml")
    root = tree.getroot()
    found = False
    for videocard in root.findall("videocard"):
        if videocard.find("name").text.lower() == name.lower():
            found = True
            print("\nТекущие данные видеокарты:")
            print(f"1. Название: {videocard.find('name').text}")
            print(f"2. Объем видеопамяти: {videocard.find('memory_size').text} ГБ")
            print(f"3. Тип видеопамяти: {videocard.find('memory_type').text}")
            print(f"4. Частота ГП: {videocard.find('gpu_frequency').text} МГц")
            print(f"5. Частота памяти: {videocard.find('memory_frequency').text} МГц")
            print(f"6. Ширина шины: {videocard.find('bus_width').text} бит")
            
            print("\nВведите новые данные:")
            new_name = input(f"Новое название [{videocard.find('name').text}]: ") or videocard.find('name').text
            new_memory_size = input_check(f"Объем видеопамяти (ГБ) [{videocard.find('memory_size').text}]: ")
            new_memory_type = input(f"Тип видеопамяти [{videocard.find('memory_type').text}]: ") or videocard.find('memory_type').text
            new_gpu_frequency = input_check(f"Частота ГП (МГц) [{videocard.find('gpu_frequency').text}]: ")
            new_memory_frequency = input_check(f"Частота памяти (МГц) [{videocard.find('memory_frequency').text}]: ")
            new_bus_width = input_check(f"Ширина шины (бит) [{videocard.find('bus_width').text}]: ")

            videocard.find('name').text = new_name
            videocard.find('memory_size').text = new_memory_size
            videocard.find('memory_type').text = new_memory_type
            videocard.find('gpu_frequency').text = new_gpu_frequency
            videocard.find('memory_frequency').text = new_memory_frequency
            videocard.find('bus_width').text = new_bus_width

            tree.write("videocards.xml", encoding='utf-8', xml_declaration=True)
            print(f"Видеокарта успешно обновлена!")
            break
    
    if not found:
        print(f"Видеокарта '{name}' не найдена!")

def get_videocard_info():
    name = input("Введите название видеокарты: ")
    tree = ET.parse("videocards.xml")
    root = tree.getroot()

    found = False
    for videocard in root.findall("videocard"):
        if videocard.find("name").text.lower() == name.lower():
            found = True
            print(f"\nНайдена видеокарта: {videocard.find('name').text}")
            print(f"Название: {videocard.find('name').text}")
            print(f"Объем видеопамяти: {videocard.find('memory_size').text} ГБ")
            print(f"Тип видеопамяти: {videocard.find('memory_type').text}")
            print(f"Частота ГП: {videocard.find('gpu_frequency').text} МГц")
            print(f"Частота памяти: {videocard.find('memory_frequency').text} МГц")
            print(f"Ширина шины: {videocard.find('bus_width').text} бит")
            break
     
    if not found:
        print(f"Видеокарта '{name}' не найдена!")

def sort_videocards():
    print("\nВыберите критерий сортировки:")
    print("1 - По названию")
    print("2 - По объему видеопамяти")
    print("3 - По частоте графического процессора")
    print("4 - По типу видеопамяти")
    item = input()
    tree = ET.parse("videocards.xml")
    root = tree.getroot()
    videocards = root.findall("videocard")
    if not videocards:
        print("Нет видеокарт для сортировки!")
        return
    
    if item == "1":
        videocards.sort(key=lambda x: x.find('name').text.lower())
        print("Отсортировано по названию (А-Я)")
    elif item == "2":
        videocards.sort(key=lambda x: int(x.find('memory_size').text))
        print("Отсортировано по объему видеопамяти (по возрастанию)")
    elif item == "3":
        videocards.sort(key=lambda x: int(x.find('gpu_frequency').text))
        print("Отсортировано по частоте ГП (по возрастанию)")
    elif item == "4":
        videocards.sort(key=lambda x: x.find('memory_type').text.lower())
        print("Отсортировано по типу видеопамяти")
    else:
        print("Неверный выбор!")
        return

    for videocard in root.findall("videocard"):
        root.remove(videocard)
    for videocard in videocards:
        root.append(videocard)
    
    tree.write("videocards.xml", encoding='utf-8', xml_declaration=True)
    
    print("\nОтсортированный список:")
    for i, videocard in enumerate(videocards, 1):
        print(f"\nВидеокарта #{i}")
        print(f"Название: {videocard.find('name').text}")
        print(f"Объем видеопамяти: {videocard.find('memory_size').text} ГБ")
        print(f"Тип видеопамяти: {videocard.find('memory_type').text}")
        print(f"Частота ГП: {videocard.find('gpu_frequency').text} МГц")

def filter_by_memory():
    print("\nФильтрация по объему памяти")
    try:
        min_memory = int(input("Введите минимальный объем видеопамяти (ГБ): "))
    except ValueError:
        print("Ошибка: введите число!")
        return
    
    tree = ET.parse("videocards.xml")
    root = tree.getroot()
    
    filtered_cards = []
    for videocard in root.findall("videocard"):
        memory_size = int(videocard.find('memory_size').text)
        if memory_size > min_memory:
            filtered_cards.append(videocard)
    
    if not filtered_cards:
        print(f"Видеокарт с объемом памяти больше {min_memory} ГБ не найдено!")
        return
    
    print(f"\nВидеокарты с памятью > {min_memory} ГБ")
    for i, videocard in enumerate(filtered_cards, 1):
        print(f"\nВидеокарта #{i}")
        print(f"Название: {videocard.find('name').text}")
        print(f"Объем видеопамяти: {videocard.find('memory_size').text} ГБ")
        print(f"Тип видеопамяти: {videocard.find('memory_type').text}")
        print(f"Частота ГП: {videocard.find('gpu_frequency').text} МГц")
        print(f"Частота памяти: {videocard.find('memory_frequency').text} МГц")
        print(f"Ширина шины: {videocard.find('bus_width').text} бит")
    
    output_file = f"videocards_above_{min_memory}GB.xml"
    new_root = ET.Element("videocards")
    for card in filtered_cards:
        new_root.append(card)
    
    new_tree = ET.ElementTree(new_root)
    new_tree.write(output_file, encoding='utf-8', xml_declaration=True)
    print(f"\nРезультаты сохранены в файл: {output_file}")

def main():
    while True:
        print_menu()
        menu_item = input()
        if menu_item == "1":
            delete_videocard()
        elif menu_item == "2":
            add_videocard()
        elif menu_item == "3":
            edit_videocard()
        elif menu_item == "4":
            get_videocard_info()
        elif menu_item == "5":
            sort_videocards()
        elif menu_item == "6":
            filter_by_memory()
        elif menu_item == "7":
            print_videocards()
        elif menu_item == "0":
            print("Программа завершена")
            break
        else:
            print("Неправильная команда. Попробуйте снова.")

if __name__ == "__main__":
    main()