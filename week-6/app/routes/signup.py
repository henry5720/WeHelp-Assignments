# 引入模組
from flask import *
import mysql.connector
from .. import config

# 設定藍圖
signup_bp = Blueprint("signup", __name__)

# 連線物件 > config
connection = mysql.connector.connect( 
                            host = config.HOST,
                            port = config.POST,
                            user = config.USER,
                            password = config.PASSWORD,
                            database = config.DATABASE                           
)

# 鼠標物件
cursor = connection.cursor() 

# SQL 語句 > [取出]
cursor.execute("SELECT `name`, `username`, `password` FROM `member`;")
# 紀錄 取出值
records = cursor.fetchall()

cursor.close() # 關閉鼠標
connection.close() # 關閉連線

@signup_bp.route("/signup", methods = ["GET", "POST"])
def signup():
    # 如果以"POST"連線
    if request.method == "POST":
        # 從 HTTP request物件的表單拿到(預設值: None)
        nickname = request.form.get("nickname", None)
        username = request.form.get("username", None)
        password = request.form.get("password", None)
    
    # 變歷 取出值
    for user in records:
        # 如果 暱稱密碼不為空 和 帳號有重複 > 跳轉錯誤頁
        if nickname != "nickname" and username == user[1] and password != "password":
            inform = "Account already exists."
            return redirect("/error/?massage="+inform)
        else:
            # 連線物件 > config
            connection = mysql.connector.connect( 
                                        host = config.HOST,
                                        port = config.POST,
                                        user = config.USER,
                                        password = config.PASSWORD,
                                        database = config.DATABASE                           
            )

            # 鼠標物件
            cursor = connection.cursor() 
            
            # SQL 語句 佔位符(%s %d %f) > [新增] 註冊頁 暱稱 帳號 密碼 
            sql = "INSERT INTO `member`(`name`, `username`, `password`) VALUES(%s, %s, %s);"
            val = (nickname, username, password) # (%s, %s, %s)的值
            cursor.execute(sql, val)

            cursor.close() # 關閉鼠標
            connection.commit() # 確認新增
            connection.close() # 關閉連線
            # print(val)
            return redirect("/") # 跳轉首頁
