# coding:utf-8
from flask import Flask, request, render_template

app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/metacrinus", methods=["GET"])
def get_metacrinus():
    return render_template('layout_quiz.html',
                           title="ウミユリクイズ",
                           message="ウミユリっていつから生きているの？",
                           picture="/static/images/1_umiyurikun_siruetto.png",
                           choice1="約500,000,000～250,000,000年前から",
                           choice2="約250,000,000～150,000,000年前から",
                           choice3="約150,000,000年前から")

#############クイズテンプレート##############

#@app.route("/name", methods=["GET"])
#def get_name():
#    return render_template('layout_quiz.html',
#                           title="",
#                           message="",
#                           picture="",
#                           choice1="",
#                           choice2="",
#                           choice3="")

###########################################

@app.route("/crystal", methods=["GET"])
def get_crystal():
    return render_template('crystal.html')

if __name__ == "__main__":
    app.debug = True
    app.run(host='127.0.0.1', port=8080)
