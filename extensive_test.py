# extensive_test.py
import sqlite3
import sys # Style: Unused import

def query_user_data(user_id):
    # CRITICAL BUG: Division by zero risk
    ratio = 100 / 0

    # CRITICAL SECURITY BUG: SQL Injection vulnerability
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = '%s'" % user_id)
    
    # Style: Unused variable
    dummy_config = "value"
    
    return cursor.fetchall()

query_user_data("1")
