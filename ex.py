'''from tkinter import *

# pip install pillow
from PIL import Image, ImageTk



def image(a):
    root = Toplevel()
    root.wm_title("Tkinter window")
    root.geometry("200x120")
    bb=Label(root,text='HIIII')
    bb.pack()
    load = Image.open(a,'r')
    load=load.resize((100,100),Image.ANTIALIAS)
    render = ImageTk.PhotoImage(load)
    img = Label(master=root,image=render)
    img.image = render
    img.place(x=0, y=0)


root1 = Tk()
root1.wm_title("Tkinter window")
root1.geometry("200x120")
e=Entry(root1)
e.pack()
b=Button(text="CLICK",command=lambda:image(e.get()))
b.pack()
root1.mainloop()'''
from time import gmtime, strftime
x = strftime("%d/%m/%Y")
y = strftime("24/06/2021")
print(x-y)