import tkinter as tk
from tkcalendar import DateEntry
import sqlite3

conn = sqlite3.connect('CarRental.db')
c = conn.cursor()


def close_window():
    window.destroy()


class Main_Window:
    def __init__(self, parent):
        self.parent = parent
        self.mainwindow = tk.Toplevel(self.parent)
        self.mainwindow.geometry("150x125")
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

        return_btn = tk.Button(mw, text="Return a car", width=15)
        return_btn.grid(row=3, column=0)

        mw.protocol("WM_DELETE_WINDOW", close_window)
        mw.mainloop()
        pass

    def open_register(self):
        self.mainwindow.destroy()
        Register_Window(self.parent)

    def open_vehicle(self):
        self.mainwindow.destroy()
        Vehicle_Window(self.parent)

    def open_rent(self):
        self.mainwindow.destroy()
        Rent_Window(self.parent)


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
        pass

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

        start_label = tk.Label(rw, text='Rent start date:', pady=20, padx=10)
        start_label.grid(row=0, column=0)
        self.start_cal = DateEntry(rw, width=12, year=2021, month=5, day=4,
                                   background='gray', foreground='white', borderwidth=2)
        self.start_cal.grid(row=0, column=1)

        end_label = tk.Label(rw, text='Return date:', pady=20, padx=10)
        end_label.grid(row=1, column=0)
        self.end_cal = DateEntry(rw, width=12, year=2021, month=5, day=5,
                                 background='gray', foreground='white', borderwidth=2)
        self.end_cal.grid(row=1, column=1)

        ### SEARCH BUTTON ###
        search_btn = tk.Button(
            rw, text="Find available cars", width=15, command=self.search)
        search_btn.grid(row=2, column=1)

        # Reference string value of the selected vehicle using self.vehicle_selected.get()
        self.vehicle_selected = tk.StringVar()
        # Make query call from database to see available cars and form them into an array (options) -- Andy

        ### BACK BUTTON ###
        back_btn = tk.Button(rw, text="Back", width=15, command=self.back)
        back_btn.grid(row=2, column=0)

        rw.protocol("WM_DELETE_WINDOW", close_window)
        rw.mainloop()
        pass

    def search(self):
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
        c.execute("SELECT VEHICLE.VehicleID, VEHICLE.Description, VEHICLE.Year FROM VEHICLE WHERE VEHICLE.Type = :Type AND VEHICLE.Category = :Category", {
                  'Type': carType, 'Category': carCategory})
        vehicles = []
        for i in c.fetchall():
            vehicles.append(i[0] + " " + i[1] + " " + str(i[2]))

        rent_label = tk.Label(
            self.rent_window, text='Select an available vehicle', pady=20, padx=10)
        rent_label.grid(row=3, column=0)
        rent_menu = tk.OptionMenu(
            self.rent_window, self.vehicle_selected, *vehicles)
        rent_menu.grid(row=3, column=1)

        ### PAY LATER BUTTON ###
        paylater_btn = tk.Button(
            self.rent_window, text="Pay Later", width=15)
        paylater_btn.grid(row=4, column=0)

        ### PAY NOW BUTTON ###
        paynow_btn = tk.Button(
            self.rent_window, text="Pay Now", width=15)
        paynow_btn.grid(row=4, column=1)

    def back(self):
        self.rent_window.destroy()
        Main_Window(self.parent)


window = tk.Tk()
window.withdraw()
Main_Window(window)
window.mainloop()
conn.close()
