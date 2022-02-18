from flask import *
import mysql.connector
from mysql.connector import errors

# 藍圖
search_bp=Blueprint("search", __name__)

@search_bp.route("/api/members", methods=["GET", "POST"])
def search():
    # [判斷] (HTTP請求方法) 如果是GET
    if request.method == "GET":
        # [獲取] Url 參數 (query string)
        username = request.args.get("username", "")
        # print(username)
        # [判斷] 如果 參數 = "ply"
        if(username=="ply"):
            # [創建] dict 
            data={
                    "data":{
                        "id":3,
                        "name":"強強",
                        "username":"strong"
                    }
                }
            # [回傳] 返回包含json格式資料響應(body)的方法
            return jsonify(data)
        else:
            return dict(data=None)
    
    # [判斷] (HTTP請求方法) 如果是POST
    elif request.method == "POST":
        # [獲取] 前端傳入 json 資料
        username = request.json["username"]
        """ print(username)

            print("-------------------")
            print("form:", request.form)
            print("data:", request.data)
            print("json:", request.json)
            print("-------------------")
        """
        
        # [引入] 資料轉json模組
        from . import db_covert_json as convert

        try:
            # create connection pool and fetch the first connection
            db1=mysql.connector.connect(option_files='my.conf',
                                        pool_name='my_connection_pool',
                                        pool_size=3)
            # 根據[獲取] > sql語句
            sql=convert.sql(username)
            # [紀錄] 資料庫查詢結果
            record=convert.query(db1, sql)
            # [判斷] 資料庫是否有資料 > 
            jsonD=convert.get_user(record)
            
            # fetch the second connection from the pool
            db2=mysql.connector.connect(pool_name='my_connection_pool')
            sql=convert.sql(username)
            record=convert.query(db2, sql)
            jsonD=convert.get_user(record)

            # fetch the third connection from the pool
            db3=mysql.connector.connect(pool_name='my_connection_pool')
            sql=convert.sql(username)
            record=convert.query(db3, sql)
            jsonD=convert.get_user(record)

            try:
                # fetch the fourth connection from the pool
                db4=mysql.connector.connect(pool_name='my_connection_pool')

            except errors.PoolError as e:
                # connection pool exhausted, so we can't fetch 4th connection
                print(e)
                db3.close()

                # lets try fetching db4 again
                db4=mysql.connector.connect(pool_name='my_connection_pool')
                sql=convert.sql(username)
                record=convert.query(db4, sql)
                jsonD=convert.get_user(record)

        except errors.Error as e:
            print(e)
            
        else:
            db1.close()
            db2.close()
            db4.close()
            return jsonify(jsonD)

