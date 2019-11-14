import pymysql
import json


def getAllInfo(UserID):
    conn = pymysql.connect(user='root', password='', database='App', charset='utf8')
    cursor = conn.cursor()
    results = []
    query = ('''SELECT Stu_ID, Stu_Name,Classes.ClassName,Score FROM Classes 
JOIN Score ON Score.ClassID=Classes.ClassID
JOIN Student ON  Score.Student_ID = Student.Stu_ID
WHERE Classes.Teacher_ID = %s 
ORDER BY Student.Stu_Name;''')
    try:
        cursor.execute(query, UserID)
    except:
        return
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return json.dumps(results)
