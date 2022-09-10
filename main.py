import sqlite3

connection = sqlite3.connect('sqlite.db')
c.connection.cursor() 

import tkinter as tk
from tkinter import *
from tkinter import massagebox
from tkinter.messagebox import showerror

window = tk.Tk()
window.title("My app")
window.minsize(width=300, height=300)
window.minsize(width=500, height=500)
#window.geometry("500x300")

def text():
    label['text'] = entry.get()
    text.insert(tk.END, entry.get())

def info():
    messagebox.showerror("info", "Hello world")

label = tk.Label(text="Hello world", bg="white", fg="000000")
lable.pack()

label2 = tk.Label(text="Hello world", bg="white", fg="000000")
lable2.pack()

button = tk.Button(text="Push me", bg="white", fg="red", command=text)
button.pack()

info_button = tk.Button(text="Info", bg="white", fg="red", command=info)
info_button.pack()

entry = tk.Entry(bg="white", fg="red")
entry.pack()

entry2 = tk.Entry(bg="white", fg="red")
entry2.pack()

text = tk.Text(width=40, height=40, wrap="word")
scrollbar = Scrollbar(orient=VERTICAL, command=text.yview)
scrollbar.pack(side="right", fill="y")
text.configure(yscrollcommand=scrollbar.set)
text.pack()

window.mainloop()