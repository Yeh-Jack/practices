# -*- coding: utf-8 -*-
"""
Created on Mon May  2 10:32:28 2022

@author: cadtc
"""

from flask import Flask,render_template

app = Flask(__name__)


@app.route("/result")
def result():
    dict = {'pyh':59,'che':60,'maths':90}
    return render_template('result.html',result=dict)

if __name__=="__main__":
    app.run(host='127.0.0.1',port='5000')
# 	app.run(debug=True,host='127.0.0.1',port='5000')