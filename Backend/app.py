#from flask_core import CORS
import hashlib
from ServerFiles import create_App



app = create_App()

    
if __name__ == '__main__':
    app.run(debug=True)