# 引入模組
from flask import * 
import mysql.connector
from .. import config

# 設定藍圖
check_bp=Blueprint("check", __name__)


# [驗證] 處理路徑 /signin 的對應函式
@check_bp.route("/signin", methods=["GET", "POST"]) # 增加 POST 方法
def signin():
    # 如果以"POST"連線
    if request.method == "POST": 
        """ get() 字典中不存在查找的鍵時 > 返回默認值
        username = request.form.get("username", None)  
        password = request.form.get("password", None)
        """
        # [] 字典中不存在查找的鍵時 > 報錯
        username=request.form["username"]
        password=request.form["password"]
        

    # 清除 session > 預設值 已登出
    session.pop("login", "已登出")

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

    # SQL 語句 > [取出] 帳密
    cursor.execute(
        """
        SELECT `username`, `password` 
        FROM `member`;
        """
    )
    # 取出值 存到 records / lsit[(tuple),(tuple)]
    records = cursor.fetchall()
    # print(records) # 列表
    """ 列表裡的每個元組
        for i in records:
            print(i) 
    """
    
    """ List Comprehension
        dataUser = []
        for user in records:
        dataUser.append(user[0])
    """
    # tuple第一個 > 加進dataUser (帳號)
    dataUser = [user[0] for user in records]
    dataPwd = [user[1] for user in records]

    # SQL 語句 佔位符(%s %d %f) > [處理] 會員頁 自訂歡迎語 
    sql = "SELECT `name` FROM `member` WHERE `username` = %s"
    val = (username,) # %s的值
    cursor.execute(sql, val)
    # 結果 > nameRecord
    nameRecord = cursor.fetchall()
    print(nameRecord)

    cursor.close() # 關閉鼠標
    connection.close() # 關閉連線


    # 輸入的帳密是否存在 dataUser, password (第20,21行)
    if username in dataUser and password in dataPwd:
        session["login"] = nameRecord[0][0] # name(第69行)
        print(session["login"])
        return redirect("/member/")
    # 如果輸入是空 (前端預設: username, password)
    elif username=="username" and password=="password":
        inform="input can not be empty."
        return redirect("/error/?massage="+inform)
    else:
        inform="Error : account or password."
        return redirect("/error/?massage="+inform)
    