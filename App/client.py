import json
from socket import *
from threading import Thread
import time
from UI.Other.Message import *

BUFFSIZE = 1024
ServerADDR = ("127.0.0.1", 1024)


class Client:
    def __init__(self):
        self.client_socket = socket(AF_INET, SOCK_STREAM)

    def Send(self, package):
        replyPac = {}
        try:
            self.client_socket.connect(ServerADDR)
        except ConnectionRefusedError:
            replyPac["ConnectInfo"] = False
            message_ask("服务器连接失败", "ERROR")
            return replyPac
        replyPac["ConnectInfo"] = True
        self.client_socket.send(json.dumps(package).encode("utf8"))
        replyPac["data"] = self.Recv()
        return replyPac

    def Recv(self):
        recv_str = ""
        time_now = time.time()
        while time.time() - time_now < 1:
            try:
                data = self.client_socket.recv(BUFFSIZE)
            except:
                message_ask("服务器连接失败", "ERROR")
                return
            if data:
                recv_str += data.decode("utf8")
            else:
                break
        self.client_socket.close()
        return json.loads(recv_str)
