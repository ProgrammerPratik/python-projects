import sys
from tkinter import Tk, Text, filedialog, Button, Menubutton, Menu, IntVar

v=sys.version_info

if "2.7" in v:
    from tkinter import *
elif "3.3" in v or "3.4" in v:
    from tkinter import *

root=Tk() 
root.title("editor")

text = Text(root)
text.grid()

def saveas():
    global text
    t = text.get("1.0","end-1c")
    saveloc = filedialog.asksaveasfilename()
    file1=open(saveloc,"w+")
    file1.write(t)
    file1.close()
    
button = Button(root, text="save", command=saveas)
button.grid()

def fontHelvetica():
    text.config(font="Helvetica")
def fontCourier():
    text.config(font="Courier")

font = Menubutton(root, text="font")
font.grid()
font.menu = Menu(font,tearoff=0)
font["menu"] = font.menu
helvetica=IntVar() 
courier=IntVar()
font.menu.add_checkbutton(label='Courier', variable = courier, command=fontCourier)
font.menu.add_checkbutton(label='Helvetica', variable = courier, command=fontHelvetica)

root.mainloop()