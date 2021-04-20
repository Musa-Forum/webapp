# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def metacrinus():
    return render_template('metacrinus.html')
@app.route('/metacrinuscorrect')
def metacrinuscorrect():
    return render_template('metacrinus_correct.html')
@app.route('/metacrinusincorrect')
def metacrinusincorrect():
    return render_template('metacrinus_incorrect.html')
"""
@app.route('/')
def index():
    return render_template('index.html')
@app.route("/receive_get", methods=["GET"])
def receive_get():
    name = request.args["my_name"]
    if len(name) == 0:
        return "名前が未入力です"
    else:
        return 'あなたが入力した名前は' + str(name) + "です"
"""
if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0',port=8080)
