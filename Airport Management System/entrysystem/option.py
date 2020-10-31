import tkinter
from tkinter import *
from subprocess import call
root = Tk()

root.geometry("900x600")

root.title('Mumbai International Airport')
def checkin():
    call(["python", "entry.py"])

def checkout():
    call(["python", "check-out.py"])

def display():
    call(["python", "displaydata.py"])

def exit():
    call(["python", quit()])

Message(root, text="Welcome To Airport",fg="red", font="Impact 36 bold").pack()


Button(root, text="Check-in Details", bg="purple", fg='#00ffff', width=51, padx=1, pady=5,command=checkin).pack()
Label(root,text="").pack()

Button(root, text="Check-out", bg="purple", fg='#00ffff', width=51, padx=1, pady=5,command=checkout).pack()
Label(root,text="").pack()

Button(root, text="Display ", bg="purple", fg='#00ffff', width=51, padx=1, pady=5,command=display).pack()
Label(root,text="").pack()

Button(root, text="exit ", bg="purple", fg='#00ffff', width=51, padx=1, pady=5,command=exit).pack()
Label(root,text="").pack()



root.mainloop()
