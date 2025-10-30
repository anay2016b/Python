from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import math
import random
import datetime
from datetime import date, time, datetime

window1 = Tk()
window1.geometry("6000x4000")
window1.title("Calculator")
window1.configure(bg = "gold")
def toplevel1():
    window2 = Toplevel()
    window2.geometry("4000x2000")
    window2.title("Top Level window - Calculator")
    window2.configure(bg = "silver")
    l1 = Label(window2, text = "This is a Top Level window - Calculator", bg = "gold", fg= "silver", font = ("Times New Roman", 20))
    l1.place(x = 2000, y = 1000) 
    window2.mainloop()
    
def toplevel2():
    window3 = Toplevel()
    window3.geometry("4000x2000")
    window3.title("Top Level window - Calculator")
    window3.configure(bg = "silver")
    l1 = Label(window3, text = "This is a Top Level window - Calculator", bg = "gold", fg= "silver", font = ("Times New Roman", 20))
    l1.place(x = 2000, y = 1000) 
    window3.mainloop()
    
def toplevel3():
    window4 = Toplevel()
    window4.geometry("4000x2000")
    window4.title("Top Level window - Calculator")
    window4.configure(bg = "silver")
    l1 = Label(window4, text = "This is a Top Level window - Calculator", bg = "gold", fg= "silver", font = ("Times New Roman", 20))
    l1.place(x = 2000, y = 1000) 
    window4.mainloop()
    
def toplevel4():
    window5 = Toplevel()
    window5.geometry("4000x2000")
    window5.title("Top Level window - Calculator")
    window5.configure(bg = "silver")
    l1 = Label(window5, text = "This is a Top Level window - Calculator", bg = "gold", fg= "silver", font = ("Times New Roman", 20))
    l1.place(x = 2000, y = 1000) 
    window5.mainloop()