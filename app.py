import requests
from flask import Flask, request
import hashlib

app = Flask(__name__)

@app.route('/messages', methods=["POST"])
def incrementer():
    print(hashlib.sha256(request.json.encode()))
    return True

'''
@app.route('/messages/<string:name>')
def hello(name):
    return "Hello " + name
'''

app.run(host='127.0.0.1', port=5000)