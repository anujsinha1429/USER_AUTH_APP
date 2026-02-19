import sqlite3
from flask import Flask,request,jsonify
from werkzeug.security import generate_password_hash , check_password_hash
import os 
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
DB_PATH=os.path.join(BASE_DIR,"user.db")


app= Flask(__name__)

# @app.route("/")
# def home():
#     return "Backend project started"

# if __name__ == "__main__":
#     app.run(debug=True)

def initdb():
    conn=sqlite3.connect(DB_PATH)
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
        conn=sqlite3.connect(DB_PATH)
        cursor=conn.cursor()
        hashed_password=generate_password_hash(password)
        cursor.execute(" INSERT INTO users (username ,password) VALUES (?,?)",(username,hashed_password))
        conn.commit()
        conn.close()
        return jsonify({"message ": "user created succcessfully"}),201

    except sqlite3.IntegrityError:
        return jsonify({"error":"username already exists"}),409 

         
    
@app.route("/login",methods=["POST"])
def login():
    data=request.get_json()
    username=data.get("username")
    password=data.get("password")
    if not username or not password:
        return jsonify({"error":"username and password required"}),400
    conn=sqlite3.connect(DB_PATH)
    cursor=conn.cursor()

    cursor.execute("SELECT password FROM users WHERE username =? ",(username,))
    user=cursor.fetchone()
    conn.close()
    if user is None:
        return jsonify({"error":"user not found "}),404
    stored_hash=user[0]
    if check_password_hash(stored_hash,password):
        return jsonify({"message":"login successfulllly "}),200
    else:
        return jsonify({"error": "Invalid credential"}),400  
if __name__=="__main__":
    initdb()
    app.run(debug=True)
  