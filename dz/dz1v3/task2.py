import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QRadioButton, QButtonGroup, QFrame)
from PyQt5.QtCore import Qt

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
     
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        top_layout = QHBoxLayout()
        btn1 = QPushButton('Построить график', self)
        btn1.clicked.connect(self.btn1_clicked)
        top_layout.addWidget(btn1)
        
        self.graph_label = QLabel('График |sin(2x)| / (sinx) был построен', self)
        self.graph_label.setStyleSheet("font-size: 18px; font-weight: bold; color: blue;")
        self.graph_label.setAlignment(Qt.AlignCenter)
        self.graph_label.hide() # надпись изначально скрыта
        top_layout.addWidget(self.graph_label)
        top_layout.addStretch()
        
        main_layout.addLayout(top_layout)
        middle_layout = QHBoxLayout()
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        
        self.figure = Figure(figsize=(8, 6))
        self.canvas = FigureCanvas(self.figure)
        left_layout.addWidget(self.canvas)
        middle_layout.addWidget(left_widget, 7)
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        traffic_light_label = QLabel('Светофор', self)
        traffic_light_label.setStyleSheet("font-size: 18px; font-weight: bold; color: darkred; padding: 10px;")
        traffic_light_label.setAlignment(Qt.AlignCenter)
        right_layout.addWidget(traffic_light_label)
        center_container = QWidget()
        center_layout = QHBoxLayout(center_container)
        center_layout.addStretch()
        traffic_light_layout = QVBoxLayout()
        self.color_group = QButtonGroup(self) # группа кнопок светофора (может быть выбрана только одна из них)
        frame_size = 80
        frame_style = "background-color: white; border: 3px solid black; border-radius: 10px;"
        
        red_widget = QWidget()
        red_layout = QHBoxLayout(red_widget)
        red_layout.setAlignment(Qt.AlignCenter)
        self.red_radio = QRadioButton('Красный', self)
        self.red_radio.setStyleSheet("font-size: 14px; font-weight: bold;")
        self.red_frame = QFrame(self)
        self.red_frame.setFixedSize(frame_size, frame_size)
        self.red_frame.setStyleSheet(frame_style)
        self.red_radio.toggled.connect(lambda: self.change_color('red'))
        self.color_group.addButton(self.red_radio)
        red_layout.addWidget(self.red_radio)
        red_layout.addSpacing(10)
        red_layout.addWidget(self.red_frame)
        traffic_light_layout.addWidget(red_widget)
        
        yellow_widget = QWidget()
        yellow_layout = QHBoxLayout(yellow_widget)
        yellow_layout.setAlignment(Qt.AlignCenter)
        self.yellow_radio = QRadioButton('Желтый', self)
        self.yellow_radio.setStyleSheet("font-size: 14px; font-weight: bold;")
        self.yellow_frame = QFrame(self)
        self.yellow_frame.setFixedSize(frame_size, frame_size)
        self.yellow_frame.setStyleSheet(frame_style)
        self.yellow_radio.toggled.connect(lambda: self.change_color('yellow'))
        self.color_group.addButton(self.yellow_radio)
        yellow_layout.addWidget(self.yellow_radio)
        yellow_layout.addSpacing(10)
        yellow_layout.addWidget(self.yellow_frame)
        traffic_light_layout.addWidget(yellow_widget)
        
        green_widget = QWidget()
        green_layout = QHBoxLayout(green_widget)
        green_layout.setAlignment(Qt.AlignCenter)
        self.green_radio = QRadioButton('Зеленый', self)
        self.green_radio.setStyleSheet("font-size: 14px; font-weight: bold;")
        self.green_frame = QFrame(self)
        self.green_frame.setFixedSize(frame_size, frame_size)
        self.green_frame.setStyleSheet(frame_style)
        self.green_radio.toggled.connect(lambda: self.change_color('green'))
        self.color_group.addButton(self.green_radio)
        green_layout.addWidget(self.green_radio)
        green_layout.addSpacing(10)
        green_layout.addWidget(self.green_frame)
        traffic_light_layout.addWidget(green_widget)
        
        center_layout.addLayout(traffic_light_layout)
        center_layout.addStretch()
        right_layout.addWidget(center_container)
        right_layout.addStretch()
        middle_layout.addWidget(right_widget, 3)
        main_layout.addLayout(middle_layout)
        self.setMinimumSize(1000, 700)
        self.setWindowTitle('График функции |sin(2x)|/sin(x) со светофором')
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
        self.graph_label.show()

    def change_color(self, color):
        color_map = {
            'red': '#FF0000',
            'yellow': '#FFFF00', 
            'green': '#00FF00'
        }
        self.red_frame.setStyleSheet("background-color: white; border: 3px solid black; border-radius: 10px;")
        self.yellow_frame.setStyleSheet("background-color: white; border: 3px solid black; border-radius: 10px;")
        self.green_frame.setStyleSheet("background-color: white; border: 3px solid black; border-radius: 10px;")
        if color == 'red' and self.red_radio.isChecked():
            self.red_frame.setStyleSheet(f"background-color: {color_map['red']}; border: 3px solid black; border-radius: 10px;")
        elif color == 'yellow' and self.yellow_radio.isChecked():
            self.yellow_frame.setStyleSheet(f"background-color: {color_map['yellow']}; border: 3px solid black; border-radius: 10px;")
        elif color == 'green' and self.green_radio.isChecked():
            self.green_frame.setStyleSheet(f"background-color: {color_map['green']}; border: 3px solid black; border-radius: 10px;")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())