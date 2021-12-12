from tkinter import *




def a (event):
    print(event.x)
    x = e.winfo_pointerx()
    y = e.winfo_pointery()
    abs_coord_x = e.winfo_pointerx() - e.winfo_rootx()
    abs_coord_y = e.winfo_pointery() - e.winfo_rooty()

    print(abs_coord_x)

root = Tk()
root.bind('<Motion>', a)

e = Toplevel(root)
e.title('44444')
e.bind('<Motion>', a)
root.mainloop()