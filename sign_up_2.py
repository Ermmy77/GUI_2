from tkinter import *
from subprocess import call
from tkinter import ttk

# ------------------ Creating a window ------------------
sign_up = Tk()
sign_up.title("Sign Up")
sign_up.geometry('350x250')


def check():
    if button_value.get() == 1:
        password_entry.config(show='')
    else:
        password_entry.config(show='*')


# ------------------ Create text ------------------
text = Label(sign_up, text="Join Now", fg="black")
text.grid(column=1, row=0, padx=20, columnspan=3)
text.configure(font=("Times New Roman", 20))

title = Label(sign_up, text="and start managing you time efficiently", fg="black")
title.grid(column=1, row=1, padx=20, pady=5, columnspan=3)
title.configure(font=("Times New Roman", 10))

third_text = Label(sign_up, text="Log in to save your progress. \nWe won't post anything anywhere.", fg="black")
third_text.grid(column=1, row=2, columnspan=3)
third_text.configure(font=("Times New Roman", 15))

username_text = Label(sign_up, text="Username:", fg="black")
username_text.grid(column=1, row=3, sticky="E")

password_text = Label(sign_up, text="Password:", fg="black")
password_text.grid(column=1, row=4, sticky="E")

# ------------------ Create entry boxes ------------------

username_entry = Entry(sign_up, fg="black")
username_entry.grid(column=2, row=3)

password_entry = Entry(sign_up, show="*", fg="black")
password_entry.grid(column=2, row=4)

# ------------------ Create button for sign in ------------------

sign_in_button = Button(sign_up, text="Sign In", fg="black")
sign_in_button.grid(column=2, row=5, pady=5)

button_value = IntVar(value=0)

check_button = Checkbutton(sign_up, text='Show Password', variable=button_value,
                 onvalue=1, offvalue=0, command=check, fg="black")
check_button.grid(row=5, column=1)

# ------------------ Run the mainloop ------------------
sign_up.mainloop()
