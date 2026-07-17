import sqlite3

connection = sqlite3.connect('users_name.db')
cursor = connection.cursor()

command1 = """CREATE TABLE IF NOT EXISTS user_info (name TEXT PRIMARY KEY, age INTEGER, income REAL, savings REAL, spending REAL)"""
cursor.execute(command1)

name = "Riley"
age = 18
income = 300.00
savings = 200.00
spending = 100.000

cursor.execute("SELECT name FROM user_info WHERE name = ?", (name,))
result = cursor.fetchone()

if result is None:
    cursor.execute(
        "INSERT INTO user_info VALUES (?, ?, ?, ?, ?)",
        (name, age, income, savings, spending)
    )
    print("New record inserted.")
else:
    answer = input("Name already found, would you like to override with new info? Y/N: ")
    if answer == "Y":
        cursor.execute(
            "UPDATE user_info SET age = ?, income = ?, savings = ?, spending = ? WHERE name = ?",
            (age, income, savings, spending, name)
        )
        print("Record updated.")
    else:
        print("Keeping existing data.")

cursor.execute("SELECT * FROM user_info")
print(cursor.fetchall())

connection.commit()
connection.close()