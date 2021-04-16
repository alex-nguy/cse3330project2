import sqlite3

conn = sqlite3.connect('CarRental.db')
c = conn.cursor()

# Prints all values in CUSTOMER Table
# c.execute("SELECT * FROM CUSTOMER")
# print(c.fetchall())

# QUESTION 1
newName = input("Enter your name: ")
c.execute("INSERT INTO CUSTOMER(Name) VALUES(:newName)", {'newName': newName})

# QUESTION 2
c.execute("UPDATE CUSTOMER SET Phone = '(837) 721-8965' WHERE Name = :newName", {'newName': newName})

# # Checks Question 1 & 2
# c.execute("SELECT CustID, Name, Phone FROM CUSTOMER WHERE Phone = '(837) 721-8965'")
# print(c.fetchall())

# QUESTION 3
c.execute("UPDATE RATE SET Daily = Daily * 1.05 WHERE Category = 1")

# # Checks Question 3
# c.execute("SELECT Daily FROM RATE WHERE Category = 1")
# print(c.fetchall())

# QUESTION 4a
c.execute("INSERT INTO VEHICLE VALUES('5FNRL6H58KB133711', 'Honda Odyssey', 2019, 6, 1)")

# Checks Question 4a
# c.execute("SELECT * FROM VEHICLE WHERE VehicleID = '1GB3KZCG1EF117132'")
# print(c.fetchall())
# print(c.fetchall())

# QUESTION 4b
c.execute("INSERT INTO RATE VALUES(5, 1, 900.00, 150.00), (6, 1, 800.00, 135.00)")

# Checks Question 4b
# c.execute("SELECT * FROM RATE")
# print(c.fetchall())

# QUESTION 5
c.execute("SELECT VEHICLE.VehicleID, VEHICLE.Description, VEHICLE.Year FROM VEHICLE, RENTAL WHERE VEHICLE.Type = 1 AND VEHICLE.Category = 1 AND RENTAL.StartDate BETWEEN DATE('2019-06-01') AND DATE('2019-06-20')")
print(c.fetchall())

# QUESTION 6
c.execute("SELECT CUSTOMER.Name, SUM(RENTAL.TotalAmount) FROM CUSTOMER, RENTAL WHERE CUSTOMER.CustID = 221 AND RENTAL.PaymentDate IS NULL")
print(c.fetchall())

# QUESTION 7
c.execute("
SELECT VEHICLE.VehicleID AS VIN, 
    VEHICLE.Description, 
    VEHICLE.Year, 
    CASE VEHICLE.Type
        WHEN 1 THEN 'Compact'
        WHEN 2 THEN 'Medium'
        WHEN 3 THEN 'Large'
        WHEN 4 THEN 'SUV'
        WHEN 5 THEN 'Truck'
        WHEN 6 THEN 'VAN'
        END Type, 
    CASE VEHICLE.Category
        WHEN 0 THEN 'Basic'
        WHEN 1 THEN 'Luxury'
        END Category, 
    RATE.Weekly, 
    RATE.Daily  
FROM VEHICLE, RATE 
WHERE VEHICLE.Type = RATE.Type AND VEHICLE.Category = RATE.Category
ORDER BY Category DESC, VEHICLE.Type ASC)
print(c.fetchall())

# QUESTION 8
c.execute("SELECT SUM(TotalAmount) FROM RENTAL WHERE PaymentDate < DATE('now')")
print(c.fetchall())

# Checks Question 9a

# Checks Question 9b

# Checks Question 10
c.execute("SELECT DISTINCT	c.Name, r.StartDate, r.ReturnDate, r.TotalAmount
            FROM	RENTAL r, CUSTOMER c, VEHICLE v
            WHERE	r.RentalType == 7 AND v.VehicleID == "19VDE1F3XEE414842" AND r.CustID == c.CustID AND r.PaymentDate IS NULL")

# Checks Question 11
c.execute("SELECT	c.CustID, c.Name, c.Phone
            FROM	CUSTOMER c,
            LEFT JOIN RENTAL ON c.CustID == RENTAL.CustID
            WHERE	RENTAL.CustID IS NULL")

# Checks Question 12
c.execute("SELECT DISTINCT c.Name, v.Description, r.StartDate, r.ReturnDate, r.TotalAmount
            FROM	CUSTOMER c, RENTAL r, VEHICLE v
            WHERE	c.CustID == r.CustID AND r.StartDate == r.PaymentDate AND v.VehicleID == r.VehicleID
            ORDER BY c.Name")

conn.commit()
conn.close()