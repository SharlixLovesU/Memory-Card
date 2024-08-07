from PyQt5.QtWidgets import QApplication

app = QApplication([])

from main_window import *
from menu_window import *
from time import sleep

class Question():
    def __init__(self, question, answer, wrong_ans1, wrong_ans2, wrong_ans3):
        self.question = question 
        self.answer = answer 
        self.wrong_answer1 = wrong_ans1 
        self.wrong_answer2 = wrong_ans2 
        self.wrong_answer3 = wrong_ans3 
        self.actual = True 
        self.count_asked = 0 
        self.count_right = 0 
    def got_right(self):
        self.count_asked += 1
        self.count_right += 1

q1 = Question("Яблуко", "apple", 'pineapple', 'aply', 'application')
q2 = Question
q3 = Question
q4 = Question

def back_menu():
    menu_w.hide()
    window.show()

btn_back.clicked.connect(back_menu)

def rest():
    window.hide()
    n = sp_rest.value() * 60
    sleep(n)
    window.show()

btn_rest.clicked.connect(rest)
menu_w.show()
app.exec_()