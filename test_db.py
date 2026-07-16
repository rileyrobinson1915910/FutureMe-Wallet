import sqlite3

# define connection and cursor

connection = sqlite3.connect('users_name.db')

cursor = connection.cursor()

# create username table

command1 = """CREATE TABLE IF NOT EXISTS user_info (name TEXT PRIMARY KEY, age INTEGER, income REAL, savings REAL, spending REAL)"""

cursor.execute(command1)

name = "Riley"

age = 18

income = 300.00

savings = 200.00

spending = 100.000

# add user_info

cursor.execute("INSERT INTO user_info VALUES (?, ?, ?, ?, ? )", (name, age, income, savings, spending))

cursor.execute("SELECT * FROM user_info")

print(cursor.fetchall())

connection.commit()

connection.close()

cursor.execute("UPDATE user_info SET age = ? WHERE name = 'result'")

result = cursor.fetchone()

def age_name_update(name):
    if name == 'result':
        answer = print("result already detected, would you like to ovverride with new info? Y/N")
    if answer == "Y":
        cursor.execute("UPDATE user_info SET age = ? WHERE name = 'result'")
    else:
       cursor.execute("INSERT INTO user_info VALUES (?)", (result,))
 

