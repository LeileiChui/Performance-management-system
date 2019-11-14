# -*- coding:utf-8 -*-
__author__ = "liaokong"
__time__ = "2018/10/16 14:16"
__link__ = "https://github.com/liaokongVFX/QFlat/blob/master/MessageWidget.py"

from PySide2 import QtWidgets as PySideQWidgets
from PySide2 import QtCore as PySideQtCore


class Message(PySideQWidgets.QDialog):
    def __init__(self, parent=None):
        super(Message, self).__init__(parent)

        self.setStyle(PySideQWidgets.QStyleFactory.create("plastique"))

        self.main_layout = PySideQWidgets.QVBoxLayout(self)

        self.frame = PySideQWidgets.QFrame()
        self.frame_layout = PySideQWidgets.QHBoxLayout()
        self.frame_layout.setSpacing(25)
        self.frame_layout.setContentsMargins(15, 15, 15, 15)
        self.frame.setLayout(self.frame_layout)

        self.btn = PySideQWidgets.QPushButton("x")
        self.btn.clicked.connect(self.close)

        self.label = PySideQWidgets.QLabel()

        self.frame_layout.addWidget(self.label)
        self.frame_layout.addWidget(self.btn)

        self.main_layout.addWidget(self.frame)

    def info(self, msg):
        self.setStyleSheet("""
                QFrame{
                    color: black;
                    background-color: #7cd1ef;
                    border-radius: 5px;
                }

                QPushButton {
                    border: 0px solid rgba(255, 255, 255, 0);
                    font-size: 18px;
                    font-family: "Microsoft YaHei";
                    color: rgba(255, 255, 255, 255);
                    padding-bottom: 5px;
                }

                QPushButton:pressed {
                    color: #6cbddc;
                }

                QLabel{
                    color: #31708f;
                    font-weight: 700;
                    font-size: 14px;
                    font-family: "Microsoft YaHei";
                }
                """)

        self.label.setText(msg)

    def success(self, msg):
        self.setStyleSheet("""
                QFrame{
                    color: black;
                    background-color: #b9df90;
                    border-radius: 5px;
                }

                QPushButton {
                    border: 0px solid rgba(255, 255, 255, 0);
                    font-size: 17px;
                    font-family: "Microsoft YaHei";
                    color: rgba(255, 255, 255, 255);
                    padding-bottom: 5px;
                }

                QPushButton:pressed {
                    color: #a0c97f;
                }

                QLabel{
                    color: #3c763d;
                    font-weight: 700;
                    font-size: 14px;
                    font-family: "Microsoft YaHei";
                }
                """)

        self.label.setText(msg)

    def warning(self, msg):
        self.setStyleSheet("""
                QFrame{
                    color: black;
                    background-color: #ffdd87;
                    border-radius: 5px;
                }

                QPushButton {
                    border: 0px solid rgba(255, 255, 255, 0);
                    font-size: 18px;
                    font-family: "Microsoft YaHei";
                    color: rgba(255, 255, 255, 255);
                    padding-bottom: 5px;
                }

                QPushButton:pressed {
                    color: #e8c677;
                }

                QLabel{
                    color: #8a6d3b;
                    font-weight: 700;
                    font-size: 14px;
                    font-family: "Microsoft YaHei";
                }
                """)

        self.label.setText(msg)

    def error(self, msg):
        self.setStyleSheet("""
                QFrame{
                    color: black;
                    background-color: #f2838f;
                    border-radius: 5px;
                }

                QPushButton {
                    border: 0px solid rgba(255, 255, 255, 0);
                    font-size: 18px;
                    font-family: "Microsoft YaHei";
                    color: rgba(255, 255, 255, 255);
                    padding-bottom: 5px;
                }

                QPushButton:pressed {
                    color: #c16872;
                }

                QLabel{
                    color: #b44e4f;
                    font-weight: 700;
                    font-size: 14px;
                    font-family: "Microsoft YaHei";
                }
                """)

        self.label.setText(msg)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(QtCore.Qt.OpenHandCursor))

    def mouseMoveEvent(self, event):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(event.globalPos() - self.m_Position)
            event.accept()

    def mouseReleaseEvent(self, event):
        self.m_flag = False
        self.setCursor(QCursor(QtCore.Qt.ArrowCursor))


