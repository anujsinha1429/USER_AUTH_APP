User Auth App (Flask Backend)

A simple backend authentication system built using Python Flask and SQLite.

Features

- User Signup API
- Password Hashing (Werkzeug Security)
- Login Authentication
- Proper HTTP Status Codes
- SQLite Database Integration

Tech Stack

- Python
- Flask
- SQLite3
- Werkzeug Security

API Endpoints

Signup

"POST /signup"

Request Body:

{
  "username": "anuj",
  "password": "1234"
}

Login

"POST /login"

Request Body:

{
  "username": "anuj",
  "password": "1234"
}

What I Learned

- How backend APIs work
- Database integration with Flask
- Password hashing and verification
- Handling authentication logic