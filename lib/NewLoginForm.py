def register_user(email, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    c.execute('INSERT INTO users (email, password) VALUES (?, ?)', (email, password))

    conn.commit()
    conn.close()
#This function takes the email and password as parameters and inserts them into the users table.


def login_user(email, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    c.execute('SELECT * FROM users WHERE email=? AND password=?', (email, password))
    user = c.fetchone()

    conn.close()

    return user  # Returns None if no user is found, otherwise returns the user data


#import bcrypt

#def register_user(email, password):
    # conn = sqlite3.connect('users.db')
    # c = conn.cursor()

    # hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # c.execute('INSERT INTO users (email, password) VALUES (?, ?)', (email, hashed_password))

    # conn.commit()
    # conn.close()

#In this code, the bcrypt.hashpw() function is used to hash the password before storing it in the database. The gensalt() function generates a random salt value for added security.


#def login_user(email, password):
    # conn = sqlite3.connect('users.db')
    # c = conn.cursor()

    # c.execute('SELECT * FROM users WHERE email=?', (email,))
    # user = c.fetchone()

    # conn.close()

    # if user and bcrypt.checkpw(password.encode('utf-8'), user[2]):
    #     return user
    # else:
    #     return None




#Here, the bcrypt.checkpw() function is used to compare the hashed password from the login input with the stored hashed password in the database. If the passwords match, the user is authenticated.

# By using bcrypt for password hashing, even if someone gains unauthorized access to the database, they won't be able to retrieve the original passwords. The hashing process with bcrypt is designed to be computationally expensive, making it difficult for attackers to perform brute-force or dictionary-based attacks.

# It's worth mentioning that this is a simplified implementation, and in real-world scenarios, you should consider additional security measures such as using a stronger hashing algorithm, adding a unique key per user, and following security best practices to further protect user information. So we have an extra security layer to show Morgan. Wanted to show you all of what was worked on since I had errors with what I expected to get working I should be able to tomorrow but we can have both as well so we have a table and something to pull up idk whatever you guys think?