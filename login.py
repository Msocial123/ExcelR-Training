def login():
    username = "makeuseof"
    password = "muo"

    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login Successful!", message="You successfully logged in.")
    else:
        messagebox.showerror(title="Error", message="Invalid login.")
