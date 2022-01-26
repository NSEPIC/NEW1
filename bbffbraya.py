import tkinter as tk

def _button_press(event):
    label.configure(text="")

def _button_release(event):
    widget_under_cursor = event.widget.winfo_containing(event.x_root, event.y_root)
    print(widget_under_cursor)
    if widget_under_cursor == event.widget:
        label.configure(text="you released over the button")
    else:
        label.configure(text="you did not release over the button")


root = tk.Tk()
label = tk.Label(root, width=40)
label.pack(side="top", fill="x")
for i in range(10):
    button = tk.Button(root, text=f"Button #{i+1}")
    button.pack()
    button.bind("<ButtonPress-1>", _button_press)
    button.bind("<ButtonRelease-1>", _button_release)

root.mainloop()