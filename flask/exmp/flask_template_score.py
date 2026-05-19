# -*- coding: utf-8 -*-
"""
Created on Mon May  2 10:31:26 2022

@author: cadtc
"""

from flask import Flask,render_template

app = Flask(__name__)


@app.route("/score/<int:score>")
def hello_score(score):
    return render_template('score.html',marks=score)

if __name__=="__main__":
    app.run(host='127.0.0.1',port='5000')
# 	app.run(debug=True,host='127.0.0.1',port='5000')