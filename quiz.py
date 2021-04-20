# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 18:46:00 2021

@author: meite
"""

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def quiz():
    return render_template('quiz.html')
@app.route('/quizcorrect')
def quizcorrect():
    return render_template('quizcorrect.html')
@app.route('/quizwrong')
def quizwrong():
    return render_template('quizwrong.html')
if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0',port=8080)