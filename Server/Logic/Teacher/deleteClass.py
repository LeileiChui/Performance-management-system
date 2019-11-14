import pymysql
import json


def deleteClass(data):
    reply = {}
    conn = pymysql.connect(user='root', password='', database='App', charset='utf8')
    cursor = conn.cursor()
    delquery1 = ('DELETE FROM App.Score WHERE ClassID = %s')
    delquery2 = ('DELETE FROM App.Classes WHERE ClassID = %s')
    try:
        cursor.execute(delquery1, (data[0]))
        cursor.execute(delquery2, (data[0]))
        conn.commit()
    except:
        reply["Result"] = "Error"
        return json.dumps(reply)
    reply["Result"] = "Success"
    return json.dumps(reply)
