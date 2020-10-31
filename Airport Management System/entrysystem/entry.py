
from tkinter import *
root = Tk()
root.geometry("900x600")
    
root.title('Checkin Details')


class enter():
    Aid = "A"
    name = "ABC"
    loc = "Delhi"
    contact=""

    def __init__(self):
        super().__init__()
       

    def ID(self, Aid):
        self.Aid = Aid

    def Name(self, name):
        self.name = name

    def loc(self, loc):
        self.loc = loc

    def num(self, mob):
        self.contact = mob

    def getall(self):
        fil1 = open("checkin.txt", "a")
        fil1.write("\n ID= {}, name= {}, departlocation= {}, contact = {}".format(self.Aid, self.name, self.loc, self.mob))
        fil1.close()

    


if __name__ == '__main__':
    

    ch = IntVar()

    def det():
        if len(e1.get()) == 0:
            res1.config(text=' ID Empty')
        else:
            if len(e2.get()) == 0:
                res1.config(text='name Empty')
            else:
                if len(e3.get()) == 0:
                    res1.config(text='location Empty')
                else:
                    if len(e4.get()) == 0:
                        res1.config(text='contact number Empty')
                    else:
                        try:
                            int(e4.get())
                            if ch.get() == 1 or ch.get() == 2:
                                
                                
                                root.ID(e1.get())
                                root.Name(e2.get())
                                root.loc(e3.get())
                                root.num(e4.get())
                               
                                root.getall()

                            else:
                                res1.config(text='You are all set to go')
                        except ValueError:
                            res1.config(text='good bye')


    
    
    f1 = Label(root, text=' ID', font="Times 20")
    f1.place(relx=0.05, rely=0)
    e1 = Entry(root, bd=5, bg='#7fffd4', width=25, font="Times 16")
    e1.place(relx=0.50, rely=0)
    f2 = Label(root, text='name', font="Times 20")
    f2.place(relx=0.05, rely=0.10)
    e2 = Entry(root, bd=5, bg='#7fffd4', width=25, font="Times 16")
    e2.place(relx=0.50, rely=0.10)
    f3 = Label(root, text='departing location', font="Times 20")
    f3.place(relx=0.05, rely=0.20)
    e3 = Entry(root, bd=5, bg='#7fffd4', width=25, font="Times 16")
    e3.place(relx=0.50, rely=0.20)
    f4 = Label(root, text='contact details', font="Times 20")
    f4.place(relx=0.05, rely=0.30)
    e4 = Entry(root, bd=5, bg='#7fffd4', width=25, font="Times 16")
    e4.place(relx=0.50, rely=0.30)
   
    Button(root, text="Submit",   width=20, font="Impact 14",  command=det).place(relx=0.20, rely=0.40)
    

    res1 = Label(root, text='')
    res1.place(relx=0.05, rely=0.50)
    res2 = Label(root, text='')
    res2.place(relx=0.05, rely=0.55)
    res3 = Label(root, text='')
    res3.place(relx=0.05, rely=0.60)
    res4 = Label(root, text='')
    res4.place(relx=0.05, rely=0.65)
    res5 = Label(root, text='')
    res5.place(relx=0.05, rely=0.70)
    root.mainloop()