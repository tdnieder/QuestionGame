import tkinter as tk
from controller_fsm import *


# ------------------------------------------------
# Global Variables
# ------------------------------------------------
# GUI Variables
root = tk.Tk()
text_label = tk.Label(root)
button_frame = tk.Frame(root)
button_a = tk.Button(button_frame)
button_b = tk.Button(button_frame)
button_c = tk.Button(button_frame)


# ------------------------------------------------
# GUI
# ------------------------------------------------
def init_gui():
    global root
    global text_label
    global button_frame
    global button_a
    global button_b
    global button_c
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    # Frame
    root.title("Question Game")
    root.overrideredirect(True)
    root.geometry("{0}x{1}+0+0".format(screenwidth, screenheight))
    root.config(bg="black", cursor="none")
    root.focus_set()
    root.bind("<Escape>", lambda e: root.destroy())
    # Label
    text_label.config(anchor="nw", justify="left", fg="green", bg="black", font=("consolas", 13), padx=15, pady=10,
                      wraplength=(screenwidth - 30))
    text_label.pack()
    text_label.place(width=(screenwidth - 20), height=(screenheight - 100))
    # Buttons
    button_frame.config(bg="black")
    button_frame.pack(side="bottom")
    button_a.config(state="disabled", bg="black", fg="green", bd=0, font=("consolas", 13),
                    activebackground="black", activeforeground="green", highlightthickness=0, width=12, pady=20)
    button_b.config(state="disabled", bg="black", fg="green", bd=0, font=("consolas", 13),
                    activebackground="black", activeforeground="green", highlightthickness=0, width=12, pady=20)
    button_c.config(state="disabled", bg="black", fg="green", bd=0, font=("consolas", 13),
                    activebackground="black", activeforeground="green", highlightthickness=0, width=12, pady=20)
    button_a.grid(column=0, row=0)
    button_b.grid(column=1, row=0)
    button_c.grid(column=2, row=0)


# ------------------------------------------------
# Main Startup
# ------------------------------------------------
init_gui()
controller = ControllerFSM(text_label, button_a, button_b, button_c)
controller.idle_task()
root.mainloop()
