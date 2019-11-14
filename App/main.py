from mainwindow import *
from PyQt5.QtWidgets import QApplication
import sys
import os
import memory_pic
import base64


def remove():
    for i in memory_pic.picDict.keys():
        try:
            os.remove(i)
        except:
            pass


def generate():
    for i in memory_pic.picDict.keys():
        image = open(i, 'wb')
        image.write(base64.b64decode(memory_pic.picDict[i]))
        image.close()


if __name__ == '__main__':
    generate()
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("APP.png"))
    app.setApplicationDisplayName("Test")
    MainWindow = Mainwindow()
    MainWindow.show()
    re = app.exec_()
    remove()
    sys.exit(re)
