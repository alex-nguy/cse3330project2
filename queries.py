import sqlite3

conn = sqlite3.connect('CarRental.db')
c = conn.cursor()


conn.commit()
conn.close()