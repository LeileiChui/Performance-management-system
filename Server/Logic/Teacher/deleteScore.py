import pymysql
import json


def deleteScore(data):
    reply = {}
    conn = pymysql.connect(user='root', password='', database='App', charset='utf8')
    cursor = conn.cursor()
    delquery = ('DELETE FROM App.Score WHERE ClassID = %s and Student_ID = %s')
    searchquery = ('SELECT Stu_Num FROM `App`.`Classes` WHERE `ClassID` = %s')
    updatequery = ('UPDATE `App`.`Classes` SET Stu_Num = %s WHERE `ClassID` = %s')
    try:
        cursor.execute(delquery, data)
        cursor.execute(searchquery, data[0])
        num = cursor.fetchall()[0][0] - 1
        cursor.execute(updatequery, (num, data[0]))
        conn.commit()
    except:
        reply["Result"] = "Error"
        return json.dumps(reply)
    reply["Result"] = "Success"
    return json.dumps(reply)
