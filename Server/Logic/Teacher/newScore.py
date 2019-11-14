import pymysql
import json


def newScore(data):
    result = "Success"
    reply = {}
    conn = pymysql.connect(user='root', password='', database='App', charset='utf8')
    cursor = conn.cursor()
    search = ('SELECT * FROM App.Student  WHERE  Stu_ID = %s')
    query = ('INSERT INTO App.Score (ClassID, Student_ID, Score) VALUES (%s, %s, %s)')
    newUser = ('INSERT INTO App.Student (Stu_ID, Stu_Name, Password) VALUES (%s, %s, %s)')
    numsearch = ('SELECT Stu_Num FROM `App`.`Classes` WHERE `ClassID` = %s')
    updatequery = ('UPDATE `App`.`Classes` SET Stu_Num = %s WHERE `ClassID` = %s')
    try:
        cursor.execute(query, data)
        conn.commit()
        cursor.execute(search, data[1])
        if cursor.rowcount == 0:
            cursor.execute(newUser, (data[1], "Default "+data[1], "default"+data[1]))
            conn.commit()
            result = "Warnning"
        cursor.execute(numsearch, data[0])
        num = cursor.fetchall()[0][0] + 1
        cursor.execute(updatequery, (num, data[0]))
        conn.commit()
    except:
        result = "Error"
    cursor.close()
    conn.close()
    reply["Result"] = result
    return json.dumps(reply)
