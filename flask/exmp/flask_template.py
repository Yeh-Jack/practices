# -*- coding: utf-8 -*-
"""
Created on Mon May  2 09:29:00 2022

@author: cadtc
"""

from flask import Flask,render_template

app = Flask(__name__)


@app.route("/hello/<user>")
def hello_name(user):
    return render_template('hello.html',name=user)

if __name__=="__main__":
	app.run(debug=True,host='127.0.0.1',port='5000')