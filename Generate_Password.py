import tkinter as tk
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate():
    length = int(length_entry.get())
    password = generate_password(length)
    result_label.config(text="Generated Password: " + password)

# Create the main window
window = tk.Tk()
window.title("Password Generator")
# Set the width and height of the window
window.geometry("400x200")  

# Create the length input field
length_label = tk.Label(window, text="Enter password length:")
length_label.pack()
length_entry = tk.Entry(window)
length_entry.pack()

# Create the Generate button
generate_button = tk.Button(window, text="Generate", command=generate)
generate_button.pack()

# Create the result label
result_label = tk.Label(window, text="")
result_label.pack()

# Run the application
window.mainloop()
