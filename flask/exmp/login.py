# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 19:58:52 2022

@author: USER
"""

from flask import Flask, redirect, url_for, request
from flask import render_template

app = Flask(__name__)


@app.route("/")
def loginPage():
    return render_template(r"login.html")


@app.route("/success/<name>")
def success(name):
    return render_template(r"hello.html", name=name)


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["name"]
        return redirect(url_for("success", name=user))
    else:
        user = request.args.get("name")
        return redirect(url_for("success", name=user))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="8080")
