from PyQt5.QtWidgets import QDialog
from UI.Other.input_class_ui import *
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp


class input_className(QDialog):
    def __init__(self):
        super().__init__(None)
        self.ui = Input_ClassName_ui()
        self.ui.setupUi(self)
        self.setWindowTitle("新建课程")
        self.ui.LeftButton.clicked.connect(self.reject)
        self.ui.RightButton.clicked.connect(self.accept)
        self.ui.lineEdit.returnPressed.connect(self.accept)
        self.ui.lineEdit.setValidator(QRegExpValidator(QRegExp('^[\u4E00-\u9FA5A-Za-z0-9]{2,20}$')))
