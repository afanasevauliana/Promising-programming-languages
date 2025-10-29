import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget)
from PyQt5.QtCore import Qt

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
     
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        btn1 = QPushButton('Построить график', self)
        btn1.clicked.connect(self.btn1_clicked)
        main_layout.addWidget(btn1)
        
        self.figure = Figure(figsize=(8, 6))
        self.canvas = FigureCanvas(self.figure)
        main_layout.addWidget(self.canvas)
        
        self.setMinimumSize(800, 600)
        self.setWindowTitle('График функции |sin(2x)|/sin(x)')
        self.show()

    def btn1_clicked(self):
        x = np.linspace(0.1, 4*np.pi, 1000)
        with np.errstate(divide='ignore', invalid='ignore'):
            y = np.abs(np.sin(2*x)) / np.sin(x)
            y = np.where(np.isinf(y), np.nan, y)
        ax = self.figure.add_subplot(111)
        ax.plot(x, y, 'b-', linewidth=2)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('График функции $\\frac{|\\sin(2x)|}{\\sin(x)}$')
        ax.grid(True, alpha=0.3)
        zero_points = [np.pi, 2*np.pi, 3*np.pi]
        for point in zero_points:
            ax.axvline(x=point, color='r', linestyle='--', alpha=0.5)
        ax.set_ylim(-5, 5)

        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())