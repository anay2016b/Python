from tkinter import *

window = Tk()
window.geometry("6000x4000")
window.title("Conversion Calculator")
window.configure(bg = "silver")
f1 = Frame(master = window, bg = "red", bd = 20, width = 1680, height = 400, relief = GROOVE)
l1 = Label(f1, text = "length", bg = "gold", fg = "black", font= ("Times New Roman", 20))
l2 = Label(f1, text = "cm - inches", bg = "red", fg = "yellow", font= ("Times New Roman", 20))
e1 = Entry(f1, width = 20, bd = 5, bg = "light blue", fg = "black", font = ("Times New Roman", 15))
l3 = Label(f1, text = "m - inches", bg = "red", fg = "yellow", font= ("Times New Roman", 20))
e2 = Entry(f1, width = 20, bd = 5, bg = "light blue", fg = "black", font = ("Times New Roman", 15))
l4 = Label(f1, text = "m - feet", bg = "red", fg = "yellow", font= ("Times New Roman", 20))
e3 = Entry(f1, width = 20, bd = 5, bg = "light blue", fg = "black", font = ("Times New Roman", 15))
l5 = Label(f1, text = "m - yards", bg = "red", fg = "yellow", font= ("Times New Roman", 20))
e4 = Entry(f1, width = 20, bd = 5, bg = "light blue", fg = "black", font = ("Times New Roman", 15))
l6 = Label(f1, text = "km - yards", bg = "red", fg = "yellow", font= ("Times New Roman", 20))
e5 = Entry(f1, width = 20, bd = 5, bg = "light blue", fg = "black", font = ("Times New Roman", 15))
l7 = Label(f1, text = "km - miles", bg = "red", fg = "yellow", font= ("Times New Roman", 20))
e6 = Entry(f1, width = 20, bd = 5, bg = "light blue", fg = "black", font = ("Times New Roman", 15))
l8 = Label(f1, text = "dm - inches", bg = "red", fg = "yellow", font= ("Times New Roman", 20))
e7 = Entry(f1, width = 20, bd = 5, bg = "light blue", fg = "black", font = ("Times New Roman", 15))
l9 = Label(f1, text = "dm - feet", bg = "red", fg = "yellow", font= ("Times New Roman", 20))
e8 = Entry(f1, width = 20, bd = 5, bg = "light blue", fg = "black", font = ("Times New Roman", 15))
def p1():
    num1 = float(e1.get())
    sum = num1 / 2.54
    l10 = Label(window, text = f"{sum} inches", bg = "light blue", fg = "black", font = ("Times New Roman", 20))
    l10.place(x = 0, y = 200)
def p2():
    num1 = float(e1.get())
    sum = num1 * 25.4
    l11 = Label(window, text = f"{sum} inches", bg = "light blue", fg = "black", font = ("Times New Roman", 20))
    l11.place(x = 250, y = 200)
def p3():
    num1 = float(e1.get())
    sum = num1 * 3.281
    l12 = Label(window, text = f"{sum} feet", bg = "light blue", fg = "black", font = ("Times New Roman", 20))
    l12.place(x = 450, y = 200)
def p4():
    num1 = float(e1.get())
    sum = num1 * 1.094
    l13 = Label(window, text = f"{sum} yards", bg = "light blue", fg = "black", font = ("Times New Roman", 20))
    l13.place(x = 650, y = 200)
def p5():
    num1 = float(e1.get())
    sum = num1 / 1094
    l14 = Label(window, text = f"{sum} yards", bg = "light blue", fg = "black", font = ("Times New Roman", 20))
    l14.place(x = 850, y = 200)
def p6():
    num1 = float(e1.get())
    sum = num1 / 1.609
    l15 = Label(window, text = f"{sum} miles", bg = "light blue", fg = "black", font = ("Times New Roman", 20))
    l15.place(x = 1050, y = 200)
def p7():
    num1 = float(e1.get())
    sum = num1 * 2.54
    l16 = Label(window, text = f"{sum} inches", bg = "light blue", fg = "black", font = ("Times New Roman", 20))
    l16.place(x = 1250, y = 200)
def p8():
    num1 = float(e1.get())
    sum = num1 / 3.281
    l17 = Label(window, text = f"{sum} feet", bg = "light blue", fg = "black", font = ("Times New Roman", 20))
    l17.place(x = 1450, y = 200)
    
btn1 = Button(f1, text = "enter", fg = "green", command= p1, width = 10, height = 1)
btn2 = Button(f1, text = "enter", fg = "green", command= p2, width = 10, height = 1)
btn3 = Button(f1, text = "enter", fg = "green", command= p3, width = 10, height = 1)
btn4 = Button(f1, text = "enter", fg = "green", command= p4, width = 10, height = 1)
btn5 = Button(f1, text = "enter", fg = "green", command= p5, width = 10, height = 1)
btn6 = Button(f1, text = "enter", fg = "green", command= p6, width = 10, height = 1)
btn7 = Button(f1, text = "enter", fg = "green", command= p7, width = 10, height = 1)
btn8 = Button(f1, text = "enter", fg = "green", command= p8, width = 10, height = 1)

