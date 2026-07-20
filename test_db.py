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

def per_field_update():
    update = input("Would you like to change any existing data? Yes/No ")
    if update == "Yes":
        data_change = input("Select from: age, income, savings, spending ")
        if data_change == "age":
            new_age = int(input("What would you like to update your age too? "))
            cursor.execute("UPDATE user_info SET age = ? WHERE name = ?", (new_age, name, ))
            print("Age record updated")
        if data_change == "income":
            new_income = float(input("What would you like your new income to be updated too? "))
            cursor.execute("UPDATE user_info SET income = ? WHERE name = ?", (new_income, name, ))
            print("Income record updated")
        if data_change == "savings":
            new_savings = float(input("What would you like your new savings to be updated too? "))
            cursor.execute("UPDATE user_info SET savings = ? WHERE name = ?", (new_savings, name, ))
            print("Savings record updated")
        if data_change == "spending":
            new_spending = float(input("What would you like your new spending to be set too? "))
            cursor.execute("UPDATE user_info SET spending = ? WHERE name = ?", (new_spending, name, ))
            print("Spending record updated")
    else: 
        print("Data will stay as is.")


if result is None:
    cursor.execute(
        "INSERT INTO user_info VALUES (?, ?, ?, ?, ?)",
        (name, age, income, savings, spending)
    )
    print("New record inserted.")
else: 
    print("Data will stay as is unless you want to update.")
    per_field_update()


cursor.execute("SELECT * FROM user_info")
print(cursor.fetchall())


connection.commit()
connection.close()