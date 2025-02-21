import tkinter as tk
import random

class Bingo:
    def __init__(self, root):
        self.root = root
        self.root.title("Bingo Game")
        self.root.configure(bg="#f0f0f0")

        screen_width = 1920
        screen_height = 1080
        self.root.geometry(f"{screen_width}x{screen_height}")

        # Header Label
        self.header_label = tk.Label(root, text="Bingo Game", font=("Arial", 48, "bold"))
        self.header_label.place(relx=0.5, y=50, anchor="center")

        # Last 5 Drawn Numbers Display Area
        self.last_5_frame = tk.Frame(root, bg="#f0f0f0")
        self.last_5_frame.place(relx=0.5, rely=0.15, anchor="center")

        # Number Boxes
        self.number_boxes = [None] * 90
        self.create_number_boxes()

        # Draw Button
        self.draw_button = tk.Button(root, text="Draw", command=self.draw_number, font=("Arial", 24, "bold"), bg="#4CAF50", fg="white")
        self.draw_button.place(relx=0.5, rely=0.95, anchor="center")

        # Reset Button
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_game, font=("Arial", 24, "bold"), bg="#FF5722", fg="white")
        self.reset_button.place(relx=0.9, rely=0.95, anchor="e")

        self.start_new_game()

    def create_number_boxes(self):
        for i in range(1, 91):
            self.number_boxes[i-1] = tk.Label(self.root, text=str(i), font=("Arial", 20), padx=10, pady=8, borderwidth=2, relief="ridge")
            row = (i - 1) // 10
            col = (i - 1) % 10
            self.number_boxes[i-1].place(relx=0.05 + col * 0.1, rely=0.3 + row * 0.055, anchor="nw")

    def draw_number(self):
        if self.numbers:
            number = self.numbers.pop()
            self.drawn_numbers.append(number)
            self.update_last_5()
            self.update_number_box(number)
        else:
            self.header_label.config(text="All numbers have been drawn!")

    def update_last_5(self):
        for widget in self.last_5_frame.winfo_children():
            widget.destroy()

        last_5 = self.drawn_numbers[-5:]
        for i, number in enumerate(last_5[::-1], start=1):
            label = tk.Label(self.last_5_frame, text=f"{number}", font=("Arial", 24), padx=15, pady=10)
            if i == 1:
                label.config(bg="#4CAF50", fg="white")
            label.pack(side="left", padx=10)

    def update_number_box(self, number):
        self.number_boxes[number - 1].config(bg="#4CAF50", fg="white")

    def start_new_game(self):
        self.numbers = list(range(1, 91))  # List of bingo numbers
        random.shuffle(self.numbers)  # Shuffle the list

        self.drawn_numbers = []  # List to keep track of drawn numbers

        self.update_last_5()

        for label in self.number_boxes:
            label.config(bg="SystemButtonFace", fg="black")  # Configurar cores padrão

        self.header_label.config(text="Bingo Game")

    def reset_game(self):
        self.start_new_game()

def main():
    root = tk.Tk()
    bingo_game = Bingo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
