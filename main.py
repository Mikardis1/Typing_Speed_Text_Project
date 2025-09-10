import tkinter as tk
from tkinter import messagebox
import time


class TypingSpeedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("800x500")

        self.sample_text = (
            "The quick brown fox jumps over the lazy dog. "
            "Typing fast and accurately requires practice. "
            "Keep going and you will improve your speed."
        )

        # Starts only when the user starts typing
        self.start_time = None

        # Ends when user finnishes (click Done)
        self.end_time = None

        # Title
        title = tk.Label(root, text="Typing Speed Test", font=("Arial", 20, "bold"))
        title.pack(pady=10)

        # Sample text display
        self.text_label = tk.Label(
            root,
            text=self.sample_text,

            # Making a paragraph when it reaches 750px of the line, if not it remains on the same line. It's good to use it because without it it would continue the sample text on the same line
            wraplength=750,

            justify="center",
            font=("Arial", 14),
            fg="blue",
        )
        self.text_label.pack(pady=20)

        # Entry box
        self.text_entry = tk.Text(root, height=8, width=90, font=("Arial", 12))
        self.text_entry.pack(pady=10)

        # To start time when the first word is pressed on the keyword
        self.text_entry.bind("<KeyPress>", self.start_timer)



        # Submit button - When submitted it needs to calculate the time
        self.submit_btn = tk.Button(root, text="Done", command=self.calculate_speed)
        self.submit_btn.pack(pady=10)

        # Result label
        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=20)

    def start_timer(self, event):
        if self.start_time is None:  # Start only on first key press
            self.start_time = time.time()

    def calculate_speed(self):
        if self.start_time is None:
            messagebox.showerror("Error", "You haven't typed anything yet!")
            return

        # Marking the new timer when clicked button DONE
        self.end_time = time.time()

        # Final time minus
        elapsed_time = self.end_time - self.start_time  # seconds
        elapsed_minutes = elapsed_time / 60

        # GET the texted typed since line 1 until the end, strip removes newlines and spaces
        typed_text = self.text_entry.get("1.0", tk.END).strip()


        # Creating an array by separating words
        typed_words = typed_text.split()


        # counting elements of the array typed_words
        word_count = len(typed_words)

        # WPM - Words per minute Calculation
        wpm = word_count / elapsed_minutes if elapsed_minutes > 0 else 0

        # Accuracy Calculation

        # Split the words of the sample_words
        sample_words = self.sample_text.split()

        # Sum +1 if typed word == sample_word: comparing in parallel each word typed with the correspondent word of the sample_words
        correct_words = sum(
            1 for tw, sw in zip(typed_words, sample_words) if tw == sw
        )
        accuracy = (correct_words / len(sample_words)) * 100

        # Cahnge the result after clicking the DONE button
        self.result_label.config(
            text=f"Time: {elapsed_time:.1f}s | Speed: {wpm:.1f} WPM | Accuracy: {accuracy:.1f}%"
        )


# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedApp(root)
    root.mainloop()
