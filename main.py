import tkinter as tk
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
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    window.after_cancel(timer)
    label1.config(text = "Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text = "00:00")
    label2.config(text = "")
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer ():
    global reps
    if reps in list(range (0,7,2)):
        work_sec = WORK_MIN * 60
        label1.config(text = "Focus", fg = GREEN) 

    elif reps in list(range(1,6,2)):
        work_sec = SHORT_BREAK_MIN * 60
        label1.config(text = "Breath" , fg = PINK) 

    elif reps == 7:
        work_sec = LONG_BREAK_MIN * 60
        label1.config(text = "Yepee!", fg = RED) 


    count_down(work_sec)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    global timer
    count_min = int(count / 60)
    count_sec = count % 60


    if count_sec == 0:
        count_sec = "00" #dynamic typing to change data type


    elif count_sec < 10:
        count_sec = f"0{count_sec}"


    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)

    else:
        reps += 1

        if reps == 1:
            label2.config(text = "✔")

        elif reps == 3:
            label2.config(text = "✔✔")

        elif reps == 5:
            label2.config(text = "✔✔✔")

        elif reps == 7:
            label2.config(text = "✔✔✔✔")


        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config (padx = 100, pady = 50, bg = YELLOW)



canvas = tk.Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
tomato_img = tk.PhotoImage(file = "tomato.png")
canvas.create_image(100,112, image = tomato_img)
timer_text = canvas.create_text(100, 130, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(column = 1, row = 1)

#count_down(5)

label1 = tk.Label (text = "Timer", font = ("Arial",  40, "bold"), fg = GREEN ,bg = YELLOW)
label1.grid(column = 1, row = 0)
label1.config (padx = 10, pady = 10)


label2 = tk.Label (text = "", font = ("Arial",  20, "bold"), fg = GREEN ,bg = YELLOW)
label2.grid(column = 1, row = 3)
label2.config (padx = 10, pady = 10)


button1 = tk.Button(text = "Start" , command = start_timer, bg = YELLOW,highlightbackground=YELLOW)
button1.grid(column = 0, row= 2)


button2 = tk.Button(text = "Reset" , command = reset_timer , bg = YELLOW ,highlightbackground=YELLOW)
button2.grid(column = 2, row= 2)


window.mainloop()