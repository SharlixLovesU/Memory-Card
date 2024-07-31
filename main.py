from PyQt5.QtWidgets import QApplication

app = QApplication([])

from main_window import *
from menu_window import *

window.show()
app.exec_()