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

# ---------------------------- VARIABLES ------------------------------- #
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_button():
    global reps
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_button():
    global reps
    reps += 1

    if reps % 8 == 0:
        # Every 8th rep: long break
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        # Every 2nd rep: short break
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text="Short Break", fg=PINK)
    else:
        # Otherwise: work session
        count_down(WORK_MIN * 60)
        title_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = count // 60
    seconds = count % 60
    time_formatted = f"{minutes:02d}:{seconds:02d}"
    canvas.itemconfig(timer_text, text=time_formatted)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_button()  # start the next session automatically

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("POMODORO TIMER:")
window.config(padx=50, pady=25, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50, "bold"), bg=YELLOW)
title_label.pack()

canvas = Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.pack()

button_frame = Frame(window, bg=YELLOW)
button_frame.pack(pady=20)

start_btn = Button(button_frame, text="START", command=start_button, font=(FONT_NAME, 12, "bold"), bg=GREEN, fg="white")
start_btn.pack(side=LEFT, padx=20)

reset_btn = Button(button_frame, text="RESET", command=reset_button, font=(FONT_NAME, 12, "bold"), bg=RED, fg="white")
reset_btn.pack(side=RIGHT, padx=20)

window.mainloop()
