from socket import *
from threading import Thread
from Login import *
from Logic.Teacher.saveClassesInfo import *
from Logic.Teacher.getClassesInfo import *
from Logic.Teacher.newClass import *
from Logic.Teacher.deleteClass import *
from Logic.Teacher.deleteScore import *
from Logic.Teacher.getScoreInfo import *
from Logic.Teacher.saveScoreInfo import *
from Logic.Teacher.newScore import *
from Logic.Teacher.getAllInfo import *
from Logic.Student.GetScoreInfo import *
from Logic.Manager.ManGetTeaInfo import *
from Logic.Manager.ManGetStuInfo import *
from Logic.Manager.MangetOneClassInfo import *
from Logic.Manager.ManSaveInfo import *
import time
import json

BUFFSIZE = 1024


def time_str():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


class Server:
    def __init__(self, HOST, PORT):
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.HOST = HOST
        self.PORT = PORT
        self.ADDR = (HOST, PORT)
        self.ConnectPool = []
        try:
            self.server_socket.bind(self.ADDR)
        except OSError:
            print("端口冲突，服务器启动失败")
            exit(1)
        self.server_socket.listen(5)
        print(time_str(), self.ADDR, "服务器已启动")

    def start(self):
        self.accept_client()

    def accept_client(self):
        while True:
            if len(self.ConnectPool) == 10:
                continue
            client_socket, addr = self.server_socket.accept()
            self.ConnectPool.append(client_socket)
            print(time_str(), addr, "已连接")
            # print(client)
            msg_handle_thread = Thread(target=self.msg_handle, args=(client_socket,))
            msg_handle_thread.setDaemon(True)
            msg_handle_thread.start()

    def msg_handle(self, client_socket):
        reply_str = ""
        try:
            recv_str = client_socket.recv(BUFFSIZE).decode("utf8")
        except:
            self.ConnectPool.remove(client_socket)
            client_socket.close()
            return
        package = json.loads(recv_str)

        if package["package_type"] == "login_package":
            print(time_str(), "login_package")
            reply_str = Login(package)

        elif package["package_type"] == "getClassesInfo":
            print(time_str(), "getClassesInfo")
            reply_str = getClassesInfo(package["UserID"])

        elif package["package_type"] == "save_class_info":
            print(time_str(), "save_class_info")
            reply_str = saveClassesInfo(package["data"])

        elif package["package_type"] == "newClass":
            print(time_str(), "newClass")
            reply_str = newClass(package["data"])

        elif package["package_type"] == "deleteClass":
            print(time_str(), "deleteClass")
            reply_str = deleteClass(package["data"])

        elif package["package_type"] == "getScoreInfo":
            print(time_str(), "getScoreInfo")
            reply_str = getScoreInfo(package["ClassID"])

        elif package["package_type"] == "save_score_info":
            print(time_str(), "save_score_info")
            reply_str = saveScoreInfo(package["data"])

        elif package["package_type"] == "deleteScore":
            print(time_str(), "deleteScore")
            reply_str = deleteScore(package["data"])

        elif package["package_type"] == "newScore":
            print(time_str(), "newScore")
            reply_str = newScore(package["data"])

        elif package["package_type"] == "getAllInfo":
            print(time_str(), "getAllInfo")
            reply_str = getAllInfo(package["UserID"])

        elif package["package_type"] == "StuGetScoreInfo":
            print(time_str(), "StuGetScore")
            reply_str = StuGetScoreInfo(package["UserID"])

        elif package["package_type"] == "getallTeacherInfo":
            print(time_str(), "getallTeacherInfo")
            reply_str = ManGetTeaInfo()

        elif package["package_type"] == "getallStudentInfo":
            print(time_str(), "getallStudentInfo")
            reply_str = ManGetStuInfo()

        elif package["package_type"] == "MangetScoreInfo":
            print(time_str(), "MangetScoreInfo")
            reply_str = MangetOneClassInfo(package["ClassID"])

        elif package["package_type"] == "ManSaveInfo":
            print(time_str(), "ManSaveInfo")
            reply_str = ManSaveInfo(package["data"][0])

        else:
            print("Other")
        client_socket.send(reply_str.encode("utf8"))
        self.ConnectPool.remove(client_socket)
        client_socket.close()
