from tkinter import *
from tkinter import messagebox
window = Tk()
window.geometry("600x500")
window.title("Message box")
window.configure(bg = "silver")
f1 = Frame(master = window, bg = "green", bd = 12, width = 300, height = 250, relief = RAISED)
l1 = Label(master = f1, text = "Click below", width = 20 , height = 1 , bg = "gold", fg = "light blue", font = ("Times New Roman", 20))
def show():
    
    messagebox.showinfo("Information", "You clicked here")
    
btn1 = Button(master = f1, text = "Click me", fg = "orange", command = show, width = 10, height = 1)


f2 = Frame(master = window, bg = "green", bd = 12, width = 300, height = 250, relief = RAISED)
l2 = Label(master = f2, text = "Click below", width = 20 , height = 1 , bg = "gold", fg = "light blue", font = ("Times New Roman", 20))

def handle_key(event):
    print(event.char)
    
window.bind("<Key>", handle_key) 

def show2():
    m2 = Message(master = f2, text = "You clicked here", bg = "silver", fg = "blue", font = ("Times New Roman", 20), width = 200 )
    m2.pack()
    
btn2 = Button(master = f2, text = "Click me", fg = "orange", command = show2, width = 10, height = 1)

f1.pack_propagate(False)
f1.pack()
l1.pack()
btn1.pack()
f2.pack_propagate(False)
f2.pack()
l2.pack()
btn2.pack()

window.mainloop()
