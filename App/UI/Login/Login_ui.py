# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *


class Login_ui(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(1200, 800)
        Widget.setMinimumSize(Widget.size())
        self.gridLayout = QtWidgets.QGridLayout(Widget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 3, 1, 1)
        self.widget = QtWidgets.QWidget(Widget)
        self.widget.setMinimumSize(QtCore.QSize(800, 500))
        self.widget.setStatusTip("")
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(332, 59, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 4, 4, 1, 2)
        self.Title = QtWidgets.QLabel(self.widget)
        self.Title.setObjectName("Title")
        self.gridLayout_2.addWidget(self.Title, 0, 1, 1, 5)
        self.InputArea = QtWidgets.QWidget(self.widget)
        self.InputArea.setMinimumSize(QtCore.QSize(300, 180))
        self.InputArea.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.InputArea.setObjectName("InputArea")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.InputArea)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.NameWidget = QtWidgets.QWidget(self.InputArea)
        self.NameWidget.setObjectName("NameWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.NameWidget)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.NameLabel = QtWidgets.QLabel(self.NameWidget)
        self.NameLabel.setMinimumSize(QtCore.QSize(55, 0))
        self.NameLabel.setObjectName("NameLabel")
        self.horizontalLayout_2.addWidget(self.NameLabel)
        self.User_ID = QtWidgets.QLineEdit(self.NameWidget)
        self.User_ID.setMinimumSize(QtCore.QSize(0, 30))
        self.User_ID.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.User_ID.setObjectName("User_ID")
        self.User_ID.setPlaceholderText("请输入用户名")
        self.horizontalLayout_2.addWidget(self.User_ID)
        self.verticalLayout.addWidget(self.NameWidget)
        self.PasswordWidget = QtWidgets.QWidget(self.InputArea)
        self.PasswordWidget.setMinimumSize(QtCore.QSize(301, 61))
        self.PasswordWidget.setObjectName("PasswordWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.PasswordWidget)
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.PasswordLabel = QtWidgets.QLabel(self.PasswordWidget)
        self.PasswordLabel.setMinimumSize(QtCore.QSize(55, 37))
        self.PasswordLabel.setObjectName("PasswordLabel")
        self.horizontalLayout_3.addWidget(self.PasswordLabel)
        self.Password = QtWidgets.QLineEdit(self.PasswordWidget)
        self.Password.setMinimumSize(QtCore.QSize(0, 30))
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setObjectName("Password")
        self.Password.setPlaceholderText("请输入密码")
        self.horizontalLayout_3.addWidget(self.Password)
        self.verticalLayout.addWidget(self.PasswordWidget)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.IdentityWidget = QtWidgets.QWidget(self.InputArea)
        self.IdentityWidget.setMinimumSize(QtCore.QSize(300, 60))
        self.IdentityWidget.setObjectName("IdentityWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.IdentityWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.IdentityLabel = QtWidgets.QLabel(self.IdentityWidget)
        self.IdentityLabel.setObjectName("IdentityLabel")
        self.horizontalLayout.addWidget(self.IdentityLabel)
        self.Student = QtWidgets.QRadioButton(self.IdentityWidget)
        self.Student.setStyleSheet("font: 75 15pt \"Heiti SC\";")
        self.Student.setObjectName("Student")
        self.Student.setChecked(True)
        self.horizontalLayout.addWidget(self.Student)
        self.Teacher = QtWidgets.QRadioButton(self.IdentityWidget)
        self.Teacher.setStyleSheet("font: 75 15pt \"Heiti SC\";")
        self.Teacher.setObjectName("Teacher")
        self.horizontalLayout.addWidget(self.Teacher)
        self.Manager = QtWidgets.QRadioButton(self.IdentityWidget)
        self.Manager.setStyleSheet("font: 75 15pt \"Heiti SC\";")
        self.Manager.setObjectName("Manager")
        self.horizontalLayout.addWidget(self.Manager)
        self.verticalLayout.addWidget(self.IdentityWidget)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.ButtonWidget = QtWidgets.QWidget(self.InputArea)
        self.ButtonWidget.setMinimumSize(QtCore.QSize(0, 50))
        self.ButtonWidget.setObjectName("ButtonWidget")
        self.accept = QtWidgets.QPushButton(self.ButtonWidget)
        self.accept.setGeometry(QtCore.QRect(180, 11, 112, 41))
        self.accept.setStyleSheet("QPushButton{\n"
                                  "    font: 75 15pt \"Heiti SC\";\n"
                                  "    background-color:rgba(15, 128, 255,0.8);\n"
                                  "    border-radius:20px;\n"
                                  "    padding:6px;\n"
                                  "}\n"
                                  "QPushButton:pressed{\n"
                                  "    font: 75 15pt \"Heiti SC\";\n"
                                  "    background-color:rgb(15, 128, 255);\n"
                                  "    border-radius:20px;\n"
                                  "    padding:6px;\n"
                                  "}")
        self.accept.setObjectName("accept")
        self.reject = QtWidgets.QPushButton(self.ButtonWidget)
        self.reject.setGeometry(QtCore.QRect(30, 10, 112, 41))
        self.reject.setStyleSheet("QPushButton{\n"
                                  "font: 75 15pt \"Heiti SC\";\n"
                                  "background-color:rgba(255, 255, 255,0.7);\n"
                                  "border-radius:20px;\n"
                                  "padding:6px;\n"
                                  "}\n"
                                  "QPushButton:pressed{\n"
                                  "    font: 75 15pt \"Heiti SC\";\n"
                                  "    background-color:rgb(204, 204, 204);\n"
                                  "    border-radius:20px;\n"
                                  "    padding:6px;\n"
                                  "}")
        self.reject.setObjectName("reject")
        self.verticalLayout.addWidget(self.ButtonWidget)
        self.gridLayout_2.addWidget(self.InputArea, 2, 5, 2, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem7, 3, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(82, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 2, 4, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem9, 2, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(332, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem10, 1, 3, 1, 3)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem11, 2, 0, 1, 1)
        self.Logo = QtWidgets.QLabel(self.widget)
        self.Logo.setMinimumSize(QtCore.QSize(250, 250))
        self.Logo.setPixmap(QtGui.QPixmap("NJUPT_Logo.png").scaled(self.Logo.size()))
        self.Logo.setObjectName("Logo")
        self.gridLayout_2.addWidget(self.Logo, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.widget, 1, 2, 1, 1)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        self.Title.setText(_translate("Widget",
                                      "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                      "p, li { white-space: pre-wrap; }\n"
                                      "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                      "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:48pt;\">学生成绩管理系统</span></p></body></html>"))
        self.NameLabel.setText(
            _translate("Widget", "<html><head/><body><p><span style=\" font-size:18pt;\">用户名</span></p></body></html>"))
        self.PasswordLabel.setText(_translate("Widget",
                                              "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">密码</span></p></body></html>"))
        self.IdentityLabel.setText(
            _translate("Widget", "<html><head/><body><p><span style=\" font-size:18pt;\">身份</span></p></body></html>"))
        self.Student.setText(_translate("Widget", "学生"))
        self.Teacher.setText(_translate("Widget", "老师"))
        self.Manager.setText(_translate("Widget", "管理员"))
        self.accept.setText(_translate("Widget", "登陆"))
        self.reject.setText(_translate("Widget", "退出"))
