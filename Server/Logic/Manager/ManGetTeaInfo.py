import pymysql
import json


def ManGetTeaInfo():
    conn = pymysql.connect(user='root', password='', database='App', charset='utf8')
    cursor = conn.cursor()
    query = ('''SELECT Teacher.Teacher_Name, Teacher.Teacher_ID, Classes.ClassName ,Classes.ClassID,Classes.Stu_Num
FROM Classes
Right JOIN Teacher ON Classes.Teacher_ID=Teacher.Teacher_ID
ORDER BY Teacher_Name
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
