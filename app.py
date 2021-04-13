from flask import Flask, request, render_template

app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/test", methods=["GET"])
def test():
    return render_template('./test.html')

@app.route("/mail", methods=["POST"])
def mail():
    name = request.form['exampleFormControlInput1']
    return render_template('mail.html', \
		message = "あなたのEmailアドレスは" + str(name) + "です。")

@app.route("/crystal", methods=["GET"])
def crystal():
    return render_template("./crystal.html")

@app.route("/crystal_correct", methods=["GET"])
def crystal_correct():
    return render_template("./crystal_correct.html")

@app.route("/crystal_incorrect", methods=["GET"])
def crystal_incorrect():
    return render_template("./crystal_incorrect.html")



 
if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
