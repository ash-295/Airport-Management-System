from tkinter import *


class Flightdepart(Tk):
    fid = "A"
    dest = "Delhi"
    passenger = 0
    flighttype = "Domestic"

    def __init__(self):
        super().__init__()
        self.wm_iconbitmap("img/logo.ico")

    def getfid(self, fid1):
        self.fid = fid1

    def getdest(self, dest1):
        self.dest = dest1

    def getpass(self, pass1):
        self.passenger = pass1

    def gettype(self, type1):
        if type1 == 1:
            self.flighttype = "Domestic"
        else:
            self.flighttype = "International"

    def getall(self):
        fil2 = open("depart.txt", "a")
        fil2.write("\nFlight ID= {}, Destination= {}, Number of Passengers = {}, Type of Flight= {}".format(
                self.fid, self.dest, self.passenger, self.flighttype))
        fil2.close()


if __name__ == '__main__':
    depart = Flightdepart()
    depart.geometry("1000x600")
    depart.configure(background='#ce69ec')
    depart.title('Mumbai International Airport')

    ch = IntVar()

    def subdep():
        if len(e1.get()) == 0:
            res1.config(text='Flight ID Empty')
        else:
            if len(e2.get()) == 0:
                res1.config(text='Destination Empty')
            else:
                if len(e4.get()) == 0:
                    res1.config(text='Passenger number Empty')
                else:
                    try:
                        int(e4.get())
                        if ch.get() == 1 or ch.get() == 2:
                            res1.config(text='Flight ID added')
                            res2.config(text='Destination added')
                            res3.config(text='Passenger Number Added')
                            res4.config(text='Type of Flight Added')
                            depart.getfid(e1.get())
                            depart.getdest(e2.get())
                            depart.getpass(e4.get())
                            depart.gettype(ch.get())
                            depart.getall()
                        else:
                            res1.config(text='Choose the Type of Flight')
                    except ValueError:
                        res1.config(text='Passenger Number not Valid')


    heading = Label(depart, text='Add Flight Departure', font="Times 36 bold", background='#ce69ec')
    heading.pack()
    formframe = Frame(depart, relief=SUNKEN, highlightthickness=3, width=850, highlightcolor='black')
    formframe.place(relx=0.02, rely=0.18, relheight=0.80, relwidth=0.96)
    f1 = Label(formframe, text='Flight ID', font="Times 20")
    f1.place(relx=0.05, rely=0)
    e1 = Entry(formframe, bd=5, bg='#7fffd4', width=25, font="Times 16")
    e1.place(relx=0.50, rely=0)
    f2 = Label(formframe, text='Destination', font="Times 20")
    f2.place(relx=0.05, rely=0.10)
    e2 = Entry(formframe, bd=5, bg='#7fffd4', width=25, font="Times 16")
    e2.place(relx=0.50, rely=0.10)
    f4 = Label(formframe, text='Number of Passengers', font="Times 20")
    f4.place(relx=0.05, rely=0.20)
    e4 = Entry(formframe, bd=5, bg='#7fffd4', width=25, font="Times 16")
    e4.place(relx=0.50, rely=0.20)
    f5 = Label(formframe, text='Type of Flight', font="Times 20")
    f5.place(relx=0.05, rely=0.30)
    r1 = Radiobutton(formframe, text='Domestic Flight', font="Times 16", variable=ch, value=1)
    r1.place(relx=0.50, rely=0.30)
    r2 = Radiobutton(formframe, text='International Flight', font="Times 16", variable=ch, value=2)
    r2.place(relx=0.70, rely=0.30)
    subm = Button(formframe, text="Submit", bg='#6f0391', fg='#00ffff', width=51, padx=1, pady=5, font="Times 24", relief=SUNKEN, command=subdep)
    subm.place(relx=0.01, rely=0.80)

    res1 = Label(formframe, text='')
    res1.place(relx=0.05, rely=0.50)
    res2 = Label(formframe, text='')
    res2.place(relx=0.05, rely=0.55)
    res3 = Label(formframe, text='')
    res3.place(relx=0.05, rely=0.60)
    res4 = Label(formframe, text='')
    res4.place(relx=0.05, rely=0.65)

    depart.mainloop()