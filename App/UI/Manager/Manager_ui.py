# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QAbstractItemView


class Manager_ui(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(1200, 800)
        Widget.setMinimumSize(Widget.size())
        self.gridLayout = QtWidgets.QGridLayout(Widget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.topWidget = QtWidgets.QWidget(Widget)
        self.topWidget.setMinimumSize(QtCore.QSize(0, 50))
        self.topWidget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.topWidget.setObjectName("topWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.topWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.exitButton = QtWidgets.QPushButton(self.topWidget)
        self.exitButton.setMinimumSize(QtCore.QSize(150, 50))
        self.exitButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.exitButton.setObjectName("exitButton")
        self.horizontalLayout.addWidget(self.exitButton)
        self.gridLayout.addWidget(self.topWidget, 0, 0, 1, 1)
        self.mainWidget = QtWidgets.QWidget(Widget)
        self.mainWidget.setEnabled(True)
        self.mainWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.mainWidget.setObjectName("mainWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.mainWidget)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget = QtWidgets.QWidget(self.mainWidget)
        self.widget.setMinimumSize(QtCore.QSize(200, 616))
        self.widget.setMaximumSize(QtCore.QSize(150, 616))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.InfoWidget = QtWidgets.QWidget(self.widget)
        self.InfoWidget.setMinimumSize(QtCore.QSize(0, 300))
        self.InfoWidget.setMaximumSize(QtCore.QSize(16777215, 300))
        self.InfoWidget.setObjectName("InfoWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.InfoWidget)
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Photo = QtWidgets.QLabel(self.InfoWidget)
        self.Photo.setMinimumSize(QtCore.QSize(125, 125))
        self.Photo.setMaximumSize(QtCore.QSize(125, 125))
        self.Photo.setPixmap(QPixmap("Manager.png").scaled(self.Photo.size()))
        self.Photo.setObjectName("Photo")
        self.gridLayout_3.addWidget(self.Photo, 0, 0, 1, 1)
        self.Name = QtWidgets.QLabel(self.InfoWidget)
        self.Name.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Name.setObjectName("User_ID")
        self.gridLayout_3.addWidget(self.Name, 1, 0, 1, 1)
        self.UserType = QtWidgets.QLabel(self.InfoWidget)
        self.UserType.setMaximumSize(QtCore.QSize(16777215, 30))
        self.UserType.setObjectName("UserType")
        self.gridLayout_3.addWidget(self.UserType, 2, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.InfoWidget)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.TeacherBtn = QtWidgets.QPushButton(self.widget)
        self.TeacherBtn.setMinimumSize(QtCore.QSize(0, 50))
        self.TeacherBtn.setObjectName("TeacherBtn")
        self.verticalLayout_2.addWidget(self.TeacherBtn)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.StudentBtn = QtWidgets.QPushButton(self.widget)
        self.StudentBtn.setMinimumSize(QtCore.QSize(0, 50))
        self.StudentBtn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.StudentBtn.setObjectName("StudentBtn")
        self.verticalLayout_2.addWidget(self.StudentBtn)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 1, 0, 1, 1)

        self.widget_2 = QtWidgets.QWidget(self.mainWidget)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 60))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)

        self.Save = QtWidgets.QPushButton(self.widget_2)
        self.Save.setMinimumSize(QtCore.QSize(150, 50))
        self.Save.setMaximumSize(QtCore.QSize(150, 50))
        self.Save.setObjectName("Save")
        self.horizontalLayout_2.addWidget(self.Save)

        self.newClass = QtWidgets.QPushButton(self.widget_2)
        self.newClass.setMinimumSize(QtCore.QSize(150, 50))
        self.newClass.setMaximumSize(QtCore.QSize(150, 50))
        self.newClass.setObjectName("newTeacher")
        self.horizontalLayout_2.addWidget(self.newClass)

        self.newStudent = QtWidgets.QPushButton(self.widget_2)
        self.newStudent.setMinimumSize(QtCore.QSize(150, 50))
        self.newStudent.setMaximumSize(QtCore.QSize(150, 50))
        self.newStudent.setObjectName("newStudent")
        self.horizontalLayout_2.addWidget(self.newStudent)

        self.newTeacher = QtWidgets.QPushButton(self.widget_2)
        self.newTeacher.setMinimumSize(QtCore.QSize(150, 50))
        self.newTeacher.setMaximumSize(QtCore.QSize(150, 50))
        self.newTeacher.setObjectName("newTeacher")
        self.horizontalLayout_2.addWidget(self.newTeacher)

        self.gridLayout_2.addWidget(self.widget_2, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.mainWidget, 1, 0, 1, 1)

        # self.Save.hide()
        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

        self.exitButton.setIcon(QIcon("Exit.png"))
        self.exitButton.setIconSize(QSize(35, 35))
        self.exitButton.setStyleSheet("font: 18pt \"Heiti SC\";"
                                      "background-color:transparent;")

        self.TeacherBtn.setIcon(QIcon("teacher_small.png"))
        self.TeacherBtn.setIconSize(QSize(35, 35))
        self.TeacherBtn.setStyleSheet("font: 18pt \"Heiti SC\";"
                                      "background-color:transparent;")

        self.StudentBtn.setIcon(QIcon("studen_small.png"))
        self.StudentBtn.setIconSize(QSize(35, 35))
        self.StudentBtn.setStyleSheet("font: 18pt \"Heiti SC\";"
                                      "background-color:transparent;")

        self.Save.setIcon(QIcon("save.png"))
        self.Save.setIconSize(QSize(35, 35))
        self.Save.setStyleSheet("font: 18pt \"Heiti SC\";"
                                "background-color:transparent;")

        self.newStudent.setIcon(QIcon("add.png"))
        self.newStudent.setIconSize(QSize(35, 35))
        self.newStudent.setStyleSheet("font: 18pt \"Heiti SC\";"
                                      "background-color:transparent;")

        self.newClass.setIcon(QIcon("add.png"))
        self.newClass.setIconSize(QSize(35, 35))
        self.newClass.setStyleSheet("font: 18pt \"Heiti SC\";"
                                    "background-color:transparent;")
        self.newClass.hide()
        self.newTeacher.hide()

        self.newTeacher.setIcon(QIcon("add.png"))
        self.newTeacher.setIconSize(QSize(35, 35))
        self.newTeacher.setStyleSheet("font: 18pt \"Heiti SC\";"
                                      "background-color:transparent;")

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.exitButton.setText(_translate("Widget", "退出"))

        self.UserType.setText(_translate("Widget",
                                         "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">身份：管理员</span></p></body></html>"))
        self.TeacherBtn.setText(_translate("Widget", "教师信息"))
        self.StudentBtn.setText(_translate("Widget", "学生信息"))
        self.Save.setText(_translate("Widget", "保存"))
        self.newStudent.setText(_translate("Widget", "添加学生"))
        self.newClass.setText(_translate("Widget", "添加课程"))
        self.newTeacher.setText(_translate("Widget", "添加教师"))

        self.newStudent.hide()
        self.Save.hide()

    def setName(self, Name):
        _translate = QtCore.QCoreApplication.translate
        self.Name.setText(_translate("Widget",
                                     "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">" + Name + "</span></p></body></html>"))
