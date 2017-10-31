
import tkinter as tk


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.add_img = tk.PhotoImage(file='add.gif')
        self.init_main()

    # инициализация элементов окна
    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        btn_open_dialog = tk.Button(toolbar, text='Добавить позицию', command=self.open_dialog(),
                                    bg='#d7d8e0', bd=0, compound=tk.TOP, image=self.add_img)
        btn_open_dialog.pack(side=tk.LEFT)

    def open_dialog(self):
        Child()

# class Main =======


class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()

    def init_child(self):
        self.title('Добавить доходы/расходы')
        self.geometry('400x220+400+300')
        self.resizable(False, False)
        # удерживать фокус на дочернем окне и перехватывать все действия
        self.grab_set()
        self.focus_set()

# class Child =======


if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Household finance")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()
    
# https://www.youtube.com/watch?v=7Hu5Vm88Q0Y
# https://gist.github.com/ithobbies/9e28614fff04d6c2fa61362329ea82d4
