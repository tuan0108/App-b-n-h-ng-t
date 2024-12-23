import tkinter as tk

def toggle_fullscreen(event=None):
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))

def end_fullscreen(event=None):
    root.attributes("-fullscreen", False)

root = tk.Tk()
root.title("Full Screen Example")

# Bind the F11 key to toggle fullscreen mode
root.bind("<F11>", toggle_fullscreen)
# Bind the Escape key to exit fullscreen mode
root.bind("<Escape>", end_fullscreen)

# Start in fullscreen mode
root.attributes("-fullscreen", True)

label = tk.Label(root, text="Press F11 to toggle full screen, Esc to exit full screen", font=("Helvetica", 16))
label.pack(expand=True)

root.mainloop()
