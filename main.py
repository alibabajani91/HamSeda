import requests
import sqlite3
from flask import *


app = Flask(__name__)
conn = sqlite3.connect("database.db")
cur = conn.cursor()


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["post","get"])
def login():
    return render_template("login.html")

def logout():
    pass

def sign_up():
    pass

def send_message():
    pass

app.run(debug=True)