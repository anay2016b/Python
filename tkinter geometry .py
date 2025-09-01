from tkinter import *

window = Tk()
window.geometry("500x400")
window.title("Tkinter Geometry Method")
window.configure(bg = "gold")


btn = Button(window, text = "Yo I am one of those random buttons", fg= "green", width = 25, height = 1)
f1 = Frame(master = window, bg = "red", bd = 25, width = 250, height = 200, relief = RAISED, )
f2 = Frame(master = window, bg = "red", bd = 25, width = 250, height = 200, relief = RAISED, )
btn.pack(side = BOTTOM)
f1.place(x = 0, y = 0)
f2.place(x = 250, y = 0)
window.mainloop()