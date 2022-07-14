# coding:utf-8
from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        email = request.form['email']
        if len(email) == 0:
            return "アドレスが未入力です"
        else:
            email_format = "{}"
            FMTemail = email_format.format(email)
            url = "https://script.google.com/macros/s/AKfycbwKwib2ecgzkCrdbZP2zvodJxuL3oG2eh5aNpouQ6PX7sFHFCBt-ihEt-daLmnRbxP4/exec?new_email={}"
            url = url.format(FMTemail)
            url = requests.get(url)
            text = url.text
        return render_template('quiztop.html', email = email)

#metacrinus
@app.route("/metacrinus", methods=["GET"])
def metacrinus():
    return render_template('/metacrinus/metacrinus.html')

@app.route("/metacrinus_correct",methods=["GET"])
def metacrinus_correct():
    return render_template('/metacrinus/metacrinus_correct.html')

@app.route("/metacrinus_incorrect",methods=["GET"])
def metacrinus_incorrect():
    return render_template('/metacrinus/metacrinus_incorrect.html')

#snowcrystal
@app.route("/snowcrystal", methods=["GET"])
def snowcrystal():
    return render_template('/snowcrystal/snowcrystal.html')

@app.route("/snowcrystal_correct",methods=["GET"])
def snowcrystal_correct():
    return render_template('snowcrystal/snowcrystal_correct.html')

@app.route("/snowcrystal_incorrect",methods=["GET"])
def snowcrystal_incorrect():
    return render_template('snowcrystal/snowcrystal_incorrect.html')

#concretion
@app.route("/concretion",methods=["GET"])
def concretion():
    return render_template('/concretion/concretion.html')

@app.route("/concretion_correct",methods=["GET"])
def concretion_correct():
    return render_template('/concretion/concretion_correct.html')

@app.route("/concretion_incorrect",methods=["GET"])
def concretion_incorrect():
    return render_template('/concretion/concretion_incorrect.html')

#tetsuo
@app.route("/tetsuo",methods=["GET"])
def tetsuo():
    return render_template('/tetsuo/tetsuo.html')

@app.route("/tetsuo_correct",methods=["GET"])
def tetsuo_correct():
    return render_template('/tetsuo/tetsuo_correct.html')

@app.route("/tetsuo_incorrect",methods=["GET"])
def tetsuo_incorrect():
    return render_template('/tetsuo/tetsuo_incorrect.html')

#kuma
@app.route("/kuma",methods=["GET"])
def kuma():
    return render_template('/kuma/kuma.html')

@app.route("/kuma_correct",methods=["GET"])
def kuma_correct():
    return render_template('/kuma/kuma_correct.html')

@app.route("/kuma_incorrect",methods=["GET"])
def kuma_incorrect():
    return render_template('/kuma/kuma_incorrect.html')


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


if __name__ == "__main__":
    app.debug = True
    app.run(host='127.0.0.1', port=8080)
