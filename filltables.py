import sqlite3
import csv

conn = sqlite3.connect('CarRental.db')
c = conn.cursor()

with open('./entryfiles/CUSTOMER.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for x in csv_reader:
        c.execute("INSERT INTO CUSTOMER VALUES(:CustID, :Name, :Phone)",{'CustID': x[0], 'Name': x[1], 'Phone': x[2]})
with open('./entryfiles/VEHICLE.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for x in csv_reader:
        c.execute("INSERT INTO VEHICLE VALUES(:VehicleID, :Description, :Year, :Type, :Category)",{'VehicleID': x[0], 'Description': x[1], 'Year': x[2], 'Type': x[3], 'Category': x[4]})
with open('./entryfiles/RENTAL.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for x in csv_reader:
        c.execute("INSERT INTO RENTAL VALUES(:CustID, :VehicleID, :StartDate, :OrderDate, :RentalType, :Qty, :ReturnDate, :TotalAmount, :PaymentDate)",{'CustID': x[0], 'VehicleID': x[1], 'StartDate': x[2], 'OrderDate': x[3], 'RentalType': x[4], 'Qty': x[5], 'ReturnDate': x[6], 'TotalAmount': x[7], 'PaymentDate': x[8]})
with open('./entryfiles/RATE.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for x in csv_reader:
        c.execute("INSERT INTO RATE VALUES(:Type, :Category, :Weekly, :Daily)",{'Type': x[0], 'Category': x[1], 'Weekly': x[2], 'Daily': x[3]})

conn.commit()
conn.close()