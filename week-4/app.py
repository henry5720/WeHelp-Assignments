# 載入 Flask 模組
from flask import Flask
from flask import request, redirect, render_template, session

# [首頁]網址：http://127.0.0.1:3000/
# [驗證]功能網址：http://127.0.0.1:3000/signin
# [成功]頁面網址：http://127.0.0.1:3000/member/
# [失敗]頁面網址：http://127.0.0.1:3000/error/?message=自訂的錯誤訊息
# [登出]功能網址：http://127.0.0.1:3000/signout

# 建立 Application > 設定 static 路徑
app=Flask(
    __name__,
    static_folder="publish",
    static_url_path="/"
)
# 設定session 密鑰
app.secret_key="something cryptic"

# [首頁] 處理路徑 / 的對應函式 
@app.route("/")
def index():
    return render_template("index.html") 

# [驗證] 處理路徑 /signin 的對應函式
@app.route("/signin", methods=["POST"]) # 改用 POST 方法
def signin():
    username=request.form["username"] # 取得前端 input(name=username) 內容
    password=request.form["password"] # 取得前端 input(name=password) 內容
    global inform # 全局變數 > 存放提示信息

    # a.如果帳號、密碼任一為空，代表輸入有誤，
    #   將使用者導向到【失敗頁面網址】，並顯示「請輸入帳號、密碼」
    if username=="username" and password=="password":
        inform="請輸入帳號、密碼"
        return redirect("/error/?massage="+inform)
    # b.如果帳號、密碼都是 test，代表驗證成功，將使用者導向到【成功頁面網址】
    elif username=="test" and password=="test":
        session["login"]="已登入" # 創建sessiont
        print(session["login"])
        return redirect("/member/")
    # c.如果帳號、密碼任一錯誤，代表驗證失敗，
    #   將使用者導向到【失敗頁面網址】，並顯示「帳號、或密碼輸入錯誤」
    else:
        inform="帳號、或密碼輸入錯誤"
        return redirect("/error/?massage="+inform)

# [成功] 處理路徑 /member/ 的對應函式
@app.route("/member/")
def member():
    # 檢查 session 值 > 跳轉網頁
    if session["login"] == "已登出":  
        return redirect("/")
    else:
        return render_template("member.html")

# [失敗] 處理路徑 /error/ 的對應函式
@app.route("/error/", methods=["GET"])
def error():
    s=request.args.get("massage", "") # 得到 query_string
    # print(s)
    # print(request.query_string)
    # 將 query_string 提交前端
    return render_template("error.html", data=s) 

# [登出] 處理路徑 /signout 的對應函式
@app.route("/signout")
def signout():
    session["login"]="已登出" # 修改 session 值
    print(session["login"])
    return redirect("/")

# app.debug=True
app.run(port="3000")