from tkinter import *


class Display(Tk):

    def __init__(self):
        super().__init__()

    def putdata(self):
        fil1 = open("checkin.txt", "r")
        text1 = fil1.readlines()
        for line in text1:
            a1.insert(INSERT, line)
        fil1.close()
        fil2 = open("out.txt", "r")
        text2 = fil2.readlines()
        for line in text2:
            d1.insert(INSERT, line)
        fil2.close()


if __name__ == '__main__':
    d = Display()
    d.geometry("900x600")
    
    d.title('Display Data')
    heading = Label(d, text='Airline Records', font="Impact 36 bold")
    heading.pack()
    formframe = Frame(d, highlightthickness=3, width=850, highlightcolor='black')
    formframe.place(relx=0.02, rely=0.18, relheight=0.80, relwidth=0.96)
    h1 = Label(formframe, text='Entry details', font="Times 20 bold")
    h1.place(relx=0.30, rely=0.00)
    a1 = Text(formframe, width=115, height=8)
    a1.place(relx=0.01, rely=0.10)
    h2 = Label(formframe, text='exit details', font="Times 20 bold")
    h2.place(relx=0.30, rely=0.40)
    d1 =Text(formframe, width=115, height=8)
    d1.place(relx=0.01, rely=0.50)
    d.putdata()
    subm = Button(formframe, text="Done", bg='#6f0391', fg='#00ffff', width=51, padx=1, pady=5, font="Times 24", relief=SUNKEN, command=quit)
    subm.place(relx=0.01, rely=0.80)
    d.mainloop()