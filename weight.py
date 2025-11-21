from tkinter import *                           
window = Tk()
window.geometry("6000x4000")
window.title("Weight Calculator")
window.configure(bg = "silver")


f2 = Frame(master = window, bg = "red", bd = 20, width = 1680, height = 250, relief = GROOVE)
l18 = Label(f2, text = "weight", bg = "gold", fg = "black", font= ("Times New Roman", 20))
l19 = Label(f2, text = "g - oz", bg = "red", fg = "yellow", font= ("Times New Roman", 20))
e9 = Entry(f2, width = 20, bd = 5, bg = "light blue", fg = "black", font = ("Times New Roman", 15))
l20 = Label(f2, text = "kg - oz", bg = "red", fg = "yellow", font= ("Times New Roman", 20))
e10 = Entry(f2, width = 20, bd = 5, bg = "light blue", fg = "black", font = ("Times New Roman", 15))
l21 = Label(f2, text = "g - lb", bg = "red", fg = "yellow", font= ("Times New Roman", 20))
e11 = Entry(f2, width = 20, bd = 5, bg = "light blue", fg = "black", font = ("Times New Roman", 15))
l22 = Label(f2, text = "kg - lb", bg = "red", fg = "yellow", font= ("Times New Roman", 20))
e12 = Entry(f2, width = 20, bd = 5, bg = "light blue", fg = "black", font = ("Times New Roman", 15))
l23 = Label(f2, text = "kg - st", bg = "red", fg = "yellow", font= ("Times New Roman", 20))
e13 = Entry(f2, width = 20, bd = 5, bg = "light blue", fg = "black", font = ("Times New Roman", 15))

def p9():
    num1 = float(e9.get())
    sum = num1 / 28.35
    l27 = Label(window, text = f"{sum} oz", bg = "light blue", fg = "black", font = ("Times New Roman", 20))
    l27.place(x = 0, y = 600)
def p10():
    num1 = float(e10.get())
    sum = num1 / 28.35 * 1000
    l28 = Label(window, text = f"{sum} oz", bg = "light blue", fg = "black", font = ("Times New Roman", 20))
    l28.place(x = 0, y = 600)
def p11():
    num1 = float(e11.get())
    sum = (num1 / 453.6) 
    l29 = Label(window, text = f"{sum} lb", bg = "light blue", fg = "black", font = ("Times New Roman", 20))
    l29.place(x = 0, y = 600)
def p12():
    num1 = float(e12.get())
    sum = num1 * 2.2046
    l30 = Label(window, text = f"{sum} lb", bg = "light blue", fg = "black", font = ("Times New Roman", 20))
    l30.place(x = 0, y = 600)
def p13():
    num1 = float(e13.get())
    sum = (num1 * 2.2046) / 14
    l31 = Label(window, text = f"{sum} st", bg = "light blue", fg = "black", font = ("Times New Roman", 20))
    l31.place(x = 0, y = 600)

    
btn9 = Button(f2, text = "enter", fg = "green", command= p9, width = 10, height = 1)
btn10 = Button(f2, text = "enter", fg = "green", command= p10, width = 10, height = 1)
btn11 = Button(f2, text = "enter", fg = "green", command= p11, width = 10, height = 1)
btn12 = Button(f2, text = "enter", fg = "green", command= p12, width = 10, height = 1)
btn13 = Button(f2, text = "enter", fg = "green", command= p13, width = 10, height = 1)
f2.pack_propagate(False)
f2.place(x= 0, y=300)
l18.pack()
l19.place(x = 250, y = 350)
l20.place(x = 450, y = 350)
l21.place(x = 650, y = 350)
l22.place(x = 850, y = 350)
l23.place(x = 1050, y = 350)
e9.place(x = 50, y = 380)
e10.place(x = 250, y = 380)
e11.place(x = 450, y = 380)
e12.place(x = 650, y = 380)
e13.place(x = 850, y = 380)
btn9.place(x = 50, y = 410)
btn10.place(x = 250, y = 410)
btn11.place(x = 450, y = 410)
btn12.place(x = 650, y = 410)
btn13.place(x = 850, y = 410)
