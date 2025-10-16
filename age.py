from tkinter import *
import datetime
from datetime import date
datetime.time()
window = Tk()
window.geometry("3000x5000")
window.title("Age calculator")
window.configure(bg = "silver")

f1 = Frame(master = window, bg = "red", bd = 20, width = 500, height = 300, relief = GROOVE)
l1 = Label(f1, text= "Enter your birth year(1) month(2) and date(3)", bg = "gold", fg = "black", font = ("Times New Roman", 20))

e1 = Entry(f1, width= 35, bd = 5, bg = "light blue", fg = "gold", font = ("Times New Roman", 15))
e2 = Entry(f1, width= 30, bd = 5, bg = "light blue", fg = "gold", font = ("Times New Roman", 15))
e3 = Entry(f1, width= 30, bd = 5, bg = "light blue", fg = "gold", font = ("Times New Roman", 15))

def age():
    birth_year = int(e1.get())
    birth_month = int(e2.get())
    birth_date = int(e3.get())
    
    today = date.today()
    age_year = today.year - birth_year
    age_month = today.month - birth_month
    age_date = today.day - birth_date
    
    if age_date < 0:
        age_month -= 1
        age_date += 30
        
    if age_month < 0:
        age_year -= 1
        age_month += 12
        
    l2 = Label(window, text = f"You are {age_year} years, {age_month} months and {age_date} days old", bg = "silver", fg = "black", font = ("Times New Roman", 20))
    l2.pack()
    
    
btn1 = Button(f1, text = "enter", fg = "silver", command = age, width = 10, height = 1)
    
f1.pack_propagate(False)
f1.pack()
l1.pack()
e1.pack()
e2.pack()
e3.pack()
btn1.pack()
window.mainloop()