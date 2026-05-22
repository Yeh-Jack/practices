# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 19:27:18 2022

@author: USER
"""

from flask import Flask, redirect, url_for, request
from flask import render_template
import sqlite3 as sql

DB_NAME = "Weight_Loss_Competition"


def advise(bmi):
    if bmi < 18.5:
        return "「體重過輕」，需要多運動，均衡飲食，以增加體能，維持健康！"
    elif bmi >= 18.5 and bmi < 24:
        return "恭喜！「健康體重」，要繼續保持！"
    elif bmi >= 24 and bmi < 27:
        return "「體重過重」了，要小心囉，趕快力行「健康體重管理」！"
    else:
        return "啊～「肥胖」，需要立刻力行「健康體重管理」囉！"


def calculateBMI(weight, height):
    return weight / (height * height)


def initDB():
    # Initiate database.
    conn = sql.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS bmi (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            gender TEXT NOT NULL,
            height REAL NOT NULL,
            weight REAL NOT NULL
        );  """)
    conn.commit()


# Initiate the web server.
app = Flask(__name__)
initDB()


@app.route("/")
def root():
    return render_template(r"index.html")


@app.route("/data_input")
def data_input():
    return render_template(r"data_input.html")


@app.route("/list_user", methods=["GET"])
def list_user():
    conn = sql.connect(DB_NAME)
    conn.row_factory = sql.Row
    cur = conn.cursor()
    cur.execute("SELECT * from bmi ORDER BY name")
    data = cur.fetchall()

    # Append 'bmi' and 'advise' columns.
    rows = []
    for row in data:
        new_row = dict(row)  # convert Row to dict
        bmi = calculateBMI(new_row["weight"], new_row["height"])
        new_row["bmi"] = bmi
        new_row["advise"] = advise(bmi)
        rows.append(new_row)

    return render_template(r"bmi.html", rows=rows)


@app.route("/submit", methods=["POST"])
def submit():
    form = request.form
    try:
        height = float(form["height"])
        weight = float(form["weight"])
        bmi = calculateBMI(weight, height)
        data = (
            form["name"],
            form["gender"],
            height,
            weight,
        )
        row = {
            "name": form["name"],
            "gender": form["gender"],
            "height": height,
            "weight": weight,
            "bmi": bmi,
            "advise": advise(bmi),
        }
    except ValueError:
        return "Height and Weight must be numbers!"

    conn = sql.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("INSERT INTO bmi (name, gender, height, weight) \
                VALUES (?, ?, ?, ?)", data)
    conn.commit()

    rows = []
    rows.append(row)
    return render_template(r"bmi.html", rows=rows)


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port="5000")
