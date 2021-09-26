from tkinter import *



class BarraTitulo(Frame):
    def __init__(self, master=None, title=None, **kwargs):
        Frame.__init__(self, master, **kwargs)
        self.master = master
        self.title = title if title else StringVar('')

        self.btn_close = Button(self, text="X", command=self.close)
        self.btn_close .pack(side=RIGHT, padx=10, pady=10)

        self.btn_minimize = Button(self, text="_", command=self.minimize)
        self.btn_minimize .pack(side=RIGHT, pady=10)

        self.title_lb = Label(self, textvariable=self.title, fg="white", bg="black")
        self.title_lb .pack(side=BOTTOM, padx=10, pady=10)

    def close(self):
        self.master.destroy()
        self.master.master.destroy()

    def minimize(self):
        pass
        self.master.withdraw()
        self.master.master.iconify()


class VentanaSinBordes(Toplevel):
    def __init__(self, master=None, **kwargs):
        Toplevel.__init__(self, master, **kwargs)
        self.overrideredirect(True)
        self.master = master
        self._x = 0
        self._y = 0

        self.borde = BarraTitulo(self, title=self.master._title, background="black")
        self.contenido = Frame(self)
        self.borde.pack(side=TOP, fill=BOTH)
        self.contenido.pack(side=TOP, fill=BOTH)
        self.borde.bind("<ButtonPress-1>", self.start_move)
        self.borde.bind("<ButtonRelease-1>", self.stop_move)
        self.borde.bind("<B1-Motion>", self.on_move)
        self.borde.title_lb.bind("<ButtonPress-1>", self.start_move)
        self.borde.title_lb.bind("<ButtonRelease-1>", self.stop_move)
        self.borde.title_lb.bind("<B1-Motion>", self.on_move)

    def start_move(self, event):
        self._x = event.x
        self._y = event.y

    def stop_move(self, event):
        self._x = None
        self._y = None

    def on_move(self, event):
        deltax = event.x - self._x
        deltay = event.y - self._y
        new_pos = "+{}+{}".format(self.winfo_x() + deltax, self.winfo_y() + deltay)

        self.geometry(new_pos)
        self.master.geometry(new_pos)


class WindRoot(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.resizable(0, 0)
        self.geometry('0x0')
        self._title = StringVar(self.title())
        self.window = VentanaSinBordes(self)
        self.window.geometry('400x200')
        self.bind("<Map>", self.on_deiconify)
        self.bind("<Unmap>", self.on_iconify)


    def title(self, *args):
        if args:
            print(args)
            self._title.set(args[0])
        Tk.title(self, args)

    def on_iconify(self, event):
        self.window.withdraw()

    def on_deiconify(self, event):
        self.window.deiconify()


if __name__ == '__main__':
    root = WindRoot()
    root.title('Aplicacion text cssfsf')
    root.mainloop()
