import sqlite3

db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT,
    email TEXT
)""")

db.commit()

us_log = input('login: ')
us_pass = input('pass: ')
us_email = input('email: ')

sql.execute("SELECT * FROM users")
if sql.fetchone() is None:
    sql.execute(f"INSERT INTO users VALUES (?, ?, ?)", (us_log, us_pass, us_email))
    db.commit()

    print('Создано')
else:
    print('Уже существует')



