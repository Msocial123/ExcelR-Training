import tkinter
from tkinter import messagebox
window = tkinter.Tk()
window.title("Login Page using Python")
window.geometry('750x550')
window.configure(bg='#8F00FF')

def login():
    username = "makeuseof"
    password = "muo"

    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login Successful!", message="You successfully logged in.")
    else:
        messagebox.showerror(title="Error", message="Invalid login.")
