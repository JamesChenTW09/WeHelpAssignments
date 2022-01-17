from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key="any string but secret" 

#首頁設定
@app.route("/")
def home():
    checkStatus = session.get("status")
    if checkStatus == "ON":  #設定ON為有登入
        return redirect("/member")  #有登入紀錄的話返回會員頁面
    return render_template("base.html")  #沒有登入紀錄的話就到登入首頁

#登入頁面判斷是否輸入有誤
@app.route("/signin", methods=["POST"])
def signIn():
    account = request.form["account"]
    password = request.form["password"]
    if account == "test" and password == "test":   #都為test
        session["status"] = "ON"
        return redirect("/member")
    elif account == "" or password == "":  #其中一個空白
        return redirect("/error/?message=請輸入帳號、密碼")
    elif account != "test" or password != "test":   #其中一個輸入錯誤
        return redirect("/error/?message=帳號或密碼輸入錯誤")

#如有誤頁面
@app.route("/error/")
def error():
    checkStatus = request.args.get("message")
    return render_template("fail.html", result = checkStatus)


#成功登入頁面
@app.route("/member")
def member():
    if session.get("status") == "OFF":  
        return redirect("/")
    return render_template("success.html")

#按下登出後改變狀態為未登入，並導到首頁
@app.route("/logOut")
def logOut():
    session['status'] = "OFF"
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True, port=3000)

