# Import Required Library
from tkinter import *
from tkcalendar import Calendar

# Create Object
time = Tk()

# Set geometry
time.geometry("400x400")

# DEF


def save_time():
    time_file = open("time_2.txt", "a")
    time_file.write(calendar.get_date())
    time_file.write("\n")
    time_file.close()


def window_destroy():
    time.destroy()


# Add Calendar
calendar = Calendar(time, selectmode='day', year=2022, month=5, day=11)

calendar.pack(pady=20)


# Add Button and Label
select_button = Button(time, text="Select Date", command=lambda: [save_time(), window_destroy()])
select_button.pack(pady=20)


# Execute Tkinter
time.mainloop()
