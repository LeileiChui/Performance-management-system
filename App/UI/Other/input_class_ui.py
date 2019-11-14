# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Input_ClassName_ui(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(396, 187)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.MsgWidget = QtWidgets.QWidget(Dialog)
        self.MsgWidget.setObjectName("MsgWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.MsgWidget)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.MsgWidget)
        self.label.setStyleSheet("font: 18pt \"Heiti SC\";")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.MsgWidget)
        self.label_2.setMinimumSize(QtCore.QSize(20, 0))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.MsgWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 45))
        self.lineEdit.setStyleSheet("font: 18pt \"Heiti SC\";")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout.addWidget(self.MsgWidget)
        self.ButtonWidget = QtWidgets.QWidget(Dialog)
        self.ButtonWidget.setObjectName("ButtonWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.ButtonWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LeftButton = QtWidgets.QPushButton(self.ButtonWidget)
        self.LeftButton.setMinimumSize(QtCore.QSize(111, 41))
        self.LeftButton.setMaximumSize(QtCore.QSize(111, 41))
        self.LeftButton.setStyleSheet("QPushButton{\n"
                                      "    font: 75 15pt \"Heiti SC\";\n"
                                      "    background-color:rgba(255, 255, 255,0.5);\n"
                                      "    border-radius:20px;\n"
                                      "    padding:6px;\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "    font: 75 15pt \"Heiti SC\";\n"
                                      "    background-color:rgb(204, 204, 204);\n"
                                      "    border-radius:20px;\n"
                                      "    padding:6px;\n"
                                      "}")
        self.LeftButton.setText("取消")
        self.LeftButton.setObjectName("LeftButton")
        self.horizontalLayout.addWidget(self.LeftButton)
        self.RightButton = QtWidgets.QPushButton(self.ButtonWidget)
        self.RightButton.setMinimumSize(QtCore.QSize(111, 41))
        self.RightButton.setMaximumSize(QtCore.QSize(111, 41))
        self.RightButton.setStyleSheet("QPushButton{\n"
                                       "    font: 75 15pt \"Heiti SC\";\n"
                                       "    background-color:rgba(15, 128, 255,0.5);\n"
                                       "    border-radius:20px;\n"
                                       "    padding:6px;\n"
                                       "}\n"
                                       "QPushButton:pressed{\n"
                                       "    font: 75 15pt \"Heiti SC\";\n"
                                       "    background-color:rgb(15, 128, 255);\n"
                                       "    border-radius:20px;\n"
                                       "    padding:6px;\n"
                                       "}")
        self.RightButton.setText("确定")
        self.RightButton.setObjectName("RightButton")
        self.horizontalLayout.addWidget(self.RightButton)
        self.verticalLayout.addWidget(self.ButtonWidget)

        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.label.setText("请输入课程名")
