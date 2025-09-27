from tkinter import *
import math

window = Tk()
window.geometry("12000x3600")
window.title("Basic Calculator")
window.configure(bg = "gold")
f1 = Frame(master = window, bg = "red", bd = 20, width = 300, height = 180, relief = GROOVE )
l1 = Label(f1, text = "Enter first number", bg = "red", fg = "yellow", font= ("Times New Roman", 20))
e1 = Entry(f1, width = 30, bd = 5, bg = "light blue", fg = "black", font = ("Arial", 15))
l2 = Label(f1, text = "Enter second number", bg = "red", fg = "yellow", font= ("Times New Roman", 20))
e2 = Entry(f1, width = 30, bd = 5, bg = "light blue", fg = "black", font = ("Arial", 15))

def p1():
    num1 = float(e1.get())
    num2 = float(e2.get())
    sum = num1 + num2
    l3 = Label(window, text = sum, bg = "silver", fg = "black", font = ("Times New Roman", 20))
    l3.pack()
btn1 = Button(f1, text = "Enter(+)", fg = "green", command= p1, width = 10, height = 1)

f2 = Frame(master = window, bg = "red", bd = 20, width = 300, height = 180, relief = GROOVE)
l4 = Label(f2, text = "Enter first number", bg = "red", fg = "yellow", font= ("Times New Roman", 20))
e3 = Entry(f2, width = 30, bd = 5, bg = "light blue", fg = "black", font = ("Arial", 15))
l5 = Label(f2, text = "Enter second number", bg = "red", fg = "yellow", font= ("Times New Roman", 20))
e4 = Entry(f2, width = 30, bd = 5, bg = "light blue", fg = "black", font = ("Arial", 15))

def p2():
    num1 = float(e3.get())
    num2 = float(e4.get())
    sum = num1 - num2
    l6 = Label(window, text = sum, bg = "silver", fg = "black", font = ("Times New Roman", 20))
    l6.pack()

btn2 = Button(f2, text = "Enter(-)", fg = "green", command= p2, width = 10, height = 1)
f3 = Frame(master = window, bg = "red", bd = 20, width = 300, height = 180, relief = GROOVE)
l7 = Label(f3, text = "Enter first number", bg = "red", fg = "yellow", font= ("Times New Roman", 20))
e5 = Entry(f3, width = 30, bd = 5, bg = "light blue", fg = "black", font = ("Arial", 15))
l8 = Label(f3, text = "Enter second number", bg = "red", fg = "yellow", font= ("Times New Roman", 20))
e6 = Entry(f3, width = 30, bd = 5, bg = "light blue", fg = "black", font = ("Arial", 15))

def p3():
    num1 = float(e5.get())
    num2 = float(e6.get())
    sum = num1 * num2
    l9 = Label(window, text = sum, bg = "silver", fg = "black", font = ("Times New Roman", 20))
    l9.pack()
btn3 = Button(f3, text = "Enter(*)", fg = "green", command= p3, width = 10, height = 1)

f4 = Frame(master = window, bg = "red", bd = 20, width = 300, height = 180, relief = GROOVE)
l10 = Label(f4, text = "Enter first number", bg = "red", fg = "yellow", font= ("Times New Roman", 20))
e7 = Entry(f4, width = 30, bd = 5, bg = "light blue", fg = "black", font = ("Arial", 15))
l11 = Label(f4, text = "Enter second number", bg = "red", fg = "yellow", font= ("Times New Roman", 20))
e8 = Entry(f4, width = 30, bd = 5, bg = "light blue", fg = "black", font = ("Arial", 15))

def p4():
    num1 = float(e7.get())
    num2 = float(e8.get())
    sum = num1 / num2
    l12 = Label(window, text = sum, bg = "silver", fg = "black", font = ("Times New Roman", 20))
    l12.pack()
btn4 = Button(f4, text = "Enter(/)", fg = "green", command= p4, width = 10, height = 1)

