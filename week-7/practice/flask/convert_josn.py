from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route('/returnjson', methods = ['GET'])
def ReturnJSON():
    # [判斷] (HTTP請求方法) 如果是GET
    if (request.method == "GET"):
        # [獲取] Url 參數 (query string)
        username = request.args.get("username", "")
        # print(username)
        # [判斷] 如果 參數 = "ply"
        if(username=="ply"):
            # [創建] dict 
            data={
                    "data":{
                        "id":3,
                        "name":"強強",
                        "username":"strong"
                    }
                }
            # [回傳] 返回包含json格式資料響應(body)的方法
            return jsonify(data)
        else:
            return dict(data=None)
    
if __name__=='__main__':
	app.run(debug=True)
