from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.configure(bg="white")
root.attributes("-topmost", 1)
root.attributes("-transparentcolor", "#633763")
root.geometry("1000x300+200+300")

def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_img.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    h .itemconfig(photo, fill='black' )

frame = Frame(root, bg='#633763')
frame.pack()

label = Canvas(frame, height=900, width=900, bg="#633763", border=0)
label.pack()
label.bind('<Configure>', resize_image)

img = Image.open("aaa.png")
imgs = ImageTk.PhotoImage(img)
h = label.create_image(200,200, anchor=NW , image=imgs )

copy_img = img.copy()


root.mainloop()