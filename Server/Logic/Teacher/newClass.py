import pymysql
import json


def newClass(data):
    reply = {}
    conn = pymysql.connect(user='root', password='', database='App', charset='utf8')
    cursor = conn.cursor()
    query = ('INSERT INTO App.Classes (Teacher_ID, ClassName) VALUES (%s, %s)')
    try:
        cursor.execute(query, data)
        conn.commit()
    except:
        reply["Result"] = "Error"
    reply["Result"] = "Success"
    return json.dumps(reply)
