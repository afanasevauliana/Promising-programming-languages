class Pond:
    def __init__(self, name, size):
        self.name = name
        self.size = size
    def get_info(self):
        return f"Водоём: {self.name}, Размер: {self.size} км²"

class Sea(Pond):
    min_size = 1000
    def __init__(self, name, size):
        super().__init__(name, size)
        if size < self.min_size:
            self.size = self.min_size
    def get_info(self):
        return f"Тип: Море, {super().get_info()}"

class Lake(Pond):
    def get_info(self):
        return f"Тип: Озеро, {super().get_info()}"

if __name__ == "__main__":
    name = input("Введите название водоёма: ")
    size = float(input("Введите размер водоёма (км²): "))
    pond_type = input("Введите тип водоёма (море/озеро): ")
    if pond_type.lower() == "море":
        pond = Sea(name, size)
    elif pond_type.lower() == "озеро":
        pond = Lake(name, size)
    else:
        print("Ошибка: допустимые типы водоёмов - 'море' или 'озеро'")
        exit()
    print(pond.get_info())