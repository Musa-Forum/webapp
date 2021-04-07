# coding:utf-8
from flask import Flask, request, render_template

app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/metacrinus", methods=["GET"])
def get_metacrinus():
    return render_template('metacrinus.html')

@app.route("/crystal", methods=["GET"])
def get_crystal():
    return render_template('crystal.html')

if __name__ == "__main__":
    app.debug = True
    app.run(host='127.0.0.1', port=8080)