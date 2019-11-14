import pymysql
import json


def ManGetStuInfo():
    conn = pymysql.connect(user='root', password='', database='App', charset='utf8')
    cursor = conn.cursor()
    #                               0              1                2               3               4             5                        6                            7
    query = ('''SELECT Student.Stu_Name,Student.Stu_ID,Classes.ClassName,Teacher.Teacher_Name,Score.Score,Score.ClassID, CONCAT(Student_ID," ",Score.ClassID),Classes.Teacher_ID FROM Student
LEFT JOIN Score ON Student.Stu_ID=Score.Student_ID
LEFT JOIN Classes ON Score.ClassID=Classes.ClassID
LEFT JOIN Teacher ON Classes.Teacher_ID=Teacher.Teacher_ID
ORDER BY Student.Stu_ID
''')
    try:
        cursor.execute(query)
    except:
        print("ERROR")
        pass
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return json.dumps(results)
