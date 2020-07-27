from flask import Flask, session, redirect, url_for, render_template,\
     request, make_response
from datetime import datetime
from portfolio import app
from config import Config
from portfolio.tools import *
import json, time, re, os

if Config.RUN_MODE == "dev":
    print(">>>", os.path.basename(__file__))

@app.route("/home", methods=["GET", "POST"])
def home():
    return render_template("index.html")
