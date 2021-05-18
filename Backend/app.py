#from flask_core import CORS
import hashlib
from ServerFiles import create_App



app = create_App()
app.config["CLIENT_IMG"] = r"C:\Users\shekh\Desktop\EzzNotes\Backend\Backend\ServerFiles\static\files\Img"

    
if __name__ == '__main__':
    app.run(debug=True)