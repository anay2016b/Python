from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = Tk()
window.title("Text Editor")
window.geometry("800x450")
window.rowconfigure(1, minsize=200, weight = 1)
window.columnconfigure(1, minsize=200, weight = 1)
window.configure(bg = "silver")
window.mainloop()

def open_file():
    filepath = askopenfilename(filetypes=([("Text Files", "*.txt"), ("All Files", "*.*")]))
    if not filepath:
        return
    txt_edit = Text(window)
    txt_edit.delete(1.0, END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(END, text) 
        