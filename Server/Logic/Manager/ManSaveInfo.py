import pymysql
import json
import copy


def ManSaveInfo(data):
    print(data)
    leftdata = copy.deepcopy(data)
    reply = {}
    errorTime = 0
    conn = pymysql.connect(user='root', password='', database='App', charset='utf8')
    cursor = conn.cursor()

    # save student name
    query = ('UPDATE APP.Student SET Student.Stu_Name = %s WHERE Stu_ID = %s')
    info = data["StudentNameChangeInfo"][0]
    for student_id in info.keys():
        try:
            cursor.execute(query, (info[student_id], student_id))
            leftdata["StudentNameChangeInfo"][0].pop(student_id)
        except:
            errorTime += 1

    # save teacher name
    query = ('UPDATE APP.Teacher SET Teacher_Name = %s WHERE Teacher_ID = %s')
    info = data["TeacherNameChangeInfo"][0]
    for teacher_id in info.keys():
        try:
            cursor.execute(query, (info[teacher_id], teacher_id))
            leftdata["TeacherNameChangeInfo"][0].pop(teacher_id)
        except:
            errorTime += 1

    # save class name
    query = ('UPDATE APP.Classes SET ClassName = %s WHERE ClassID = %s')
    info = data["ClassNameChangeInfo"][0]
    for class_id in info.keys():
        try:
            cursor.execute(query, (info[class_id], class_id))
            leftdata["ClassNameChangeInfo"][0].pop(class_id)
        except:
            errorTime += 1

    # save score info
    query = ('UPDATE APP.Score SET Score = %s WHERE Student_ID = %s and ClassID = %s')
    info = data["ScoreChangeInfo"][0]
    # score_id is student_id + " " + class_id
    for score_id in info.keys():
        try:
            cursor.execute(query, (info[score_id], str.split(score_id)[0], str.split(score_id)[1]))
            leftdata["ScoreChangeInfo"][0].pop(score_id)
        except:
            errorTime += 1

    # save student id
    query = ('UPDATE APP.Student SET Student.Stu_ID = %s WHERE Stu_ID = %s')
    info = data["StudentIDChangeInfo"][0]
    for student_id in info.keys():
        try:
            cursor.execute(query, (info[student_id], student_id))
        except:
            pass
    query = ('UPDATE APP.Score SET Student_ID = %s WHERE Student_ID = %s')
    for student_id in info.keys():
        try:
            cursor.execute(query, (info[student_id], student_id))
            leftdata["StudentIDChangeInfo"][0].pop(student_id)
        except:
            errorTime += 1

    # save teacher id
    query = ('UPDATE APP.Teacher SET Teacher_ID = %s WHERE Teacher_ID = %s')
    info = data["TeacherIDChangeInfo"][0]
    for teacher_id in info.keys():
        try:
            cursor.execute(query, (info[teacher_id], teacher_id))
        except:
            pass
    query = ('UPDATE APP.Classes SET Teacher_ID = %s WHERE Teacher_ID = %s')
    for teacher_id in info.keys():
        try:
            cursor.execute(query, (info[teacher_id], teacher_id))
            leftdata["TeacherIDChangeInfo"][0].pop(teacher_id)
        except:
            errorTime += 1

    # save class id
    query = ('UPDATE APP.Classes SET ClassID = %s WHERE ClassID = %s')
    info = data["ClassIDChangeInfo"][0]
    for class_id in info.keys():
        try:
            cursor.execute(query, (info[class_id], class_id))
        except:
            pass
    query = ('UPDATE APP.Score SET ClassID = %s WHERE ClassID = %s')
    for class_id in info.keys():
        try:
            cursor.execute(query, (info[class_id], class_id))
            leftdata["ClassIDChangeInfo"][0].pop(class_id)
        except:
            errorTime += 1

    conn.commit()
    cursor.close()
    conn.close()
    print(leftdata)
    if errorTime == 0:
        reply["Result"] = "Success"
    else:
        reply["Result"] = "Error"
    reply["errorTime"] = errorTime

    reply["leftInfo"] = json.dumps(leftdata)
    return json.dumps(reply)
