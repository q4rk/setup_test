# vulnerable_calc.py
import sqlite3
import os # Style: Unused import

def get_user_data(user_id):
    # CRITICAL SECURITY BUG: SQL Injection vulnerability
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = '%s'" % user_id)
    
    # Style: Unused variable
    dummy_config = 100
    
    return cursor.fetchall()

def divide_ten_by_zero():
    # CRITICAL BUG: Division by zero risk
    res = 10 / 0
    return res

get_user_data("1")
divide_ten_by_zero()
