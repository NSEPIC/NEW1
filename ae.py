from cgitb import text
from tkinter import *

def cambiarr():
    print('ejecutando....')
    dra3.lower()

tk = Tk()
tk.geometry('150x150')

dra0 = Frame(tk, bg='black')
dra0 .pack(fill='both', expand=True)

b = Button(dra0, text='cambiar', command=cambiarr)
b.pack()

dra1 = Frame(tk, bg='green')
dra1 .pack(fill='both', expand=True)


dra2 = Frame(dra1, bg='red')
dra2 .pack(fill='both', expand=True, side='top', anchor=N)

dra3 = Frame(dra1, bg='blue')
dra3 .pack(fill='both', expand=True, side='top', anchor=N)



dra2 .lower()


tk.mainloop()
