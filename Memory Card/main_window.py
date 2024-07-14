from PyQt5.QTWidgets import QWidget, QHBoxLayout, QVBoxLayout, QRadioButton, \
    QPushButton, QLabel, QSpinBox, QButtonGroup, QGroupBox, QApplication

from PyQt5.QtCore import Qt

window = QWidget()

btn_menu = QPushButton()
btn_rest = QPushButton
btn_next = QPushButton

rb_ans1 = QRadioButton("1")
rb_ans2 = QRadioButton("2")
rb_ans3 = QRadioButton("3")
rb_ans4 = QRadioButton("4")

rbGroup = QButtonGroup()
rbGroup.addButton(rb_ans1)
rbGroup.addButton(rb_ans2)
rbGroup.addButton(rb_ans3)
rbGroup.addButton(rb_ans4)

lb_question = QLabel("Запитання")
lb_rest = QLabel("хвилин")
lb_rightAns = QLabel("відповідь")
lb_result = QLabel("Вірно!")

sp_rest = QSpinBox()

gbAns = QGroupBox("Варіанти відповідей:")

rb_v1 = QVBoxLayout()
rb_v2 = QVBoxLayout()
rb_h = QHBoxLayout()

rb_v1.addWidget(rb_ans1)
rb_v1.addWidget(rb_ans2)
rb_v2.addWidget(rb_ans3)
rb_v2.addWidget(rb_ans4)

rb_h.addLayout(rb_v1)
rb_h.addLayout(rb_v2)

gbAns.setLayout(rb_h)