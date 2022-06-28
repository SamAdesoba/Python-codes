import sqlite3
# if you don't want to use commit and close, you can start with
# with connection = sqlite3.connect("testdb.db") as connection
connection = sqlite3.connect("testdb.db")
cursor = connection.cursor()
# cursor.execute('CREATE TABLE User(name TEXT, age INT);')
# cursor.execute(f'INSERT INTO User VALUES ("ADESOBA", 34)')
# cursor.execute('SELECT * FROM User')
# print(cursor.fetchone())
# To avoid SQL injection, i.e to avoid vulnerability, you can insert like this
name = "Uche"
age = 100
cursor.execute('INSERT INTO User VALUES (?,?)', (name, age))
# cursor.execute("")
# cursor.executemany("")
# cursor.executescript("")
connection.commit()
cursor.close()
