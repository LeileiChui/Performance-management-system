import pymysql
import json


def saveClassesInfo(data):
    reply = {}
    conn = pymysql.connect(user='root', password='', database='App', charset='utf8')
    cursor = conn.cursor()
    query = ('UPDATE App.Classes SET ClassName = %s WHERE ClassID = %s')
    for i in data:
        try:
            cursor.execute(query, (str(i[1]), str(i[0])))
            conn.commit()
        except:
            reply["Result"] = "Error"
            return json.dumps(reply)
    reply["Result"] = "Success"
    return json.dumps(reply)
