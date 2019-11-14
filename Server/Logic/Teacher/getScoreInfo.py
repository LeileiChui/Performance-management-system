import pymysql
import json


def getScoreInfo(ClassID):
    conn = pymysql.connect(user='root', password='', database='App', charset='utf8')
    cursor = conn.cursor()
    results = []
    query = ('''SELECT Classes.ClassName, Student.Stu_ID,Student.Stu_Name,Score.Score FROM Classes 
JOIN Score ON Score.ClassID=Classes.ClassID
JOIN Student ON  Score.Student_ID = Student.Stu_ID
WHERE Classes.ClassID= %s
ORDER BY Stu_ID''')
    try:
        cursor.execute(query, str(ClassID))
    except:
        return
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return json.dumps(results)
