import os
import shutil

def find_main_files(dir_path):
    main_files = []
    for current_dir, dirs, files in os.walk(dir_path): # os.walk() рекурсивно обходит все папки
        print(f"\nПроверяем {current_dir}")
        print(f"Подпапки: {dirs}")
        print(f"Файлы: {files}")
        
        for file in files:
            filename, extension = os.path.splitext(file) # разделяем имя файла и расширение
            if filename == "main":
                my_path = os.path.join(current_dir, file)
                main_files.append(my_path)
                print(f"Есть файл {file}")
    
    return main_files

dir = r"D:\git\Promising-programming-languages-1\dz"
main_files = find_main_files(dir)
print(f"\nВсего найдено файлов с именем 'main': {len(main_files)}")

file = "results_dz2"
with open(file, 'w', encoding='utf-8') as f:
    for i in main_files:
        f.write(f"{i}\n")
    print("Результаты сохранены в файл results_dz2")

archive_name = "dz2_task1"
shutil.make_archive(archive_name, 'zip', dir)
print(f"Создан архив: {archive_name}.zip")

