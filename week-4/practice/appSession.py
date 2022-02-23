from unicodedata import name
from flask import Flask # 載入 Flask
from flask import request 
from flask import render_template 
from flask import session
# 建立 Appalication 物件, 設定靜態檔案的路徑處理
app=Flask(__name__,static_folder="public",static_url_path="/")
app.secret_key="any string but secret" # 設定Session密鑰
# 建立路徑 / 對應的處理函式
@app.route("/")
def index():
    return render_template(
        "index",
        name="henry"
    )
# 使用GET方法 > 處理路徑 /hello?name=使用者名稱
@app.route("/hello")
def hello():
    name=request.args.get("name", "")
    session["username"]=name
    return "hello "+name
# 使用GET方法 > 處理路徑 /talk
@app.route("/talk")
def talk():
    name=session["username"]
    return "hello "+name
    
# 啟動網站伺服器,可用 port 指定埠號
app.run(port=3000)