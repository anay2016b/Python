from tkinter import *
from tkinter import messagebox
# Not yet submitted
Window = Tk()
Window.title("Password strength checker")
Window.geometry("800x600")
Window.config(bg="yellow")
f1 = Frame(master = Window, width=400, height=200, bg="lightblue", relief=RAISED, borderwidth=10)
f1.pack()
label = Label(f1, text="Enter your password:")
label.pack(pady = 10)

entry = Entry(f1, show="*")
entry.pack(pady = 20)

b2 = Button(f1, text="Show Password", command=lambda: entry.config(show=""))
b2.pack(pady = 10)
b3 = Button(f1, text="Hide Password", command=lambda: entry.config(show="*"))
b3.pack(pady = 10)

def check_password_strength():
    password = entry.get()
    if len(password) <= 5:
        if any(char in password for char in "!@$%^&*()#_+-=₹~¡™£₹§ˆ¶•̐°⁄€‹›†‡°·©®·‚–≠—±✓Œ˙´®Þ¥¨ʼØ,¯SSÐƒ©ˍ˝˚-ˀ.¸ˇ˘˜˛,.<>/?≤≥÷"):
            result = "Weak"
        else:
            result = "Very Weak"
    elif len(password) <= 8:
        if any(char in password for char in "!@$%^&*()#_+-=₹~¡™£₹§ˆ¶•̐°⁄€‹›†‡°·©®·‚–≠—±✓Œ˙´®Þ¥¨ʼØ,¯SSÐƒ©ˍ˝˚-ˀ.¸ˇ˘˜˛,.<>/?≤≥÷"):
            result = "Moderate"
        else:
            result = "Weak"
    elif len(password) <= 13:
        if any(char in password for char in "!@$%^&*()#_+-=₹~¡™£₹§ˆ¶•̐°⁄€‹›†‡°·©®·‚–≠—±✓Œ˙´®Þ¥¨ʼØ,¯SSÐƒ©ˍ˝˚-ˀ.¸ˇ˘˜˛,.<>/?≤≥÷"):
            result = "Strong"
        else:
            result = "Moderate"
    elif len(password) > 13:
        if any(char in password for char in "!@$%^&*()#_+-=₹~¡™£₹§ˆ¶•̐°⁄€‹›†‡°·©®·‚–≠—±✓Œ˙´®Þ¥¨ʼØ,¯SSÐƒ©ˍ˝˚-ˀ.¸ˇ˘˜˛,.<>/?≤≥÷"):
            result = "Very Strong"
        else:
            result = "Strong"
    messagebox.showinfo("Password Strength", f"Your password is: {result}")
button = Button(f1, text="Check Password", command=check_password_strength)
button.pack(pady = 25)
# Not yet submitted
Window.mainloop()