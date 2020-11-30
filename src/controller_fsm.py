from settings import *
from csv_reader import *
from printer import *


# ------------------------------------------------
# Game Controller FSM
# Control operates a Q&A game with on text label and three answer buttons
# ------------------------------------------------
class ControllerFSM:
    def __init__(self, text_label_c, button_a_c, button_b_c, button_c_c):
        self.text_label = text_label_c
        self.button_a = button_a_c
        self.button_b = button_b_c
        self.button_c = button_c_c
        self.button_a.config(command=self.button_a_callback)
        self.button_b.config(command=self.button_b_callback)
        self.button_c.config(command=self.button_c_callback)
        self.printer = Printer(character_delay_ms)
        self.text_line = csv_read(file_path)
        # Game controlling attributes
        self.game_progress_line = 0
        self.game_progress_line_max = len(self.text_line)
        self.question_answered = True

    # Button pressing event evaluation
    def button_a_callback(self):
        if self.printer.printer_ready():
            if self.text_line[self.game_progress_line][1] == self.text_line[self.game_progress_line][4]:
                self.game_progress_line += 1
                if self.game_progress_line >= self.game_progress_line_max - 1:
                    self.game_progress_line = 0
            else:
                self.game_progress_line = self.game_progress_line_max - 1
            self.question_answered = True

    def button_b_callback(self):
        if self.printer.printer_ready():
            if self.text_line[self.game_progress_line][2] == self.text_line[self.game_progress_line][4]:
                self.game_progress_line += 1
                if self.game_progress_line >= self.game_progress_line_max - 1:
                    self.game_progress_line = 0
            else:
                self.game_progress_line = self.game_progress_line_max - 1
            self.question_answered = True

    def button_c_callback(self):
        if self.printer.printer_ready():
            if self.text_line[self.game_progress_line][3] == self.text_line[self.game_progress_line][4]:
                self.game_progress_line += 1
                if self.game_progress_line >= self.game_progress_line_max - 1:
                    self.game_progress_line = 0
            else:
                self.game_progress_line = self.game_progress_line_max - 1
            self.question_answered = True

    # Questioning
    def ask_question(self):
        self.question_answered = False
        if self.text_line[self.game_progress_line][1]:
            self.button_a.config(text=self.text_line[self.game_progress_line][1], state="normal")
        else:
            self.button_a.config(text="", state="disabled")

        if self.text_line[self.game_progress_line][2]:
            self.button_b.config(text=self.text_line[self.game_progress_line][2], state="normal")
        else:
            self.button_b.config(text="", state="disabled")

        if self.text_line[self.game_progress_line][3]:
            self.button_c.config(text=self.text_line[self.game_progress_line][3], state="normal")
        else:
            self.button_c.config(text="", state="disabled")

        self.printer.print(self.text_line[self.game_progress_line][0], self.text_label)

    # Idling (Wait for question to be printed and user to answer it)
    def idle_task(self):
        if self.printer.printer_ready():
            if self.question_answered:
                self.ask_question()
        self.text_label.after(500, self.idle_task)
