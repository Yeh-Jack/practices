# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 19:27:18 2022

@author: USER
"""

from flask import Flask
from flask import render_template
import sqlite3 as sql
app = Flask(__name__)
@app.route('/list')
def list():
    con=sql.connect("database.db")
    con.row_factory=sql.Row
    
    cur=con.cursor()
    cur.execute("select * from students")
    
    rows = cur.fetchall();
    return render_template("list.html",rows=rows)

if __name__=="__main__":
	app.run(debug=True,host='127.0.0.1',port='5000')
