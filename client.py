import tkinter as tk
from socket import *

def click():
    client.send(bytes("\00", 'ascii'))

def finish():
    win.destroy()

win = tk.Tk()

win.title('POPtoSigma')
win.geometry("120x80+120+80")
win.config(bg='black')
btn = tk.Button(win, text='POP', font="Arial 15", width=4, height=2, command=click)
btn.place(relx=0.5, rely=0.5, anchor='center')

client = socket(AF_INET, SOCK_STREAM)
client.connect(("192.168.0.15", 1488))

win.mainloop()
client.close()
