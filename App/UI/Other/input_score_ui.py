# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'input_score.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class input_score_ui(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 281)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.StudentID = QtWidgets.QWidget(Dialog)
        self.StudentID.setObjectName("StudentID")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.StudentID)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.StudentID)
        self.label.setStyleSheet("font: 18pt \"Heiti SC\";")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.StudentID)
        self.label_2.setMinimumSize(QtCore.QSize(20, 0))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.StudentID)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 45))
        self.lineEdit.setStyleSheet("font: 18pt \"Heiti SC\";")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout.addWidget(self.StudentID)
        self.Score = QtWidgets.QWidget(Dialog)
        self.Score.setObjectName("Score")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.Score)
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.Score)
        self.label_3.setStyleSheet("font: 18pt \"Heiti SC\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.Score)
        self.label_4.setMinimumSize(QtCore.QSize(20, 0))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.score = QtWidgets.QLineEdit(self.Score)
        self.score.setMinimumSize(QtCore.QSize(0, 45))
        self.score.setStyleSheet("font: 18pt \"Heiti SC\";")
        self.score.setAlignment(QtCore.Qt.AlignCenter)
        self.score.setObjectName("score")
        self.horizontalLayout_3.addWidget(self.score)
        self.verticalLayout.addWidget(self.Score)
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
        self.RightButton.setObjectName("RightButton")
        self.horizontalLayout.addWidget(self.RightButton)
        self.verticalLayout.addWidget(self.ButtonWidget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "请输入学号"))
        self.label_3.setText(_translate("Dialog", "请输入分数"))
        self.LeftButton.setText(_translate("Dialog", "取消"))
        self.RightButton.setText(_translate("Dialog", "确认"))
