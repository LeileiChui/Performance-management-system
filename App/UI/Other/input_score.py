from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from UI.Other.input_score_ui import *


class input_score(QDialog):
    def __init__(self):
        super().__init__(None)
        self.ui = input_score_ui()
        self.ui.setupUi(self)
        self.setWindowTitle("录入成绩")
        self.ui.LeftButton.clicked.connect(self.reject)
        self.ui.RightButton.clicked.connect(self.accept)
        self.ui.score.returnPressed.connect(self.accept)
        self.ui.lineEdit.setValidator(QRegExpValidator(QRegExp('[A-Z][0-9]{1,}')))
        self.ui.score.setValidator(QtGui.QIntValidator())
