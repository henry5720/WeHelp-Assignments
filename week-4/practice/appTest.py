from http.client import OK
import imp
from os import path
import this
from flask import Flask
from flask import request
from flask import redirect
import json
app=Flask(
    __name__,
    static_folder="public",
    static_url_path="/"
) # __name__ 目前執行模組

# 建立路徑 / 對應處理函數
@app.route("/")
def index():
    # print("請求方法",request.method)
    # print("通訊協議",request.scheme)
    # print("主機名稱",request.host)
    # print("路徑",request.path)
    # print("完整的網址",request.url)
    # print("瀏覽器&作業系統",request.headers.get("user-agent"))
    # print("語言篇好",request.headers.get("accept-language"))
    # print("引薦網址",request.headers.get("referrer"))

    # if lang.startswith("en"):
    #     return json.dumps({
    #          "status":"ok",
    #          "text":"hello"
    #     })
    # else:
    #     return json.dumps({
    #          "status":"ok",
    #          "text":"你好"
    #     }, ensure_ascii=False)
    lang=request.headers.get("accept-language")
    print("語言偏好",lang)
    if lang.startswith("en"):
        return redirect("/en/")
    else:
        return redirect("/zh/")

@app.route("/en/")
def index_english():
    return json.dumps({
         "status":"ok",
         "text":"hello"
    })

@app.route("/zh/")
def index_chinese():
    return json.dumps({
         "status":"ok",
         "text":"你好"
    }, ensure_ascii=False)

# 建立路徑 /data 對應處理函數
@app.route("/data")
def handleData():
    return "My Data"

@app.route("/user/<username>")
def handleUser(username):
    return "hello"+username

if __name__=="__main__": # 如果以主程式運作
    app.run(port=3000) # 立刻啟動伺服器