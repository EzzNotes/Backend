import sqlite3
import os
import logging as lg

root = os.path.dirname(os.path.relpath((__file__)))

def access_site(username, email, password):
    try:
        con = sqlite3.connect(os.path.join(root,"Archivio.db"))
        cur = con.cursor()
    except Exception as e :
        lg.error(f"Connaction Error : {e}")
        

    result = cur.execute("SELECT password FROM user WHERE username = ?", username)

    if (result == password):
        # Loged in
        return True
    


    pass

