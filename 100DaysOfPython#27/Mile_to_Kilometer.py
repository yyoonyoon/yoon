from tkinter import *

window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=300, height=150)
window.config(padx= 20, pady= 20)

# Function
def mile_to_km():
    miles = user_input.get()
    km = int(miles) * 1.609
    result_label.config(text=km)

# Entry
user_input = Entry(width= 10)
user_input.grid(column= 10, row= 5)

# Label
mile_label = Label(text= "Miles", font=('Arial', 15, 'bold'))
mile_label.grid(column= 15, row= 5)

km_label = Label(text= "Km", font=('Arial', 15, 'bold'))
km_label.grid(column= 15, row= 7)

my_label = Label(text= "is equal to", font=('Arial', 15, 'bold'))
my_label.grid(column=10, row=6)

result_label = Label(text= "0", font=('Arial', 15, 'bold'))
result_label.grid(column=10, row=7)

# Button
button = Button(text="Convert", command= mile_to_km)
button.grid(column= 10, row= 10)

window.mainloop()