import tkinter as tk

canvas_width = 700
canvas_height = 500

root = tk.Tk()
root.title('Paint')
w = tk.Canvas(root,
              width=canvas_width,
              height=canvas_height,
              bg='white')
w.bind('<B1-Motion>')

root.mainloop()
