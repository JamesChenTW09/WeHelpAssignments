
from flask import Flask, Blueprint, render_template, request, redirect, session,jsonify
import mysql.connector
import json
logIn = Blueprint("logIn", __name__, template_folder="templates",static_folder="static")

#連線資料庫
myDB = mysql.connector.connect(host="localhost",
                               user="root",
                               password="!weHELP0721james",
                               database="website")



#首頁設定，登入紀錄(check ON or OFF)? 返回會員頁面:登入首頁
@logIn.route("/")
def home():
    checkStatus = session.get("status")
    if checkStatus == "ON":  
        return redirect("/member") 
    return render_template("base.html")  


#登入頁面判斷 1.有值且正確(將資料存進session，供後續使用) 2.有誤導向錯誤頁面
@logIn.route("/signin", methods=["POST"])
def signIn():
    cursor = myDB.cursor(dictionary=True)

    account = request.form["account"]
    password = request.form["password"]
    
    if account and password:
        cursor.execute("SELECT * FROM `member` WHERE `username`=%s AND `password`=%s",[account,password])
        data = cursor.fetchone()
        if data == None:
            cursor.close()
            return redirect("/error/?message=帳號或密碼輸入錯誤")
        else:
            session["status"] = "ON"
            session["user"] = data["name"]
            session["userName"] = data["username"]
            session["password"] = data["password"]
            cursor.close()
            return redirect("/member")
    else:
        return redirect("/error/?message=請輸入帳號、密碼")


#錯誤頁面，取得query string並顯示在html頁面上
@logIn.route("/error/")
def error():
    checkStatus = request.args.get("message")
    return render_template("fail.html", result = checkStatus)


#會員頁面
@logIn.route("/member")
def member():
    cursor = myDB.cursor(dictionary=True)
    #確認是否為登入狀態
    if session.get("status") == "OFF" or session.get("status") == None:  
        return redirect("/")
    #找到登入帳號對應的姓名，並傳給html
    username = session["userName"]
    cursor.execute("SELECT `name` FROM `member` WHERE `username` = %s",[username])
    dataName = cursor.fetchone()
    name = dataName["name"]
    cursor.close()
    return render_template("success.html", name = name)


#按下登出後改變狀態為未登入，並導到首頁
@logIn.route("/logOut")
def logOut():
    session['status'] = "OFF"
    return redirect("/")


#註冊
@logIn.route("/signup", methods=["POST"])
def signUp():
    cursor = myDB.cursor(dictionary=True)

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
            return render_template("base.html")
        else:
            cursor.close()
            return redirect("/error/?message=帳號已被註冊")
    #如果有一項未填，導入失敗頁面
    else :   
        cursor.close()   
        return redirect("/error/?message=資料未填寫完全")  
        
#-------------------以下為第七週作業(更改姓名以及查詢姓名)-----------------------------------
@logIn.route("/api/members")
def checkUsername():
    cursor = myDB.cursor(dictionary=True)
    #取得query string
    userName = request.args.get("username")
    cursor.execute("SELECT `id`,`name`,`username` FROM `member` WHERE `username` = %s",[userName])
    data = cursor.fetchone()
    if data == None:
        cursor.close()
        return {"data": None}
    else:
        cursor.close()
        return {"data":data}


@logIn.route("/api/member", methods=["POST"])
def updateName():
    cursor = myDB.cursor(dictionary=True)

    #取得前端傳遞的資料
    updateName = request.get_json()
    #如果為空值，回傳錯誤提示，由前端渲染到頁面
    if updateName["name"] == "":
        cursor.close()
        return {"title":"請輸入姓名"}
    #找到登入的帳號和密碼
    originName = session["userName"]
    originPassword = session["password"]
    #判斷是否有登入資料，如沒有返回錯誤
    if originName == "" or originPassword =="":
        cursor.close()
        return {"error":True}
    #找到登入帳號對應的姓名，並更改
    cursor.execute("UPDATE `member` SET `name` = %s WHERE `username` = %s",[updateName["name"],originName])
    myDB.commit()
    cursor.close()
    return {"ok":True}
    
    
    