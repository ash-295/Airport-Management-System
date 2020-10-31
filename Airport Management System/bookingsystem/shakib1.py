from subprocess import call
from tkinter import *
from tkinter import ttk
win = Tk()

win.geometry("1000x600")
win.title('Mumbai International Airport')
win.wm_iconbitmap("img/logo.ico")


def verification(): 
    fil1 = open("book1.txt", "w")
    fil1.write("\nFrom= {}, To= {}, Return Date= {}, Departure Date = {}, Class= {}, No of Travellers= {}".format(fchoose.get(), fchoose1.get(), rdate.get(), ddate.get(), cchoose1.get(), notrav.get()))
    fil1.close()
    call(["python", "shakib2.py"])

        
pic1 = PhotoImage(file="img/from.png")
mainpic = Label(image=pic1)
mainpic.place(relx=0.00, rely=0.00)


rdate = Entry(win, bd=2 ,font="SF",width="15", relief=RAISED)
rdate.place(relx=0.26, rely=0.57)

ddate = Entry(win, bd=2 ,font="SF",width="15", relief=RAISED)
ddate.place(relx=0.57, rely=0.57)

notrav = Entry(win, bd=2 ,font="SF",width="17", relief=RAISED)
notrav.place(relx=0.55, rely=0.74)

src = Button(win, text='SEARCH', font="SF", bg='#589DDC', width=10, borderwidth="3", command=verification)
src.place(relx=0.45, rely=0.90)


n = StringVar()
fchoose = ttk.Combobox(win, font="SF", width = 17, textvariable = n)
# Adding combobox drop down list 
fchoose['values'] = ("BOMBAY")
fchoose.grid(column = 1, row = 5) 
fchoose.current() 
fchoose.place(relx=0.15, rely=0.43)

# Combobox creation fro "to"
m = StringVar()
fchoose1 = ttk.Combobox(win, font="SF", width=17, textvariable=m)
fchoose1['values'] = ("DELHI", "PUNE", "JAIPUR", "PATNA", "GOA", "LUCKNOW", "CHENNAI", "KANPUR")
fchoose1.grid(column = 1, row = 5) 
fchoose1.current() 
fchoose1.place(relx=0.70, rely=0.41)

# Combobox creation fro "class"
m = StringVar()
cchoose1 = ttk.Combobox(win, font="SF", width = 17, textvariable = m)
# Adding combobox drop down list 
cchoose1['values'] = ("Economy", "Business", "First")
cchoose1.grid(column = 1, row = 5) 
cchoose1.current() 
cchoose1.place(relx=0.16, rely=0.75)

win.mainloop()