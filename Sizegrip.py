from tkinter import *
from tkinter import ttk

#
# Callbacks:
#
# Change "bottom_right_corner" to "size_nw_se" and
# "arrow" to "left_ptr" if running on Windows.
#

def button_press(event):
    sizegrip["cursor"] = "bottom_right_corner"

def resize(event):
    deltax = event.x_root - root.winfo_rootx()
    deltay = event.y_root - root.winfo_rooty()
    if deltax < 1:
        deltax = 1
    if deltay < 1:
        deltay = 1
    root.geometry("%sx%s" % (deltax, deltay))

def button_release(event):
    sizegrip["cursor"] = "arrow"

# Widget Creation
root = Tk()                    
sizegrip = ttk.Label(root, style="Sizer.TLabel")

# Styling
style = ttk.Style()
style.layout("Sizer.TLabel", [("Sizegrip.sizegrip",
                               {"side": "bottom", "sticky": "se"})])

# Geometry Management
sizegrip.pack(side="bottom", anchor="se")

# Bindings
sizegrip.bind("<ButtonPress-1>", button_press)
sizegrip.bind("<B1-Motion>", resize)
sizegrip.bind("<ButtonRelease-1>", button_release)

root.mainloop()