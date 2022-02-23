from flask import *

''' json & database
{
    "data":{
        "id":3,
        "name":"強強",
        "username":"strong"
    }
}
+----+--------+----------+
| id | name   | username |
+----+--------+----------+
|  1 | first  | one      |
|  2 | second | two      |
|  3 | third  | three    |
+----+--------+----------+
'''

# 要查詢的帳號 > sql語句
def sql(user):
    # 帳號
    username=user
    # sql語句
    sql="""
            SELECT `id`, `name`, `username` 
            FROM `member`
            WHERE `username`='%s';
        """ %(username)
    return sql
# 資料庫,sql > 結果(list)
def query(db, sql):
    # 創建鼠標
    cursor= db.cursor()
    # 執行
    cursor.execute(sql)
    # 紀錄
    record=cursor.fetchall()
    # 關閉鼠標
    cursor.close()
    return record

# 結果 > json格式資料
def sql_json(record):
    # mysql資料 > dict字典 > json
    for r in record:
        # 第1層
        data = {}
        # 第2層
        user = {}
        user['id'] = r[0]
        user['name'] = r[1]
        user['username'] = r[2]
        data['data'] = user
    return data

# json > 判斷是否存在資料庫
def get_user(record):
    if(record != []):
        jsonD=sql_json(record)
    else:
        jsonD={
            "data": "null"
        }
    return jsonD
