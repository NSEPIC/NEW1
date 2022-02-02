 
from tkinter import *
from tkinter import ttk
 
 
 
class Picture:
    def __init__(self, parent):
        self.parent = parent
        img = PhotoImage(file='ma.png')
        self.label = Label(self.parent,)
        self.label.config(image=img)
        #self.label['image'] = img          # original
        self.label.image = img
        #img.image = img         # original
        self.label.pack(pady=5)
 
        btn  = Button(self.parent, command=self.iniciar_test, text='Test').pack(side='bottom', pady=10)

        btsn = Button(self.parent, command=self.reiniciar_conteo, text='Reiniciar').pack(side='bottom', pady=5)
 
        self.lab = Label(self.parent)
        self.lab['text'] = None
        self.lab.pack(expand=True, fill='x')
 
 
    def reiniciar_conteo(self):
        self.lab.after_cancel(self.myvar)
        self.conteo = 8
        self.timer()
 
    def iniciar_test(self):
        img = PhotoImage(file='ma2.png')
        self.label['image'] = img
        self.label.image = img
        #img.image = img
        self.conteo = 8
        self.timer()
 
    def display(self):
        img = PhotoImage(file='mi.png')
        self.label['image'] = img
        img.image = img
        self.lab['text'] = None
 
 
 
 
    def run_timer(self):
        if self.conteo >= 0:
            self.conteo -= 1
 
    def timer(self):
        self.run_timer()
        if self.conteo >= 0:
            self.myvar = self.lab.after(1000, self.timer)
            self.lab['text'] = f'Resetting in {self.conteo}'
            self.lab['bg'] = 'burlywood'
            self.lab['fg'] = 'brown'
            self.lab['font'] = 'serif 10 normal'
        else:
            self.myvar = None
            self.lab['text'] = ''
            self.lab['bg'] = 'grey86'
            self.display()
 
 
 
def main():
    root = Tk()
 
    Picture(root)
    root.mainloop()
 
main()