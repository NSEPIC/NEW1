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



def minimize_all(self):    
        visibility = self.check_visible_windows()

        for i in range(len(self.master._open)):
            # Dice: Si hay alguna ventana abierta:
            if self.master._open[i]:
                # OCULTA LAS VENNTANAS:
                if not self._minimize == True and visibility:
                    #self._minimize = True if i == 2 else False    #Funciona mal, innecesario el else
                    #if i == 2: self._minimize = True

                    # Dice: Si alguna ventana esta abierta:
                    if self.master._open[i] == True:
                        self.master._windows[i] .frame_manager .minimize()
                        #self.master.all_minimize[i] = True

                # MUESTRA LAS VENTANAS:
                else:
                    #self._minimize = False if i == 2 else True    #Funciona mal, innecesario el else
                    #if i == 2: self._minimize = False

                    # Dice: Si alguna ventana esta abierta:
                    if self.master._open[i] == True:
                        self.master._windows[i] .frame_manager .window_manager_off()
                        self.update_position(self.master._windows[i]) 



        """ def test_version(self):
            print('testtttttt')
            if self.master.version == 'activado':
                self.list_images[0] = self.frame_image_base_3
                self.frame_image_base_3 .grid()
                self.frame_image_base_initial .grid_remove()

            else:
                self.list_images[0] = self.frame_image_base_initial
                self.frame_image_base_initial .grid()
                self.frame_image_base_3 .grid_remove() """