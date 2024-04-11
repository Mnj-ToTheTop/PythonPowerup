import tkinter as tk        #Shorten the name
from tkinter import filedialog, Text

root = tk.Tk()
root.title("Notepad")
root.geometry("600x400")

#Creating functionality of menu

def open_file():
    filename = filedialog.askopenfilename()
    if filename:
        with open(filename, 'r') as f:
            content = f.read()
            root.text_widget.delete('1.0', "end")    # deleting the already present data in the notepad.
            root.text_widget.insert('1.0', content)  # inserting the new content

def new_file():
    root.text_widget.delete('1.0', "end")    # deleting the already present data in the notepad.

def save_file():
    filename = filedialog.asksaveasfilename()
    if filename:
        with open(filename, 'w') as f:
            f.write(root.text_widget.get('1.0', "end"))

menubar = tk.Menu()
fileMenu = tk.Menu(menubar)
fileMenu.add_command(label = "New", command = new_file)
fileMenu.add_command(label = "Open", command = open_file)
fileMenu.add_command(label = "Save", command = save_file)
fileMenu.add_command(label = "Exit", command = root.quit)
root.config(menu=fileMenu)

root.text_widget = Text(root)
root.text_widget.pack(expand = True, fill = 'both')

root.mainloop()     # Layout is created
