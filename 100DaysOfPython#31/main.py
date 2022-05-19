from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
SMALL_FONT = ("ariel", 40, "italic")
BIG_FONT =("Ariel", 60, "bold")
current_card = {}
should_learn = {}

try:
    read_origin = pandas.read_csv("/Users/yeomsangyoon/Visual Studio/Practice File/100DaysOfPython#31/data/word_should_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("/Users/yeomsangyoon/Visual Studio/Practice File/100DaysOfPython#31/data/french_words.csv")
    should_learn = original_data.to_dict(orient="records")
else:
    should_learn = read_origin.to_dict(orient="records")

# Function
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(all_data)
    canvas.itemconfig(card_lang, text= "French", fill= "black")
    canvas.itemconfig(card_word, text= current_card["French"], fill= "black")
    canvas.itemconfig(background, image= front_image)
    flip_timer = window.after(3000, func=flip_card)
def flip_card():
    canvas.itemconfig(card_lang, text= "English", fill= "white")
    canvas.itemconfig(card_word, text= current_card["English"], fill= "white")
    canvas.itemconfig(background, image= back_image)

def push_right_button():
    should_learn.remove(current_card)
    new_data = pandas.DataFrame(should_learn)
    new_data.to_csv("/Users/yeomsangyoon/Visual Studio/Practice File/100DaysOfPython#31/data/word_should_learn.csv", index=False)
    next_card()

# window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

word_data = pandas.read_csv("/Users/yeomsangyoon/Visual Studio/Practice File/100DaysOfPython#31/data/french_words.csv")
all_data = word_data.to_dict(orient="records")


canvas = Canvas(width=800 ,height=526)
front_image = PhotoImage(file="/Users/yeomsangyoon/Visual Studio/Practice File/100DaysOfPython#31/images/card_front.png")
back_image = PhotoImage(file="/Users/yeomsangyoon/Visual Studio/Practice File/100DaysOfPython#31/images/card_back.png")
background = canvas.create_image(400, 263, image= front_image)
card_lang = canvas.create_text(400, 150, text="Language", font=SMALL_FONT, fill= "black")
card_word = canvas.create_text(400, 263, text="Word", font=BIG_FONT, fill= "black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Button
right_button_image = PhotoImage(file="/Users/yeomsangyoon/Visual Studio/Practice File/100DaysOfPython#31/images/right.png")
wrong_button_image = PhotoImage(file="/Users/yeomsangyoon/Visual Studio/Practice File/100DaysOfPython#31/images/wrong.png")
right_button = Button(image=right_button_image, highlightthickness=0, command= push_right_button)
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command= next_card)
right_button.grid(column=1, row=1)
wrong_button.grid(column=0, row=1)


next_card()

window.mainloop()