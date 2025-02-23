from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=100)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file='./14_Password_Manager/logo.png')
canvas.create_image(100,100, image=image)
canvas.grid(row=0 , column=1)

#website label
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)

# username Label
username_label = Label(text='Username/Email:')
username_label.grid(row=2, column=0)

#password_label
password_label = Label(text='Password:')
password_label.grid(row=3, column=0)


# Entries fields

# website_entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky='ew')
website_entry.focus()

#username_entry
username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2, sticky='ew')
username_entry.insert(0,'riddhiairan@gmail.com')

#password_entry
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky='ew')

generator_button = Button(text='Generate Password')
generator_button.grid(row=3, column=2)

add_button = Button(text='Add', width=36)
add_button.grid(row=4, column=1, columnspan=2, sticky='ew')


window.mainloop()