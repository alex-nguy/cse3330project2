import tkinter as tk
from tkcalendar import DateEntry
from tkinter import ttk
import sqlite3

conn = sqlite3.connect('CarRental.db')
c = conn.cursor()


def close_window():
    window.destroy()


class Main_Window:
    def __init__(self, parent):
        self.parent = parent
        self.mainwindow = tk.Toplevel(self.parent)
        self.mainwindow.geometry("150x200")
        mw = self.mainwindow

        register_btn = tk.Button(
            mw, text="Register New Customer", width=20, command=self.open_register)
        register_btn.grid(row=0, column=0)

        vehicle_btn = tk.Button(mw, text="Register New Vehicle",
                                width=15, command=self.open_vehicle)
        vehicle_btn.grid(row=1, column=0)

        rental_btn = tk.Button(mw, text="Rent a car",
                               width=15, command=self.open_rent)
        rental_btn.grid(row=2, column=0)

        return_btn = tk.Button(mw, text="Return a car",
                               width=15, command=self.open_return)
        return_btn.grid(row=3, column=0)

        customersearch_btn = tk.Button(mw, text="Search customers",
                                       width=15, command=self.open_customersearch)
        customersearch_btn.grid(row=4, column=0)

        vehiclesearch_btn = tk.Button(mw, text="Search vehicles",
                                      width=15, command=self.open_vehiclesearch)
        vehiclesearch_btn.grid(row=5, column=0)

        mw.protocol("WM_DELETE_WINDOW", close_window)
        mw.mainloop()

    def open_register(self):
        self.mainwindow.destroy()
        Register_Window(self.parent)

    def open_vehicle(self):
        self.mainwindow.destroy()
        Vehicle_Window(self.parent)

    def open_rent(self):
        self.mainwindow.destroy()
        Rent_Window(self.parent)

    def open_return(self):
        self.mainwindow.destroy()
        Return_Window(self.parent)

    def open_customersearch(self):
        self.mainwindow.destroy()
        CustomerSearch_Window(self.parent)

    def open_vehiclesearch(self):
        self.mainwindow.destroy()
        VehicleSearch_Window(self.parent)
        pass


class Register_Window:
    def __init__(self, parent):
        self.parent = parent
        self.registerwindow = tk.Toplevel(self.parent)
        self.registerwindow.geometry("300x200")
        rw = self.registerwindow

        self.user = tk.StringVar()
        self.phone = tk.StringVar()

        # Name field
        name_label = tk.Label(rw, text='Customer Name:',
                              pady=20, padx=10)
        name_label.grid(column=0, row=0)
        name_entry = tk.Entry(rw, textvariable=self.user)
        name_entry.grid(row=0, column=1)
        ########################################################################
        # Phone field
        phone_label = tk.Label(rw, text='Phone Number:',
                               pady=20, padx=10)
        phone_label.grid(row=1, column=0)
        phone_entry = tk.Entry(rw, textvariable=self.phone)
        phone_entry.grid(row=1, column=1)

        submit = tk.Button(rw, text='submit', width=10,
                           command=self.submit_handler)
        submit.grid(row=2, column=1)

        back_button = tk.Button(rw, text='back', width=10, command=self.back)
        back_button.grid(row=2, column=0)
        rw.protocol("WM_DELETE_WINDOW", close_window)
        rw.mainloop()

    def back(self):
        self.registerwindow.destroy()
        Main_Window(self.parent)

    def submit_handler(self):
        newName = self.user.get()
        a = self.phone.get()
        newPhone = '('+a[0]+a[1]+a[2]+') '+a[3] + \
            a[4]+a[5]+'-'+a[6]+a[7]+a[8]+a[9]
        print(newPhone)

        if not self.user.get().isnumeric():
            print("valid name")
            if self.phone.get().isnumeric() and len(self.phone.get()) == 10:
                print("valid number")
                c.execute("INSERT INTO CUSTOMER(Name, Phone) VALUES(:newName, :newPhone)", {
                          'newName': newName, 'newPhone': newPhone})
                conn.commit()
                self.back()
            else:
                print("invalid number")
        else:
            print("invalid name")


