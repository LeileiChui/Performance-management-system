from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QLayoutItem
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from UI.Login.LoginWidget import *
from UI.Student.StuWidget import *
from UI.Teacher.TeacherWidget import *
from UI.Manager.ManagerWidget import *
import sip


class Mainwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1200, 800)
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")

        self.background = QPixmap("Background.png")
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(self.background.scaled(self.size())))
        self.setPalette(self.palette)
        self.setWindowIcon(QIcon("APP.png"))

        self.gridLayout.addWidget(LoginWidget())

    def resizeEvent(self, QResizeEvent):
        self.palette.setBrush(QPalette.Background, QBrush(self.background.scaled(self.size())))
        self.setPalette(self.palette)

    def LoginSuccess(self, LoginWidget, UserType, UserID, UserName):
        sip.delete(LoginWidget)
        if UserType is 0:
            self.gridLayout.addWidget(StuWidget(UserName, UserID))
        elif UserType is 1:
            self.gridLayout.addWidget(TeacherWidget(UserName, UserID))
        elif UserType is 2:
            self.gridLayout.addWidget(ManagerWidget(UserName, UserID))

    def Logout(self, Widget):
        sip.delete(Widget)
        self.gridLayout.addWidget(LoginWidget())
