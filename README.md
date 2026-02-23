🔐 Flask User Authentication API

A simple backend authentication system built using Flask + SQLite.
This project demonstrates how real websites handle login sessions securely using password hashing and cookies.

---

🚀 Features

- User Signup
- Secure Login (hashed passwords using Werkzeug)
- Session-based Authentication
- Protected Route ("/profile")
- Logout functionality
- Proper database path handling (absolute DB path)

---

🧠 What I Learned

- Difference between Authentication vs Authorization
- How sessions and cookies work
- Why passwords are never stored in plain text
- How a server remembers logged-in users
- Handling multiple users securely

---

🛠 Tech Stack

- Python
- Flask
- SQLite3
- Werkzeug Security (hashing)

---

⚙️ Installation & Setup

1. Clone the repository

git clone https://github.com/anujsinha1429/USER_AUTH_APP.git
cd user_auth_app

2. Create virtual environment

python -m venv venv

Activate:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate

3. Install dependencies

pip install flask werkzeug

4. Run the server

python app.py

Server will start at:

http://127.0.0.1:5000

---

📬 API Endpoints

Signup

"POST /signup"

Body:

{
  "username": "anuj",
  "password": "1234"
}

---

Login

"POST /login"

Body:

{
  "username": "anuj",
  "password": "1234"
}

---

Profile (Protected Route)

"GET /profile"

Requires login session cookie.

---

Logout

"GET /logout"

Destroys session.

---

🔒 Security

- Passwords are hashed using Werkzeug
- Session cookies are signed using Flask secret key
- Unauthorized users cannot access protected routes

---

📌 Future Improvements

- JWT Authentication
- Role-based access (Admin/User)
- Frontend UI
- Database migration to PostgreSQL

---

Author

Anuj Sinha