class Vehicle_Window:
    def __init__(self, parent):
        self.parent = parent
        self.vehiclewindow = tk.Toplevel(self.parent)
        self.vehiclewindow.geometry("300x350")

        self.vehicleID = tk.StringVar()
        self.desc = tk.StringVar()
        self.year = tk.StringVar()
        self.ty = 0
        self.cat = 0

        self.type = tk.StringVar()
        type_options = ["Compact", "Medium", "Large", "SUV", "Truck", "Van"]

        self.category = tk.StringVar()
        category_options = ["Basic", "Luxury"]

        vw = self.vehiclewindow
        ### VEHICLEID ###
        vehicle_label = tk.Label(vw, text='Enter VehicleID', pady=20, padx=10)
        vehicle_label.grid(row=0, column=0)
        vehicle_entry = tk.Entry(vw, textvariable=self.vehicleID)
        vehicle_entry.grid(row=0, column=1)
        ### CAR DESCRIPTION ###
        desc_label = tk.Label(
            vw, text='Enter Car Description', pady=20, padx=10)
        desc_label.grid(row=1, column=0)
        desc_entry = tk.Entry(vw, textvariable=self.desc)
        desc_entry.grid(row=1, column=1)
        ### MODEL YEAR ###
        year_label = tk.Label(
            vw, text='Enter year of model', pady=20, padx=10)
        year_label.grid(row=2, column=0)
        year_entry = tk.Entry(vw, textvariable=self.year)
        year_entry.grid(row=2, column=1)

        ### CAR TYPE ###
        type_label = tk.Label(
            vw, text='Select Type', pady=20, padx=10)
        type_label.grid(row=3, column=0)
        type_menu = tk.OptionMenu(vw, self.type, *type_options)
        type_menu.grid(row=3, column=1)

        ### CATEGORY ###
        category_label = tk.Label(
            vw, text='Select Category', pady=20, padx=10)
        category_label.grid(row=4, column=0)
        category_menu = tk.OptionMenu(vw, self.category, *category_options)
        category_menu.grid(row=4, column=1)

        ### SEARCH BUTTON ###
        search_btn = tk.Button(
            vw, text="Register", width=15, command=self.register)
        search_btn.grid(row=5, column=1)

        ### BACK BUTTON ###
        return_btn = tk.Button(vw, text="Back", width=15, command=self.back)
        return_btn.grid(row=5, column=0)

        vw.protocol("WM_DELETE_WINDOW", close_window)
        vw.mainloop()

    def register(self):
        type_options = ["Compact", "Medium", "Large", "SUV", "Truck", "Van"]
        carType = 0
        carCategory = 0
        for i in range(len(type_options)):
            if self.type.get() == type_options[i]:
                carType = i + 1

        if self.category.get() == "Basic":
            carCategory = 0
        else:
            carCategory = 1
        c.execute("INSERT INTO VEHICLE VALUES(:VehicleID, :Description, :Year, :Type, :Category)", {'VehicleID': self.vehicleID.get(
        ), 'Description': self.desc.get(), 'Year': self.year.get(), 'Type': carType, 'Category': carCategory})
        conn.commit()
        self.vehiclewindow.destroy()
        Main_Window(self.parent)

    def back(self):
        self.vehiclewindow.destroy()
        Main_Window(self.parent)


