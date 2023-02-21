import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
window = Tk()
# ---------------------------- TIMER RESET ------------------------------- # 


def stop_timer():
    global reps
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(time, text="00:00")
    check.config(text="")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    work = 3
    break_time = 2
    long_break = 4
    if reps == 8:
        timer_label.config(text="Break", fg=PINK)
        countdown(long_break)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=RED)
        countdown(break_time)
    else:
        timer_label.config(text="Work", fg=GREEN)
        countdown(work)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    minute = math.floor(count/60)
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"
    canvas.itemconfig(time, text=f"{minute}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        marks = ""
        session = math.floor(reps/2)
        for i in range(session):
            marks += '✔'
            print(i)
        check.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #


window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Timer Label
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, 'bold'))
timer_label.grid(row=0, column=1)


# Inserting Image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
time = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, 'bold'))
canvas.grid(row=1, column=1)

# Start Button
start = Button(text="Start", bg="white", font=(FONT_NAME, 10), command=start_timer)
start.grid(row=2, column=0)

# Reset Button
reset = Button(text="Reset", bg="white", font=(FONT_NAME, 10), command=stop_timer)
reset.grid(row=2, column=2)

# Check Label
check = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15))
check.grid(row=3, column=1)


window.mainloop()
