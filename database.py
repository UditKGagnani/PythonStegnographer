from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

# conn = mysql.connect(host="localhost", user="root", passwd="root", database="steganographer_database")
# c = conn.cursor()
# c.execute("DROP TABLE test1")

# c.execute("CREATE DATABASE steganographer_database")
# c.execute("CREATE TABLE demo1(secret_key text, image_name text)")
# c.execute("CREATE TABLE demo2(secret_key text, image_name text)")

# c.execute("INSERT INTO demo1(secret_key, image_name) VALUES('aaa', 'a1a1a1')")
# c.execute("INSERT INTO demo1(secret_key, image_name) VALUES('bbb', 'b2b2b2')")
# c.execute("INSERT INTO demo1(secret_key, image_name) VALUES('ccc', 'c3c3c3')")
# c.execute("INSERT INTO demo1(secret_key, image_name) VALUES('ddd', 'd4d4d4')")
#
#
# c.execute("INSERT INTO demo2(secret_key, image_name) VALUES('aaa', 'a1a1a1')")
# c.execute("INSERT INTO demo2(secret_key, image_name) VALUES('bbb', 'b2b2b2')")
# c.execute("INSERT INTO demo2(secret_key, image_name) VALUES('ccc', 'c3c3c3')")
# c.execute("INSERT INTO demo2(secret_key, image_name) VALUES('ddd', 'd4d4d4')")
#
# conn.commit()

# c.execute("SELECT * FROM demo1")
# content = []
# for i in c:
#     content.append(i)
# print(content)
#
# c.execute("SELECT * FROM demo2")
# content = []
# for i in c:
#     content.append(i)
# print(content)

# c.execute("DROP TABLE demo1")
# c.execute("DROP TABLE demo2")
# conn.commit()

def list_all_tables():
    conn = mysql.connect(host="localhost", user="root", passwd="root", database="steganographer_database")
    c = conn.cursor()
    c.execute("SHOW TABLES FROM steganographer_database")
    tables = []
    for i in c:
        tables.append(i[0])
    return tables
    conn.commit()

tables = list_all_tables()
print(tables)

def add_content(table_name,image_name,key,hash_key,text_file):
    conn = mysql.connect(host="localhost", user="root", passwd="root", database="steganographer_database")
    c = conn.cursor()
    print(table_name)
    query = ""
    for i in tables:
        if table_name == i:
            query = f"INSERT INTO {i}(secret_key, image_name) VALUES('{key}', '{image_name}')"
            break
    if query == "":
        query = f"CREATE TABLE {table_name}(secret_key text, image_name text)"
    print(query)
    c.execute(query)
    c.execute(f"SELECT * FROM {table_name}")
    contents = []
    for i in c:
        contents.append(i[0])
    with open(f'Admin_{table_name}.txt','a') as f:
        f.write(f"Key             : {key}\n" +
                f"Hashed Key      : {hash_key}\n" +
                f"Image Location  : {image_name}\n" +
                f"Text File       : {text_file}\n"+"\n\n")
    # MessageBox.showinfo("Data Inserted Successfully")
    conn.commit()


def view_content(table_name):
    conn = mysql.connect(host="localhost", user="root", passwd="root", database="steganographer_database")
    c = conn.cursor()
    view_window = Tk()
    view_window.title("Steganographer (View)")
    view_window.iconbitmap("images/key_icon.ico")
    view_window.configure(background="#39014c")

    app_height = 400
    app_width = 700

    sw = view_window.winfo_screenwidth()
    sh = view_window.winfo_screenheight()

    x = int((sw / 2) - (app_width / 2))
    y = int((sh / 2) - (app_height / 2))

    view_window.geometry(f'{app_width}x{app_height}+{x}+{y}')

    c.execute(f"SELECT * FROM {table_name}")

    a = []
    for i in c:
        a.append(i[1])

    print("Query: ",f"SELECT * FROM {table_name}")
    print(a)

    conn.commit()

    # key_head_label = Label(view_window,text="Secret Key", font=("Times New Roman", 15, "bold"),bg="#39014c",
    #                 fg="white").grid(row=0, column=0)
    # empty_head_label = Label(view_window, text="\t\t\t", font=("Times New Roman", 15, "bold"), bg="#39014c",
    #                        fg="white").grid(row=0, column=1)
    image_head_label = Label(view_window, text="Image Location", font=("Times New Roman", 15, "bold"), bg="#39014c",
                           fg="white").grid(row=0, column=0)

    if len(a) == 0:
        no_content_label = Label(view_window, text="No Content Available", font=("Times New Roman", 15, "bold"), bg="#39014c",
                           fg="white").place(x=0, y=35)
    else:
        for i in range(len(a)):
            if len(a[i])>40:
                img_label = Label(view_window, text=" "+a[i][:40]+"\n"+a[i][40:], font=("Times New Roman", 15, "bold"), bg="#39014c",
                               fg="white").grid(row=1+i, column=0)
            else:
                img_label = Label(view_window, text=" " + a[i], font=("Times New Roman", 15, "bold"), bg="#39014c",
                                  fg="white").grid(row=1 + i, column=0)
            empty_label = Label(view_window, text="\t\t", font=("Times New Roman", 15, "bold"), bg="#39014c",
                              fg="white").grid(row=1 + i, column=1)
            open_btn = Button(view_window, text="Open", font=("Times New Roman", 15, "bold"), bg="#39014c",
                              fg="white").grid(row=1+i, column=2)


    view_window.mainloop()

def delete_table(table_name):
    print(f"TABLE THAT IS GOING TO BE DELETED: {table_name}")
    conn = mysql.connect(host="localhost", user="root", passwd="root", database="steganographer_database")
    c = conn.cursor()
    c.execute(f"DROP TABLE {table_name}")
    conn.commit()


# print(tables)
#
# a = c.execute("""SELECT name FROM sqlite_master WHERE type='table'
#   AND name='temp1';""")
# print(a)

# c.execute("""CREATE TABLE table1(
# key text,
# image text
# )""")
# c.execute("""CREATE TABLE table2(
# key text,
# image text
# )""")
# c.execute("""CREATE TABLE table3(
# key text,
# image text
# )""")
#
# c.execute("""DROP TABLE demo1""")
# c.execute("""DROP TABLE table2""")
# c.execute("""DROP TABLE table3""")

# c.execute("""INSERT INTO table3(key,image) VALUES('CCCC','CCCC')""")
# c.execute("""INSERT INTO table3(key,image) VALUES('DDDD','DDDD')""")
# 
# c.execute("""SELECT * FROM table1""")
# a = c.fetchall()
# print(a[0][0])
# c.execute("""SELECT * FROM table2""")
# print(c.fetchall())
# c.execute("""SELECT * FROM table3""")
# print(c.fetchall())
# 
#
# c.execute("commit")




