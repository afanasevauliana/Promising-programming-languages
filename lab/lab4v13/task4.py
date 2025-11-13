from abc import ABC, abstractmethod
import random

class Student(ABC):
    def __init__(self, name):
        self.name = name
        self.rating = 0
    
    @abstractmethod
    def makeProgramming(self):
        pass
    
    @abstractmethod
    def makeElecEngineering(self):
        pass

class ITDStudent(Student):
    def makeProgramming(self):
        points = random.choice([4, 5])
        self.rating += points
        return points
    
    def makeElecEngineering(self):
        points = random.choice([3, 4])
        self.rating += points
        return points

class EVMStudent(Student):
    def makeProgramming(self):
        points = random.choice([3, 4])
        self.rating += points
        return points
    
    def makeElecEngineering(self):
        points = random.choice([4, 5])
        self.rating += points
        return points

class QueueManager: #управление очередью
    def __init__(self):
        self.students = []
    
    def generate_queue(self, num_students):
        for i in range(num_students):
            if random.choice([True, False]):
                student = ITDStudent(f"ИТД_Студент_{i+1}")
            else:
                student = EVMStudent(f"ЭВМ_Студент_{i+1}")
            self.students.append(student)
    
    def conduct_labs(self, num_programming_labs, num_elec_labs):
        for lab in range(num_programming_labs):
            for student in self.students:
                student.makeProgramming()
        
        for lab in range(num_elec_labs):
            for student in self.students:
                student.makeElecEngineering()
    
    def distribute_macbooks(self):
        sorted_students = sorted(self.students, key=lambda s: s.rating, reverse=True)
        num_macbooks = max(1, len(self.students) // 4)
        macbook_recipients = sorted_students[:num_macbooks]
        
        itd_count = 0
        evm_count = 0
        
        for student in macbook_recipients:
            if isinstance(student, ITDStudent):
                itd_count += 1
            elif isinstance(student, EVMStudent):
                evm_count += 1
        
        return itd_count, evm_count, macbook_recipients

if __name__ == "__main__":
    manager = QueueManager()
    manager.generate_queue(12)
    manager.conduct_labs(2, 2)
    itd_macbooks, evm_macbooks, recipients = manager.distribute_macbooks()
    
    print(f"Всего студентов: {len(manager.students)}")
    print(f"Макбуков к раздаче: {len(recipients)}")
    print("Рейтинги получивших макбуки:")
    for student in recipients:
        print(f"  {student.name}: {student.rating} баллов")
    print("ИТД получили макбуков:", itd_macbooks)
    print("ЭВМ получили макбуков:", evm_macbooks)