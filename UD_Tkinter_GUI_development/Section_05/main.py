import tkinter as tk
from tkinter import ttk
import tkinter.font as font

root = tk.Tk()
root.title("Distance converter")

font.nametofont("TkDefaultFont").configure(size=15)

meters_value = tk.StringVar()
feet_value = tk.StringVar()


def calculate_feet(*args):
    try:
        meters = float(meters_value.get())
        feet = meters * 3.28084
        feet_value.set(f"{feet:.3f}")
    except ValueError:
        pass

root.columnconfigure(0, weight=1)

main = ttk.Frame(root, padding=(30, 15))
main.grid(row=0, column=0)

meters_label = ttk.Label(main, text="Metres:")
meters_input = ttk.Entry(main, width=10, textvariable=meters_value, font=("Segou UI", 15))
feet_label = ttk.Label(main, text="Feet:")
feet_display = ttk.Label(main, text="Feet shown here", textvariable=feet_value)
calc_button = ttk.Button(main, text="Calculate", command=calculate_feet)

meters_label.grid(row=0, column=0, sticky='W')
meters_input.grid(row=0, column=1, sticky='EW')
meters_input.focus()

feet_label.grid(row=1, column=0, sticky='W')
feet_display.grid(row=1, column=1, sticky='EW')
calc_button.grid(row=2, column=0, columnspan=2, sticky="EW")

for child in main.winfo_children():
    child.grid_configure(padx=15, pady=15)

root.bind("<Return>", calculate_feet)
root.bind("<KP_Enter>", calculate_feet)


root.mainloop()