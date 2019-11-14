import pymysql
import json


def MangetOneClassInfo(ClassID):
    conn = pymysql.connect(user='root', password='', database='App', charset='utf8')
    cursor = conn.cursor()
    results = []
    #                               0               1               2           3                       4                5
    query = ('''SELECT Classes.ClassName, Student.Stu_ID,Student.Stu_Name,Score.Score, CONCAT(Score.Student_ID," ",Score.ClassID), Score.ClassID  FROM Classes 
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
