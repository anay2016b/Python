from tkinter import *
window = Tk()
window.geometry("700x1100")
window.title("Main/Root window")
window.configure(bg = "gold")

def topwin():
    top = Toplevel()
    top.geometry("550x350")
    top.title("Top Level window")
    top.configure(bg = "silver")
    l1 = Label(top, text = "This is a Top Level window", bg = "gold", fg= "silver", font = ("Times New Roman", 20))
    l1.place(x = 275, y = 175) 
    top.mainloop()
    
l2 = Label(window, text = "This is the Main/Root window", bg = "silver", fg= "gold", font = ("Times New Roman", 20))
l3 = Label(window, text = "Click below to open top level window", bg = "silver", fg= "gold", font = ("Times New Roman", 20))
btn1 = Button(window, text = "Open Top Level window", fg = "gold", command = topwin, width = 20, height = 2)

l2.place(x = 550, y = 750)
l3.place(x = 550, y = 800)
btn1.place(x = 550, y = 850)
l2.pack()
l3.pack()
btn1.pack()
window.mainloop()