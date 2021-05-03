import tkinter as tk


def callback():
    print(user.get())
    print(phone.get())


window = tk.Tk()

user = tk.StringVar()
phone = tk.StringVar()

# Customer Entry


# Name field
name_label = tk.Label(window, text='Customer Name:',
                      pady=20, padx=10)
name_label.grid(column=0, row=0)
name_entry = tk.Entry(window, textvariable=user)
name_entry.grid(row=0, column=1)
########################################################################
# Phone field
phone_label = tk.Label(window, text='Phone Number:',
                       pady=20, padx=10)
phone_label.grid(row=1, column=0)
phone_entry = tk.Entry(window, textvariable=phone)
phone_entry.grid(row=1, column=1)

submit = tk.Button(window, text='submit', width=10,
                   command=callback)
submit.grid(row=2, column=1)

window.title('Customer Info')
window.geometry('300x200')
window.mainloop()
