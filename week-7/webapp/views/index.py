# 載入 Flask 模組
from flask import *
index_bp = Blueprint("index", __name__)
# from flask import request, redirect, render_template, session
''' 需求網址
[首頁]網址：http://127.0.0.1:3000/
[註冊]網址：http://127.0.0.1:3000/signup
[驗證]功能網址：http://127.0.0.1:3000/signin
[成功]頁面網址：http://127.0.0.1:3000/member/
[失敗]頁面網址：http://127.0.0.1:3000/error/?message=自訂的錯誤訊息
[登出]功能網址：http://127.0.0.1:3000/signout
'''

# [首頁] 處理路徑 / 的對應函式 
@index_bp.route("/")
def index():
    return render_template("index.html") 

# [註冊] 處理路徑 /register 的對應函式 
@index_bp.route("/register")
def register():
    return render_template("register.html")
