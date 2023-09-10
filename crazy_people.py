from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox
from random import randint
#створення додатка та вікна
app = QApplication([]) #додаток
main_win = QWidget() #вікно

question = QLabel('Коли януковича обідили')

btn1 = QRadioButton('2005')
btn2 = QRadioButton('2011')
btn3 = QRadioButton('2014')
btn4 = QRadioButton('2022')

vline = QVBoxLayout()
hline1 = QHBoxLayout()
hline2 = QHBoxLayout()


vline.addWidget(question, alignment= Qt.AlignCenter)

hline1.addWidget(btn1, alignment= Qt.AlignCenter)
hline1.addWidget(btn2, alignment= Qt.AlignCenter)

hline2.addWidget(btn3, alignment= Qt.AlignCenter)
hline2.addWidget(btn4, alignment= Qt.AlignCenter)

vline.addLayout(hline1)
vline.addLayout(hline2)

main_win.setWindowTitle('Конкурс від CrazyPeople') #назва вікна
main_win.resize(400, 200) #розмір вікна
#запуск додатка та показ вікна


def show_win():
    message = QMessageBox()
    message.setText('Ви виграли!')
    message.exec_()

def show_loose():
    message = QMessageBox()
    message.setText('Ви програли!')
    message.exec_()

btn3.clicked.connect(show_win)
btn1.clicked.connect(show_loose)
btn2.clicked.connect(show_loose)
btn4.clicked.connect(show_loose)

main_win.setLayout(vline)
main_win.show() #показуємо вікно
app.exec_() #запуск програми
