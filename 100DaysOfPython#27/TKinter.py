from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(height=300,width=500)
window.config(padx= 20, pady= 20)

# Label
my_label = Label(text= "New Text", font=('Arial', 24, 'bold'))
my_label.grid(column=0, row=0)

# Button
def button_clicked():
    print("I got clicked")
    user_input = input.get()
    my_label["text"] = user_input

button = Button(text="click me", command=button_clicked)
button.grid(column= 2, row= 2)
button_2 = Button(text="Second Button", command=button_clicked)
button_2.grid(column=3, row=1)

# Entry
input = Entry()
input.grid(column= 4, row= 3)


window.mainloop()