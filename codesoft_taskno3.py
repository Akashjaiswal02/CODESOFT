import tkinter as tk
from tkinter import messagebox
import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to handle the generate button click
def on_generate():
    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError("Length must be positive")
        password = generate_password(length)
        result_label.config(text=password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the password length")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and place the widgets
tk.Label(root, text="Enter the desired length of the password:").pack(pady=10)

entry_length = tk.Entry(root)
entry_length.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=on_generate)
generate_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the application
root.mainloop()