from tkinter import *
import database
from PIL import ImageTk, Image

def open(sh,sw):
    storage_window = Tk()
    storage_window.title("Steganographer (Storage)")
    storage_window.iconbitmap("images/key_icon.ico")
    storage_window.configure(background="#39014c")

    app_height = 400
    app_width = 500

    x = int((sw / 2) - (app_width / 2))
    y = int((sh / 2) - (app_height / 2))

    storage_window.geometry(f'{app_width}x{app_height}+{x}+{y}')
    
    tables = database.list_all_tables()
    # print(tables)
    if len(tables) == 0:
        status_lb = Label(storage_window,text="Our Database is empty",
                          bg="#39014c",fg="white",font=("Times New Roman", 25, "bold")).place(x=85,y=10)
    else:
        for i in range(len(tables)):
            name = tables[i]
            lb = Label(storage_window,text=name,bg="#39014c",fg="white",
                       font=("Times New Roman", 25, "bold")).grid(row=i+1,column=0)
            empty_lb1 = Label(storage_window,text="\t\t\t\t\t\t", bg="#39014c").grid(row=i+1,column=1)
            btn= Button(storage_window,text="View",
                        command=lambda name=name:[storage_window.destroy(),
                                                  database.view_content(name)]).grid(row=i+1, column=2)
            empty_lb2 = Label(storage_window, text="  ", bg="#39014c").grid(row=i + 1, column=3)
            del_btn = Button(storage_window, text="Delete",
                             command=lambda name=name: [storage_window.destroy(), database.delete_table(name),
                                                        open(sh, sw)]).grid(row=i + 1, column=4)

    storage_window.mainloop()
