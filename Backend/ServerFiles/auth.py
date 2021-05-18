from flask import Flask, Blueprint, request, url_for, redirect, render_template, make_response
import hashlib
import sqlite3
import os
import logging

#from flask.helpers import flash

root = os.path.dirname(os.path.relpath((__file__)))
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(asctime)s:%(message)s')

Auth = Blueprint("auth", __name__)

# --------------------------------------------------- Landing Page ----------------------------------------------------
@Auth.route('/')
def index():
    if request.method == 'GET':
        return render_template("index.html")
    

# ---------------------------------------------------- Login Page ----------------------------------------------------
@Auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")

    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = hashlib.md5(request.form.get('password').encode('utf-8')).hexdigest()
        
        login = access_site_login(username, email, password)

        return "LOGGED" if login else "FAILED"

        

# ----------------------------------------------------- SignUP Page ---------------------------------------------------
@Auth.route("/SignUp", methods=['GET', 'POST'])
def signUp():
    if request.method == 'GET':
        return render_template("signup.html")
    
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = hashlib.md5(request.form.get('password').encode('utf-8')).hexdigest()
        password2 = hashlib.md5(request.form.get('password2').encode('utf-8')).hexdigest()

        if password == password2 : 
            signUP = access_site_signUP(username, email, password)
        else: 
            return render_template("signup.html")

        return "Registerd" if signUP else "FAILED"



# ------------------------------------------------------ Logout Page ---------------------------------------------------
@Auth.route("/logout")
def logout():
    return redirect(url_for("index.html"))


# ----------------------------------------------- File Downloading And Uploading ------------------------------------------------------
@Auth.route("/file_sending") # Il si scarica il file messo a disposizione 
def file_download():
    

    
    return None


@Auth.route("/file_receiving") # Il server manda il file richiesto
def file_upload():



    return None




# ------------------------------------------------------ Functions ------------------------------------------------------

def access_site_login(username, email, password):
    try:
        con = sqlite3.connect(os.path.join(root,"Ezznotes.db"))
        cur = con.cursor()
    except Exception as e :
        logging.error(f"Connaction Error : {e}")
        
    
    result = cur.execute(f"SELECT Password FROM USERTABLE WHERE username = '{username}'")
    result = cur.fetchone()
    print (result[0])

    if (result[0] == password):
        print(result[0])
        return True
    else:
        return False
    

def access_site_signUP(username, email, password):
    try:
        con = sqlite3.connect(os.path.join(root,"Ezznotes.db"))
        cur = con.cursor()
    except Exception as e :
        logging.error(f"Connaction Error : {e}")
        return False

    query = f"INSERT INTO USERTABLE VALUES('{username}','{password}','{email}');"
    try :  
        print(query)
        result = cur.execute(query)
        print(result.lastrowid)
    except Exception as e :
        print(e)
    
    if (result.lastrowid > 1):
        print(username)
        con.commit()
        return True
    else:
        con.close()
        return False
    

