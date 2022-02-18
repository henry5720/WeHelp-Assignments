from flask import *
import mysql.connector
from mysql.connector import errors

# [引入] 資料轉json模組
from . import db_covert_json as convert

# 藍圖
search_bp=Blueprint("search", __name__)

@search_bp.route("/api/members", methods=["GET"])
def search():
    # [判斷] (HTTP請求方法) 如果是GET
    if (request.method == "GET"):
        # [獲取] Url 參數 (query string)
        username = request.args.get("username", "")
        print(username)
        """ print(username)

            print("-------------------")
            print("form:", request.form)
            print("data:", request.data)
            print("json:", request.json)
            print("-------------------")
        """
        
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
            
        except errors.Error as e:
            print(e)
            
        else:
            db1.close()
            return jsonify(jsonD)
 




