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
            username TEXT UNIQUE,
            password TEXT)
""")

@app.route("/")
def home():
    """home page of site"""
    return render_template("home.html")

@app.route("/login", methods=["post","get"])
def login():
    """login page of site"""
    msg = ""
    conn = sqlite3.connect("database.db",check_same_thread=False)
    cur = conn.cursor()
    if request.method == "POST" and "username" in request.form and "password" in request.form:
        cur.execute("""SELECT * FROM users WHERE username=? AND password=?""",
                    (request.form["username"],request.form["password"]))
        account = cur.fetchone()
        if account:
            session["loggedin"] = True
            session["id"] = account[0]
            session['username'] = account[1]
            msg = "loged in successfully!"
            return redirect('/')
        else:
            msg = "incorrect username/password!"
            return render_template('login.html',msg=msg)
    else: 
        return render_template("login.html",msg=msg)

def logout():
    """this will logout a user"""
    pass

@app.route("/sign_up", methods=["post","get"])
def sign_up():
    """it's the signup page"""
    global conn,cur
    if request.method == "POST" and "username" in request.form and "password" in request.form:
        user = cur.execute("SELECT id FROM users WHERE username = ?",(request.form["username"],)).fetchone()
        if user:
            return render_template("sign_up.html",msg="This username already exists!")
        else:
            cur.execute("INSERT INTO users (username, password) VALUES(?,?)",
                        (request.form["username"],request.form["password"]))
            conn.commit()
            flash("user created.please log in.")
            return redirect("/login")
    else:
        return render_template("sign_up.html") 

def send_message():
    """people can send message here"""

app.run(debug=True)