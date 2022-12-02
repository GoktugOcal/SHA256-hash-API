import requests
from flask import Flask, request, render_template
import hashlib

mess_store = {}

app = Flask(__name__)

@app.route('/messages', methods=["POST"])
def post():
    mess = request.json
    hashed = hashlib.sha256(request.json.encode()).hexdigest()
    mess_store[hashed] = mess
    return hashed

@app.route('/messages/<string:hashed>', methods=["GET"])
def get(hashed):
    if hashed in mess_store.keys():
        return mess_store[hashed]
    else: return "404 - sent <hash> string not found in the storage"

app.run(host='0.0.0.0', port=5000)