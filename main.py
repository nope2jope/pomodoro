from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK = "✔"
TITLE = "p o m o t i m e r"
reps = 0
check_array = []
timer = None
is_running = False

# ---------------------------- TIMER RESET ------------------------------- #

def timer_reset():

    global is_running
    global reps
    reps = 0
    is_running = False
    window.after_cancel(timer)
    canvas.itemconfig(timer_count, text="00:00")
    timer_label.config(text=TITLE, fg=GREEN)
    check_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def timer_start():
    global reps
    global is_running
    if is_running:
        pass
    else:
        is_running = True
        reps += 1
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60

        if reps % 8 == 0:
            count_down(long_break_sec)
            timer_label.config(text="b r e a k t i m e", fg=RED)
        elif reps % 2 == 0:
            count_down(short_break_sec)
            timer_label.config(text="b r e a k t i m e", fg=PINK)
        else:
            count_down(work_sec)
            timer_label.config(text="g r i n d", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    check_count = 0

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_count, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        timer_start()
        check_count += .5
        work_sessions = math.floor(reps/2)
        checks = ""
        for check in range(work_sessions):
            checks += CHECK
        check_label.config(text=checks)




# ---------------------------- UI SETUP ------------------------------- #

# window

window = Tk()
window.title("p o m o d o r o")
window.config(padx=100, pady=50, bg=YELLOW)




# timer label

timer_label = Label(text=TITLE, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 22))
timer_label.grid(row=0, column=1)

# canvas, image

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_count = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# timer initialize

start_button = Button(text="START", command=timer_start)
start_button.grid(row=2, column=0)

reset_button = Button(text="RESET", command=timer_reset)
reset_button.grid(row=2, column=3)

# progress hashes

check_label = Label(text=check_array, bg=YELLOW, fg=GREEN)
check_label.grid(row=3, column=1)


window.mainloop()