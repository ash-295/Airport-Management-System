from subprocess import call
from tkinter import *
flight = Tk()

flight.geometry("1000x600")
flight.configure(background='#ff927f')
flight.title('Mumbai International Airport')
flight.wm_iconbitmap("img/logo.ico")


def flightms():
    call(["python", "flightsystem/main.py"])


def entryms():
    call(["python", "entrysystem/option.py"])


def bookingms():
    call(["python", "bookingsystem/shakib1.py"])


airport = Label(flight, text='Mumbai International Airport', font="Times 36 bold", background='#ff927f', fg='#831400')
airport.pack()
user = Label(flight, text='Welcome, Airport Admin', font="Helvetica 30 bold", background='#ff927f')
user.pack()
mainframe = Frame(flight, relief=SUNKEN, highlightthickness=3, width=850, highlightcolor='black')
mainframe.place(relx=0.02, rely=0.18, relheight=0.80, relwidth=0.96)

btn1 = Button(mainframe, text='Flight Management System', font="Times 24", bg='#831400', fg='#00ffff', width=51, padx=1, pady=5, command=flightms)
btn1.place(relx=0.01, rely=0.40)
btn1 = Button(mainframe, text='Entry Management System', font="Times 24", bg='#831400', fg='#00ffff', width=51, padx=1, pady=5, command=entryms)
btn1.place(relx=0.01, rely=0.60)
btn1 = Button(mainframe, text='Booking Management System', font="Times 24", bg='#831400', fg='#00ffff', width=51, padx=1, pady=5, command=bookingms)
btn1.place(relx=0.01, rely=0.80)
flight.mainloop()