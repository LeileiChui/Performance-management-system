import pymysql
import json


def StuGetScoreInfo(UserID):
    conn = pymysql.connect(user='root', password='', database='App', charset='utf8')
    cursor = conn.cursor()
    query = ('''SELECT Teacher.Teacher_Name, Classes.ClassName,Score.Score FROM Score
JOIN Student ON Score.Student_ID=Student.Stu_ID
JOIN Classes ON Score.ClassID=Classes.ClassID
JOIN Teacher ON Classes.Teacher_ID = Teacher.Teacher_ID
WHERE Student.Stu_ID = %s
ORDER BY Teacher_Name''')
    try:
        cursor.execute(query, UserID)
    except:
        print("ERROR")
        pass
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return json.dumps(results)
