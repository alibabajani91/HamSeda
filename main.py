import sqlite3
import app_config
from flask import *


app = Flask(__name__)
app.secret_key = app_config.secret_key


conn = sqlite3.connect("database.db",check_same_thread=False)
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT)
""")

@app.route("/")
def home():
    """home page of site"""
    return render_template("home.html")

@app.route("/login", methods=["post","get"])
def login():
    """login page of site"""
    return render_template("login.html")

def logout():
    """this will logout a user"""
    pass

@app.route("/sign_up", methods=["post","get"])
def sign_up():
    """it's the signup page"""
    global conn,cur
    if request.method == "GET":
        return render_template("sign_up.html") 
    else:
        cur.execute("INSERT INTO users (username, password) VALUES(?,?)",
                    (request.form["username"],request.form["password"]))
        conn.commit()
        return redirect("/login")

def send_message():
    """people can send message here"""

app.run(debug=True)