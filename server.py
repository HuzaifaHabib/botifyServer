from gevent import config
from pyttsx3 import speak
import configs
import requests
import Prototype as pt
import dbService as dbs
from flask import Flask, request
import json
from flask_cors import CORS


app = Flask(__name__)


from flask_mysqldb import MySQL
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345'
app.config['MYSQL_DB'] = 'db2'
 
mysql = MySQL(app)
CORS(app)

# Adds support for GET requests to our webhook
@app.route('/webhook', methods=['GET'])
def webhook():
    verify_token = request.args.get("hub.verify_token")
    # Check if sent token is correct
    if verify_token == configs.WEBHOOK_VERIFY_TOKEN:
        # Responds with the challenge token from the request
        return request.args.get("hub.challenge")
    return 'Unable to authorise.'

@app.route('/talk', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        #do something.....
        y = json.loads(request.data)
        msg = pt.extract(y['message'])
        print(msg)
        return msg, 200

@app.route('/addTrans', methods=["GET", "POST"])
def addTrans():
    if request.method == 'POST':
        #do something.....
        y = json.loads(request.data)
        dbs.addCartTransaction(y)
        return 'record added', 200


if __name__ == "__main__":
    app.run(threaded=True, port=5000)