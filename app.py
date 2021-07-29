# coding:utf-8
from flask import Flask, request, render_template

app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/metacrinus", methods=["GET"])
def metacrinus():
    return render_template('layout_quiz.html',
                           title="ウミユリクイズ",
                           message="ウミユリっていつから生きているの？",
                           picture="/static/images/1_umiyurikun_siruetto.png",
                           choice1="約500,000,000～250,000,000年前から",
                           answer1="location.href='./metacrinus_correct'",
                           choice2="約250,000,000～150,000,000年前から",
                           answer2="location.href='./metacrinus_incorrect'",
                           choice3="約150,000,000年前から",
                           answer3="location.href='./metacrinus_incorrect'")

@app.route("/metacrinus_correct",methods=["GET"])
def metacrinus_correct():
    return render_template('correct.html',
                           title="ウミユリクイズ",
                           message="ウミユリは約500,000,000年前(オルドビス紀)に出現したとされています。当時の海には他にまっすぐ伸びた殻が特徴的なチョッカクガイや、顎や胸びれの未発達な魚、アランダスピスなど生息していており、無脊椎動物と脊椎動物がともに多様化していった時期として知られています。",
                           picture="/static/images/1_umiyurikun.png")


@app.route("/metacrinus_incorrect",methods=["GET"])
def metacrinus_incorrect():
    return render_template('incorrect.html',
                           title="ウミユリクイズ",
                           quiz="location.href='./metacrinus'")

#############クイズテンプレート##############

#@app.route("/name", methods=["GET"])
#def get_name():
#    return render_template('layout_quiz.html',
#                           title="",
#                           message="問題文",
#                           picture="シルエット画像",
#                           choice1="選択肢",
#                           answer1="正解か不正解かのページ",
#                           choice2="",
#                           answer2="",
#                           choice3="",
#                           answer3="")

#@app.route("/name_correct",methods=["GET"])
#def name_correct():
#    return render_template('correct.html',
#                           title="",
#                           message="解説",
#                           picture="キャラクター写真")
#

#@app.route("/name_incorrect",methods=["GET"])
#def name_incorrect():
#    return render_template('incorrect.html',
#                           title="",
#                           quiz="クイズのページ")

###########################################

@app.route("/crystal", methods=["GET"])
def get_crystal():
    return render_template('crystal.html')

if __name__ == "__main__":
    app.debug = True
    app.run(host='127.0.0.1', port=8080)
