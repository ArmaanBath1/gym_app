import sqlite3
import os
os.system('clear')
connection = sqlite3.connect("customer.db")
cursor = connection.cursor()

command1 = """CREATE TABLE IF NOT EXISTS
customer (first_name text, last_name text, email text)"""

cursor.execute(command1)

cursor.execute("INSERT INTO customer VALUES ('Armaan', 'Bath', armaanbath@gmail.com')")
cursor.execute("INSERT INTO customer VALUES ('Veer', 'Parmar', veerparmar@gmail.com')")
print("Records added to the table")

print ("---------------------------- \n Cutomer  Table")
cursor.execute("SELECT * FROM customer ")
connection .commit()
results = cursor.fetchall()
print(results)

print(" FName" + " " + "Surname" + " " + "email")
for item in results:
    print(item[0] + " "+ item[1] + " " + item[2] )
    print("\n")

    cursor.close()