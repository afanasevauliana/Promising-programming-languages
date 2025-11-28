import threading
import time
import multiprocessing

class myThread(threading.Thread):
    def __init__(self, name, array):
        threading.Thread.__init__(self)
        self.name = name
        self.array = array
        self.max_v = None
    
    def run(self):
        print("Запуск: " + self.name)
        self.max_value = find_max(self.array)
        print(f"Максимум в {self.name}: {self.max_value}")
        print("Завершение: " + self.name)

def find_max(arr):
    m = arr[0]
    for i in arr[1:]:
        if i > m:
            m = i
    return m

def process_worker(name, array, result_queue):
    print(f"Запуск: {name}")
    max_value = find_max(array)
    result_queue.put((name, max_value))
    print(f"Максимум в {name}: {max_value}")
    print(f"Завершение: {name}")

def main():
    array1 = [1, 4, -5, 9, 15, 14, -40, 50, 51, 23, -23, 1, 2, 3, 4, 5, 6, 7, 8, 0, 43, 12, 5, -3, 5, 67, 91, 34, 23, 44, -45, -3, -6, 7, 56, 56, 74, 32, 1, 4, -5, 9]
    array2 = [3, -4, 1, 10, 20, -20, 43, 12, 5, -3, 5, 67, 91, 34, 23, 44, -45, -3, -6, 7, 56, 56, 74, 32, 1, 4, -5, 9, 15, 14, -40, 50, 51, 23, -23, 1, 2, 3, 4, 5, 6, 7, 8, 0, 43, 12, 5, -3, 5, 67, 91, 34, 23, 44, -45, -3, -6, 7, 56, 56, 74, 32, 1, 4, -5, 9]

    print("\n\nОбычный способ:")
    start_time_sync = time.time()

    max1 = find_max(array1)
    max2 = find_max(array2)

    end_time_sync = time.time()
    sync_time = end_time_sync - start_time_sync
    print(f"Максимум в array1: {max1}")
    print(f"Максимум в array2: {max2}")
    print(f"Время: {sync_time:.6f} секунд")

    print("\n\nМногопоточный способ:")
    start_time_thread = time.time()

    thread1 = myThread("Поток 1", array1)
    thread2 = myThread("Поток 2", array2)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    end_time_thread = time.time()
    thread_time = end_time_thread - start_time_thread
    print(f"Общее время: {thread_time:.6f} секунд")

    print("\n\nМногопроцессный способ:")
    start_time_process = time.time()

    result_queue = multiprocessing.Queue()
    process1 = multiprocessing.Process(target=process_worker, args=("Процесс 1", array1, result_queue))
    process2 = multiprocessing.Process(target=process_worker, args=("Процесс 2", array2, result_queue))

    process1.start()
    process2.start()

    results = []
    results.append(result_queue.get())
    results.append(result_queue.get())

    process1.join()
    process2.join()

    end_time_process = time.time()
    process_time = end_time_process - start_time_process

    for name, max_value in results:
        print(f"{name}: {max_value}")

    print(f"Общее время: {process_time:.6f} секунд")

    print(f"\nВыводы:")
    if thread_time < sync_time:
        print(f"- Многопоточный метод быстрее обычного в {sync_time/thread_time:.2f} раз")
    else:
        print(f"- Многопоточный метод медленнее обычного")
        
    if process_time < sync_time:
        print(f"- Многопроцессный метод быстрее обычного в {sync_time/process_time:.2f} раз")
    else:
        print(f"- Многопроцессный метод медленнее обычного")

if __name__ == '__main__':
    main()