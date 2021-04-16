import sqlite3

conn = sqlite3.connect('CarRental.db')
c = conn.cursor()

c.execute("""
CREATE TABLE CUSTOMER(
    [CustID]    INTEGER PRIMARY KEY,
    [Name] VARCHAR(30)  NOT NULL,
    [Phone] VARCHAR(15)
);
""")
c.execute("""
CREATE TABLE VEHICLE(
    [VehicleID] VARCHAR(18) PRIMARY KEY,
    [Description]   VARCHAR(30) NOT NULL,
    [Year]  INT NOT NULL,
    [Type]  INT NOT NULL,
    [Category]  INT NOT NULL
);
""")
c.execute("""
CREATE TABLE RENTAL(
    [CustID]    INT NOT NULL,
    [VehicleID] VARCHAR(18) NOT NULL,
    [StartDate] VARCHAR(12) NOT NULL,
    [OrderDate] VARCHAR(12) NOT NULL,
    [RentalType]    INT     NOT NULL,
    [Qty]   INT NOT NULL,
    [ReturnDate]    VARCHAR(12) NOT NULL,
    [TotalAmount]   INT NOT NULL,
    [PaymentDate]   VARCHAR(12),
    FOREIGN KEY(CustID) REFERENCES CUSTOMER(CustID),
    FOREIGN KEY(VehicleID) REFERENCES VEHICLE(VehicleID)
);
""")
c.execute("""
CREATE TABLE RATE(
    [Type]  INT NOT NULL,
    [Category]  INT NOT NULL,
    [Weekly]    INT NOT NULL,
    [Daily] INT NOT NULL
);
""")

conn.commit()
conn.close()