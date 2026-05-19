# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 19:27:18 2022

@author: USER
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route('/')
def index1():
    #路徑不需加template
    return render_template(r"index.html")

@app.route('/index')
def index2():
    #路徑不需加template
    return render_template(r"abc.html")
	
if __name__=="__main__":
	app.run(debug=True,host='127.0.0.1',port='5000')
