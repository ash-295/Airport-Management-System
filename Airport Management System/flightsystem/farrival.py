
from tkinter import *


class flightsystem(Tk):
    fid = "A"
    airline = "Indigo"
    src = "Delhi"
    passenger = 0
    flighttype = "Domestic"

    def __init__(self):
        super().__init__()
        self.wm_iconbitmap("img/logo.ico")

    def getfid(self, fid1):
        self.fid = fid1

    def getairline(self, airline1):
        self.airline = airline1

    def getsrc(self, src1):
        self.src = src1

    def getpassenger(self, passenger1):
        self.passenger = passenger1

    def gettype(self, type1):
        if type1 == 1:
            self.flighttype = "Domestic"
        else:
            self.flighttype = "International"

    def getall(self):
        fil1 = open("arrival.txt", "a")
        fil1.write("\nFlight ID= {}, Airline= {}, Source= {}, Number of Passengers = {}, Type of Flight= {}".format(self.fid, self.airline, self.src, self.passenger, self.flighttype))
        fil1.close()


if __name__ == '__main__':
    arrival = flightsystem()
    arrival.geometry("1000x600")
    arrival.configure(background='#ce69ec')
    arrival.title('Mumbai International Airport')

    ch = IntVar()

    def infosub():
        if len(e1.get()) == 0:
            res1.config(text='Flight ID Empty')
        else:
            if len(e2.get()) == 0:
                res1.config(text='Airline Empty')
            else:
                if len(e3.get()) == 0:
                    res1.config(text='Source Empty')
                else:
                    if len(e4.get()) == 0:
                        res1.config(text='Passenger number Empty')
                    else:
                        try:
                            int(e4.get())
                            if ch.get() == 1 or ch.get() == 2:
                                res1.config(text='Flight Id added')
                                res2.config(text='Airline added')
                                res3.config(text='Fight Source added')
                                res4.config(text='Number of Passengers added')
                                res5.config(text='Type of Flight added')
                                arrival.getfid(e1.get())
                                arrival.getairline(e2.get())
                                arrival.getsrc(e3.get())
                                arrival.getpassenger(e4.get())
                                arrival.gettype(ch.get())
                                arrival.getall()

                            else:
                                res1.config(text='Choose the Type of Flight')
                        except ValueError:
                            res1.config(text='Passenger number not a Valid Number')


    heading = Label(arrival, text='Add Flight Arrival', font="Times 36 bold", background='#ce69ec')
    heading.pack()

    formframe = Frame(arrival, relief=SUNKEN, highlightthickness=3, width=850, highlightcolor='black')
    formframe.place(relx=0.02, rely=0.18, relheight=0.80, relwidth=0.96)
    f1 = Label(formframe, text='Flight ID', font="Times 20")
    f1.place(relx=0.05, rely=0)
    e1 = Entry(formframe, bd=5, bg='#7fffd4', width=25, font="Times 16")
    e1.place(relx=0.50, rely=0)
    f2 = Label(formframe, text='Airline', font="Times 20")
    f2.place(relx=0.05, rely=0.10)
    e2 = Entry(formframe, bd=5, bg='#7fffd4', width=25, font="Times 16")
    e2.place(relx=0.50, rely=0.10)
    f3 = Label(formframe, text='Source', font="Times 20")
    f3.place(relx=0.05, rely=0.20)
    e3 = Entry(formframe, bd=5, bg='#7fffd4', width=25, font="Times 16")
    e3.place(relx=0.50, rely=0.20)
    f4 = Label(formframe, text='Number of Passengers', font="Times 20")
    f4.place(relx=0.05, rely=0.30)
    e4 = Entry(formframe, bd=5, bg='#7fffd4', width=25, font="Times 16")
    e4.place(relx=0.50, rely=0.30)
    f5 = Label(formframe, text='Type of Flight', font="Times 20")
    f5.place(relx=0.05, rely=0.40)
    r1 = Radiobutton(formframe, text='Domestic Flight', font="Times 16", variable=ch, value=1)
    r1.place(relx=0.50, rely=0.40)
    r2 = Radiobutton(formframe, text='International Flight', font="Times 16", variable=ch, value=2)
    r2.place(relx=0.70, rely=0.40)
    subm = Button(formframe, text="Submit", bg='#6f0391', fg='#00ffff', width=51, padx=1, pady=5, font="Times 24", relief=SUNKEN, command=infosub)
    subm.place(relx=0.01, rely=0.80)

    res1 = Label(formframe, text='')
    res1.place(relx=0.05, rely=0.50)
    res2 = Label(formframe, text='')
    res2.place(relx=0.05, rely=0.55)
    res3 = Label(formframe, text='')
    res3.place(relx=0.05, rely=0.60)
    res4 = Label(formframe, text='')
    res4.place(relx=0.05, rely=0.65)
    res5 = Label(formframe, text='')
    res5.place(relx=0.05, rely=0.70)
    arrival.mainloop()