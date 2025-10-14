import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import math

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('График функции |sin(2x)| / sin(x)')
        
        # Создаем layout
        layout = QVBoxLayout()
        
        # Создаем кнопку для построения графика
        self.btn = QPushButton('Построить график', self)
        self.btn.clicked.connect(self.plot_function)
        layout.addWidget(self.btn)
        
        # Создаем область для графика
        self.figure = Figure(figsize=(8, 6), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)
        
        self.setLayout(layout)
        self.show()
        
    def plot_function(self):
        # Очищаем предыдущий график
        self.figure.clear()
        
        # Создаем оси для графика
        ax = self.figure.add_subplot(111)
        
        # Генерируем значения x, избегая точек, где sin(x) = 0
        x = np.linspace(0.1, 4 * np.pi, 1000)  # Начинаем с 0.1 чтобы избежать деления на 0
        
        # Вычисляем значения функции
        # |sin(2x)| / sin(x) = |2*sin(x)*cos(x)| / sin(x) = 2*|cos(x)|
        y = np.abs(np.sin(2 * x)) / np.sin(x)
        
        # Строим график
        ax.plot(x, y, 'b-', linewidth=2, label='|sin(2x)| / sin(x)')
        
        # Настраиваем график
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('График функции |sin(2x)| / sin(x)')
        ax.grid(True, alpha=0.3)
        ax.legend()
        
        # Устанавливаем пределы по y для лучшего отображения
        ax.set_ylim(-1, 5)
        
        # Добавляем вертикальные асимптоты в точках, где sin(x) = 0
        asymptotes = [np.pi * i for i in range(1, 5)]
        for asymptote in asymptotes:
            ax.axvline(x=asymptote, color='red', linestyle='--', alpha=0.5, label='Асимптота' if asymptote == np.pi else "")
        
        # Обновляем canvas
        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())