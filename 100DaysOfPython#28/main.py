from tkinter import *
from time import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 1
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    timer_label.config(text= "Timer", fg= GREEN)
    check_mark.config(text= "")
    reps = 1
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 == 1:
        timer_label.config(text= "Work")
        reps += 1
        count_down(work_sec)
    elif reps % 2 == 0:
        timer_label.config(text= "Break", fg= PINK)
        reps += 1
        count_down(short_break_sec)
    elif reps == 8:
        timer_label.config(text= "Work", fg= RED)
        count_down(long_break_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    k = 2
    k += 1
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if int(count_min) < 10:
        count_min = f"0{count_min}"
    if int(count_sec) < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
            check_mark.config(text= marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg= YELLOW)

canvas = Canvas(width=200, height= 224, bg= YELLOW, highlightthickness= 0)
tomato_img = PhotoImage(file= "/Users/yeomsangyoon/Visual Studio/Practice File/100DaysOfPython#28/tomato.png")
# Label
timer_label = Label(text= "Timer", bg= YELLOW, fg= GREEN, font=(FONT_NAME, 50, "bold"), highlightthickness=0)
timer_label.grid(column=2, row=1)
# Canvas (tomatoimg, time text)
canvas.create_image(100 ,112, image = tomato_img)
timer_text = canvas.create_text(100, 135, text= "00:00", fill= "white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)
# Button
start_button = Button(text="Start", highlightthickness=0, command= start_timer)
start_button.grid(column= 1, row= 3)
reset_button = Button(text="Reset", highlightthickness=0, command= reset_timer)
reset_button.grid(column= 3, row= 3)
# count
check_mark = Label(bg= YELLOW, fg= GREEN, font=(FONT_NAME, 35, "bold"), highlightthickness=0)
check_mark.grid(column=2, row=4)

window.mainloop()