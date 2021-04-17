import sqlite3

conn = sqlite3.connect('CarRental.db')
c = conn.cursor()

# QUESTION 1
newName = input("Enter your name: ")
c.execute("INSERT INTO CUSTOMER(Name) VALUES(:newName)", {'newName': newName})

# QUESTION 2
c.execute("UPDATE CUSTOMER SET Phone = '(837) 721-8965' WHERE Name = :newName", {'newName': newName})

# QUESTION 3
c.execute("UPDATE RATE SET Daily = Daily * 1.05 WHERE Category = 1")

# QUESTION 4a
c.execute("INSERT INTO VEHICLE VALUES('5FNRL6H58KB133711', 'Honda Odyssey', 2019, 6, 1)")

# QUESTION 4b
c.execute("INSERT INTO RATE VALUES(5, 1, 900.00, 150.00), (6, 1, 800.00, 135.00)")

# QUESTION 5
c.execute("SELECT VEHICLE.VehicleID, VEHICLE.Description, VEHICLE.Year FROM VEHICLE, RENTAL WHERE VEHICLE.Type = 1 AND VEHICLE.Category = 1 AND RENTAL.StartDate BETWEEN DATE('2019-06-01') AND DATE('2019-06-20')")

# QUESTION 6
c.execute("SELECT CUSTOMER.Name, SUM(RENTAL.TotalAmount) FROM CUSTOMER, RENTAL WHERE CUSTOMER.CustID = 221 AND RENTAL.PaymentDate IS NULL")

# QUESTION 7
c.execute("""
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
ORDER BY Category DESC, VEHICLE.Type ASC""")

# QUESTION 8
c.execute("SELECT SUM(TotalAmount) FROM RENTAL WHERE PaymentDate < DATE('now')")

# Checks Question 9a
c.execute("""
SELECT v.Description, 
    v.Year, 
    CASE v.Type
        WHEN 1 THEN 'Compact'
        WHEN 2 THEN 'Medium'
        WHEN 3 THEN 'Large'
        WHEN 4 THEN 'SUV'
        WHEN 5 THEN 'Truck'
        WHEN 6 THEN 'VAN'
        END Type,
    CASE v.Category
        WHEN 0 THEN 'Basic'
        WHEN 1 THEN 'Luxury'
        END Category,
    r.TotalAmount / r.Qty AS UnitPrice,
    CASE
        WHEN julianday(r.returndate) - julianday(r.startdate) = 1 THEN (julianday(r.returndate) - julianday(r.startdate)) || ' Day'
        WHEN julianday(r.returndate) - julianday(r.startdate) < 7 THEN (julianday(r.returndate) - julianday(r.startdate)) || ' Days'
        WHEN julianday(r.returndate) - julianday(r.startdate) = 7 THEN ((julianday(r.returndate) - julianday(r.startdate)) / 7) || ' Week'
        ELSE ((julianday(r.returndate) - julianday(r.startdate)) / 7) || ' Weeks'
        END TotalDuration,
    CASE r.rentaltype
        WHEN 1 THEN 'Daily'
        When 7 THEN 'Weekly'
        END RentalType,
    CASE When r.PaymentDate IS NULL
        THEN 'Unpaid'
        ELSE 'Paid'
        END PaymentStatus,
    r.TotalAmount
FROM VEHICLE v
INNER JOIN RENTAL r
ON r.VehicleID = v.VehicleID
INNER JOIN CUSTOMER c
ON r.CustID = c.CustID AND c.Name = 'J. Brown'
ORDER By r.StartDate""")

# Checks Question 9b
c.execute("""SELECT SUM(r.TotalAmount) 
            FROM CUSTOMER c
            INNER JOIN RENTAL r
            ON r.CustID = c.CustID AND c.Name = 'J. Brown'
            WHERE r.PaymentDate IS NULL""")

# Checks Question 10
c.execute("""SELECT DISTINCT	c.Name, r.StartDate, r.ReturnDate, r.TotalAmount
            FROM	RENTAL r, CUSTOMER c, VEHICLE v
            WHERE	r.RentalType == 7 AND v.VehicleID == '19VDE1F3XEE414842' AND r.CustID == c.CustID AND r.PaymentDate IS NULL""")


# Checks Question 11
c.execute("""SELECT	c.CustID, c.Name, c.Phone
            FROM	CUSTOMER c
            LEFT JOIN RENTAL ON c.CustID = RENTAL.CustID
            WHERE	RENTAL.CustID IS NULL""")

# Checks Question 12
c.execute("""SELECT DISTINCT c.Name, v.Description, r.StartDate, r.ReturnDate, r.TotalAmount
            FROM	CUSTOMER c, RENTAL r, VEHICLE v
            WHERE	c.CustID == r.CustID AND r.StartDate == r.PaymentDate AND v.VehicleID == r.VehicleID
            ORDER BY c.Name""")


conn.commit()
conn.close()