import sqlite3
from flask import Flask,request,jsonify
from werkzeug.security import generate_password_hash , check_password_hash


app= Flask(__name__)

# @app.route("/")
# def home():
#     return "Backend project started"

# if __name__ == "__main__":
#     app.run(debug=True)

def initdb():
    conn=sqlite3.connect("user.db")
    cursor=conn.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT,
                   username TEXT UNIQUE,
                   password TEXT )
""")
    conn.commit()
    conn.close()

@app.route("/signup",methods=["POST"])
def signup():
    data=request.get_json()
    username=data.get("username")
    password=data.get("password")

    # validation 
    if not username or not password:
        return jsonify({"error":"username and password required "}),400
    try:
        conn=sqlite3.connect("user.db")
        cursor=conn.cursor()
        hashed_password=generate_password_hash(password)
        cursor.execute(" INSERT INTO users (username ,password) VALUES (?,?)",(username,hashed_password))
        conn.commit()
        conn.close()
        return jsonify({"message ": "user created succcessfully"}),201

    except:
        return jsonify({"error":"username already exists"}),409    

if __name__=="__main__":
    initdb()
    app.run(debug=True)    