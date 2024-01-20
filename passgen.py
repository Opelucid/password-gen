import tkinter as tk
from tkinter import ttk
import secrets
import string
import math

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("350x400")
        self.center_window()

        self.length_var = tk.IntVar(value=12)
        self.upper_var = tk.BooleanVar(value=True)
        self.lower_var = tk.BooleanVar(value=True)
        self.digit_var = tk.BooleanVar(value=True)
        self.special_var = tk.BooleanVar(value=True)

        self.create_widgets()
        self.tooltip = None

    def center_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width - 350) // 2
        y = (screen_height - 400) // 2

        self.root.geometry(f"350x400+{x}+{y}")

    def create_widgets(self):
        # Container Frame
        container = ttk.Frame(self.root, padding=(20, 10))
        container.grid(row=0, column=0, sticky="nsew")

        # Title Label
        title_label = ttk.Label(container, text="Secure Password Generator", font=("Helvetica", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Length Label and Entry
        length_label = ttk.Label(container, text="Password Length:")
        length_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        length_entry = ttk.Entry(container, textvariable=self.length_var, width=5)
        length_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        # Character options Checkbuttons
        upper_check = ttk.Checkbutton(container, text="Uppercase", variable=self.upper_var)
        upper_check.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        lower_check = ttk.Checkbutton(container, text="Lowercase", variable=self.lower_var)
        lower_check.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        digit_check = ttk.Checkbutton(container, text="Digits", variable=self.digit_var)
        digit_check.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        special_check = ttk.Checkbutton(container, text="Special Characters", variable=self.special_var)
        special_check.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        # Generate Button with Tooltip
        generate_button = ttk.Button(container, text="Generate Password", command=self.generate_password)
        generate_button.grid(row=4, column=0, columnspan=2, pady=10)
        self.add_tooltip(generate_button, "Click to generate a secure password")

         # Password Entry Field
        password_entry = ttk.Entry(container, show="*", state="readonly", font=("Courier", 14))  # Increased font size
        password_entry.grid(row=5, column=0, columnspan=2, pady=10, padx=5, sticky="we", ipady=10)  # Increased ipady for height
        self.password_var = tk.StringVar()
        password_entry["textvariable"] = self.password_var

        # Display Label for Entropy
        self.entropy_var = tk.StringVar()
        entropy_label = ttk.Label(container, textvariable=self.entropy_var, foreground="gray")
        entropy_label.grid(row=6, column=0, columnspan=2, pady=5)

        # Copy Password Button
        copy_button = ttk.Button(container, text="Copy Password", command=self.copy_password)
        copy_button.grid(row=7, column=0, columnspan=2, pady=10)

    def copy_password(self):
        # Function to copy the generated password to the clipboard
        self.root.clipboard_clear()
        self.root.clipboard_append(self.password_var.get())
        self.root.update()
        
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
            self.entropy_var.set("")
            return

        num_combinations = len(selected_chars) ** self.length_var.get()
        entropy_bits = math.log2(num_combinations)
        self.entropy_var.set(f"Entropy: {entropy_bits:.2f} bits")

        password = ''.join(secrets.choice(selected_chars) for _ in range(self.length_var.get()))
        self.password_var.set(password)

    def add_tooltip(self, widget, text):
        # Function to add tooltips to widgets
        widget.bind("<Enter>", lambda event: self.show_tooltip(text))
        widget.bind("<Leave>", lambda event: self.hide_tooltip())

    def show_tooltip(self, text):
        # Function to show tooltip
        if not self.tooltip:
            geometry_str = self.root.geometry()
            geometry_values = geometry_str.split("+")
            
            if len(geometry_values) >= 2:
                x = int(geometry_values[1]) + 10
                y = int(geometry_values[2]) + 10
                self.tooltip = tk.Toplevel(self.root, bd=1, relief=tk.SOLID)
                self.tooltip.wm_overrideredirect(True)
                self.tooltip.wm_geometry(f"+{x}+{y}")
                label = tk.Label(self.tooltip, text=text, justify='left',
                                 background="#ffffe0", relief='solid', borderwidth=1,
                                 font=("Helvetica", "8", "normal"))
                label.pack()

    def hide_tooltip(self):
        # Function to hide tooltip
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None  # Reset tooltip to None after destroying

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
