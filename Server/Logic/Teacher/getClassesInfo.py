import pymysql
import json


def getClassesInfo(UserID):
    conn = pymysql.connect(user='root', password='', database='App', charset='utf8')
    cursor = conn.cursor()
    query = ('select ClassID , ClassName , Stu_Num from Classes where Teacher_ID = %s')
    try:
        cursor.execute(query, UserID)
    except:
        print("getClassesInfo Error")
        return
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    if len(results) == 0:
        print("None")
        return ""
    return json.dumps(results)
