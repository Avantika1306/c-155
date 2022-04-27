from tkinter import *
import random
root=Tk()
root.geometry("600x600")
root.title("color changer")
dictionary={"color":["purple","red","blue","black","pink","yellow","brown"]}

def changeColor():
    randomnumber=random.randint(0,6)
    root.configure(background=dictionary["color"][randomnumber])
    

button1=Button(root,text="change background",command=changeColor)
button1.place(relx=0.5,rely=0.4,anchor=CENTER)

root.mainloop()