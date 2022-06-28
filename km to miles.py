from tkinter import *

window = Tk()
window.minsize(width=400,height=100)
window.title('km to miles converter')
window.config(pady=20,padx=20)

def convert():
    kms = float(input.get())
    miles = round(kms*.62137119224, 2)
    label_4.config(text=miles)

label_1 = Label(text='is equal to ')
label_1.grid(row=1,column=0)

label_2 = Label(text='km ')
label_2.grid(row=0,column=2)

label_3 = Label(text='miles ')
label_3.grid(row=1,column=2)

button = Button(text='calculate', command=convert)
button.grid(row=2,column=1)

input = Entry(width=10)
input.grid(row=0,column=1)

label_4 = Label(text=0)
label_4.grid(row=1,column=1)














window.mainloop()