from tkinter import Toplevel
from tkinter import *

class A (Frame):
    def __init__(self, master, nwindows=2, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master

        # Preparamos la lista de booleanos y la de windows
        self._open = [False] * nwindows
        self.windows = [None] * nwindows
        #self._frame = [None] * nwindows

        self.btn = Button(self, text='create windows', command= self.create)
        self.btn.pack()

    def create(self):
        #container = [None] * 4
        # Crear mediante un bucle las ventanas que no estén creadas
        for i in range(len(self._open)):
            if not self._open[i]:
                w = Toplevel(self.master, width=300)
                w.title(f'window {i+1}')
                w.geometry('300x150')
                w.bind('<Destroy>', 
                        lambda event, number=i: self.close_windows(number, event))
                # Actualizar las listas
                self.windows[i] = w
                self._open[i] = True

            """ container[i] = Frame (self.windows[i], bg='red')"""
            """ if self._frame[i] is not None: """
            """     self._frame[i] .destroy() """
            """ self._frame[i] = container[i] """
            """ self._frame[i] .pack(fill='both', expand=True) """

    def close_windows(self, number, event=None):
        print(11111)
        # Como medida de seguridad, aunque esto no debería ocurrir
        # verifico si la ventana ya estaba cerrada
        if not self._open[number]:
            return
        # La cierro y actualizo la lista
        self._open[number] = False
        #event.widget.destroy()
        print(f"DEBUG: Close {number}")

root = Tk()
a = A(root, nwindows=4)  # Probamos con 4 ventanas
a.pack()
root.mainloop()