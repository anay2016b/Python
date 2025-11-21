from tkinter import *
window = Tk()
window.geometry("400x200")
window.title("Main")
window.configure(bg = "silver")
f1 = Frame(master = window, bg = "gold", bd = 20, width = 300, height = 180, relief = GROOVE)
l1 = Label(f1, text = "Enter number", bg = "gold", fg = "black", font= ("Times New Roman", 20))
e1 = Entry(f1, width = 30, bd = 5, bg = "light blue", fg = "black", font = ("Arial", 15))
def p1():
    num1 = float(e1.get())
    global sum
    sum = num1 / 2.54         
    l2 = Label(f1, text = sum, bg = "silver", fg = "black", font = ("Times New Roman", 20))
    l2.pack()

def p2():
  l5 = Label(f1, text = "Are you sure you want to switch?", bg = "silver", fg = "black", font = ("Times New Roman", 20))
  l5.pack()
  btn2 = Button(f1, text = "Yes", fg = "green", command= p3, width = 10, height = 1)
  btn2.pack()
  btn3 = Button(f1, text = "No", fg = "green", command= p4, width = 10, height = 1)
  btn3.pack()
  def p3():
      num1 = float(e1.get())
      global sum
      sum = num1 * 3.937         
      l3 = Label(f1, text = sum, bg = "silver", fg = "black", font = ("Times New Roman", 20))
      l3.pack()
  def p4():
        l4 = Label(f1, text = "Operation cancelled", bg = "silver", fg = "black", font = ("Times New Roman", 20))
        l4.pack()

btn1 = Button(f1, text = "Enter(cm to inch)", fg = "green", command= p1, width = 15, height = 1)

