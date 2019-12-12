from tkinter import *
root = Tk()

Heros= ['tk','ck','pander','cat']
v = []

for hero in Heros:
    v.append(IntVar)
    b = Checkbutton(root,text = hero,variable = v[-1])
    b.pack()
mainloop()