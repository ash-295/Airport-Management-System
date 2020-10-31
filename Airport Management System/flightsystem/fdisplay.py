from tkinter import *


class Flightdisplay(Tk):

    def __init__(self):
        super().__init__()
        self.wm_iconbitmap("img/logo.ico")

    def display(self):
        fil1 = open("arrival.txt", "r")
        text1 = fil1.readlines()
        for line in text1:
            a1.insert(INSERT, line)
        fil1.close()
        fil2 = open("depart.txt", "r")
        text2 = fil2.readlines()
        for line in text2:
            d1.insert(INSERT, line)
        fil2.close()


if __name__ == '__main__':
    display = Flightdisplay()
    display.geometry("1000x600")
    display.configure(background='#ce69ec')
    display.title('Mumbai International Airport')
    heading = Label(display, text='Complete Flight Report', font="Times 36 bold", background='#ce69ec')
    heading.pack()
    formframe = Frame(display, relief=SUNKEN, highlightthickness=3, width=850, highlightcolor='black')
    formframe.place(relx=0.02, rely=0.18, relheight=0.80, relwidth=0.96)
    h1 = Label(formframe, text='Arrival Report', font="Times 20 bold")
    h1.place(relx=0.30, rely=0.00)
    a1 = Text(formframe, width=115, height=8)
    a1.place(relx=0.01, rely=0.10)
    h2 = Label(formframe, text='Departure Report', font="Times 20 bold")
    h2.place(relx=0.30, rely=0.40)
    d1 =Text(formframe, width=115, height=8)
    d1.place(relx=0.01, rely=0.50)
    display.display()
    subm = Button(formframe, text="Done", bg='#6f0391', fg='#00ffff', width=51, padx=1, pady=5, font="Times 24", relief=SUNKEN, command=quit)
    subm.place(relx=0.01, rely=0.80)
    display.mainloop()