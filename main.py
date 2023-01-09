# *********************** PROGRAM BY: *****************************
# ||          ||  ||====\\      ===============  ================ #
# ||          ||  ||      \\          ||                ||        #
# ||          ||  ||        \\        ||                ||        #
# ||          ||  ||          ||      ||                ||        #
# ||          ||  ||          ||      ||                ||        #
# ||          ||  ||        //        ||                ||        #
# ||          ||  ||      //          ||                ||        #
# ||==========||  ||====//      ===============         ||        #
# ********************** ON: 19/9/2021 ****************************

from tkinter import *
import encode
import decode
import storage
from PIL import ImageTk, Image

root = Tk()

root.title("Steganographer")
root.iconbitmap("images/key_icon.ico")
root.configure(background="#39014c")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

app_width = 260
app_height = 300

x = int((screen_width / 2) - (app_width / 2))
y = int((screen_height / 2) - (app_height / 2))

root.geometry(f'{app_width}x{app_height}+{x}+{y}')

pic_1 = Image.open("images/encodebutton.png")
pic_2 = Image.open("images/decodebutton.png")
pic_3 = Image.open("images/databasebutton.png")

pic_1 = pic_1.resize((250, 80), Image.ANTIALIAS)
pic_2 = pic_2.resize((250, 80), Image.ANTIALIAS)
pic_3 = pic_3.resize((250, 80), Image.ANTIALIAS)

en_btn = ImageTk.PhotoImage(pic_1)
de_btn = ImageTk.PhotoImage(pic_2)
db_btn = ImageTk.PhotoImage(pic_3)

encode_btn = Button(root, image=en_btn, borderwidth=0, bg="#39014c",
                    command=lambda: [root.destroy(), encode.open(screen_height, screen_width)]).place(x=5, y=10)
decode_btn = Button(root, image=de_btn, borderwidth=0, bg="#39014c",
                    command=lambda: [root.destroy(), decode.open(screen_height, screen_width)]).place(x=5, y=95)
database_btn = Button(root, image=db_btn, borderwidth=0, bg="#39014c",
                      command=lambda: [root.destroy(), storage.open(screen_height, screen_width)]).place(x=5, y=180)

# encode_btn = Button(root, text="Encode", font=("Times New Roman", 20, "bold"),
#                     command=lambda: [root.destroy(), encode.open(screen_height, screen_width)]).place(x=50, y=50)
# decode_btn = Button(root, text="Decode", font=("Times New Roman", 20, "bold"),
#                     command=lambda: [root.destroy(), decode.open(screen_height, screen_width)]).place(x=200, y=50)

creator_label = Label(root, text="Created By: Udit Gagnani", font=("bold", 15), bg="#39014c", fg="white").place(x=15, y=270)

root.mainloop()
