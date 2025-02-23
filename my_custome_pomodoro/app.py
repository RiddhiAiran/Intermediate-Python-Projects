import tkinter as tk
from tkinter import ttk
import time

# Global variables for timer and mode
current_mode = "Pomodoro"
timer_running = False
time_remaining = 25 * 60  # 25 minutes in seconds

# Timer update function
def update_timer():
    global time_remaining, timer_running
    if timer_running and time_remaining > 0:
        mins, secs = divmod(time_remaining, 60)
        timer_label.config(text=f"{mins:02}:{secs:02}")
        time_remaining -= 1
        root.after(1000, update_timer)
    elif time_remaining == 0:
        timer_running = False
        timer_label.config(text="00:00")
        mode_label.config(text="Time's up!")

def start_timer():
    global timer_running
    if not timer_running:
        timer_running = True
        update_timer()

def reset_timer(duration, mode):
    global time_remaining, current_mode, timer_running
    timer_running = False
    current_mode = mode
    time_remaining = duration * 60
    mins, secs = divmod(time_remaining, 60)
    timer_label.config(text=f"{mins:02}:{secs:02}")
    mode_label.config(text=f"{mode} Time")
    # update_buttons()

def switch_mode(mode):
    if mode == "Pomodoro":
        reset_timer(25, mode)
    elif mode == "Short Break":
        reset_timer(5, mode)
    elif mode == "Long Break":
        reset_timer(15, mode)

# def update_buttons():
#     pomodoro_btn.config(bg="#E16A54" if current_mode == "Pomodoro" else "#9F5255", fg="white")
#     short_break_btn.config(bg="#E16A54" if current_mode == "Short Break" else "#9F5255", fg="white")
#     long_break_btn.config(bg="#E16A54" if current_mode == "Long Break" else "#9F5255", fg="white")

# Create Main Window
root = tk.Tk()
root.title("Focus Timer")
root.geometry("400x500")
root.configure(bg="#7C444F")

# Title Bar
title_bar = tk.Frame(root, bg="#9F5255", height=50, width=400)
title_bar.place(x=0, y=0)
title_label = tk.Label(title_bar, text="Focus Timer", bg="#9F5255", fg="#ffffff", font=("Arial", 20, "bold"))
title_label.pack(expand=True)

# Timer Display Panel
timer_panel = tk.Frame(root, bg="#F39E60", width=300, height=160, highlightbackground="#9F5255", highlightthickness=1)
timer_panel.place(x=50, y=80)
timer_label = tk.Label(timer_panel, text="25:00", bg="#F39E60", fg="#7C444F", font=("Arial", 50, "bold"))
timer_label.place(relx=0.5, rely=0.4, anchor="center")
mode_label = tk.Label(timer_panel, text="Focus Time", bg="#F39E60", fg="#7C444F", font=("Arial", 16))
mode_label.place(relx=0.5, rely=0.8, anchor="center")

# Mode Selection Buttons - Using flat modern style
button_style = {
    'font': ("Helvetica", 12,'bold'),
    'relief': 'flat',
    'width': 12,
    'height': 2,
    'bg': '#E4C087',  # Slightly darker blue
    'fg': '#E4C087',  # Light grey text
    'activebackground': '#3498DB',  # Bright blue when clicked
    'activeforeground': '#ECF0F1',
    "highlightbackground":"#E4C087", 
    "highlightthickness":1
}


# Mode Selection Buttons
pomodoro_btn = tk.Button(root, text="Pomodoro", **button_style,
                         command=lambda: switch_mode("Pomodoro"))
pomodoro_btn.place(x=50, y=280)

short_break_btn = tk.Button(root, text="Short Break", **button_style,
                            command=lambda: switch_mode("Short Break"))
short_break_btn.place(x=150, y=280)

long_break_btn = tk.Button(root, text="Long Break", **button_style,
                           command=lambda: switch_mode("Long Break"))
long_break_btn.place(x=250, y=280)

# Control Buttons
start_button = tk.Button(root, text="START", bg="#E4C087", fg="#E4C087", font=("Arial", 16, "bold"), width=14, height=2,
                         relief="flat", command=start_timer, highlightbackground="#E4C087", highlightthickness=1)
start_button.place(x=120, y=360)

# Progress Section
progress_bar_bg = tk.Frame(root, bg="#9F5255", width=300, height=10)
progress_bar_bg.place(x=50, y=440)
progress_bar_fg = tk.Frame(root, bg="#E16A54", width=120, height=10)
progress_bar_fg.place(x=50, y=440)

# Session Counter
session_label = tk.Label(root, text="Session: 1/4", bg="#7C444F", fg="#F39E60", font=("Arial", 14))
session_label.place(x=50, y=470)

root.mainloop()