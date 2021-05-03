import tkinter as tk


def close_window():
    window.destroy()


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
                           command=self.callback)
        submit.grid(row=2, column=1)

        back_button = tk.Button(rw, text='back', width=10, command=self.back)
        back_button.grid(row=2, column=0)
        rw.protocol("WM_DELETE_WINDOW", close_window)
        rw.mainloop()
        pass

    def back(self):
        self.registerwindow.destroy()
        Main_Window(self.parent)

    def callback(self):
        print(self.user.get())
        print(self.phone.get())

        if self.user.get().isalpha():
            print("valid name")
        else:
            print("invalid name")

        if self.phone.get().isnumeric() and len(self.phone.get()) == 10:
            print("valid number")
        else:
            print("invalid number")
            self.back()


class Main_Window:
    def __init__(self, parent):
        self.parent = parent
        self.mainwindow = tk.Toplevel(self.parent)
        self.mainwindow.geometry("150x125")
        mw = self.mainwindow
        vehicle_btn = tk.Button(mw, text="Vehicle Lookup",
                                width=15, command=self.open_vehicle)
        vehicle_btn.grid(row=0, column=0)

        register_btn = tk.Button(
            mw, text="Register new customer", width=20, command=self.open_register)
        register_btn.grid(row=1, column=0)

        rental_btn = tk.Button(mw, text="Rent a car", width=15)
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
            vw, text="Search", width=15, command=self.search)
        search_btn.grid(row=5, column=1)

        ### BACK BUTTON ###
        return_btn = tk.Button(vw, text="Back", width=15, command=self.back)
        return_btn.grid(row=5, column=0)

        vw.protocol("WM_DELETE_WINDOW", close_window)
        vw.mainloop()

    def search(self):
        print(self.type.get())
        print(self.category.get())
        pass

    def back(self):
        self.vehiclewindow.destroy()
        Main_Window(self.parent)


window = tk.Tk()
window.withdraw()
Main_Window(window)
window.mainloop()
