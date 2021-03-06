# -*- coding: utf-8 -*-
"""
@author: Katherine Samuel


"""

#import statements
from flask import Flask, render_template

#Flask app variable
app = Flask(__name__)

#static route
@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/assignments")
def assignments():
    return render_template("1006.html")

@app.route("/courses")
def classes():
    return render_template("courses.html")

#start the server
if __name__ == "__main__":
    app.run()