class Rent_Window:
    def __init__(self, parent) -> None:
        self.parent = parent
        self.rent_window = tk.Toplevel(self.parent)
        self.rent_window.geometry("600x400")
        rw = self.rent_window

        self.user = tk.StringVar()
        self.ty = 0
        self.cat = 0
        self.startDate = ""
        self.returnDate = ""

        self.type = tk.StringVar()
        type_options = ["Compact", "Medium", "Large", "SUV", "Truck", "Van"]

        self.category = tk.StringVar()
        category_options = ["Basic", "Luxury"]

        ### CAR TYPE ###
        type_label = tk.Label(
            rw, text='Select Type', pady=20, padx=10)
        type_label.grid(row=0, column=0)
        type_menu = tk.OptionMenu(rw, self.type, *type_options)
        type_menu.grid(row=0, column=1)

        ### CATEGORY ###
        category_label = tk.Label(
            rw, text='Select Category', pady=20, padx=10)
        category_label.grid(row=1, column=0)
        category_menu = tk.OptionMenu(rw, self.category, *category_options)
        category_menu.grid(row=1, column=1)

        start_label = tk.Label(rw, text='Rent start date:', pady=20, padx=10)
        start_label.grid(row=2, column=0)
        self.start_cal = DateEntry(rw, width=12, year=2021, month=5, day=4,
                                   background='gray', foreground='white', borderwidth=2)
        self.start_cal.grid(row=2, column=1)

        end_label = tk.Label(rw, text='Return date:', pady=20, padx=10)
        end_label.grid(row=3, column=0)
        self.end_cal = DateEntry(rw, width=12, year=2021, month=5, day=5,
                                 background='gray', foreground='white', borderwidth=2)
        self.end_cal.grid(row=3, column=1)

        ### SEARCH BUTTON ###
        search_btn = tk.Button(
            rw, text="Find available cars", width=15, command=self.search)
        search_btn.grid(row=4, column=1)

        # Reference string value of the selected vehicle using self.vehicle_selected.get()
        self.vehicle_selected = tk.StringVar()
        # Make query call from database to see available cars and form them into an array (options) -- Andy

        ### BACK BUTTON ###
        back_btn = tk.Button(rw, text="Back", width=15, command=self.back)
        back_btn.grid(row=4, column=0)

        rw.protocol("WM_DELETE_WINDOW", close_window)
        rw.mainloop()

    def search(self):
        type_options = ["Compact", "Medium", "Large", "SUV", "Truck", "Van"]
        carType = 0
        carCategory = 0

        for i in range(len(type_options)):
            if self.type.get() == type_options[i]:
                self.ty = i + 1

        if self.category.get() == "Basic":
            self.cat = 0
        else:
            self.cat = 1

        temp = self.start_cal.get().split('/')
        if int(temp[0]) < 10:
            temp[0] = '0' + temp[0]
        if int(temp[1]) < 10:
            temp[1] = '0' + temp[1]
        self.startDate = "20" + temp[2] + '-' + temp[0] + '-' + temp[1]

        temp2 = self.start_cal.get().split('/')
        if int(temp[0]) < 10:
            temp2[0] = '0' + temp2[0]
        if int(temp[1]) < 10:
            temp2[1] = '0' + temp2[1]
        self.returnDate = "20" + temp2[2] + '-' + temp2[0] + '-' + temp2[1]

        c.execute("SELECT VEHICLE.VehicleID, VEHICLE.Description, VEHICLE.Year FROM VEHICLE WHERE VEHICLE.Type = :Type AND VEHICLE.Category = :Category", {
                  'Type': self.ty, 'Category': self.cat, 'startDate': self.startDate, 'returnDate': self.returnDate})
        vehicles = []
        for i in c.fetchall():
            vehicles.append(i[0] + " " + i[1] + " " + str(i[2]))

        rent_label = tk.Label(
            self.rent_window, text='Select an available vehicle', pady=20, padx=10)
        rent_label.grid(row=5, column=0)
        rent_menu = tk.OptionMenu(
            self.rent_window, self.vehicle_selected, *vehicles)
        rent_menu.grid(row=5, column=1)

        name_label = tk.Label(
            self.rent_window, text='Customer ID:', pady=20, padx=10)
        name_label.grid(row=6, column=0)
        name_entry = tk.Entry(self.rent_window, textvariable=self.user)
        name_entry.grid(row=6, column=1)

        ### PAY LATER BUTTON ###
        paylater_btn = tk.Button(
            self.rent_window, text="Pay Later", width=15, command=self.payLater)
        paylater_btn.grid(row=7, column=0)

        ### PAY NOW BUTTON ###
        paynow_btn = tk.Button(
            self.rent_window, text="Pay Now", width=15, command=self.back)
        paynow_btn.grid(row=7, column=1)

    def payLater(self):
        vID = self.vehicle_selected.get().split(' ')[0]
        c.execute("INSERT INTO RENTAL VALUES(:CustID, :VehicleID, :StartDate, :OrderDate, :RentalType, :Qty, :ReturnDate, :TotalAmount, NULL)", {'CustID': int(
            self.user.get()), 'VehicleID': vID, 'StartDate': self.startDate, 'OrderDate': '2021-05-04', 'RentalType': 1, 'Qty': 3, 'ReturnDate': self.returnDate, 'TotalAmount': 1400})
        conn.commit()
        self.back()

    def payNow(self):
        vID = self.vehicle_selected.get().split(' ')[0]
        c.execute("INSERT INTO RENTAL VALUES(:CustID, :VehicleID, :StartDate, :OrderDate, :RentalType, :Qty, :ReturnDate, :TotalAmount, :PaymentDate)", {'CustID': int(self.user.get(
        )), 'VehicleID': vID, 'StartDate': self.startDate, 'OrderDate': '2021-05-04', 'RentalType': 1, 'Qty': 3, 'ReturnDate': self.returnDate, 'TotalAmount': 1400, 'PaymentDate': '2021-05-04'})
        conn.commit()
        self.back()

    def back(self):
        self.rent_window.destroy()
        Main_Window(self.parent)


