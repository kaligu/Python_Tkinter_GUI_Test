import tkinter as tk
from tkinter import font

# execute when the "Start" button is clicked
def btnStart_clicked():
    add_text_txtArea("Start button clicked")

# execute when the "Stop" button is clicked
def btnStop_clicked():
    add_text_txtArea("Stop button clicked")



# -----------------------------------------------------------------------
#                                  GUI  
# -----------------------------------------------------------------------
# Create Tkinter object
window = tk.Tk()
window.title("Vehicle Parking System Control Panel")
window.geometry("600x600")

# ------------ Add label widget
lblGreet = tk.Label(window, text="Have a Nice day...", font=10)
# place widget
lblGreet.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# ------------ add start button widget
btnStart = tk.Button(
    window,
    text="Start",
    width=20,
    height=3,
    bg="#00b02f",
    fg="white",
    command=btnStart_clicked
)
btnStart.grid(row=1, column=0, padx=10, pady=10)

# ------------ add stop button widget
btnStop = tk.Button(
    window,
    text="Stop",
    width=20,
    height=3,
    bg="red",
    fg="white",
    command=btnStop_clicked
)
btnStop.grid(row=1, column=1, padx=10, pady=10)

# execute when the mouse wheel is scrolled
def on_mousewheel(event):
    txtArea.yview_scroll(int(-1*(event.delta/120)), "units")

# --------------- add text area widget
txtArea = tk.Text(window, width=50, height=10, font=("Arial", 12), wrap=tk.WORD, bg="black", fg="white")
txtArea.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Configure tag for italic and gray font color
txtArea.tag_configure("italic_gray", font=("Arial", 12, "italic"), foreground="gray")

# Add scrollbar
scrollbar = tk.Scrollbar(window, command=txtArea.yview, bg='gray', troughcolor='dark gray')
scrollbar.grid(row=2, column=2, sticky='nsew')
txtArea['yscrollcommand'] = scrollbar.set

# Bind mouse wheel scroll event to text area
txtArea.bind("<MouseWheel>", on_mousewheel)

# Text area text add method
def add_text_txtArea(text):
    txtArea.insert(tk.END, text + "\n\n", "italic_gray")
    txtArea.see(tk.END)  # Scrolls the text area to the end

# Configure row and column weights
window.grid_rowconfigure(2, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

add_text_txtArea("done")
add_text_txtArea("done")

# Run Tkinter object
window.mainloop()
