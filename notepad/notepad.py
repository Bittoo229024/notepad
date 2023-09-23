from tkinter import *
from tkinter import filedialog as fd
import tkinter as tk
from tkinter.filedialog import asksaveasfile
# from tkinter import font
notepad = Tk()


#open file


def open():
    global t
    filetypes = (('Text files', '.txt'), ('All files', '.*'))
    f = fd.askopenfile(filetypes=filetypes)
    if f:
        t.delete('1.0', tk.END) 
        t.insert('1.0', f.read())
        f.close()


#save file



def save():
    content = t.get('1.0', tk.END)
    f = asksaveasfile(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("Text Documents", "*.txt")])
    if f:
        f.write(content)
        f.close()


# font 
def Brush_Script_Std():
     t["font"]= ("Brush Script Std",18)	
    
def Courier():
     t["font"]= ("Courier",18)

def bold():
     t["font"]= ("Bold",18)


def Cooper_Std_Black():
     t["font"]= ("Cooper Std Black",18)    



def curlz_mt():
     t["font"]= ("Curlz MT",18)

def Harlow_Solid_Italic():
     t["font"]= ("Harlow Solid Italic",18)


def Imprint_MT_Shadow():
     t["font"]= ("Imprint MT Shadow",18)

def Rosewood_Std_Regular():
     t["font"]= ("Rosewood Std Regular",18)

def TypoUpright_BT():
     t["font"]= ("TypoUpright BT",18)





    
notepad.title("Notepad Bittoo")


#starting file menu

menubar = Menu(notepad)
notepad.config(menu=menubar)

file_Menu = Menu(menubar)

file_Menu.add_command(label="Open",command=open )
file_Menu.add_command(label="Save",command=save)



menubar.add_cascade(menu=file_Menu,label="File")

#second edit menu barr

notepad.config(menu=menubar)


edit_Menu = Menu(menubar)


menubar.add_cascade(menu=edit_Menu,label="Edit")


#third view menu  bar

notepad.config(menu=menubar)


view_Menu = Menu(menubar)


menubar.add_cascade(menu=view_Menu,label="View")


#forth font menu bar

font_menu = Menu(menubar)

font_menu.add_command(label="Bold",command=bold)
font_menu.add_separator()


font_menu.add_command(label="Courier",command=Courier)
font_menu.add_separator()


font_menu.add_command(label="Brush Script Std",command=Brush_Script_Std)
font_menu.add_separator()


font_menu.add_command(label="Cooper Std Black",command=Cooper_Std_Black)
font_menu.add_separator()


font_menu.add_command(label="Curlz MT",command=curlz_mt)
font_menu.add_separator()


font_menu.add_command(label="Harlow Solid Italic",command=Harlow_Solid_Italic)
font_menu.add_separator()



font_menu.add_command(label="Imprint MT Shadow",command=Imprint_MT_Shadow)
font_menu.add_separator()


font_menu.add_command(label="Rosewood Std Regular",command=Rosewood_Std_Regular)
font_menu.add_separator()

font_menu.add_command(label="TypoUpright BT",command=TypoUpright_BT)
font_menu.add_separator()







menubar.add_cascade(menu=font_menu,label="Font")





t = Text(notepad,height=43,width=560)
t.pack(expand=True)
mainloop()