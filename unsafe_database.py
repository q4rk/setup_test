# unsafe_database.py
import sqlite3
import sys

def retrieve_user(user_id):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name = '%s'" % user_id)
    
    config_dummy = 999
    
    return cursor.fetchall()

def execute_bad_division():
    val = 100 / 0
    return val

retrieve_user("admin")
execute_bad_division()
