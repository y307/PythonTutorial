
from tkinter import *
from tkinter import ttk


root = Tk()
root.geometry("500x300")
root.title("Простой проект")

btn1 = ttk.Button(root, text="Кнопка 1")
btn1.pack()

btn2 = ttk.Button(root, text="Кнопка 2")
btn2.pack()

text1 = Label(root, text="Новый шрифт", font="Arial 24")
text1.pack()

btn3 = ttk.Button(root, text="Кнопка left")
btn3.pack(side="left")

btn4 = ttk.Button(root, text="Кнопка right")
btn4.pack(side="right")

btn5 = ttk.Button(root, text="Кнопка top")
btn5.pack(side="top")

btn6 = ttk.Button(root, text="Кнопка bottom")
btn6.pack(side="bottom")

root.mainloop()