f2 = Frame(master = window, bg = "red", bd = 20, width = 1680, height = 400, relief = GROOVE)
l18 = Label(f1, text = "weight", bg = "gold", fg = "black", font= ("Times New Roman", 20))
l19 = Label(f1, text = "g - oz", bg = "red", fg = "yellow", font= ("Times New Roman", 20))
e9 = Entry(f1, width = 20, bd = 5, bg = "light blue", fg = "black", font = ("Times New Roman", 15))
l20 = Label(f1, text = "kg - oz", bg = "red", fg = "yellow", font= ("Times New Roman", 20))
e10 = Entry(f1, width = 20, bd = 5, bg = "light blue", fg = "black", font = ("Times New Roman", 15))
l21 = Label(f1, text = "g - lb", bg = "red", fg = "yellow", font= ("Times New Roman", 20))
e11 = Entry(f1, width = 20, bd = 5, bg = "light blue", fg = "black", font = ("Times New Roman", 15))
l22 = Label(f1, text = "kg - lb", bg = "red", fg = "yellow", font= ("Times New Roman", 20))
e12 = Entry(f1, width = 20, bd = 5, bg = "light blue", fg = "black", font = ("Times New Roman", 15))
l23 = Label(f1, text = "kg - st", bg = "red", fg = "yellow", font= ("Times New Roman", 20))
e13 = Entry(f1, width = 20, bd = 5, bg = "light blue", fg = "black", font = ("Times New Roman", 15))

def p9():
    num1 = float(e1.get())
    sum = num1 / 2.54
    l27 = Label(window, text = f"{sum} inches", bg = "light blue", fg = "black", font = ("Times New Roman", 20))
    l27.place(x = 0, y = 600)
def p10():
    num1 = float(e1.get())
    sum = num1 * 25.4
    l28 = Label(window, text = f"{sum} inches", bg = "light blue", fg = "black", font = ("Times New Roman", 20))
    l28.place(x = 0, y = 600)
def p11():
    num1 = float(e1.get())
    sum = num1 * 3.281
    l12 = Label(window, text = f"{sum} feet", bg = "light blue", fg = "black", font = ("Times New Roman", 20))
    l12.place(x = 0, y = 600)
def p12():
    num1 = float(e1.get())
    sum = num1 * 1.094
    l13 = Label(window, text = f"{sum} yards", bg = "light blue", fg = "black", font = ("Times New Roman", 20))
    l13.place(x = 0, y = 600)
def p13():
    num1 = float(e1.get())
    sum = num1 / 1094
    l14 = Label(window, text = f"{sum} yards", bg = "light blue", fg = "black", font = ("Times New Roman", 20))
    l14.place(x = 0, y = 600)

    
btn9 = Button(f1, text = "enter", fg = "green", command= p9, width = 10, height = 1)
btn10 = Button(f1, text = "enter", fg = "green", command= p10, width = 10, height = 1)
btn11 = Button(f1, text = "enter", fg = "green", command= p11, width = 10, height = 1)
btn12 = Button(f1, text = "enter", fg = "green", command= p12, width = 10, height = 1)
btn13 = Button(f1, text = "enter", fg = "green", command= p13, width = 10, height = 1)

l1.pack()
l2.place(x = 50, y = 50)
l3.place(x = 250, y = 50)
l4.place(x = 450, y = 50)
l5.place(x = 650, y = 50)
l6.place(x = 850, y = 50)
l7.place(x = 1050, y = 50)
l8.place(x = 1250, y = 50)
l9.place(x = 1450, y = 50)
l18.place(x = 50, y = 50)
l19.place(x = 250, y = 50)
l20.place(x = 450, y = 50)
l21.place(x = 650, y = 50)
l6.place(x = 850, y = 50)
e1.place(x = 50, y = 80)
e2.place(x = 250, y = 80)
e3.place(x = 450, y = 80)
e4.place(x = 650, y = 80)
e5.place(x = 850, y = 80)
e6.place(x = 1050, y = 80)
e7.place(x = 1250, y = 80)
e8.place(x = 1450, y = 80)
btn1.place(x = 50, y = 110)
btn2.place(x = 250, y = 110)
btn3.place(x = 450, y = 110)
btn4.place(x = 650, y = 110)
btn5.place(x = 850, y = 110)
btn6.place(x = 1050, y = 110)
btn7.place(x = 1250, y = 110)
btn8.place(x = 1450, y = 110)
f1.pack_propagate(False)
f1.place(x= 0, y=0)
window.mainloop()