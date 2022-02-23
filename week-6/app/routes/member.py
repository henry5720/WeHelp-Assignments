from flask import *
member_bp=Blueprint("member", __name__)

# [成功] 處理路徑 /member/ 的對應函式
@member_bp.route("/member/")
def member():
    # 檢查 session 值 > 跳轉頁面
    # 登出狀態 > 首頁
    if session["login"] == "已登出":  
        return redirect("/")
    # 登入狀態 > 會員頁 (session["login"] 在 /signin 頁面已紀錄)
    else: 
        return render_template("member.html", data=session["login"])

# [失敗] 處理路徑 /error/ 的對應函式
@member_bp.route("/error/", methods=["GET"])
def error():
    s=request.args.get("massage", "") # 得到 query_string
    # print(s)
    # print(request.query_string)
    # 將 query_string 提交前端
    return render_template("error.html", data=s) 

# [登出] 處理路徑 /signout 的對應函式
@member_bp.route("/signout")
def signout():
    session["login"]="已登出" # 修改 session 值
    print(session["login"])
    return redirect("/")
