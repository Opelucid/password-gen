import tkinter as tk
from tkinter import ttk
import secrets
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.length_var = tk.IntVar(value=12)
        self.upper_var = tk.BooleanVar(value=True)
        self.lower_var = tk.BooleanVar(value=True)
        self.digit_var = tk.BooleanVar(value=True)
        self.special_var = tk.BooleanVar(value=True)

        self.create_widgets()

    def create_widgets(self):
        # Length Label and Entry
        length_label = ttk.Label(self.root, text="Password Length:")
        length_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        length_entry = ttk.Entry(self.root, textvariable=self.length_var)
        length_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        # Character options Checkbuttons
        upper_check = ttk.Checkbutton(self.root, text="Uppercase", variable=self.upper_var)
        upper_check.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        lower_check = ttk.Checkbutton(self.root, text="Lowercase", variable=self.lower_var)
        lower_check.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        digit_check = ttk.Checkbutton(self.root, text="Digits", variable=self.digit_var)
        digit_check.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        special_check = ttk.Checkbutton(self.root, text="Special Characters", variable=self.special_var)
        special_check.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Generate Button
        generate_button = ttk.Button(self.root, text="Generate Password", command=self.generate_password)
        generate_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Display Label
        self.password_var = tk.StringVar()
        password_label = ttk.Label(self.root, textvariable=self.password_var)
        password_label.grid(row=4, column=0, columnspan=2, pady=5)

    def generate_password(self):
        selected_chars = ""
        if self.upper_var.get():
            selected_chars += string.ascii_uppercase
        if self.lower_var.get():
            selected_chars += string.ascii_lowercase
        if self.digit_var.get():
            selected_chars += string.digits
        if self.special_var.get():
            selected_chars += string.punctuation

        if not selected_chars:
            self.password_var.set("Please select at least one character type.")
            return

        password = ''.join(secrets.choice(selected_chars) for _ in range(self.length_var.get()))
        self.password_var.set(password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
