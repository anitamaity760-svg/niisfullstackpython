import tkinter as tk
from tkinter import filedialog

# Functions
def new_file():
    text_area.delete(1.0, tk.END)

def open_file():
    file = filedialog.askopenfile(mode='r')
    if file:
        content = file.read()
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, content)

def save_file():
    file = filedialog.asksaveasfile(mode='w')
    if file:
        content = text_area.get(1.0, tk.END)
        file.write(content)

# Main Window
root = tk.Tk()
root.title("Simple Notepad")
root.geometry("600x400")

# Text Area
text_area = tk.Text(root)
text_area.pack(expand=True, fill='both')

# Menu Bar
menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)

# Run App
root.mainloop()