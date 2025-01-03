import tkinter as tk

def greet():
    lbl_greeting.config(text=f"Hello, {entry_name.get()}!")

# Create the main window
root = tk.Tk()
root.title("Simple App")
root.geometry("300x200")

# Create a label
lbl_name = tk.Label(root, text="Enter your name:")
lbl_name.pack(pady=5)

# Create a text entry box
entry_name = tk.Entry(root)
entry_name.pack(pady=5)

# Create a button
btn_greet = tk.Button(root, text="Greet", command=greet)
btn_greet.pack(pady=5)

# Create a label for the greeting
lbl_greeting = tk.Label(root, text="")
lbl_greeting.pack(pady=10)

# Run the application
root.mainloop()
