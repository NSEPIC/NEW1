import tkinter as tk
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
from PIL import Image, ImageTk
 
def get_svg(svg_file):
	drawing = svg2rlg(svg_file)
	renderPM.drawToFile(drawing, "temp.png", fmt="PNG")
 
 
 
class Root:
	def __init__(self):
		root = tk.Tk()
		img = Image.open('temp.png')
		pimg = ImageTk.PhotoImage(img)
		size = img.size
		frame = tk.Canvas(root, width=size[0], height=size[1])
		frame.pack()
		frame.create_image(0,0,anchor='nw',image=pimg)
		root.mainloop()
 
get_svg("logo_home")
root = Root()