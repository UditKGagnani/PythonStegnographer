from tkinter import *
from tkinter import filedialog
import bcrypt
import database
from PIL import ImageTk, Image


def display():
    print("Image File :",file_img)
    print("Text File  :",file_txt)
    print("Hashed Key :",hash_key)

def store_data(key):
    global hash_key
    print("Original Key:",key)
    key = bytes(key,'utf-8')
    hash_key = bcrypt.hashpw(key,bcrypt.gensalt())

def choose_image():
    global file_img
    global hash_filename
    file_img = filedialog.askopenfilename(title="Choose an Image", filetypes=(("jpg file","*.jpg"),("png file","*.png")))
    hash_file_img = bytes(file_img,'utf-8')
    hash_filename = bcrypt.hashpw(hash_file_img,bcrypt.gensalt())
    print(file_img)

def choose_text():
    global file_txt
    file_txt = filedialog.askopenfilename(title="Choose a Text File", filetypes=(("text file","*.txt"),("word file","*.word")))
    print(file_txt)

def open(sh,sw):

    def return_entry():
        global key
        global table_name
        key = keyValue.get()
        table_name = tableValue.get()
        print("Main Part:", key, table_name)

    encode_window = Tk()
    encode_window.title("Steganographer (Encode)")
    encode_window.iconbitmap("images/key_icon.ico")
    encode_window.configure(background="#39014c")

    app_height = 400
    app_width = 500

    x = int((sw / 2) - (app_width / 2))
    y = int((sh / 2) - (app_height / 2))

    encode_window.geometry(f'{app_width}x{app_height}+{x}+{y}')

    photo_lbl = Label(encode_window,text="Choose an Image     : ", font=("Times New Roman", 15, "bold"),bg="#39014c",
                      fg="white").place(x=50,y=30)
    text_lbl = Label(encode_window, text="Choose Text File     : ", font=("Times New Roman", 15, "bold"),bg="#39014c",
                     fg="white").place(x=50, y=105)
    key_lbl = Label(encode_window, text="Enter Secret Code  : ", font=("Times New Roman", 15, "bold"),bg="#39014c",
                    fg="white").place(x=50, y=180)
    table_lbl = Label(encode_window, text="Enter Table Name  : ", font=("Times New Roman", 15, "bold"), bg="#39014c",
                    fg="white").place(x=50, y=255)

    pic_1 = Image.open("images/encodebutton.png")
    pic_2 = Image.open("images/choosefilebutton.png")
    pic_1 = pic_1.resize((180, 60), Image.ANTIALIAS)
    pic_2 = pic_2.resize((180, 60), Image.ANTIALIAS)

    en_btn = ImageTk.PhotoImage(pic_1)
    choose_btn = ImageTk.PhotoImage(pic_2)

    photo_btn = Button(encode_window, image=choose_btn, bg="#39014c", borderwidth=0, command=choose_image).place(x=250, y=18)
    text_btn = Button(encode_window, image=choose_btn, bg="#39014c", borderwidth=0, command=choose_text).place(x=250, y=93)

    keyValue = StringVar()
    tableValue = StringVar()

    key_entry = Entry(encode_window, textvariable=keyValue, width=16, font=("Times New Roman", 15, "bold"))
    key_entry.place(x=260,y=183)

    table_entry = Entry(encode_window, textvariable=tableValue, width=16, font=("Times New Roman", 15, "bold"))
    table_entry.place(x=260, y=255)

    convert_btn = Button(encode_window,image=en_btn, bg="#39014c", borderwidth=0,
                         command=lambda: [encode_window.destroy(), return_entry(), store_data(key),
                                          display(), database.add_content(table_name, 
                                                                          file_img, key, hash_key, file_txt)]).place(x=160,y=315)

    encode_window.mainloop()

