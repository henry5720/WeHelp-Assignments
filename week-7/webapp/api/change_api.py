from unicodedata import name
from flask import *
import mysql.connector
from mysql.connector import errors
from numpy import record

from . import db_covert_json as convert

# 藍圖
change_bp=Blueprint("change", __name__)

@change_bp.route("/api/member", methods=["GET", "POST"])
def change():
    if request.method == "POST":
        if session["login"] != "已登出":
            nowName=session["login"]
            print(nowName)
            newName=request.get_json()["name"]
            print(newName)

            try:
                # create connection pool and fetch the first connection
                db1=mysql.connector.connect(option_files='my.conf',
                                            pool_name='my_connection_pool',
                                            pool_size=3)
                cursor=db1.cursor()
                # 根據[獲取] > sql語句
                sql="SELECT `username` FROM `member` WHERE `name` = '%s'"%(nowName)
                cursor.execute(sql)
                record=cursor.fetchone()
                # print(record)
                
                sql="""
                    UPDATE `member`
                    SET `name` = '%s'
                    WHERE `username` = '%s';
                    """%(newName, record[0])
                cursor.execute(sql)

                cursor.close() # 關閉鼠標
                db1.commit() # 確認新增


            except errors.Error as e:
                print(e)

            finally:
                db1.close()
                session["login"]=newName
                return jsonify({
                        "ok":True
                    })
        else:
            return jsonify({
                    "error":True
                })