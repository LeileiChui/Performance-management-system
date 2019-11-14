from PyQt5.QtWidgets import QItemDelegate, QLineEdit
from PyQt5 import QtGui
from PyQt5.QtCore import Qt


class EmptyDelegate(QItemDelegate):
    def __init__(self, parent):
        super(EmptyDelegate, self).__init__(parent)

    def createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex):
        return None


class intOnlyDelegate(QItemDelegate):
    def __init__(self, parent=None):
        super(intOnlyDelegate, self).__init__(parent)

    def createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex):
        editor = QLineEdit(QWidget)
        editor.setValidator(QtGui.QIntValidator())
        return editor

    def setEditorData(self, lineEdit, QModelIndex):
        text = QModelIndex.model().data(QModelIndex, Qt.EditRole)
        lineEdit.setText(str(text))

    def updateEditorGeometry(self, QWidget, QStyleOptionViewItem, QModelIndex):
        QWidget.setGeometry(QStyleOptionViewItem.rect)

    def setModelData(self, lineEditor, QAbstractItemModel, QModelIndex):
        text = lineEditor.text()
        QAbstractItemModel.setData(QModelIndex, text, Qt.EditRole)
        QAbstractItemModel.setData(QModelIndex, text, Qt.EditRole)