class Return_Window:
    def __init__(self, parent):
        self.parent = parent
        self.return_window = tk.Toplevel(self.parent)
        self.return_window.geometry("300x300")
        rw = self.return_window

        self.user_name = tk.StringVar()
        self.vehicle_id = tk.StringVar()

        return_label = tk.Label(rw, text='Return date:', pady=20, padx=10)
        return_label.grid(row=0, column=0)
        self.return_cal = DateEntry(rw, width=12, year=2021, month=5, day=4,
                                    background='gray', foreground='white', borderwidth=2)
        self.return_cal.grid(row=0, column=1)

        name_label = tk.Label(rw, text='Enter your name:', pady=20, padx=10)
        name_label.grid(row=1, column=0)
        name_entry = tk.Entry(rw, textvariable=self.user_name)
        name_entry.grid(row=1, column=1)

        vehicle_label = tk.Label(
            rw, text='Enter Vehicle ID:', pady=20, padx=10)
        vehicle_label.grid(row=2, column=0)
        vehicle_entry = tk.Entry(rw, textvariable=self.vehicle_id)
        vehicle_entry.grid(row=2, column=1)

        search_btn = tk.Button(
            rw, text="Search", width=15, command=self.search)
        search_btn.grid(row=3, column=1)

        back_btn = tk.Button(
            rw, text="Back", width=15, command=self.back)
        back_btn.grid(row=3, column=0)

        rw.protocol("WM_DELETE_WINDOW", close_window)
        rw.mainloop()

    def back(self):
        self.return_window.destroy()
        Main_Window(self.parent)

    def search(self):

        # TODO: SEARCH THROUGH DATABASE TO FIND THE SPECIFIC CAR AND PRINT TOTAL DUE FOR THE RENTAL AND UPDATE THE CAR AS RETURNED IN THE DATABASE
        temp = self.return_cal.get().split('/')
        if int(temp[0]) < 10:
            temp[0] = '0' + temp[0]
        if int(temp[1]) < 10:
            temp[1] = '0' + temp[1]
        returnDate = "20" + temp[2] + '-' + temp[0] + '-' + temp[1]

        c.execute("SELECT RENTAL.TotalAmount FROM RENTAL, CUSTOMER WHERE CUSTOMER.Name = :Name AND CUSTOMER.CustID = RENTAL.CustID AND RENTAL.VehicleID = :VehicleID AND RENTAL.ReturnDate == DATE(:ReturnDate)", {
                  'Name': self.user_name.get(), 'VehicleID': self.vehicle_id.get(), 'ReturnDate': returnDate})
        balance = c.fetchall()


