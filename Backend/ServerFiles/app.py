from flask import Flask, Blueprint, app, request, url_for, redirect, render_template, make_response, send_from_directory, abort
import hashlib
import sqlite3
import os
import logging
import zipfile

def create_App():
    app = Flask(__name__)
    app.config["SECURE_KEY"] = "lkjhgfdsa"

    return app

app = create_App()

root = os.path.dirname(os.path.relpath((__file__)))
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(asctime)s:%(message)s')
DOWNLOAD_DIRECTORY_IMG = r"C:\Users\shekh\Desktop\EzzNotes\Backend\Backend\Files\Img"
DOWNLOAD_DIRECTORY_PDF = r"C:\Users\shekh\Desktop\EzzNotes\Backend\Backend\Files\pdf"
DOWNLOAD_DIRECTORY_PPTX = r"C:\Users\shekh\Desktop\EzzNotes\Backend\Backend\Files\pptx"
DOWNLOAD_DIRECTORY_DOCS = r"C:\Users\shekh\Desktop\EzzNotes\Backend\Backend\Files\docs"


# --------------------------------------------------- Landing Page ----------------------------------------------------
@app.route('/')
def index():
    if request.method == 'GET':
        return render_template("index.html")
    

# ---------------------------------------------------- Login Page ----------------------------------------------------
@app.route("/login", methods=['GET', 'POST'])
def login():
    
    if request.method == 'GET':
        print("Hello!")
        return render_template("login.html")

    if request.method == 'POST':
        print("Hello!")
        username = request.form.get('username')
        email = request.form.get('email')
        password = hashlib.md5(request.form.get('password').encode('utf-8')).hexdigest()
        
        login = access_site_login(username,email, password)

        return "LOGGED" if login else "FAILED"

        

# ----------------------------------------------------- SignUP Page ---------------------------------------------------
@app.route("/SignUp", methods=['GET', 'POST'])
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
@app.route("/logout")
def logout():
    return redirect(url_for("index.html"))


# ----------------------------------------------- File Downloading And Uploading ------------------------------------------------------

@app.route("/get-file/<string:img_name>") # Il si scarica il file messo a disposizione 
def file_download(img_name):
    try:
        return send_from_directory(DOWNLOAD_DIRECTORY_IMG, img_name, as_attachment=True)
    except FileNotFoundError:
        abort(404, "File download")


    return None


@app.route("/file_receiving")
def file_upload():
    file = request.files['inputfile']

    


    return None

@app.route("/search/<string:ricerca>")
def search(ricerca):

    ricercato =  search_in_files(ricerca)
    return "TODO"



# ------------------------------------------------------ Functions ------------------------------------------------------

def search_in_files(ricerca):
    try:
        con = sqlite3.connect(os.path.join(root,"Ezznotes.db"))
        cur = con.cursor()
    except Exception as e :
        logging.error(f"Connaction Error : {e}")
    
    query = f"SELECT fileName FROM Filelinks WHERE fileName like('{ricerca}')"
    try :  
        result = cur.execute(query)
        result = result.fetchall()
        print(result)
    except Exception as e :
        print(e)

    return "Something"





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


def getIMGpath(filename):



    return None

def getPDFpath(filename):

    return None

def getPPTXpath(filename):

    return None
    



if __name__ == '__main__':
    app.run(debug=True)
