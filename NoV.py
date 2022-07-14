import os
import sys
from flask import Flask, request, render_template
import requests
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route("/receive_get", methods=["GET"])
def receive_get():
    name = request.args["my_name"]
    if len(name) == 0:
        return "アドレスが未入力です"
    else:
        email = str(name)
        email_format = "{}"
        FMTemail = email_format.format(email)
        url = "デプロイする?new_email={}"
        url = url.format(FMTemail)
        url = requests.get(url)
        text = url.text
        return 'あなたの来館は' + str(text) + "回目です。"

if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0',port=8080)
