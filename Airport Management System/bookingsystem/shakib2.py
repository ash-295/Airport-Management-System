from subprocess import call
from tkinter import *
from tkinter import ttk
win = Tk()

win.geometry("1000x600")
# win.configure(background='#ff927f')
win.title('Mumbai International Airport')
win.wm_iconbitmap("img/logo.ico")


def verification1():
    fil1 = open("book2.txt", "w")
    fil1.write("\nAirline= SpiceJet, Timing= 03:30pm - 05:50pm, Fare= 4500")
    fil1.close()
    call(["python", "shakib3.py"])
    #return airline= SpiceJet, Timing, price
        
def verification5():
    fil1 = open("book2.txt", "w")
    fil1.write("\nAirline= Air Asia, Timing=02:15pm - 05:15pm , Fare= 10580")
    fil1.close()
    call(["python", "shakib3.py"])
def verification2():
    fil1 = open("book2.txt", "w")
    fil1.write("\nAirline= Indigo, Timing =10:45pm - 03:45am , Fare= 7500")
    fil1.close()
    call(["python", "shakib3.py"])
def verification3():
    fil1 = open("book2.txt", "w")
    fil1.write("\nAirline= Air India, Timing=01:15am - 02:45pm, Fare= 6540")
    fil1.close()
    call(["python", "shakib3.py"])


def verification4():
    fil1 = open("book2.txt", "w")
    fil1.write("\nAirline= Vistara, Timing= 02:15pm - 05:15pm , Fare= 10580")
    fil1.close()
    call(["python", "shakib3.py"])


pic1 = PhotoImage(file="img/from2.png")
mainpic = Label(image=pic1)
mainpic.place(relx=0.00, rely=0.00)


jet1 = Button(win, text='Spice Jet ( 03:30pm - 05:50pm ) ₹ 4,500', font="Montserrat 12 ", bg='#589DDC',width="100", borderwidth="5", command=verification1)
jet1.place(relx=0.00, rely=0.43)

jet2 = Button(win, text='Indigo ( 10:45pm - 03:45am ) ₹ 7,500', font="Montserrat 12 ", bg='#589DDC',width="100", borderwidth="5", command=verification2)
jet2.place(relx=0.00, rely=0.50)

jet3 = Button(win, text='Air India ( 01:15am - 02:45pm ) ₹ 6,540', font="Montserrat 12 ", bg='#589DDC',width="100", borderwidth="5", command=verification3)
jet3.place(relx=0.00, rely=0.57)

jet4 = Button(win, text='Vistara ( 02:15pm - 05:15pm ) ₹ 10,580', font="Montserrat 12 ", bg='#589DDC',width="100", borderwidth="5", command=verification4)
jet4.place(relx=0.00, rely=0.64)

jet4 = Button(win, text='Air Asia ( 02:15pm - 05:15pm ) ₹ 10,580', font="Montserrat 12 ", bg='#589DDC',width="100", borderwidth="5", command=verification5)
jet4.place(relx=0.00, rely=0.71)


win.mainloop()