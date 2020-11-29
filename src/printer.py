# ------------------------------------------------
# Printer enables printing an array character by character with a given delay
# ------------------------------------------------
class Printer:
    def __init__(self, character_print_delay):
        self.character_delay = character_print_delay
        self.is_ready = True

    # ------------------------------------------------
    # Prints array character by character
    # ------------------------------------------------
    def print(self, text, text_label):
        i = 0
        s = text[i]
        self.is_ready = False

        # Creating inner (protected) function which prints character after character
        def printing():
            nonlocal i
            nonlocal s

            text_label.config(text=s)
            i += 1
            # Print characters till all characters of a line/row is added to the displayed text.
            if i < len(text):
                s = s + text[i]
                text_label.after(self.character_delay, printing)
            else:
                self.is_ready = True

        printing()

    def printer_ready(self):
        return self.is_ready
