from tkinter import *
from tkinter import ttk
 
 
# Main tkinter window
x = Tk()
x.geometry("400x300")
 
 
# Label Widget
b = Label(x, bg="#f5f5f5", bd=4, relief=RAISED, text="With Separator")
b.place(relx=0.1, rely=0.05, relheight=0.4, relwidth=0.8)
 
 
# Separator object
separator = ttk.Separator(x, orient='horizontal', bg='green')
separator.place(relx=0, rely=0.47, relwidth=1, relheight=1)
 
 
# Label Widget
a = Label(x, bg="#f5f5f5", bd=4, relief=RAISED, text="With Separator")
a.place(relx=0.1, rely=0.5, relheight=0.4, relwidth=0.8)
 
 
mainloop()