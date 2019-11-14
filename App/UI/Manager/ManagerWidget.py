from UI.Manager.Manager_ui import *
from UI.Other.ItemButton import *
from PyQt5.QtWidgets import QWidget, QTableWidget, QHeaderView, QTableWidgetItem, QMenu, QApplication, QAbstractItemView
from PyQt5.QtGui import QBrush, QColor, QGradient
from PyQt5.QtCore import Qt, QSize
from PyQt5.Qt import *
from client import *
import json
import sip
import copy


class ManagerWidget(QWidget):
    def __init__(self, UserName, UserID):
        super().__init__()
        self.UserID = UserID
        self.UserName = UserName
        self.ClassID = None
        self.ui = Manager_ui()
        self.ui.setupUi(self)
        self.ui.setName(self.UserName)
        self.InfoTable = None
        self.ui.exitButton.clicked.connect(self.Logout)
        self.ui.TeacherBtn.clicked.connect(lambda: self.showInfo(data={"Mood": "allTeacher"}))
        self.ui.StudentBtn.clicked.connect(lambda: self.showInfo(data={"Mood": "allStudent"}))
        self.ui.Save.clicked.connect(self.save)
        self.ChangedInfo = {
            "StudentNameChangeInfo": [{}],
            "StudentIDChangeInfo": [{}],
            "ScoreChangeInfo": [{}],
            "TeacherNameChangeInfo": [{}],
            "TeacherIDChangeInfo": [{}],
            "ClassNameChangeInfo": [{}],
            "ClassIDChangeInfo": [{}]
        }
        self.showInfo(data={"Mood": "allTeacher"})

    def Logout(self):
        unSavedInfoItem = 0
        for i in self.ChangedInfo.values():
            unSavedInfoItem += len(i[0])
        if unSavedInfoItem:
            info = "您有 " + str(unSavedInfoItem) + " 条数据未保存，退出登陆将不会被保存"
        else:
            info = "是否退出登陆?"
        result = message_ask(info, "WARN")
        if result:
            self.parent().Logout(self)

    @staticmethod
    def getallTeacherInfo():
        package = {"package_type": "getallTeacherInfo"}
        client = Client()
        replyPac = client.Send(package)
        if replyPac["ConnectInfo"]:
            return replyPac["data"]
        else:
            return []

    @staticmethod
    def getallStudentInfo():
        package = {"package_type": "getallStudentInfo"}
        client = Client()
        replyPac = client.Send(package)
        if replyPac["ConnectInfo"]:
            return replyPac["data"]
        else:
            return []

    @staticmethod
    def getOneClassInfo(ClassID):
        package = {}
        package["package_type"] = "MangetScoreInfo"
        package["ClassID"] = ClassID
        client = Client()
        relpyPack = client.Send(package)
        if relpyPack["ConnectInfo"]:
            return relpyPack["data"]
        else:
            return []

    # reload
    def reloadSaveBtn(self):
        re = False
        for i in self.ChangedInfo.values():
            if len(i[0]):
                re = True
                break
        if re:
            self.ui.Save.show()
        else:
            self.ui.Save.hide()

    def save(self):
        conflict = 0
        for i in self.ChangedInfo["StudentIDChangeInfo"][0].keys():
            old_id = i
            new_id = self.ChangedInfo["StudentIDChangeInfo"][0][old_id]
            time = 0
            for row in self.studentInfo:
                if new_id == row[0]:
                    time += 1
            conflict += time

        for i in self.ChangedInfo["TeacherIDChangeInfo"][0].keys():
            old_id = i
            new_id = self.ChangedInfo["TeacherIDChangeInfo"][0][old_id]
            time = 0
            for row in self.teacherInfo:
                if new_id == row[1]:
                    time += 1
            conflict += time

        for i in self.ChangedInfo["ClassIDChangeInfo"][0].keys():
            old_id = i
            new_id = self.ChangedInfo["ClassIDChangeInfo"][0][old_id]
            time = 0
            for row in self.teacherInfo:
                if new_id == row[3]:
                    time += 1
            conflict += time
        if conflict:
            message_ask("有 " + str(conflict) + " 条新信息与其他信息产生冲突，请更正后再保存", "ERROR")
            return

        package = {}
        package["package_type"] = "ManSaveInfo"
        package["data"] = []
        package["data"].append(self.ChangedInfo)
        client = Client()
        relpyPack = client.Send(package)
        if not relpyPack["ConnectInfo"]:
            return
        if relpyPack["data"]["Result"] == "Success":
            message_ask("保存成功")
            for i in self.ChangedInfo.values():
                i[0].clear()
            self.ui.Save.hide()
        else:
            errortime = relpyPack["data"]["errorTime"]
            message_ask(str(errortime) + "条信息保存失败", "ERROR")

        self.showInfo({"Mood": self.tableMood, "ClassID": self.ClassID})

    # if Item changed, this func will be triggered twice
    def Changed(self):
        Infodict = {}
        key = ""
        IDdict = {}
        Item = self.InfoTable.currentItem()
        if not Item:
            return

        i = Item.row()
        j = Item.column()
        Item.setText(Item.text().strip())

        haschanged = True
        # Changed StudentName
        if self.tableMood == "allStudent" and j == 0:
            Infodict = self.ChangedInfo["StudentNameChangeInfo"][0]
            key = self.studentInfo[i][1]
        if self.tableMood == "oneClass" and j == 2:
            Infodict = self.ChangedInfo["StudentNameChangeInfo"][0]
            key = self.studentInfo[i][1]
        # student ID
        if self.tableMood == "allStudent" and j == 1:
            Infodict = self.ChangedInfo["StudentIDChangeInfo"][0]
            key = self.studentInfo[i][1]
        if self.tableMood == "oneClass" and j == 1:
            Infodict = self.ChangedInfo["StudentIDChangeInfo"][0]
            key = self.oneClassInfo[i][1]
        # score
        if self.tableMood == "allStudent" and j == 4:
            Infodict = self.ChangedInfo["ScoreChangeInfo"][0]
            key = self.oneClassInfo[i][5]
        if self.tableMood == "oneClass" and j == 3:
            Infodict = self.ChangedInfo["ScoreChangeInfo"][0]
            key = self.oneClassInfo[i][4]
        # Teacher Name
        if self.tableMood == "allTeacher" and j == 0:
            Infodict = self.ChangedInfo["TeacherNameChangeInfo"][0]
            key = self.teacherInfo[i][1]
        if self.tableMood == "allStudent" and j == 3:
            Infodict = self.ChangedInfo["TeacherNameChangeInfo"][0]
            key = self.studentInfo[i][7]
        # Teacher ID
        if self.tableMood == "allTeacher" and j == 1:
            Infodict = self.ChangedInfo["TeacherIDChangeInfo"][0]
            key = self.teacherInfo[i][1]

        # class name
        if self.tableMood == "allTeacher" and j == 2:
            Infodict = self.ChangedInfo["ClassNameChangeInfo"][0]
            key = self.teacherInfo[i][3]
        if self.tableMood == "oneClass" and j == 0:
            Infodict = self.ChangedInfo["ClassNameChangeInfo"][0]
            key = self.oneClassInfo[i][5]
        # class ID
        if self.tableMood == "allTeacher" and j == 3:
            Infodict = self.ChangedInfo["StudentIDChangeInfo"][0]
            key = self.teacherInfo[i][3]

        if self.tableMood == "allStudent":
            realvalue = self.studentInfo[i][j]
        elif self.tableMood == "allTeacher":
            realvalue = self.teacherInfo[i][j]
        elif self.tableMood == "oneClass":
            realvalue = self.oneClassInfo[i][j]

        if Item.text() != realvalue:
            Infodict[key] = Item.text()
            Item.setBackground(QColor(255, 255, 0))
        else:
            Item.setBackground(QColor(255, 255, 255))
            try:
                Infodict.pop(key)
            except:
                pass

        if self.tableMood == "allStudent" and j == 3:
            teacher_id = self.studentInfo[i][7]
            for i in range(len(self.studentInfo)):
                if self.studentInfo[i][7] == teacher_id:
                    self.InfoTable.item(i, 3).setText(Item.text())
                    if haschanged:
                        self.InfoTable.item(i, 3).setBackground(QColor(255, 255, 0))
                    else:
                        self.InfoTable.item(i, 3).setBackground(QColor(255, 255, 255))

        self.reloadSaveBtn()

    def showInfo(self, data):
        Mood = data["Mood"]
        self.tableMood = Mood
        allInfo = []
        if Mood == "allStudent":
            self.studentInfo = self.getallStudentInfo()
            allInfo = self.studentInfo
        elif Mood == "allTeacher":
            self.teacherInfo = self.getallTeacherInfo()
            allInfo = self.teacherInfo
        elif Mood == "oneClass":
            ClassID = data["ClassID"]
            self.ClassID = ClassID
            self.oneClassInfo = self.getOneClassInfo(ClassID)
            allInfo = self.oneClassInfo

        if self.InfoTable:
            sip.delete(self.InfoTable)

        self.InfoTable = QtWidgets.QTableWidget(self.ui.mainWidget)
        self.ui.gridLayout_2.addWidget(self.InfoTable, 0, 1, 2, 1)

        table = self.InfoTable
        table.itemChanged.connect(self.Changed)
        table.setObjectName(Mood + "Info")
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.verticalHeader().setVisible(False)
        table.setRowCount(len(allInfo))
        if Mood == "allStudent":
            table.setColumnCount(5)
            table.setHorizontalHeaderLabels(['姓名', '学号', '课程名称', '授课教师', '成绩'])

        elif Mood == "allTeacher":
            table.setColumnCount(5)
            table.setHorizontalHeaderLabels(['姓名', '教师编号', '课程名称', '课程ID', '选课人数'])

        elif Mood == "oneClass":
            table.setColumnCount(4)
            table.setHorizontalHeaderLabels(['课程名称', '学号', '姓名', '分数'])

        for i in range(len(allInfo)):
            table.setRowHeight(i, 40)
            for j in range(len(allInfo[0])):
                # basic item info set
                Item = QTableWidgetItem(str(allInfo[i][j]))
                Item.setTextAlignment(Qt.AlignCenter)
                if not allInfo[i][j]:
                    Item.setFlags(Qt.NoItemFlags)
                table.setItem(i, j, Item)
                # clean and reset
                if j == 4 and Mood == "allTeacher" and allInfo[i][j]:
                    table.setItem(i, j, None)
                    button = ItemButton(self.showInfo, data={"Mood": "oneClass", "ClassID": allInfo[i][3]})
                    button.setText(str(allInfo[i][j]))
                    button.setStyleSheet("color:rgb(0,0,255);"
                                         "background-color:transparent;")
                    table.setCellWidget(i, j, button)

                if j == 2 and Mood == "allStudent" and allInfo[i][j]:
                    table.setItem(i, j, None)
                    button = ItemButton(self.showInfo, data={"Mood": "oneClass", "ClassID": allInfo[i][5]})
                    button.setText(allInfo[i][j])

                    if allInfo[i][5] in self.ChangedInfo["ClassNameChangeInfo"][0].keys():
                        button.setText(self.ChangedInfo["ClassNameChangeInfo"][0][allInfo[i][5]])
                        button.setStyleSheet("color:rgb(0,0,255);"
                                             "background-color:rgb(255,255,0);")
                    else:
                        button.setStyleSheet("color:rgb(0,0,255);"
                                             "background-color:transparent;")
                    table.setCellWidget(i, j, button)

        # Colour
        for i in range(len(allInfo)):
            for j in range(len(allInfo[0])):
                Infodict = {}
                key = ""
                Item = table.item(i, j)
                if Mood == "allStudent":
                    student_id = allInfo[i][1]
                    class_id = allInfo[i][5]
                    score_id = allInfo[i][6]
                    teacher_id = allInfo[i][7]
                    # student name
                    if j == 0:
                        Infodict = self.ChangedInfo["StudentNameChangeInfo"][0]
                        key = student_id
                    # student ID
                    if j == 1:
                        Infodict = self.ChangedInfo["StudentIDChangeInfo"][0]
                        key = student_id
                    # Class Name noneed to reset
                    # teacher name
                    if j == 3:
                        Infodict = self.ChangedInfo["TeacherNameChangeInfo"][0]
                        key = teacher_id
                    # Score
                    if j == 4:
                        Infodict = self.ChangedInfo["ScoreChangeInfo"][0]
                        key = score_id

                if Mood == "oneClass":
                    student_id = allInfo[i][1]
                    class_id = ClassID
                    score_id = allInfo[i][4]
                    # class name
                    if j == 0:
                        Infodict = self.ChangedInfo["ClassNameChangeInfo"][0]
                        key = class_id
                    # student id
                    if j == 1:
                        Infodict = self.ChangedInfo["StudentIDChangeInfo"][0]
                        key = student_id
                    # student name
                    if j == 2:
                        Infodict = self.ChangedInfo["StudentNameChangeInfo"][0]
                        key = student_id
                    # score
                    if j == 3:
                        Infodict = self.ChangedInfo["ScoreChangeInfo"][0]
                        key = score_id
                if Mood == "allTeacher":
                    # teacherName
                    if j == 0:
                        Infodict = self.ChangedInfo["TeacherNameChangeInfo"][0]
                        key = allInfo[i][1]
                    # teacher ID
                    if j == 1:
                        Infodict = self.ChangedInfo["TeacherIDChangeInfo"][0]
                        key = allInfo[i][1]
                    # class name
                    if j == 2:
                        Infodict = self.ChangedInfo["ClassNameChangeInfo"][0]
                        key = allInfo[i][3]
                    # class ID
                    if j == 3:
                        Infodict = self.ChangedInfo["ClassIDChangeInfo"][0]
                        key = allInfo[i][3]

                if Infodict.keys().__contains__(key):
                    Item.setBackground(QColor(255, 255, 0))
                    Item.setText(Infodict[key])

        # show save btn

        # merge cell
        # mast use deepcopy
        temp = copy.deepcopy(allInfo)
        nums2 = []
        k = 1
        try:
            lastLine = temp.pop(0)
        except:
            return
        while True:
            try:
                line = temp.pop(0)
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
            if Mood == "oneClass":
                continue
            table.setSpan(nums1[i], 1, nums2[i], 1)
        table.update()
