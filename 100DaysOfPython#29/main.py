from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def rand_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_is_clicked():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message= "Please don't leave any fields empty")

    else:
        is_ok = messagebox.askokcancel(title="Website", message=f"These are the details entered: \n\
            Email: {email}\n Password: {password}\n Is it ok to save?")
        if is_ok:
            with open("/Users/yeomsangyoon/Visual Studio/Practice File/100DaysOfPython#29/data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
# canvas
canvas = Canvas(width=200, height= 200)
locker_img = PhotoImage(file= "/Users/yeomsangyoon/Visual Studio/Practice File/100DaysOfPython#29/logo.png")
canvas.create_image(100 ,100, image = locker_img)
canvas.grid(column=1, row=0)
# label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
name_label = Label(text="E-mail/User name:")
name_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
# entry
website_entry = Entry(width= 38)
website_entry.grid(column=1, row=1, columnspan= 2)
website_entry.focus()
email_entry = Entry(width= 38)
email_entry.grid(column=1, row=2, columnspan= 2)
email_entry.insert(0, "duatkddbs25@naver.com")
password_entry = Entry(width= 21)
password_entry.grid(column=1, row=3)
# button
generate_password_button = Button(text="Generate Password", command= rand_password)
generate_password_button.grid(column=2, row= 3)
add_button = Button(text="Add", width= 36, command= add_is_clicked)
add_button.grid(column=1, row=4, columnspan=2)
# loop
window.mainloop()