# 引入模組
from flask import *
from .. import config
import mysql.connector

# 設定藍圖
signup_bp = Blueprint("signup", __name__)

@signup_bp.route("/signup", methods = ["GET", "POST"])
def signup():
    # 如果以"POST"連線
    if request.method == "POST":
        # 從 HTTP request物件的表單拿到(預設值: None)
        nickname = request.form.get("nickname", None)
        username = request.form.get("username", None)
        password = request.form.get("password", None)
        
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
        # SQL 語句 > 如果輸入的帳密存在 返回 id
        cursor.execute(
                    """
                        SELECT `id` 
                        FROM `member`
                        WHERE `username` = '%s'
                    """ %(username)
        )
        # 取出值 存到 records
        records = cursor.fetchall()
        # print(records)
        # print(len(records))

    """ 如果 用戶有輸入內容 and 帳號已存在 > 跳轉錯誤頁
        用戶有輸入內容: 暱稱 and 密碼 不為空值 (前端預設)
        帳號已存在: 列表[]有長度 > 數據庫有內容
    """
    if nickname != "nickname" and password != "password" and len(records) != 0:
        inform = "Account already exists."
        return redirect("/error/?massage="+inform)

    # 暱稱, 帳號, 密碼 皆為空 (前端預設) > 跳轉錯誤頁
    elif nickname == "nickname" or username == "username" or password == "password":
        inform = "input can not be empty."
        return redirect("/error/?massage="+inform)

    # 連線數據庫 > 創建新資料
    else:
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
