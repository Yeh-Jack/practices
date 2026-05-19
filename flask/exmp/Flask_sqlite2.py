# -*- coding: utf-8 -*-
"""
Created on Mon May  2 13:31:30 2022

@author: cadtc
"""
import sqlite3 as sql
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index1():
    #路徑不需加template
    return "abc"

@app.route('/enternew')
def new_student():
    return render_template(r'student2.html')

@app.route('/addrec',methods = ['POST','GET'])
def addrec():
    msg="123"
    if request.method =='POST':
        try:
            nm = request.form['nm']
            addr = request.form['addr']
            city = request.form['city']
            pin = request.form['pin']
            with sql.connect("database.db") as con:
                cur=con.cursor()
                cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin))
                con.commit()
            msg="Record successfully added"
        except:
            con.rollback()
            msg="error in insert operation"
        finally:
            return render_template("result2.html",msg=msg)
            con.close()
        

if __name__=="__main__":
	app.run(host='127.0.0.1',port='5000')
    
    