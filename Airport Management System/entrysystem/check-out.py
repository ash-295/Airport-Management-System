from tkinter import *
root=Tk()
root.geometry("900x600")
root.title('Check-out Details')


class Flightdepart():
    Aid = "A"
    name = "abc"
    contact = ""
    loc = "Delhi"

    def __init__(self):
        super().__init__()
       

    def ID(self, A_id):
        self.aid = A_id

    def Name(self, name):
        self.name = name

    def Mo(self, mob):
        self.contact = mob

    

    def getall(self):
        fil2 = open("out.txt", "a")
        fil2.write("\n ID= {}, Name= {}, Contact-details = {}= {}".format(self.aid, self.name, self.passenger))
        fil2.close()


if __name__ == '__main__':
    

    ch = IntVar()

    def sub():
        if len(e1.get()) == 0:
            res1.config(text=' ID N/A')
        else:
            if len(e2.get()) == 0:
                res1.config(text='Not available')
            else:
                if len(e4.get()) == 0:
                    res1.config(text='not here')
                else:
                    try:
                        int(e4.get())
                        if ch.get() == 1 or ch.get() == 2:
                            
                            root.ID(e1.get())
                            root.Name(e2.get())
                            root.Mo(e4.get())
                            
                            root.getall()
                        else:
                            res1.config(text='Done')
                    except ValueError:
                        res1.config(text=' not Applicable')


    
   
    f1 = Label(root, text='AAdhar ID', font="Times 20")
    f1.place(relx=0.05, rely=0)
    e1 = Entry(root, bd=5, bg='#7fffd4', width=25, font="Times 16")
    e1.place(relx=0.50, rely=0)
    f2 = Label(root, text='Name of the passenger', font="Times 20")
    f2.place(relx=0.05, rely=0.10)
    e2 = Entry(root, bd=5, bg='#7fffd4', width=25, font="Times 16")
    e2.place(relx=0.50, rely=0.10)
    f4 = Label(root, text='Contact', font="Times 20")
    f4.place(relx=0.05, rely=0.20)
    e4 = Entry(root, bd=5, bg='#7fffd4', width=25, font="Times 16")
    e4.place(relx=0.50, rely=0.20)
    
     
    
    Button(root, text="Submit",    font="Times 24", command=sub).place(relx=0.01, rely=0.80)

    res1 = Label(root, text='')
    res1.place(relx=0.05, rely=0.50)
    res2 = Label(root, text='')
    res2.place(relx=0.05, rely=0.55)
    res3 = Label(root, text='')
    res3.place(relx=0.05, rely=0.60)
    res4 = Label(root, text='')
    res4.place(relx=0.05, rely=0.65)

    root.mainloop()