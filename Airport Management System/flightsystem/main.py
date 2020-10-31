from subprocess import call
from tkinter import *
flight = Tk()


def addarrive():
    call(["python", "farrival.py"])


def adddepart():
    call(["python", "fdepart.py"])


def delflight():
    call(["python", "fremove.py"])


def fdisplay():
    call(["python", "fdisplay.py"])


flight.geometry("1000x600")
flight.configure(background='#ce69ec')
flight.title('Mumbai International Airport')
flight.wm_iconbitmap("img/logo.ico")
airport = Label(flight, text='Mumbai International Airport', font="Times 36 bold", background='#ce69ec')
airport.pack()
user = Label(flight, text='Welcome, Flight Manager', font="Helvetica 30 bold", background='#ce69ec')
user.pack()
mainframe = Frame(flight, relief=SUNKEN, highlightthickness=3, width=850, highlightcolor='black')
mainframe.place(relx=0.02, rely=0.18, relheight=0.80, relwidth=0.96)
pic = PhotoImage(file="img/flight.png", width=400)
mainpic = Label(image=pic)
mainpic.pack()
menu = Label(mainframe, text='MENU', pady=20, font="Times 36")
menu.place(relx=0.40, rely=0.20)
opt1 = Button(mainframe, text='Add Flight Arrival', bg='#6f0391', fg='#00ffff', width=25, padx=1, pady=5, font="Times 24", relief=SUNKEN, command=addarrive)
opt1.place(relx=0.01, rely=0.40)
opt2 = Button(mainframe, text='Add Flight Departure', bg='#6f0391', fg='#00ffff', width=25, padx=1, pady=5, font="Times 24", relief=SUNKEN, command=adddepart)
opt2.place(relx=0.50, rely=0.40)
opt3 = Button(mainframe, text='Remove Flight Data', bg='#6f0391', fg='#00ffff', width=25, padx=1, pady=5, font="Times 24", relief=SUNKEN, command=delflight)
opt3.place(relx=0.01, rely=0.60)
opt4 = Button(mainframe, text='Flight Report', bg='#6f0391', fg='#00ffff', width=25, padx=1, pady=5, font="Times 24", relief=SUNKEN, command=fdisplay)
opt4.place(relx=0.50, rely=0.60)
opt5 = Button(mainframe, text='Exit', bg='#6f0391', fg='#00ffff', width=51, padx=1, pady=5, font="Times 24", relief=SUNKEN, command=quit)
opt5.place(relx=0.01, rely=0.80)
flight.mainloop()