class MessageAsk(PySideQWidgets.QDialog):
    status = False

    def __init__(self, parent=None):
        super(MessageAsk, self).__init__(parent)

        self.setStyle(PySideQWidgets.QStyleFactory.create("plastique"))

        self.setWindowOpacity(0.98)  # 设置窗口透明度
        self.setAttribute(PySideQtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowFlags(PySideQtCore.Qt.FramelessWindowHint)

        self.main_layout = PySideQWidgets.QVBoxLayout(self)

        self.frame = PySideQWidgets.QFrame()
        self.frame_layout = PySideQWidgets.QVBoxLayout()
        self.frame.setLayout(self.frame_layout)

        # head_layout
        self.head_layout = PySideQWidgets.QHBoxLayout()

        self.label = PySideQWidgets.QLabel()
        self.head_spacer = PySideQWidgets.QSpacerItem(377, 0, PySideQWidgets.QSizePolicy.Expanding,
                                                      PySideQWidgets.QSizePolicy.Minimum)
        self.close_btn = PySideQWidgets.QPushButton("x")
        self.close_btn.setObjectName("close_btn")
        self.close_btn.clicked.connect(self.close)

        self.head_layout.addWidget(self.label)
        self.head_layout.addItem(self.head_spacer)
        self.head_layout.addWidget(self.close_btn)

        # body
        self.body_browser = PySideQWidgets.QTextBrowser()
        self.body_browser.setMaximumHeight(80)
        self.body_browser.setContextMenuPolicy(PySideQtCore.Qt.NoContextMenu)

        # footer_layout
        self.footer_layout = PySideQWidgets.QHBoxLayout()
        self.footer_layout.setContentsMargins(15, 0, 0, 15)

        self.yes_btn = PySideQWidgets.QPushButton(u"确定")
        self.yes_btn.setObjectName("yes_btn")
        self.no_btn = PySideQWidgets.QPushButton(u"取消")
        self.no_btn.setObjectName("no_btn")
        self.yes_btn.clicked.connect(self.return_yes)
        self.no_btn.clicked.connect(self.close)

        self.footer_spacer = PySideQWidgets.QSpacerItem(77, 0, PySideQWidgets.QSizePolicy.Expanding,
                                                        PySideQWidgets.QSizePolicy.Minimum)

        self.footer_layout.addWidget(self.yes_btn)
        self.footer_layout.addWidget(self.no_btn)
        self.footer_layout.addItem(self.footer_spacer)

        self.frame_layout.addLayout(self.head_layout)
        self.frame_layout.addWidget(self.body_browser)
        self.frame_layout.addLayout(self.footer_layout)

        self.main_layout.addWidget(self.frame)

    def return_yes(self):
        self.status = True
        self.close()

    def info(self, msg):
        self.setStyleSheet("""
            QFrame{
                color: black;
                background-color: #7cd1ef;
                border-radius: 8px;
            }
            
            QPushButton#close_btn {
                border: 0px solid rgba(255, 255, 255, 0);
                font-size: 17px;
                font-family: "Microsoft YaHei";
                color: rgba(255, 255, 255, 255);
                padding-right: 15px;
            }

            QPushButton#close_btn:pressed {
                color: #6cbddc;
            }
            
            QLabel{
                color: #31708f;
                font-weight: 800;
                font-size: 22px;
                font-family: "Microsoft YaHei";
                padding-left: 10px;
                padding-top: 6px;
            }
            
            QTextBrowser{
                padding-left: 10px;
                padding-top: 2px;
                font-size: 15px;
                font-family: "Microsoft YaHei";
                color: #235a82;
                font-weight: 500;
            }
            
            QPushButton#yes_btn,#no_btn{
                border: 2px solid #3bafda;
                width: 110px;
                height: 30px;
                border-radius: 4px;
                font-size: 14px;
                font-family: "Microsoft YaHei";
                color: #31709e;
                font-weight: 500;
            }
            
            QPushButton#yes_btn:hover,#no_btn:hover{
                border: 0px solid rgba(255, 255, 255, 0);
                background-color: #3bafda;
                color: #FFFFFF;
                font-weight: 600;
            }
        """)

        self.label.setText(u"提示")
        self.body_browser.setText(u"    " + msg)

    def warning(self, msg):
        self.setStyleSheet("""
                    QFrame{
                        color: black;
                        background-color: #FFF68F;
                        border-radius: 8px;
                    }

                    QPushButton#close_btn {
                        border: 0px solid rgba(255, 255, 255, 0);
                        font-size: 17px;
                        font-family: "Microsoft YaHei";
                        color: rgba(255, 255, 255, 255);
                        padding-right: 15px;
                    }

                    QPushButton#close_btn:pressed {
                        color: #e9c778;
                    }

                    QLabel{
                        color: #282826;
                        font-weight: 800;
                        font-size: 22px;
                        font-family: "Microsoft YaHei";
                        padding-left: 10px;
                        padding-top: 6px;
                    }

                    QTextBrowser{
                        padding-left: 10px;
                        padding-top: 2px;
                        font-size: 14px;
                        font-family: "Microsoft YaHei";
                        color: gray;
                        font-weight: 500;
                    }

                    QPushButton#yes_btn,#no_btn{
                        border: 2px solid #a77c2d;
                        width: 110px;
                        height: 30px;
                        border-radius: 4px;
                        font-size: 15px;
                        font-family: "Microsoft YaHei";
                        color: #8a6d3b;
                        font-weight: 500;
                    }

                    QPushButton#yes_btn:hover,#no_btn:hover{
                        border: 0px solid rgba(255, 255, 255, 0);
                        background-color: #f6bb42;
                        color: #FFFFFF;
                        font-weight: 600;
                    }
                """)

        self.label.setText(u"警告")
        self.body_browser.setText(u"    " + msg)

    def error(self, msg):
        self.setStyleSheet("""
                    QFrame{
                        color: #FA8072;
                        background-color: #f58f98;
                        border-radius: 8px;
                    }

                    QPushButton#close_btn {
                        border: 0px solid rgba(255, 255, 255, 0);
                        font-size: 17px;
                        font-family: "Microsoft YaHei";
                        color: rgba(255, 255, 255, 255);
                        padding-right: 15px;
                    }

                    QPushButton#close_btn:pressed {
                        color: #e9c778;
                    }

                    QLabel{
                        color: black;
                        font-weight: 800;
                        font-size: 22px;
                        font-family: "Microsoft YaHei";
                        padding-left: 10px;
                        padding-top: 6px;
                    }

                    QTextBrowser{
                        padding-left: 10px;
                        padding-top: 2px;
                        font-size: 15px;
                        font-family: "Microsoft YaHei";
                        color: black;
                        font-weight: 500;
                    }

                    QPushButton#yes_btn,#no_btn{
                        border: 2px solid #f05b72;
                        width: 110px;
                        height: 30px;
                        border-radius: 4px;
                        font-size: 14px;
                        font-family: "Microsoft YaHei";
                        color: balck;
                        font-weight: 500;
                    }

                    QPushButton#yes_btn:hover,#no_btn:hover{
                        border: 0px solid rgba(255, 255, 255, 0);
                        background-color: #7bbfea;
                        color: #FFFFFF;
                        font-weight: 600;
                    }
                """)

        self.label.setText(u"错误")
        self.body_browser.setText(u"    " + msg)

    def mousePressEvent(self, event):
        if event.button() == PySideQtCore.Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(PySideQWidgets.QCursor(
                PySideQtCore.Qt.OpenHandCursor))

    def mouseMoveEvent(self, event):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(event.globalPos() - self.m_Position)
            event.accept()

    def mouseReleaseEvent(self, event):
        self.m_flag = False
        self.setCursor(PySideQWidgets.QCursor(QtCore.Qt.ArrowCursor))


def message(msg, msg_type="info"):
    """
    msg_type:['success','info','warning','error']
    """
    m = Message()
    if msg_type == "info":
        m.info(msg)
    elif msg_type == "success":
        m.success(msg)
    elif msg_type == "warning":
        m.warning(msg)
    elif msg_type == "error":
        m.error(msg)
    else:
        raise ValueError

    m.exec_()


def message_ask(msg, msg_type="INFO"):
    """
    msg_type:['info','warning']
    """
    ma = MessageAsk()
    if msg_type == "INFO":
        ma.info(msg)
    elif msg_type == "WARN":
        ma.warning(msg)
    elif msg_type == "ERROR":
        ma.error(msg)
    else:
        raise ValueError

    ma.exec_()

    return ma.status


if __name__ == '__main__':
    app = PySideQWidgets.QApplication()
    message_ask("Test", "ERROR")
    app.exec_()
