import tkinter as tk
import random
import time

def start_typing():
    global start_time
    start_time = time.time()
    entry.delete(0, tk.END)
    entry.insert(tk.END, random.choice(sentences))
    entry.config(state=tk.NORMAL)
    entry.focus()

def finish_typing():
    elapsed_time = time.time() - start_time
    words_typed = len(entry.get().split())
    typing_speed = words_typed / (elapsed_time / 60)
    result_label.config(text=f"Your typing speed: {typing_speed:.2f} words per minute")

# List of sentences for the typing test
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "The only way to do great work is to love what you do.",
    "Be yourself; everyone else is already taken.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
]

# Create the main tkinter window
root = tk.Tk()
root.title("Speed Typing Test")

# Entry box for typing area
entry = tk.Entry(root, font=("Arial", 14), width=50, state=tk.DISABLED)
entry.grid(row=0, column=0, padx=10, pady=10)

# Start button
start_button = tk.Button(root, text="Start Typing", font=("Arial", 14), command=start_typing)
start_button.grid(row=1, column=0, padx=10, pady=5)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.grid(row=2, column=0, padx=10, pady=5)

# Set the time limit in seconds (e.g., 60 seconds)
time_limit = 60

def update_timer():
    remaining_time = max(0, time_limit - (time.time() - start_time))
    timer_label.config(text=f"Time remaining: {int(remaining_time)} seconds")
    if remaining_time <= 0:
        entry.config(state=tk.DISABLED)
        finish_typing()
    else:
        root.after(1000, update_timer)

timer_label = tk.Label(root, text="", font=("Arial", 14))
timer_label.grid(row=3, column=0, padx=10, pady=5)

root.after(1000, update_timer)
root.mainloop()
