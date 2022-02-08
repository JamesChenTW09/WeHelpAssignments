from sqlite3 import Cursor
from flask import Flask, Blueprint, render_template, request, redirect, session
import mysql.connector
logIn = Blueprint("logIn", __name__, template_folder="templates",static_folder="static")


#首頁設定
@logIn.route("/")
def home():
    checkStatus = session.get("status")
    #設定ON為有登入
    if checkStatus == "ON":  
        #有登入紀錄的話返回會員頁面
        return redirect("/member") 
    #沒有登入紀錄的話就到登入首頁    
    return render_template("base.html")  

#登入頁面判斷是否輸入有誤
@logIn.route("/signin", methods=["POST"])
def signIn():

    #連線資料庫
    myDB = mysql.connector.connect(host="localhost",
                               user="root",
                               password="!weHELP0721james",
                               database="website")
    cursor = myDB.cursor()

    #取得客戶傳回來的帳號密碼
    account = request.form["account"]
    password = request.form["password"]

    
    if account and password:
        #如果都有填寫，找到是否有帳號和密碼皆符合的user
        cursor.execute("SELECT * FROM `member` WHERE `username`=%s AND `password`=%s",[account,password])
        data = cursor.fetchone()
        #如果沒有符合的user，關閉連線，導入錯誤頁面
        if data == None:
            cursor.close()
            myDB.close() 
            return redirect("/error/?message=帳號或密碼輸入錯誤")
        else:
        #如果有符合的user，關閉連線，並將user的name保存在session，並導入成功登入頁面
            cursor.close()
            myDB.close() 
            session["status"] = "ON"
            session["user"] = data[1]
            return redirect("/member")
    else:
        #如果其中一項未填，取消連線資料庫，並導入錯誤頁面
        cursor.close()
        myDB.close() 
        return redirect("/error/?message=請輸入帳號、密碼")


#如有誤頁面
@logIn.route("/error/")
def error():
    checkStatus = request.args.get("message")
    return render_template("fail.html", result = checkStatus)


#成功登入頁面
@logIn.route("/member")
def member():
    if session.get("status") == "OFF" or session.get("status") == None:  
        return redirect("/")
    userID = session["user"]
    return render_template("success.html", userID = userID)

#按下登出後改變狀態為未登入，並導到首頁
@logIn.route("/logOut")
def logOut():
    session['status'] = "OFF"
    return redirect("/")



#註冊
@logIn.route("/signup", methods=["POST"])
def signUp(): 
    #連線資料庫
    myDB = mysql.connector.connect(host="localhost",
                               user="root",
                               password="!weHELP0721james",
                               database="website")
    cursor = myDB.cursor()

    #取得客戶端輸入的資料
    registerName = request.form["registerName"]
    registerAccount = request.form["registerAccount"]
    registerPassword = request.form["registerPassword"]


    #檢查資料庫是否有相同的username，有的話導入失敗頁面
    if registerName and registerAccount and registerPassword:
        cursor.execute("SELECT * FROM `member` WHERE `username` = %s",[registerAccount])
        matchUsername = cursor.fetchone()
        if matchUsername == None:
             #如果都有資料，且未重複username，在資料庫新增一筆資料，並導回登入頁面
            cursor.execute("INSERT INTO `member`(`name`,`username`,`password`) VALUES(%s,%s,%s)",[registerName,registerAccount,registerPassword])
            myDB.commit()         
            cursor.close()
            myDB.close() 
            return render_template("base.html")
        else:
            cursor.close()
            myDB.close() 
            return redirect("/error/?message=帳號已被註冊")
      
    #如果有一項未填，導入失敗頁面
    else :      
        cursor.close()
        myDB.close()
        return redirect("/error/?message=資料未填寫完全")  
        

