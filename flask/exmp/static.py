# -*- coding: utf-8 -*-
"""
Created on Mon May  2 10:40:16 2022

@author: cadtc
"""


from flask import Flask,render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('static.html')

if __name__=="__main__":
    app.run(host='127.0.0.1',port='5000')
# 	app.run(debug=True,host='127.0.0.1',port='5000')