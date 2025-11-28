import threading
import time
import numpy as np

class MyThread(threading.Thread):
    def __init__(self, thread_id, A, B, C, lock, completed_threads):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.A = A
        self.B = B
        self.C = C
        self.summ = 0
        self.lock = lock
        self.completed_threads = completed_threads  # для отслеживания завершения

    def find_next(self):
        with self.lock:
            for i in range(self.C.shape[0]):      # все строки
                for j in range(self.C.shape[1]):  # все столбцы (cij+1 если j<k)
                    if self.C[i, j] is None:
                        self.C[i, j] = "calculating"
                        return i, j
            return -1, -1
    
    def run(self):
        print(f"Поток {self.thread_id} начал работу")
        
        while True:
            i, j = self.find_next()
            if i == -1:
                break  # работа закончилась
                
            print(f"Поток {self.thread_id} вычисляет С[{i}][{j}]")
            # A.shape[0] = 5 (количество строк)
            # A.shape[1] = 4 (количество столбцов)
            self.summ = 0
            for k in range(self.A.shape[1]):
                self.summ += self.A[i, k] * self.B[k, j]
            time.sleep(0.1)
            
            # Записываем результат
            with self.lock:
                self.C[i, j] = self.summ
                print(f"Поток {self.thread_id} завершил: C[{i}][{j}] = {self.summ}")
        
        # Сообщение о полном завершении работы потока
        with self.lock:
            self.completed_threads.append(self.thread_id)
            print(f"Поток {self.thread_id}: завершил работу (сообщение о завершении)")

def save_to_file(matrix, filename="protocol.txt"):
    """Записывает результат в файл в отдельном потоке"""
    def save_worker():
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"\nРезультат умножения матриц (записано {time.strftime('%Y-%m-%d %H:%M:%S')}):\n")
            for i in range(matrix.shape[0]):
                row = " ".join(f"{matrix[i, j]:8.1f}" for j in range(matrix.shape[1]))
                f.write(row + "\n")
            f.write("=" * 50 + "\n")
        print(f"Результат записан в файл {filename}")
    
    save_thread = threading.Thread(target=save_worker)
    save_thread.start()
    return save_thread

def main():
    A = np.array([
        [1, 2, 3],
        [5, -6, -7],
        [5, 6, 7],
        [50, 1, 2]
    ])

    B = np.array([
        [5, 8, 5, -3],
        [2, 3, -2, 13],
        [5, 6, -9, 11]
    ])

    C = np.full((A.shape[0], B.shape[1]), None)

    print("Матрица A:\n", A)
    print("Матрица B:\n", B)
    lock = threading.Lock()
    completed_threads = []
    p = 3
    print(f"\nЗапускаем {p} потока для вычисления матрицы C...")
    
    # Создаем и запускаем p потоков
    threads = []
    start_time = time.time()
    
    for i in range(p):
        thread = MyThread(i + 1, A, B, C, lock, completed_threads)
        threads.append(thread)
        thread.start()

    # Ждем завершения всех потоков
    for thread in threads:
        thread.join()
    
    end_time = time.time()

    print(f"\nВсе потоки завершили работу за {end_time - start_time:.2f} секунд")
    print(f"Порядок завершения потоков: {completed_threads}")
    
    print("\nРезультирующая матрица C = A × B:")
    print(C)
    
    # Запускаем запись в файл в отдельном потоке
    print("\nЗапускаем запись результата в файл...")
    save_thread = save_to_file(C)
    save_thread.join()

if __name__ == "__main__":
    main()