from socket import *
import tkinter as tk
import threading
from PIL import ImageTk, Image


def change_image():
    global image_index, label
    image_index = (image_index + 1) % len(images)
    image = images[image_index]
    label.configure(image=image)
    label.image = image


def start_server():
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(("192.168.0.15", 1488))
    server.listen()
    user, addr = server.accept()
    while True:
        data = user.recv(1)
        if not data:
            break
        change_image()


def finish():
    win.destroy()

    
new_thread = threading.Thread(target=start_server)
new_thread.start()

win = tk.Tk()
win.title('Sigma')
win.geometry("448x308+150+80")
win.config(bg='black')
win.minsize(448, 308)
img = ImageTk.PhotoImage(Image.open("images/Am1.png"))
label = tk.Label(win, image=img)
label.pack()
images = [ImageTk.PhotoImage(Image.open("images/Am1.png")), ImageTk.PhotoImage(Image.open("images/Am2.png"))]
image_index = 0
win.protocol("WM_DELETE_WINDOW", finish)
win.mainloop()