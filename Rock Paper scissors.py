from tkinter import * 
from tkinter import messagebox
import PIL
from PIL import Image, ImageTk
import random
from datetime import date, time, datetime

window = Tk()
window.geometry("800x600")
window.title("Rock Paper Scissors")
score_user = 0
score_computer = 0
combination = 0
def play():
    choices = ["Rock", "Paper", "Scissors"]
    user_choice = ""
    computer_choice = random.choice(choices)
    b2 = Button(window, text = "Rock", bg = "silver", fg = "black", font = ("Times New Roman", 20, "bold"))
    b2.pack(pady=10)
    b3 = Button(window, text = "Paper", bg = "silver", fg = "black", font = ("Times New Roman", 20, "bold"))
    b3.pack(pady=10)
    b4 = Button(window, text = "Scissors", bg = "silver", fg = "black", font = ("Times New Roman", 20, "bold"))
    b4.pack(pady=10)
    if user_choice == computer_choice:
        combination = 1
    elif user_choice == "Rock" and computer_choice == "Scissors":
        combination = 2
    elif user_choice == "Scissors" and computer_choice == "Paper":
        combination = 3
    elif user_choice == "Paper" and computer_choice == "Rock":
        combination = 4    
    elif user_choice == "Scissors" and computer_choice == "Rock":
        combination = 5
    elif user_choice == "Paper" and computer_choice == "Scissors":
        combination = 6
    elif user_choice == "Rock" and computer_choice == "Paper":
        combination = 7 
        
        
        
l1 = Label(window, text="First to 5 wins!", bg="gold", fg="black", font=("Times New Roman", 20, "bold"))
b1= Button(window, text="Let's Play", command=play)
b1.pack(pady=20)

window.mainloop()