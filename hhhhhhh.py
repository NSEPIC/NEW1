from tkinter import Tk, Frame, Canvas , PhotoImage
from PIL import ImageTk, Image

t = Tk() 
t.title("Transparency") 

frame = Frame(t) 
frame.pack() 

canvas = Canvas(frame, bg='black', width=500, height=500) 
canvas.pack() 


photoimage = PhotoImage(file="11.png") 
canvas.create_image(150, 150, image=photoimage) 

t.mainloop() 


""" #____Detectanda el tipo de ventana:
    self.window = event.widget.master.winfo_toplevel()
    print('detect', self.window.master) """
