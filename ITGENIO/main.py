from tkinter import *
from tkinter import messagebox
import pickle

root = Tk()
root.geometry("300x350")
root.title("Войти в систему")


def registration():
    text = Label(text="Для входа в систему зарегистрируйтесь!")
    text_log = Label(text="Введите Ваш логин:")
    registr_login = Entry()
    text_pass1 = Label(text="Введите Ваш пароль:")
    registr_pass1 = Entry()
    text_pass2 = Label(text="Еще раз Ваш пароль:")
    registr_pass2 = Entry(show="*")
    button_register = Button(text="Регистрация", command=lambda: save())
    text.pack()
    text_log.pack()
    registr_login.pack()
    text_pass1.pack()
    registr_pass1.pack()
    text_pass2.pack()
    registr_pass2.pack()
    button_register.pack()

    def save():
        login_pass_save = {registr_login.get(): registr_pass1.get()}
        # login_pass_save[registr_login.get()] = registr_pass1.get()
        f = open("login.txt", "wb")
        pickle.dump(login_pass_save, f)
        f.close()
        login()


def login():
    text_log = Label(text="Вход в систему")
    text_enter_login = Label(text="Введите логин:")
    enter_login = Entry()
    text_enter_pass = Label(text="Введите пароь:")
    enter_pass = Entry(show="*")
    button_enter = Button(text="Войти", command=lambda: log_pass())
    text_log.pack()
    text_enter_login.pack()
    enter_login.pack()
    text_enter_pass.pack()
    enter_pass.pack()
    button_enter.pack()

    def log_pass():
        f = open("login.txt", "rb")
        a = pickle.load(f)
        f.close()
        if enter_login.get() in a:
            if enter_pass.get() == a[enter_login.get()]:
                messagebox.showinfo("Вход выполнен", "Привет!")
            else:
                messagebox.showerror("Ошибка входа!", "Неправильный пароль!")
        else:
            messagebox.showerror("Ошибка входа!", "Неправильный логин!")


registration()
# login()
root.mainloop()
