from tkinter import *

class Example(Frame):
    def __init__(self, master, x=None, y=None, *args, **kwargs):
        super().__init__(master, *args, kwargs)


        self.lblframe = LabelFrame(self, text='Ajustes 0', bg='#2b313c', fg='green2', cursor='arrow')
        self.lblframe .pack(side='left', fill='both', expand=True, padx=(10,5), pady=(0,10))

        self.canvas = Canvas(self.lblframe, borderwidth=0,  bg='red', width=x, height=100, bd=0, highlightthickness=0)
        self.canvas .pack(side="left", fill='x', expand=True)

        self.scrolly = Scrollbar(self.lblframe, orient="vertical", command=self.canvas.yview)
        self.scrolly .pack(side="right", fill="y")


        self.frame = Frame(self.canvas, bg='#2b313c', width=x, height=100)
        self.frame .pack(fill='both', expand=True)

        self.canvas .config(yscrollcommand=self.scrolly.set)
        self.canvas .bind("<Configure>", self.canvas_resize)
        self.frame_id = self.canvas .create_window((0,0), window=self.frame, anchor="nw")

        #---loop----
        for i in range(8):
            label = Label(self.frame, text='number : %s' % i, font=('Calibri',9,'bold'), bg='#2b313c', fg='white', bd=0)
            label .grid(column=0, row=i, padx= (10,5), pady=(0,0), sticky='w')
      
    def canvas_resize(self, event):
        w = max(event.width, self.frame.winfo_width())
        h = max(event.height, self.frame.winfo_height())
        # resize the frame
        self.canvas.itemconfig(self.frame_id, width=w, height=h)
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

root = Tk()
root .geometry('300x150')
frame = Example(root, 200, 100).pack()
root.mainloop()