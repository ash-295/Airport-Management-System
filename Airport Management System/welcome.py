from subprocess import call
from tkinter import *
flight = Tk()

flight.geometry("1000x600")
flight.configure(background='#ff927f')
flight.title('Mumbai International Airport')
flight.wm_iconbitmap("img/logo.ico")


def verification():
    for i in range(4):
        if user.get() == roles[i]:
            if e2.get() == password[i]:
                if i == 0:
                    call(["python", "menu.py"])
                elif i == 1:
                    call(["python", "flightsystem/main.py"])
                elif i == 2:
                    call(["python", "entrysystem/option.py"])
                else:
                    call(["python", "bookingsystem/shakib1.py"])
            else:
                res.config(text='Incorrect Password')


airport = Label(flight, text='Mumbai International Airport', font="Times 36 bold", background='#ff927f', fg='#831400')
airport.pack()
mainframe = Frame(flight, relief=SUNKEN, highlightthickness=3, width=850, highlightcolor='black')
mainframe.place(relx=0.02, rely=0.18, relheight=0.80, relwidth=0.96)
pic = PhotoImage(file="img/airport.png", width=400)
mainpic = Label(image=pic)
mainpic.place(relx=0.05, rely=0.50)
menu = Label(mainframe, text='ACCOUNT LOGIN', pady=20, font="Times 36")
menu.place(relx=0.50, rely=0.01)
f1 = Label(mainframe, text='Role :', font="Times 20")
f1.place(relx=0.50, rely=0.20)
roles = ['Admin', 'Flight Manager', 'Entry Manager', 'Booking Manager']
password = ['airport123', 'flight123', 'entry123', 'booking123']
user = StringVar()
user.set(roles[0])
e1 = OptionMenu(mainframe, user, *roles)
e1.place(relx=0.70, rely=0.20)
f2 = Label(mainframe, text='Password :', font="Times 20")
f2.place(relx=0.50, rely=0.40)
e2 = Entry(mainframe, bd=5, font="Times 16", relief=RAISED, show='*')
e2.place(relx=0.70, rely=0.40)
sub = Button(mainframe, text='LOGIN', font="Times 20", bg='#831400', fg='#00ffff', width=28, command=verification)
sub.place(relx=0.50, rely=0.60)
res = Label(mainframe, text='')
res.place(relx=0.50, rely=0.80)
flight.mainloop()