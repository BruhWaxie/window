from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout


app = QApplication([])
main_win = QWidget()


main_win.setWindowTitle('TRASH')
main_win.resize(400, 250)

label = QLabel("Натисни щоб дізнатись переможця")
result = QLabel("?")
btn = QPushButton('Згенерувати')

line = QVBoxLayout()
line.addWidget(label)
line.addWidget(result)
line.addWidget(btn)

main_win.setLayout(line)
main_win.show()
app.exec_()

