import pymysql
import json


def saveScoreInfo(data):
    reply = {}
    conn = pymysql.connect(user='root', password='', database='App', charset='utf8')
    cursor = conn.cursor()
    query = ('UPDATE `App`.`Score` SET `Score` = %s WHERE `ClassID` = %s and `Student_ID` = %s')
    for i in data:
        try:
            cursor.execute(query, i)
            conn.commit()
        except:
            reply["Result"] = "Error"
            return json.dumps(reply)
    reply["Result"] = "Success"
    return json.dumps(reply)
