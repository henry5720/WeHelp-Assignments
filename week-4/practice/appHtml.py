from flask import Flask
from flask import request
from flask import render_template
# 建立 Application > 設定 static 路徑
app=Flask(__name__,static_folder="public",static_url_path="/")
# 處理路徑 / 的對應函式
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/calculate", methods=["POST"])
def calculate():
    # 接收GET方法的Query String
    # maxNumber=request.args.get("max", "")
    maxNumber=request.form["max"]
    maxNumber=int(maxNumber)
    result=0
    for n in range(1, maxNumber+1):
        result+=n
    return render_template("result.html", data=result)
@app.route("/show")
def show():
    username=request.args.get("username", "")
    return render_template("secondPage.html")
@app.route("/page")
def page():
    return render_template("secondPage.html")
# 啟動伺服器 > 設定 port
app.run(port="3000")