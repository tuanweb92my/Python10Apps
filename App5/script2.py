from tkinter import *


window = Tk()

def km_to_miles():
    print(e1_value.get())
    grams = float(e1_value.get())*1000
    pounds = float(e1_value.get())*2.2
    ounces = float(e1_value.get())*35.274
    t1.insert(END,grams)
    t2.insert(END,pounds)
    t3.insert(END,ounces)



b1 = Button(window,text="Convert",command=km_to_miles)
# b1.pack()
b1.grid(row=0,column=2)

e1_value = StringVar()
e1 = Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

t1 = Text(window,height=1,width=20)
t1.grid(row=1,column=0)

t2 = Text(window,height=1,width=20)
t2.grid(row=1,column=1)

t3 = Text(window,height=1,width=20)
t3.grid(row=1,column=2)

e2 = Label(window,text="Kg")
e2.grid(row=0,column=0)

window.mainloop()
