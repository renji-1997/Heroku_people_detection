from flask import Flask
from detection import getDetector
from detection import closeDector
app = Flask(__name__)

@app.route("/")
def index():
   return 'People Detection',getDetector()
   
@app.route('/close')
def hello():
    return 'Camera Closed',closeDector() 

