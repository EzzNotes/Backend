from flask import Flask, Blueprint, request, url_for, redirect, render_template, make_response
import hashlib
import sqlite3
import os
import logging

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
        
        login = access_site(username, email, password)

        return "LOGGED" if login else "FAILED"

        

# ----------------------------------------------------- SignUP Page ---------------------------------------------------
@Auth.route("/SignUp")
def signUp():
    return "Sign Up"


# ------------------------------------------------------ Logout Page ---------------------------------------------------
@Auth.route("/logout")
def logout():
    return redirect(url_for("index.html"))



# ------------------------------------------------------ Functions ------------------------------------------------------

def access_site(username, email, password):
    try:
        con = sqlite3.connect(os.path.join(root,"Archivio.db"))
        cur = con.cursor()
    except Exception as e :
        lg.error(f"Connaction Error : {e}")
        
    """
    result = cur.execute("SELECT password FROM user WHERE username = ?", username)

    if (result == password):
        # Loged in
        return True
    else:
        return False
    
    """
    return True