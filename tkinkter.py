from tkinter import *
import datetime

def display():
    global message
    name = e1.get()
    message = "Welcome to my application! \n"
    greet = "Hello" ,name
    t = " Today's date and time is:"
    t1.insert(END, message)
    t1.insert(END, greet)
    t1.insert(END, t)
    t1.insert(END, datetime.datetime.now())
    
window = Tk()
window.configure(bg = "gold")
window.title("Window 1")
window.geometry("500x500")
label1 = Label(window, text= "Hello there", bg= "silver", fg= "black", font=("Times New Roman", 20, "bold"), width = 500, height = 1)


e1 = Entry(window, width = 50, bg = "brown", fg = "black", font = ("Times New Roman", 20))

b1 = Button(window, text= "Enter", bg = "turquoise", fg = "black", font = ("Times New Roman", 20, "bold"), command =  display)



    
    
    
label1.pack()
e1.pack()
b1.pack()
t1 = Text(window, width = 50, height = 10, bg = "light blue", fg = "black", font = ("Times New Roman", 20))

t1.pack()
window.mainloop()



