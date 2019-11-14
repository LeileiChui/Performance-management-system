# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QSize


class Student_ui(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(1200, 800)
        Widget.setMaximumSize(Widget.size())
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
        self.exitButton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.exitButton.setStyleSheet("font: 18pt \"Heiti SC\";")
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
        self.Photo.setPixmap(QPixmap("Stu.png").scaled(self.Photo.size()))
        self.Photo.setObjectName("Photo")
        self.gridLayout_3.addWidget(self.Photo, 0, 0, 1, 1)
        self.Name = QtWidgets.QLabel(self.InfoWidget)
        self.Name.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Name.setObjectName("Name")
        self.gridLayout_3.addWidget(self.Name, 1, 0, 1, 1)
        self.UserType = QtWidgets.QLabel(self.InfoWidget)
        self.UserType.setMaximumSize(QtCore.QSize(16777215, 30))
        self.UserType.setObjectName("UserType")
        self.gridLayout_3.addWidget(self.UserType, 2, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.InfoWidget)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)
        self.table = QtWidgets.QTableWidget(self.mainWidget)
        self.table.setMinimumSize(QtCore.QSize(0, 0))
        self.table.setObjectName("table")
        self.gridLayout_2.addWidget(self.table, 0, 1, 2, 1)
        self.gridLayout.addWidget(self.mainWidget, 1, 0, 1, 1)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)
        self.exitButton.setIcon(QIcon("Exit.png"))
        self.exitButton.setIconSize(QSize(35, 35))
        self.exitButton.setStyleSheet("font: 18pt \"Heiti SC\";"
                                      "background-color:transparent;")

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.exitButton.setText(_translate("Widget", "退出"))
        self.UserType.setText(_translate("Widget",
                                         "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">身份：学生</span></p></body></html>"))

    def setName(self, Name):
        _translate = QtCore.QCoreApplication.translate
        self.Name.setText(_translate("Widget",
                                     "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">" + Name + "</span></p></body></html>"))
