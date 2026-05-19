# -*- coding: utf-8 -*-
"""
Created on Mon May  2 11:33:39 2022

@author: cadtc
"""


from flask import Flask,render_template,request

app = Flask(__name__)


@app.route("/")
def student():
    return render_template(r'student.html')

@app.route("/result1",methods = ['POST','GET'])
def result1():
    if request.method =='POST':
        result = request.form
        return render_template(r'result1.html',result=result)

if __name__=="__main__":
	app.run(debug=True,host='127.0.0.1',port='5000')