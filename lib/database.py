import sqlite3

def create_database():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY_KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        )
    ''')

    conn.commit()
    conn.close()

create_database()