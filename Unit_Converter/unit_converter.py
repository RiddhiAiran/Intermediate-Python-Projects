from tkinter import *

def convert():
    '''Convert miles to kms and shows the output on GUI'''
    miles = float(user_input.get())
    kms = miles * 1.60934
    output_text.config(text=round(kms,2))

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=500, height=500)
window.config(padx=50, pady=50)

user_input = Entry(width=10)
user_input.grid(column=1, row=0)

miles = Label(text='Miles',font=('Arial',15))
miles.grid(column=2, row=0)

equals_to = Label(text='is equals to',font=('Arial',15))
equals_to.grid(column=0, row=1)

output_text = Label()
output_text.grid(column= 1, row=1)

km = Label(text='Km',font=('Arial',15))
km.grid(column=2, row=1)

submit = Button(text='Submit', command=convert)
submit.grid(column=1, row=2)




window.mainloop()

