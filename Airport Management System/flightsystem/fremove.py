from tkinter import *


class Flightremove(Tk):

    def __init__(self):
        super().__init__()
        self.wm_iconbitmap("img/logo.ico")

    def deleteflight(self, fid):
        pass


if __name__ == '__main__':
    fremove = Flightremove()
    fremove.geometry("1000x600")
    fremove.configure(background='#ce69ec')
    fremove.title('Mumbai International Airport')

    def takeflight():
        if len(e1.get()) == 0:
            res.config(text='Enter the Flight ID')
        else:
            if checkentry == 0:
                res.config(text='Confirm by Clicking the CheckBox')
            else:
                fil1 = open("arrival.txt", "r")
                for line in fil1:
                    found1 = 0
                    if e1.get() in line:
                        found1 = 1
                fil1.close()
                if found1 == 0:
                    fil2 = open("arrival.txt", "r")
                    for line in fil2:
                        found2 = 0
                        if e1.get() in line:
                            found2 = 1
                    fil2.close()
                    if found2 == 0:
                        res.config(text='Flight ID not found')
                    else:
                        with open("depart.txt", "r") as f2:
                            data = f2.readlines()
                        with open("depart.txt", "w") as f2:
                            for line in data:
                                if e1.get() not in line:
                                    f2.write(line)
                        res.config(text='Data Deleted')
                else:
                    with open("arrival.txt", "r") as f1:
                        data = f1.readlines()
                    with open("arrival.txt", "w") as f1:
                        for line in data:
                            if e1.get() not in line:
                                f1.write(line)
                    res.config(text='Data Deleted')


    heading = Label(fremove, text='Remove Flight Data', font="Times 36 bold", background='#ce69ec')
    heading.pack()
    formframe = Frame(fremove, relief=SUNKEN, highlightthickness=3, width=850, highlightcolor='black')
    formframe.place(relx=0.02, rely=0.18, relheight=0.80, relwidth=0.96)
    f1 = Label(formframe, text='Enter the Flight ID whose data you wish to delete', font="Times 20")
    f1.place(relx=0.01, rely=0.20)
    e1 = Entry(formframe, bd=5, font="Times 18", relief=RAISED)
    e1.place(relx=0.01, rely=0.30)
    checkentry = Checkbutton(formframe, text='Are you sure you wish to remove the flight Data', font="Times 16")
    checkentry.place(relx=0.20, rely=0.40)
    res = Label(formframe, text='')
    res.place(relx=0.01, rely=0.70)
    subm1 = Button(formframe, text="Remove", bg='#6f0391', fg='#00ffff', width=25, padx=1, pady=5, font="Times 24", relief=SUNKEN, command=takeflight)
    subm1.place(relx=0.01, rely=0.80)
    subm2 = Button(formframe, text="Cancel", bg='#6f0391', fg='#00ffff', width=25, padx=1, pady=5, font="Times 24", relief=SUNKEN, command=quit)
    subm2.place(relx=0.50, rely=0.80)
    fremove.mainloop()