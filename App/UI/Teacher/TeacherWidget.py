from UI.Teacher.Teacher_ui import *
from UI.Other.ItemButton import *
from PyQt5.QtWidgets import QWidget, QTableWidget, QHeaderView, QTableWidgetItem, QMenu, QApplication, QAbstractItemView
from PyQt5.QtGui import QBrush, QColor, QGradient
from PyQt5.QtCore import Qt, QSize
from client import *
import json
from UI.Other.editDelegate import *
from UI.Other.input_class import *
from UI.Other.input_score import *


class TeacherWidget(QWidget):
    def __init__(self, UserName, UserID):
        super().__init__()
        self.UserID = UserID
        self.UserName = UserName
        self.ClassInfo = []
        self.classID = 0
        self.ScoreInfo = []
        self.changedClassInfo = []
        self.changedScoreInfo = []
        self.ui = Teacher_ui()
        self.ui.setupUi(self)
        self.ui.setName(self.UserName)
        self.showclass()
        self.ui.exitButton.clicked.connect(self.Logout)
        self.ui.MyClasses.clicked.connect(self.showclass)
        self.ui.MyStudents.clicked.connect(self.allinOne)
        self.ui.classtable.itemChanged.connect(self.classRename)
        self.ui.scoretable.itemChanged.connect(self.reScore)
        self.ui.Save.clicked.connect(self.Save)
        self.ui.newClass.clicked.connect(self.newClass)
        self.ui.newStudent.clicked.connect(self.newScore)
        self.ui.classtable.customContextMenuRequested.connect(self.deleteClass)
        self.ui.scoretable.customContextMenuRequested.connect(self.deleteScoreInfo)

    def Logout(self):
        result = message_ask("是否退出登陆", "WARN")
        if result:
            self.parent().Logout(self)

    def getMyClassesInfo(self):
        package = {}
        package["package_type"] = "getClassesInfo"
        package["UserID"] = self.UserID
        client = Client()
        relpyPack = client.Send(package)
        if relpyPack["ConnectInfo"]:
            self.ClassInfo = relpyPack["data"]
        else:
            return

    def showclass(self):
        if len(self.changedClassInfo) != 0 or len(self.changedScoreInfo) != 0:
            result = message_ask("您有未保存的数据，是否刷新？", "WARN")
            if not result:
                return
        self.ui.scoretable.hide()
        self.ui.AllinOnetable.hide()
        self.ui.classtable.show()
        self.ui.classtable.clear()
        self.ui.scoretable.clear()
        self.ui.AllinOnetable.clear()
        self.ui.newStudent.hide()
        self.ui.newClass.show()
        self.getMyClassesInfo()
        self.ui.newClass.show()
        table = self.ui.classtable
        table.setColumnCount(3)
        table.setRowCount(len(self.ClassInfo))
        table.setHorizontalHeaderLabels(['课程ID', '课程名', '选课人数'])
        table.verticalHeader().setVisible(False)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setItemDelegateForColumn(0, EmptyDelegate(table))
        table.setItemDelegateForColumn(2, EmptyDelegate(table))
        for i in range(len(self.ClassInfo)):
            table.setRowHeight(i, 40)
            for j in range(len(self.ClassInfo[i])):
                if j != 2:
                    Item = QTableWidgetItem(str(self.ClassInfo[i][j]))
                    Item.setTextAlignment(Qt.AlignCenter)
                    table.setItem(i, j, Item)
                else:
                    button = ItemButton(self.oneClassScoreInfo, self.ClassInfo[i][0])
                    button.setText(str(self.ClassInfo[i][j]))
                    button.setStyleSheet("color:rgb(0,0,255);"
                                         "background-color:transparent;")
                    table.setCellWidget(i, j, button)

        self.changedClassInfo.clear()
        self.ui.Save.hide()

    def classRename(self):
        item = self.ui.classtable.currentItem()
        try:
            item.setText(item.text().strip())
        except:
            return
        if item.text() != str(self.ClassInfo[item.row()][item.column()]):
            item.setBackground(QColor(255, 255, 0))
            for i in self.changedClassInfo:
                if i.row() == item.row() and i.column() == item.column():
                    self.changedClassInfo.remove(i)
            self.changedClassInfo.append(item)
            if len(self.changedClassInfo) == 1:
                self.ui.Save.show()
        else:
            try:
                self.changedClassInfo.remove(item)
            except:
                pass
            item.setBackground(QColor(255, 255, 255))
            if len(self.changedClassInfo) == 0:
                self.ui.Save.hide()

    def SaveRename(self):
        data = []
        package = {}
        table = self.ui.classtable
        for item in self.changedClassInfo:
            data.append([table.item(item.row(), item.column() - 1).text(), item.text()])
            self.ClassInfo[item.row()][item.column()] = item.text()
            item.setBackground(QColor(0, 255, 0))

        self.changedClassInfo.clear()
        self.ui.Save.hide()

        package["package_type"] = "save_class_info"
        package["data"] = data
        client = Client()
        replyPac = client.Send(package)
        if replyPac["ConnectInfo"]:
            data = replyPac["data"]
            if data["Result"] == "Success":
                message_ask("保存成功", "INFO")
            else:
                message_ask("保存失败", "ERROR")

    def Save(self):
        if not self.ui.classtable.isHidden():
            self.SaveRename()
            self.showclass()
        if not self.ui.scoretable.isHidden():
            self.SaveScore()
            self.oneClassScoreInfo(self.classID)

    def newClass(self):
        dialog = input_className()
        ClassName = ""
        result = dialog.exec_()
        if result != 1:
            return
        ClassName = dialog.ui.lineEdit.text().strip()
        for i in self.ClassInfo:
            if i[1] == ClassName:
                message_ask("已存在该课程", "WARN")
                return
        package = {}
        package["package_type"] = "newClass"
        package["data"] = [self.UserID, ClassName]
        client = Client()
        replyPac = client.Send(package)
        if replyPac["ConnectInfo"]:
            data = replyPac["data"]
            if data["Result"] == "Success":
                message_ask("保存成功", "INFO")
            else:
                message_ask("保存失败", "ERROR")
            self.showclass()

    def deleteClass(self, pos):
        row_num = -1
        info = []
        package = {}
        for i in self.ui.classtable.selectionModel().selection().indexes():
            row_num = i.row()

        if row_num < len(self.ClassInfo) and row_num != -1:
            menu = QMenu()
            item1 = menu.addAction("删除课程")
            action = menu.exec_(self.ui.classtable.mapToGlobal(pos))
            if action == item1:
                result = message_ask("是否删除课程： " + self.ClassInfo[row_num][1] + "？", "WARN")
                if result:
                    package["package_type"] = "deleteClass"
                    package["data"] = self.ClassInfo.pop(row_num)
                    client = Client()
                    replyPac = client.Send(package)
                    if replyPac["ConnectInfo"]:
                        data = replyPac["data"]
                        if data["Result"] == "Success":
                            message_ask("删除成功", "INFO")
                        else:
                            message_ask("删除失败", "ERROR")
                        self.showclass()

    def oneClassScoreInfo(self, ClassID):
        if len(self.changedClassInfo) != 0 or len(self.changedScoreInfo) != 0:
            result = message_ask("您有未保存的数据，是否刷新？", "WARN")
            if not result:
                return
        self.ui.classtable.hide()
        self.ui.AllinOnetable.hide()
        self.ui.scoretable.show()
        self.ui.scoretable.clear()
        self.ui.classtable.clear()
        self.ui.AllinOnetable.clear()
        self.changedClassInfo.clear()
        self.changedScoreInfo.clear()

        self.getScoreInfo(ClassID)
        self.classID = ClassID
        table = self.ui.scoretable
        self.ui.newClass.hide()
        self.ui.newStudent.show()
        table.setColumnCount(4)
        table.setRowCount(len(self.ScoreInfo))
        table.setHorizontalHeaderLabels(['课程', '学号', '姓名', '分数'])
        table.verticalHeader().setVisible(False)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setItemDelegateForColumn(0, EmptyDelegate(table))
        table.setItemDelegateForColumn(1, EmptyDelegate(table))
        table.setItemDelegateForColumn(2, EmptyDelegate(table))
        table.setItemDelegateForColumn(3, intOnlyDelegate(table))
        for i in range(len(self.ScoreInfo)):
            table.setRowHeight(i, 40)
            for j in range(len(self.ScoreInfo[i])):
                Item = QTableWidgetItem(str(self.ScoreInfo[i][j]))
                Item.setTextAlignment(Qt.AlignCenter)
                table.setItem(i, j, Item)

        self.changedScoreInfo.clear()

    def getScoreInfo(self, ClassID):
        package = {}
        package["package_type"] = "getScoreInfo"
        package["ClassID"] = ClassID
        client = Client()
        replyPac = client.Send(package)
        if replyPac["ConnectInfo"]:
            self.ScoreInfo = replyPac["data"]

    def reScore(self):
        item = self.ui.scoretable.currentItem()
        try:
            item.setText(str(int(item.text())))
        except:
            return
        if item.text() != str(self.ScoreInfo[item.row()][item.column()]):
            item.setBackground(QColor(255, 255, 0))
            for i in self.changedScoreInfo:
                if i.row() == item.row() and i.column() == item.column():
                    self.changedScoreInfo.remove(i)
            self.changedScoreInfo.append(item)
            if len(self.changedScoreInfo) == 1:
                self.ui.Save.show()
        else:
            try:
                self.changedScoreInfo.remove(item)
            except:
                pass
            item.setBackground(QColor(255, 255, 255))
            if len(self.changedScoreInfo) == 0:
                self.ui.Save.hide()

    def SaveScore(self):
        data = []
        package = {}
        table = self.ui.scoretable
        for item in self.changedScoreInfo:
            data.append([item.text(), self.classID, table.item(item.row(), item.column() - 2).text()])
            item.setBackground(QColor(255, 255, 255))
            self.ScoreInfo[item.row()][item.column()] = int(item.text())

        self.changedScoreInfo.clear()
        self.ui.Save.hide()

        package["package_type"] = "save_score_info"
        package["data"] = data
        client = Client()
        replyPac = client.Send(package)
        if replyPac["ConnectInfo"]:
            data = replyPac["data"]
            if data["Result"] == "Success":
                message_ask("保存成功", "INFO")
            else:
                message_ask("保存失败", "ERROR")
                self.oneClassScoreInfo(self.classID)

    def deleteScoreInfo(self, pos):
        row_num = -1
        info = []
        package = {}
        for i in self.ui.scoretable.selectionModel().selection().indexes():
            row_num = i.row()

        if row_num < len(self.ScoreInfo) and row_num != -1:
            menu = QMenu()
            item1 = menu.addAction(u"删除成绩")
            action = menu.exec_(self.ui.classtable.mapToGlobal(pos))
            if action == item1:

                result = message_ask("是否删除 " + self.ScoreInfo[row_num][2] + " 的成绩？", "WARN")
                if result:
                    info = self.ScoreInfo.pop(row_num)
                    package["package_type"] = "deleteScore"
                    package["data"] = [self.classID, info[1]]
                    client = Client()
                    replyPac = client.Send(package)
                    if replyPac["ConnectInfo"]:
                        data = replyPac["data"]
                        if data["Result"] == "Success":
                            message_ask("删除成功", "INFO")
                        else:
                            message_ask("删除失败", "ERROR")
                        self.oneClassScoreInfo(self.classID)

    def newScore(self):
        dialog = input_score()
        result = dialog.exec_()
        if result != 1:
            return
        student_id = dialog.ui.lineEdit.text()
        score = int(dialog.ui.score.text())
        for i in self.ScoreInfo:
            if i[1] == student_id:
                message_ask("已存在该生", "ERROR")
                return
        package = {}
        package["package_type"] = "newScore"
        package["data"] = [self.classID, student_id, score]
        client = Client()
        replyPac = client.Send(package)
        if replyPac["ConnectInfo"]:
            data = replyPac["data"]
            if data["Result"] == "Success":
                message_ask("保存成功")
            elif data["Result"] == "Warnning":
                message_ask("该生未创建账号，已自动创建", "WARN")
            else:
                message_ask("保存失败", "ERROR")
            self.oneClassScoreInfo(self.classID)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_S:
            if QApplication.keyboardModifiers() == Qt.ControlModifier:
                if not self.ui.Save.isHidden():
                    self.Save()

    def allinOne(self):
        if len(self.changedClassInfo) != 0 or len(self.changedScoreInfo) != 0:
            result = message_ask("您有未保存的数据，是否刷新？", "WARN")
            if not result:
                return
        self.ui.classtable.hide()
        self.ui.scoretable.hide()
        self.ui.AllinOnetable.show()
        self.ui.classtable.clear()
        self.ui.scoretable.clear()
        self.ui.AllinOnetable.clear()
        self.ui.newStudent.hide()
        if not self.ui.newClass.isHidden():
            self.ui.newClass.hide()
            self.resize(self.size() + QSize(1, 1))
        allInfo = self.getAllInfo()
        table = self.ui.AllinOnetable
        table.setRowCount(len(allInfo))
        table.setColumnCount(4)
        table.setHorizontalHeaderLabels(['学号', '姓名', '课程', '分数'])
        table.verticalHeader().setVisible(False)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for i in range(len(allInfo)):
            table.setRowHeight(i, 40)
            for j in range(0, 4):
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
            table.setSpan(nums1[i], 1, nums2[i], 1)

    def getAllInfo(self):
        package = {}
        package["package_type"] = "getAllInfo"
        package["UserID"] = self.UserID
        client = Client()
        replyPac = client.Send(package)
        if replyPac["ConnectInfo"]:
            return replyPac["data"]
        else:
            return []
