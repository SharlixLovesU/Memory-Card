from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QRadioButton, \
    QPushButton, QLabel, QSpinBox, QButtonGroup, QGroupBox, QLineEdit, QApplication

from PyQt5.QtCore import Qt

menu_w = QWidget()

lb_question = QLabel("Введіть запитання")
lb_right_ans = QLabel("Введіть вірну відповідь")
lb_wrong_ans1 = QLabel("Введіть першу хибну відповідь")
lb_wrong_ans2 = QLabel("Введіть другу хибну відповідь")
lb_wrong_ans3 = QLabel("Введіть третю хибну відповідь")

le_question = QLineEdit()
le_right_ans = QLineEdit()
le_wrong_ans1 = QLineEdit()
le_wrong_ans2 = QLineEdit()
le_wrong_ans3 = QLineEdit()


