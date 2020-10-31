from subprocess import call
from tkinter import *
from tkinter import ttk
win = Tk()

win.geometry("1000x600")
win.title('Mumbai International Airport')
win.wm_iconbitmap("img/logo.ico")


def verification(): 
    fil1 = open("book1.txt", "r")
    text1 = fil1.readlines()
    fil1.close()
    tot.insert(INSERT, text1)
    fil2 = open("book2.txt", "r")
    text2 = fil2.readlines()
    fil2.close()
    tot.insert(INSERT, text2)
    

def bock(): call(["python", "shakib1.py"])

        
pic1 = PhotoImage(file="img/from3.png")
mainpic = Label(image=pic1)
mainpic.place(relx=0.00, rely=0.00)

labl1 = Label(win,bd=3 ,font="SF", text="Customer Details",bg="White")
labl1.place(relx=0.01,rely=0.36)

labl2 = Label(win,bd=2 ,font="SF", text="First name",bg="White")
labl2.place(relx=0.01,rely=0.43)

labl3 = Label(win,bd=2 ,font="SF", text="Last name",bg="White")
labl3.place(relx=0.01,rely=0.50)

labl4 = Label(win,bd=2 ,font="SF", text="Address",bg="White")
labl4.place(relx=0.01,rely=0.57)

labl5 = Label(win,bd=2 ,font="SF", text="Pincode ",bg="White")
labl5.place(relx=0.01,rely=0.64)

labl6 = Label(win,bd=2 ,font="SF", text="Mobile no.",bg="White")
labl6.place(relx=0.01,rely=0.71)

labl7 = Label(win,bd=2 ,font="SF", text="Email",bg="White")
labl7.place(relx=0.01,rely=0.78)

en1 = Entry(win,font="SF",borderwidth=2)
en1.place(relx=0.13,rely=0.43)

en2 = Entry(win,font="SF",borderwidth=2)
en2.place(relx=0.13,rely=0.50)

en3 = Entry(win,font="SF",borderwidth=2)
en3.place(relx=0.13,rely=0.57)

en4 = Entry(win,font="SF",borderwidth=2)
en4.place(relx=0.13,rely=0.64)

en5= Entry(win,font="SF",borderwidth=2)
en5.place(relx=0.13,rely=0.71)

en6 = Entry(win,font="SF",borderwidth=2)
en6.place(relx=0.13,rely=0.78)

jet1 = Button(win, text='TICKET', font="Montserrat 12 ", bg='#589DDC',width="24", borderwidth="5", command=verification)
jet1.place(relx=0.1, rely=0.87)

tot = Text(win, width=54, height=9, relief=SUNKEN)
tot.place(relx=0.45,rely=0.50)








#file open, read, display, file2 open , read, display price.


win.mainloop()