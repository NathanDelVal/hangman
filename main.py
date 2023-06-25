import tkinter as tk
from tkinter import messagebox

def say_hello():
    messagebox.showinfo("Message", "Hello!")

def say_goodbye():
    messagebox.showinfo("Message", "Goodbye!")

root = tk.Tk()

# Create the menu bar
menu_bar = tk.Menu(root)

# Create the File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Hello", command=say_hello)
file_menu.add_command(label="Goodbye", command=say_goodbye)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Add the File menu to the menu bar
menu_bar.add_cascade(label="File", menu=file_menu)

# Configure the root window to use the menu bar
root.config(menu=menu_bar)

root.mainloop()