f5 = Frame(master = window, bg = "red", bd = 20, width = 300, height = 180, relief = GROOVE)
l13 = Label(f5, text = "Enter first number", bg = "red", fg = "yellow", font= ("Times New Roman", 20))
e9 = Entry(f5, width = 30, bd = 5, bg = "light blue", fg = "black", font = ("Arial", 15))
l14 = Label(f5, text = "Enter second number", bg = "red", fg = "yellow", font= ("Times New Roman", 20))
e10 = Entry(f5, width = 30, bd = 5, bg = "light blue", fg = "black", font = ("Arial", 15))

def p5():
    num1 = float(e9.get())
    num2 = float(e10.get())
    sum = num1 ** num2
    l15 = Label(window, text = sum, bg = "silver", fg = "black", font = ("Times New Roman", 20))
    l15.pack()
btn5 = Button(f5, text = "Enter(pow)", fg = "green", command= p5, width = 10, height = 1)

f6 = Frame(master = window, bg = "red", bd = 20, width = 300, height = 180, relief = GROOVE)
l16 = Label(f6, text = "Enter first number", bg = "red", fg = "yellow", font= ("Times New Roman", 20))
e11 = Entry(f6, width = 30, bd = 5, bg = "light blue", fg = "black", font = ("Arial", 15))
l17 = Label(f6, text = "Enter second number", bg = "red", fg = "yellow", font= ("Times New Roman", 20))
e12 = Entry(f6, width = 30, bd = 5, bg = "light blue", fg = "black", font = ("Arial", 15))

def p6():
    num1 = float(e11.get())
    num2 = float(e12.get())
    sum = num1 ** (1/num2)
    l18 = Label(window, text = sum, bg = "silver", fg = "black", font = ("Times New Roman", 20))
    l18.pack()
btn6 = Button(f6, text = "Enter(y√x)", fg = "green", command= p6, width = 10, height = 1)



f7 = Frame(master = window, bg = "red", bd = 20, width = 300, height = 180, relief = GROOVE)
l19 = Label(f7, text = "Enter first number", bg = "red", fg = "yellow", font= ("Times New Roman", 20))
e13 = Entry(f7, width = 30, bd = 5, bg = "light blue", fg = "black", font = ("Arial", 15))


def p7():
    num1 = int(e13.get())

    sum = math.factorial(num1)
    l20 = Label(window, text = sum, bg = "silver", fg = "black", font = ("Times New Roman", 20))
    l20.pack()
btn7 = Button(f7, text = "Enter(!)", fg = "green", command= p7, width = 10, height = 1)

f8 = Frame(master = window, bg = "red", bd = 20, width = 300, height = 180, relief = GROOVE)
l21 = Label(f8, text = "Enter first number", bg = "red", fg = "yellow", font= ("Times New Roman", 20))
e14 = Entry(f8, width = 30, bd = 5, bg = "light blue", fg = "black", font = ("Arial", 15))


def p8():
    num1 = float(e14.get())

    sum = -(num1)
    l22 = Label(window, text = sum, bg = "silver", fg = "black", font = ("Times New Roman", 20))
    l22.pack()
btn8 = Button(f8, text = "Enter(+/-)", fg = "green", command= p8, width = 10, height = 1)




f1.place(x = 0, y = 0)
l1.pack()
e1.pack()
l2.pack()
e2.pack()
btn1.pack()
f2.place(x = 300, y = 0)
l4.pack()
e3.pack()
l5.pack()
e4.pack()
btn2.pack()
f3.place(x = 600, y = 0)
l7.pack()
e5.pack()
l8.pack()
e6.pack()
btn3.pack()
f4.place(x = 900, y = 0)
l10.pack()
e7.pack()
l11.pack()
e8.pack()
btn4.pack()
f5.place(x = 1200, y = 0)
l13.pack()
e9.pack()
l14.pack()
e10.pack()
btn5.pack()
f6.place(x = 0, y = 195)
l16.pack()
e11.pack()
l17.pack()
e12.pack()
btn6.pack()
f7.place(x = 300, y = 195)
l19.pack()
e13.pack()
btn7.pack()
f8.place(x = 600, y = 195)
l21.pack()
e14.pack()
btn8.pack()
window.mainloop()