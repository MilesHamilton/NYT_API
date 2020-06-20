from flask import Flask, jsonify, request, session
from urllib.parse import urlencode


# import requests
app = Flask(__name__)


@ app.route('/', methods=['GET'])
def home():
    return "this is the books home"


app.run(debug=True)
