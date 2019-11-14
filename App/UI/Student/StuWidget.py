from UI.Student.Student_ui import *
from PyQt5.QtWidgets import QWidget, QHeaderView, QTableWidgetItem
from PyQt5.QtCore import Qt
from client import *
import json


class StuWidget(QWidget):
    def __init__(self, UserName, UserID):
        super().__init__()
        self.ui = Student_ui()
        self.ui.setupUi(self)
        self.UserName = UserName
        self.UserID = UserID
        self.ui.setName(self.UserName)
        self.ui.exitButton.clicked.connect(self.Logout)

        self.ScoreInfo = []
        self.ShowScore()

    def Logout(self):
        result = message_ask("确认退出？", "WARN")
        if result:
            self.parent().Logout(self)

    def ShowScore(self):
        self.getScoreInfo()
        table = self.ui.table
        table.setRowCount(len(self.ScoreInfo))
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(['教师', '课程', '分数'])
        table.verticalHeader().setVisible(False)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        allInfo = self.ScoreInfo
        for i in range(len(allInfo)):
            table.setRowHeight(i, 40)
            for j in range(len(allInfo[0])):
                Item = QTableWidgetItem(str(allInfo[i][j]))
                Item.setTextAlignment(Qt.AlignCenter)
                table.setItem(i, j, Item)

        nums2 = []
        k = 1
        try:
            lastLine = allInfo.pop(0)
        except:
            return
        while True:
            try:
                line = allInfo.pop(0)
                if line[0] == lastLine[0]:
                    k += 1
                else:
                    nums2.append(k)
                    lastLine = line
                    k = 1
            except:
                nums2.append(k)
                break
        k = 0
        nums1 = [k]
        for i in nums2:
            k += i
            nums1.append(k)
        for i in range(len(nums2)):
            if nums2[i] == 1:
                continue
            table.setSpan(nums1[i], 0, nums2[i], 1)

    def getScoreInfo(self):
        package = {}
        package["package_type"] = "StuGetScoreInfo"
        package["UserID"] = self.UserID
        client = Client()
        replyPac = client.Send(package)
        if replyPac["ConnectInfo"]:
            self.ScoreInfo = replyPac["data"]
