
from tkinter import *
from tkinter import ttk


root = Tk()
root.geometry("500x300")
root.title("Test 3")

btn1 = ttk.Button(root, text="Кнопка 1")
btn1.grid(row=1, column=2, pady=3)

btn2 = ttk.Button(root, text="Кнопка 2")
btn2.grid(row=2, rowspan=3, column=3, pady=6)

text1 = Label(root, text="Новый шрифт", font="Arial 24")
text1.grid()


root.mainloop()
