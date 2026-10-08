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
    return render_template("home.html")

@app.route("/login", methods=["post","get"])
def login():
    return render_template("login.html")

def logout():
    pass

@app.route("/sign_up", methods=["post","get"])
def sign_up():
    global conn,cur
    if request.method == "GET":
        return render_template("sign_up.html") 
    else:
        cur.execute("INSERT INTO users (username, password) VALUES(?,?)",(request.form["username"],request.form["password"]))
        conn.commit()
        return redirect("/login")

def send_message():
    pass

app.run(debug=True)