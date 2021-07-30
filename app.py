# coding:utf-8
from flask import Flask, request, render_template

app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('index.html')

#metacrinus
@app.route("/metacrinus", methods=["GET"])
def metacrinus():
    return render_template('metacrinus.html')

@app.route("/metacrinus_correct",methods=["GET"])
def metacrinus_correct():
    return render_template('metacrinus_correct.html')

@app.route("/metacrinus_incorrect",methods=["GET"])
def metacrinus_incorrect():
    return render_template('metacrinus_incorrect.html')

#snowcrystal
@app.route("/snowcrystal", methods=["GET"])
def snowcrystal():
    return render_template('snowcrystal.html')

@app.route("/snowcrystal_correct",methods=["GET"])
def snowcrystal_correct():
    return render_template('snowcrystal_correct.html')

@app.route("/snowcrystal_incorrect",methods=["GET"])
def snowcrystal_incorrect():
    return render_template('snowcrystal_incorrect.html')

#############クイズテンプレート##############

#@app.route("/name", methods=["GET"])
#def get_name():
#    return render_template('name.html')

#@app.route("/name_correct",methods=["GET"])
#def name_correct():
#    return render_template('name_correct.html')

#@app.route("/name_incorrect",methods=["GET"])
#def name_incorrect():
#    return render_template('name_incorrect.html')
###########################################

@app.route("/crystal", methods=["GET"])
def get_crystal():
    return render_template('crystal.html')

if __name__ == "__main__":
    app.debug = True
    app.run(host='127.0.0.1', port=8080)
