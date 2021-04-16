import sqlite3

conn = sqlite3.connect('CarRental.db')
c = conn.cursor()

# Prints all values in CUSTOMER Table
# c.execute("SELECT * FROM CUSTOMER")
# print(c.fetchall())

conn.commit()
conn.close()