class CustomerSearch_Window:
    def __init__(self, parent):
        self.parent = parent
        self.customersearch_window = tk.Toplevel(self.parent)
        self.customersearch_window.geometry("800x800")
        csw = self.customersearch_window

        self.customerID = tk.StringVar()
        self.customer_name = tk.StringVar()

        customerID_label = tk.Label(
            csw, text='Enter customer ID', pady=20, padx=10)
        customerID_label.grid(row=0, column=0)
        customerID_entry = tk.Entry(csw, textvariable=self.customerID)
        customerID_entry.grid(row=0, column=1)

        customerName_label = tk.Label(
            csw, text='Enter customer name', pady=20, padx=10)
        customerName_label.grid(row=1, column=0)
        customerName_entry = tk.Entry(
            csw, textvariable=self.customer_name)
        customerName_entry.grid(row=1, column=1)

        back_btn = tk.Button(csw, text="Back", width=15, command=self.back)
        back_btn.grid(row=2, column=0)

        search_btn = tk.Button(csw, text="Search",
                               width=15, command=self.search)
        search_btn.grid(row=2, column=1)

        csw.protocol("WM_DELETE_WINDOW", close_window)
        csw.mainloop()

    def search(self):
        # TODO: RETURN A SEARCH QUERY BASED ON THE FILTERS GIVEN
        # USE self.customerID.get() to get customer ID as a string
        # USE self.customer_name.get() to get customer name as a string
        c.execute("SELECT CUSTOMER.CustID, CUSTOMER.Name, SUM(RENTAL.TotalAmount) FROM CUSTOMER LEFT JOIN RENTAL ON CUSTOMER.CustID = RENTAL.CustID WHERE CUSTOMER.Name LIKE :Name GROUP BY CUSTOMER.CustID", {
                  'Name': '%'+self.customer_name.get()+'%'})
        info = c.fetchall()
        print(info)
        for i in range(len(info)):
            x = list(info[i])
            if not x[2] == None:
                x[2] = 0
            info[i] = tuple(x)

        customer_table = ttk.Treeview(self.customersearch_window, columns=(
            "Customer ID", "Name", "Remaining Balance"), show="headings")

        for i in range(len(info)):
            customer_table.insert("", "end", values=info[i])
        customer_table.grid(row=3, column=0)
        pass

    def back(self):
        self.customersearch_window.destroy()
        Main_Window(self.parent)


class VehicleSearch_Window:
    def __init__(self, parent):
        self.parent = parent
        self.vehiclesearch_window = tk.Toplevel(self.parent)
        self.vehiclesearch_window.geometry("800x800")
        vsw = self.vehiclesearch_window

        self.VIN = tk.StringVar()
        self.desc = tk.StringVar()

        VIN_label = tk.Label(
            vsw, text='Enter VIN', pady=20, padx=10)
        VIN_label.grid(row=0, column=0)
        VIN_entry = tk.Entry(vsw, textvariable=self.VIN)
        VIN_entry.grid(row=0, column=1)

        desc_label = tk.Label(
            vsw, text='Enter vehicle description', pady=20, padx=10)
        desc_label.grid(row=1, column=0)
        customerName_entry = tk.Entry(
            vsw, textvariable=self.desc)
        customerName_entry.grid(row=1, column=1)

        back_btn = tk.Button(vsw, text="Back", width=15, command=self.back)
        back_btn.grid(row=2, column=0)

        search_btn = tk.Button(vsw, text="Search",
                               width=15, command=self.search)
        search_btn.grid(row=2, column=1)

        vsw.protocol("WM_DELETE_WINDOW", close_window)
        vsw.mainloop()

    def search(self):
        # TODO: RETURN A SEARCH QUERY BASED ON THE FILTERS GIVEN
        # USE self.VIN.get() to get vehicle VIN as a string
        # USE self.desc.get() to get vehicle description as a string
        c.execute("SELECT VEHICLE.VehicleID, VEHICLE.Description, RATE.Daily FROM VEHICLE, RATE WHERE VEHICLE.Type = RATE.Type AND VEHICLE.Category = RATE.Category AND VEHICLE.Description LIKE :Description", {
                  'Description': '%'+self.desc.get()+'%'})
        info = c.fetchall()
        vehicle_table = ttk.Treeview(self.vehiclesearch_window, columns=(
            "VIN", "Vehicle Description", "Average Daily Prices"), show="headings")

        for i in range(len(info)):
            vehicle_table.insert("", "end", values=info[i])
        vehicle_table.grid(row=3, column=0)

        pass
        pass

    def back(self):
        self.vehiclesearch_window.destroy()
        Main_Window(self.parent)


window = tk.Tk()
window.withdraw()
Main_Window(window)
window.mainloop()
conn.close()
