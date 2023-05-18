def create_database():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT,
            password TEXT
        )
    ''')

    conn.commit()
    conn.close()
# I can hide the passwords and create that with this due to the fact of all my vs errors I am not adding until I get fixed tomorrow and we decide which one we go with. I have to fix what I had to download for the other one that I thought I didn't I accidentally downloaded the wrong one and messed up my system because I stayed up too late and started making errors grrrr!! 