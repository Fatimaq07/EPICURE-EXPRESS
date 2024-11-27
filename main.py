from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import mysql.connector
import bcrypt
from jose import JWTError, jwt
from typing import Optional

# Configuration
SECRET_KEY = "your_jwt_secret_key"  # Secret key for encoding JWT
ALGORITHM = "HS256"  # Algorithm for encoding JWT

app = FastAPI()

# MySQL Connection Function
def get_db_connection():
    """
    Connect to MySQL database.
    """
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Replace with your MySQL password
            database="epicure_express"
        )
    except mysql.connector.Error as err:
        raise HTTPException(status_code=500, detail="Database connection error")

class User(BaseModel):
    """
    Data model for user input (sign-up and login).
    """
    username: str
    password: str

# Sign-Up Route
@app.post("/signup")
async def signup(user: User):
    """
    Handle user sign-up by storing hashed password in the database.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", 
                       (user.username, hashed_password.decode('utf-8')))
        conn.commit()
        return {"message": "User registered successfully"}
    except mysql.connector.Error as err:
        raise HTTPException(status_code=400, detail="Username already exists")
    finally:
        cursor.close()
        conn.close()

# Login Route
@app.post("/login")
async def login(user: User):
    """
    Handle user login by verifying password and generating JWT token.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT username, password FROM users WHERE username = %s", (user.username,))
        result = cursor.fetchone()
        if result and bcrypt.checkpw(user.password.encode('utf-8'), result[1].encode('utf-8')):
            token = jwt.encode({"sub": user.username}, SECRET_KEY, algorithm=ALGORITHM)
            return {"token": token}
        else:
            raise HTTPException(status_code=401, detail="Invalid credentials")
    finally:
        cursor.close()
        conn.close()

# Secure Data Route
@app.get("/secure-data")
async def get_secure_data(token: str = Query(...)):
    """
    Handle access to secure data by decoding JWT token.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return {"message": "This is protected data", "user": payload["sub"]}
    except JWTError:
        raise HTTPException(status_code=403, detail="Invalid token")
