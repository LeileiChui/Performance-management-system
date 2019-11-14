import pymysql
import json


def Login(data):
    conn = pymysql.connect(user='root', password='', database='App', charset='utf8')
    cursor = conn.cursor()
    if data["user_type"] == 0:
        query = ('select Stu_Name from Student where Stu_ID = %s and Password= %s')
    elif data["user_type"] == 1:
        query = ('select Teacher_Name from Teacher where Teacher_ID = %s and Password= %s')
    elif data["user_type"] == 2:
        query = ('select Manager_Name from Manager where Manager_ID = %s and Password= %s')
    cursor.execute(query, (data["user_id"], data["password"]))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    result = {}
    if len(results) == 1:
        result["LoginResult"] = "True"
        result["Name"] = results[0][0]
    else:
        result["LoginResult"] = "False"
    return json.dumps(result)
