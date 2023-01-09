from tkinter import *
from PIL import ImageTk, Image

def open(sh,sw):
    decode_window = Tk()
    decode_window.title("Steganographer (Decode)")
    decode_window.iconbitmap("images/key_icon.ico")

    app_height = 400
    app_width = 500

    x = int((sw / 2) - (app_width / 2))
    y = int((sh / 2) - (app_height / 2))

    decode_window.geometry(f'{app_width}x{app_height}+{x}+{y}')

    decode_window.mainloop()
