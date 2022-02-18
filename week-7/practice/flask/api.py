from flask import *
import mysql.connector
from mysql.connector import errors

app=Flask(
    __name__,
    static_url_path="/"
) # __name__ 目前執行模組

@app.route("/")
def member():
    return render_template("member.html") 

@app.route("/api/members/<username>", methods=["GET"])
def search():
    username = request.form.get("username", None)  
    def query(db, sql):
        cursor= db.cursor()
        cursor.execute(sql)
        record=cursor.fetchall()
        cursor.close()
        for r in record:
            data = {}
            user = {}
            user['id'] = r[0]
            user['name'] = r[1]
            user['username'] = r[2]
            data['data'] = user
            jsonStr = json.dumps(data)
        return jsonStr
    try:
        db1=mysql.connector.connect(
            option_files='my.conf',
            pool_name='my_connection_pool',
            pool_size=3
        )
        jstr=query(
            db1,
            """
                SELECT `id`, `name`, `username` 
                FROM `member`
                username `id`='%s';
            """ %(username,)
        )
        db2=mysql.connector.connect(pool_name='my_connection_pool')
        print("db2:", db2.connection_id)
        db3=mysql.connector.connect(pool_name='my_connection_pool')
        print("db3:", db3.connection_id)    
        try:
            db4=mysql.connector.connect(pool_name='my_connection_pool')
        except errors.PoolError as e:
            print(e)
            print('Closing db3')
            db3.close()
            db4=mysql.connector.connect(pool_name='my_connection_pool')
    except errors.Error as e:
        print(e)
    finally:
        print("db1:", db1.connection_id)
        print("db2:", db2.connection_id)
        print("db4:", db4.connection_id)
        db1.close()
        db2.close()
        db4.close()
    return jsonify(jstr)

if __name__=="__main__": # 如果以主程式運作
    app.run() # 立刻啟動伺服器