from tkinter import *

window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('400x200')

lbl = Label(window, text="Hello")
# Set label font size
# lbl = Label(window, text="Hello", font=("Arial Bold", 50))
# lbl.pack()
lbl.grid(column=0, row=0)

# Get input using Entry class (Tkinter textbox)
txt = Entry(window, width=10)
txt.grid(column=1, row=0)
txt.focus()
txt1 = Entry(window, width=10, state='disable')
txt1.grid(column=1, row=2)


# Handle button click event
def clicked():
    res = "Welcome to " + txt.get()
    # lbl.configure(text="Button was clicked !!")
    lbl.configure(text=res)
    # txt1.delete(0, END)
    txt1.insert(0, txt.get())


# btn = Button(window, text="Click Me")
# Change button foreground and background colors
# btn = Button(window, text="Click Me", bg="orange", fg="white")
# btn.grid(column=1, row=0)
btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=2, row=0)


window.mainloop()
