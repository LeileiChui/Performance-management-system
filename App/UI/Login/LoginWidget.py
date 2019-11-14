from UI.Login.Login_ui import *
from PyQt5.QtWidgets import QWidget
from client import *
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import *


class LoginWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Login_ui()
        self.ui.setupUi(self)
        self.ui.accept.clicked.connect(self.accept)
        self.ui.reject.clicked.connect(self.reject)
        self.ui.User_ID.setValidator(QRegExpValidator(QRegExp("[A-Z][0-9]{1,}")))

    def reject(self):
        result = message_ask("是否退出客户端")
        if result:
            self.parent().close()

    def accept(self):
        self.ui.accept.setDisabled(True)
        if not self.ui.User_ID.text():
            message_ask("请输入用户名", "WARN")
        elif not self.ui.Password.text():
            message_ask("请输入密码", "WARN")
        else:
            user_id = self.ui.User_ID.text()
            password = self.ui.Password.text()
            user_type = 0
            if self.ui.Student.isChecked():
                user_type = 0
            elif self.ui.Teacher.isChecked():
                user_type = 1
            elif self.ui.Manager.isChecked():
                user_type = 2
            login_info = {"package_type": "login_package", "user_id": user_id,
                          "password": password, "user_type": user_type}
            client = Client()
            replyPack = client.Send(login_info)
            if replyPack["ConnectInfo"]:
                data = replyPack["data"]
                if data["LoginResult"]:
                    print("Login Success")
                    user_name = data["Name"]
                    self.ui.User_ID.clear()
                    self.ui.Password.clear()
                    self.ui.Student.setChecked(True)
                    self.parent().LoginSuccess(self, user_type, user_id, user_name)
                    return
                else:
                    message_ask("用户名或密码错误", "ERROR")
                    self.ui.Password.clear()
                try:
                    self.ui.accept.setEnabled(True)
                except:
                    pass
        self.ui.accept.setEnabled(True)
