from tkinter import *
from tkinter import ttk 
from tkinter import filedialog
from typing import Sized
from PIL import ImageTk, Image
import cv2
import imutils
import numpy as np
import os 
import sys

class Interface(Tk):

    def __init__(self): #-------------------------------------------------------------NO TOCAR     
        super().__init__()                                                 # Llamando a Tk ()

        path = 'E:/1-RICHI/MovilesDB'
 #______Lista de Imágenes         
        self.Images_0 = self.generate_list (path, 'u')                     # Lista de imgs para la ventana: Interface
        self.Images_1 = self.generate_list (path, 'a')                     # Lista de imgs para las ventanas: 1 y 2
 #______Métodos de Configuración y Posicionamiento de Widget: [Interface]
        self. configure_interface()          
        self. widgets()   

 #______V A R I A B L E S  de  C O N T R O L  para las  V E N T A N A S   S U P E R I O R E S :  [1, 2, 3]

        self._frame_1 = None
        self._frame_2 = None
        self._frame_3 = None

        self.open_1 = True  
        self.open_2 = True  
        self.open_3 = True

    def configure_interface(self):   # Configuracion de la ventana -------------------NO TOCAR (despues)
      
        #ventana.overrideredirect(1)
        #ventana.attributes("-toolwindow",-1)
        self.title ('_AshmanBot_')                                 #  BORRAR
        self.geometry ('1000x150')                                 # TAMANIO DE LA VENTANA
        self.resizable (1,1)                                       # OTORGA PERMISO PARA CAMBIAR DE TAMANIO ALA VENTANA
        self.config (bg='magenta2')                                # CONFIGURA EL FONDO DE LA VENTANA, etc
        self.attributes ('-topmost', True)                         # SUPERPONE LA VENTANA A OTRAS APLICACIONES ABIERTAS
        self.wm_attributes ('-transparentcolor', 'magenta2')       # BORRA EL COLOR SELECCIONADO DE LA VENTANA
        #root.attributes("-alpha", 0.5 )   

    def generate_list (self, file, option):   # Metodo para leer todas las imageneS ------NO TOCAR 

        ouput = os.listdir (file)
        empty = [] 
       
        _lst = [[] for x in range(22)] 
        
        #_str = ['Fro','Fox','Boo','Ice','JD','Gru','Lig','Adu','Kni','Cal','Mag','Ran','Jol','Tur','Arm','Asa','Rao','Tri','Nak','Big','Dr1','Dr2']
        if option == 'a':  #  Esta lista foza la lista principal si funciona
            for i in ouput:
                """
                for index,iter in enumerate(_str):
                    if iter in i: 
                        full = file + '/' + i
                        open = cv2.imread (full)
                        RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB) 
                        _lst[index].append(RGB)
                return _lst
                """

                if 'Fro' in i: 
                    full = file + '/' + i
                    open = cv2.imread (full)
                    RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB) 
                    _lst[0].append(RGB)     

                if 'Fox' in i:
                    full = file + '/' + i
                    open = cv2.imread (full)
                    RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB) 
                    _lst[1].append(RGB)     

                if 'Boo' in i:
                    full = file + '/' + i
                    open = cv2.imread (full)
                    RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB)                        
                    _lst[2].append(RGB)  

                if 'Ice' in i: 
                    full = file + '/' + i
                    open = cv2.imread (full)
                    RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB)
                    _lst[3].append(RGB)

                if 'JD' in i: 
                    full = file + '/' + i
                    open = cv2.imread (full)
                    RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB)
                    _lst[4].append(RGB)

                if 'Gru' in i: 
                    full = file + '/' + i
                    open = cv2.imread (full)
                    RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB)
                    _lst[5].append(RGB)

                if 'Lig' in i: 
                    full = file + '/' + i
                    open = cv2.imread (full)
                    RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB)                        
                    _lst[6].append(RGB)

                if 'Adu' in i: 
                    full = file + '/' + i
                    open = cv2.imread (full)
                    RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB)
                    _lst[7].append(RGB)

                if 'Kni' in i: 
                    full = file + '/' + i
                    open = cv2.imread (full)
                    RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB)
                    _lst[8].append(RGB)

                if 'Kal' in i: 
                    full = file + '/' + i
                    open = cv2.imread (full)
                    RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB)
                    _lst[9].append(RGB)

                if 'Mag' in i: 
                    full = file + '/' + i
                    open = cv2.imread (full)
                    RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB)
                    _lst[10].append(RGB)

                if 'Ran' in i: 
                    full = file + '/' + i
                    open = cv2.imread (full)
                    RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB)
                    _lst[11].append(RGB)

                if 'Jol' in i: 
                    full = file + '/' + i
                    open = cv2.imread (full)
                    RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB)
                    _lst[12].append(RGB)

                if 'Tur' in i: 
                    full = file + '/' + i
                    open = cv2.imread (full)
                    RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB)
                    _lst[13].append(RGB)

                if 'Arm' in i: 
                    full = file + '/' + i
                    open = cv2.imread (full)
                    RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB)
                    _lst[14].append(RGB)

                if 'Asa' in i: 
                    full = file + '/' + i
                    open = cv2.imread (full)
                    RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB)
                    _lst[15].append(RGB)

                if 'Rao' in i: 
                    full = file + '/' + i
                    open = cv2.imread (full)
                    RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB)
                    _lst[16].append(RGB)

                if 'Tri' in i: 
                    full = file + '/' + i
                    open = cv2.imread (full)
                    RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB)
                    _lst[17].append(RGB)

                if 'Nak' in i: 
                    full = file + '/' + i
                    open = cv2.imread (full)
                    RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB)
                    _lst[18].append(RGB)

                if 'Big' in i: 
                    full = file + '/' + i
                    open = cv2.imread (full)
                    RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB)
                    _lst[19].append(RGB)

                if 'Dr1' in i: 
                    full = file + '/' + i
                    open = cv2.imread (full)
                    RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB)
                    _lst[20].append(RGB)
                    
                if 'Dr2' in i: 
                    full = file + '/' + i
                    open = cv2.imread (full)
                    RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB)
                    _lst[21].append(RGB)            
                    
            return _lst
 
        
        if option == 'u':
            for i in ouput:
                if i.split('.')[0] in ['__SubList__00','__SubList__01'] :       

                    full = file + '/' + i
                    open = cv2.imread (full)
                    RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB)
                    array = Image.fromarray (RGB)
                    img = ImageTk.PhotoImage (array)

                    empty. append (img)
            return empty       
        
    def widgets(self):  # widgets de la ventana Principal ----------------------------NO TOCAR  EDITAR DESPUES A CLASE BOTON O LABEL

        self.frame_initial = Create_Frame (self, bg='#11161d', width=60, height=65)    # Frame Contenedor del logo y la rueda     
        self.frame_initial .img_gear()                                                # Metodo de la clase segundaria                                              
        self.frame_initial .img_ash()                                                 # Metodo de la clase segundaria
        self.frame_initial .grid (column= 0, row= 0, padx=(0,0), pady=(0,0))
        self.frame_initial .grid_propagate (0)

        self.frame_plomo = Create_Frame (self, bg='#31343a', width=756, height=65)     # Frame Contenedor del Contenedor de los Botones
        self.frame_plomo .grid (column= 1, row= 0, padx=0, pady=0, sticky='n')
        self.frame_plomo .grid_propagate (0)

        self.button_container = Create_Frame (self.frame_plomo, bg = '#11161d',)       # Frame Contenedor de los Botones
        self.button_container .img_moviles()                                          # Metodo de la clase segundaria                                             
        self.button_container .grid (padx = (10,0), pady = (6,0))  
     
    def configure_height(self):  # Metodo para configurar Frame ---------------------NO TOCAR

        self.winfo = self.frame_initial .winfo_reqheight()
         
        if self.winfo == 65:
            self.frame_initial .config (width=60, height=165)   
        else:
            self.frame_initial .config (width=60, height=65)

    def remove_frame(self):  # Metodo para Remover Frame ----------------------------NO TOCAR

        if self.frame_plomo .winfo_ismapped():      
            self.frame_plomo .grid_remove()   
        else:
            self.frame_plomo .grid()  

############   M E T O D O S   P A R A   G E S T I O N A R   L A S   V E N T A N A S   S U P E R I O R E S   ############ 

    def windows_123(self, var_1, var_2, var_3):

        if self.open_1 == True: 
            self.toplevel_LEFT = _Toplevel()  #############################################################   VENTANA TOPLEVEL IZQUIERDA
            self.toplevel_LEFT .configure_toplevel ('izq', '220x690') #  metodo 

        self.open_1 = False     
                                
        container_frame_left = var_1 (self.toplevel_LEFT)  #  var_1 es un frame

        if self._frame_1 is not None:  
            self._frame_1 .destroy()
        self._frame_1 = container_frame_left
        self._frame_1 .pack()
        
        
        self.toplevel_LEFT .protocol ('WM_DELETE_WINDOW', lambda: self.close_windows(1))

#_______

        if self.open_2 == True:
            self.toplevel_RIGHT = _Toplevel()  #############################################################   VENTANA TOPLEVEL DERECHA
            self.toplevel_RIGHT .configure_toplevel ('der', '220x690')

        self.open_2 = False

        container_frame_right = var_2 (self.toplevel_RIGHT)  # ES UN FRAME POSICIONADO EN TOPLEVEL

        if self._frame_2 is not None:
            self._frame_2 .destroy()
        self._frame_2 = container_frame_right
        self._frame_2 .pack()


        self.toplevel_RIGHT.protocol ('WM_DELETE_WINDOW', lambda: self.close_windows(2))

#_______ desde aqui falta completar este if
        
        if self.open_3 == True:
            self.toplevel_STUF = _Toplevel()  #############################################################   VENTANA TOPLEVEL STUFF
            self.toplevel_STUF .configure_toplevel ('der', '620x190')

        self.open_3 = False

        container_frame_stuf = var_3 (self.toplevel_STUF)  # ES UN FRAME POSICIONADO EN TOPLEVEL

        if self._frame_3 is not None:
            self._frame_3 .destroy()
        self._frame_3 = container_frame_stuf
        self._frame_3 .pack()


        self.toplevel_STUF.protocol ('WM_DELETE_WINDOW', lambda: self.close_windows(3))





    def close_windows(self, number):

        if number == 1:
            self.toplevel_LEFT. destroy()
            self.open_1 = True

        if number == 2:
            self.toplevel_RIGHT. destroy()
            self.open_2 = True

        if number == 3:
            self.toplevel_STUF. destroy()
            self.open_3 = True


#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-

class _Toplevel (Toplevel):

    def __init__(self, *args): #---------------------------------------------------------NO TOCAR 
        Toplevel. __init__(self, *args) 
        #self.masters = master
          
    def configure_toplevel(self, head, size): #--------------------------------NO TOCAR (despues)
     
        self.title (head)    #  titulo
        self.geometry (size)  #  tamaño
        self.resizable (1,1)
        self.wm_attributes ('-topmost', True)
        self.config (bg = 'magenta2')
        self.wm_attributes ('-transparentcolor', 'magenta2')

#   desde ahy que editar...

    def widgets_toplevel(self, name):

        self.label0 = name
        self.label0 = Label (self, image = self.master.Imagenes [0])
        self.label0. bind ('<Configure>', self.resize_image)
        self.label0. pack (fill=BOTH, expand = YES)

    def resize_image(self, event):

        new_width = event.width
        new_height = event.height

        var1 = self.master.Imagenes_copia [0].resize((new_width, new_height))
        var2 = ImageTk.PhotoImage(var1)

        self.label0 . config (image = var2) 
        self.label0 . image = var2 


#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-
#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_--_-_-_-_-_-_-_-_-

class Create_Frame (Frame):   

    def __init__(self, *args, **kwargs):   #---------------------------------------NO TOCAR (despues) 
        Frame.__init__(self, *args, **kwargs)   # Llamando a Frame ()  #, **kwargs : pasar mas valores al momento de la llamada (diccionarios)

    def img_ash(self):   # Metodo que crea -1- Boton (logo) -------------------NO TOCAR (despues)
        
        self.btn_ash = Button (self, image= self.master.Images_0 [0], bg= '#11161d', bd= 0, activebackground= '#11161d' , command= self.master.remove_frame)
        self.btn_ash .grid (column= 0, row= 0, padx= 3, pady= 1)
          
    def img_gear(self):   # Metodo que crea -1- Boton (rueda)-----------------NO TOCAR (despues)

        self.btn_gear = Button (self, image= self.master.Images_0 [1], bg= '#11161d', bd= 0, activebackground= '#11161d', command= self.master.configure_height)
        self.btn_gear .grid (column= 0, row= 1)
       
    def img_moviles(self):   # Metodo que crea -22- Botones (moviles)  #command = lambda:images(1))
        
        self.Frog_1 = Button (self, text='Frog', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Fr_frog_left, Fr_frog_right, Fr_frog_stuf)) 

        self.Fox_2 = Button (self, text='Fox', font=('Calibri',9,'bold'), bg='#11161d', fg='yellow', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Fr_fox_left, Fr_fox_right, Fr_fox_stuf)) 
        
        self.Boomer_3 = Button (self, text='Boomer', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Fr_boomer_left, Fr_boomer_right, Fr_boomer_stuf))     
        
        self.Ice_4 = Button (self, text='Ice', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Fr_ice_left, Fr_ice_right, Fr_ice_stuf))

        self.JD_5 = Button (self, text='J.D', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Fr_jd_left, Fr_jd_right, Fr_jd_stuf))

        self.Grub_6 = Button (self, text='Grub', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Fr_grub_left, Fr_grub_right, Fr_grub_stuf))   

        self.Light_7 = Button (self, text='Light', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width=10, bd=0, command= lambda: self.master.master.windows_123 (Fr_light_left, Fr_light_right, Fr_light_stuf))       

        self.Aduka_8 = Button (self, text='Aduka', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Fr_aduka_left, Fr_aduka_right, Fr_aduka_stuf))      

        self.Knight_9 = Button (self, text='Knight', font=('Calibri',9,'bold'), bg='#11161d', fg='yellow', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Fr_knight_left, Fr_knight_right, Fr_knight_stuf))     

        self.Kalsiddon_10 = Button (self, text='Kalsiddon', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Fr_calziddon_left, Fr_calziddon_right, Fr_calziddon_stuf))

        self.Mage_11 = Button (self, text='Mage', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Fr_mage_left, Fr_mage_right, Fr_mage_stuf))  
   

        self.Randomizer_12 = Button (self, text='Randomizer', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Fr_randomizer_left, Fr_randomizer_right, Fr_randomizer_stuf))
 
        self.Jolteon_13 = Button (self, text='Jolteon', font=('Calibri',9,'bold'), bg='#11161d', fg='yellow', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Fr_jolteon_left, Fr_jolteon_right, Fr_jolteon_stuf))
 
        self.Turtle_14 = Button (self, text='Turtle', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Fr_turtle_left, Fr_turtle_right, Fr_turtle_stuf))

        self.Armor_15 = Button (self, text='Armor', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Fr_armor_left, Fr_armor_right, Fr_armor_stuf))

        self.Asate_16 = Button (self, text='A.Sate', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Fr_asate_left, Fr_asate_right, Fr_asate_stuf))

        self.Raon_17 = Button (self, text='Raon', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Fr_raon_left, Fr_raon_right, Fr_raon_stuf))
 
        self.Trico_18 = Button (self, text='Trico', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Fr_trico_left, Fr_trico_right, Fr_trico_stuf))

        self.Nak_19 = Button (self, text='Nak', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Fr_nak_left, Fr_nak_right, Fr_nak_stuf))
 
        self.Big_20 = Button (self, text='Big', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Fr_big_left, Fr_big_right, Fr_big_stuf))
 
        self.Dragon1_21 = Button (self, text='Dragon 1', font=('Calibri',9,'bold'), bg='#11161d', fg='yellow', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Fr_dragon1_left, Fr_dragon1_right, Fr_dragon1_stuf))
 
        self.Dragon2_22 = Button (self, text='Dragon 2', font=('Calibri',9,'bold'), bg='#11161d', fg='yellow', width= 10, bd=0, command= lambda: self.master.master.windows_123 (Fr_dragon2_left, Fr_dragon2_right, Fr_dragon2_stuf))
        
        
        self.Frog_1 .grid (column= 1, row= 1, pady= 3, padx= (5,0))
        self.Fox_2 .grid (column= 2, row= 1, pady= 3, padx= (0,0))       
        self.Boomer_3 .grid (column= 3, row= 1, pady= 3, padx= (0,0))           
        self.Ice_4 .grid (column= 4, row= 1, pady= 3, padx= (0,0))
        self.JD_5 .grid (column= 5, row= 1, pady= 3, padx= (0,0))
        self.Grub_6 .grid (column= 6, row= 1, pady= 3, padx= (0,0))
        self.Light_7 .grid (column= 7, row= 1, pady= 3, padx= (0,0))
        self.Aduka_8 .grid (column= 8, row= 1, pady= 3, padx= (0,0))
        self.Knight_9 .grid (column= 9, row= 1, pady= 3, padx= (0,0))
        self.Kalsiddon_10 .grid (column= 10, row= 1, pady= 3, padx= (0,0))
        self.Mage_11 .grid (column= 11, row= 1, pady= 3, padx= (0,5))

        self.Randomizer_12 .grid (column= 1, row= 2, pady= 2, padx= (5,0))
        self.Jolteon_13 .grid (column= 2, row= 2, pady= 2, padx= (0,0))
        self.Turtle_14 .grid (column= 3, row= 2, pady= 2, padx= (0,0))
        self.Armor_15 .grid (column= 4, row= 2, pady= 2, padx= (0,0))
        self.Asate_16 .grid (column= 5, row= 2, pady= 2, padx= (0,0))
        self.Raon_17 .grid (column= 6, row= 2, pady= 2, padx= (0,0))
        self.Trico_18 .grid (column= 7, row= 2, pady= 2, padx= (0,0))
        self.Nak_19 .grid (column= 8, row= 2, pady= 2, padx= (0,0))
        self.Big_20 .grid (column= 9, row= 2, pady= 2, padx= (0,0))
        self.Dragon1_21 .grid (column= 10, row= 2, pady= 2, padx= (0,0))
        self.Dragon2_22 .grid (column= 11, row= 2, pady= 2, padx= (0,5))
        


class Example(Frame):
    def __init__(self, master, index, *args, **kwargs):
        Frame.__init__(self, master, *args, kwargs)

        self.image = Image.fromarray (index)
        self.image_copy = self.image .copy()

        self.background = ImageTk.PhotoImage (self.image)

        self.img = Label (self, image= self.background)
        self.img .pack (fill= 'both', expand= True)
        self.img .bind ('<Configure>', self.resize)

    def resize(self, event):

        self.image2 = self.image_copy .resize ((self.master .winfo_width(), self.master .winfo_height()))

        self.background2 = ImageTk.PhotoImage (self.image2)
        self.img .config (image= self.background2)
        #self.img .image = self.backgroundd



################################                           ################################
################################            EL             ################################ 
################################          INICIO           ################################ 
################################   F R A M E  " F R O G "  ################################  


class Fr_frog_left (Frame, Interface):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [0] 

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.master.Images_1 [0][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.master.Images_1 [0][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

    
class Fr_frog_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [0] 

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.master.Images_1 [0][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.master.Images_1 [0][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Fr_frog_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [0]
     pass

################################   F R A M E  " F O X "  ################################
################################   F R A M E  " F O X "  ################################


class Fr_fox_left (Frame, Interface):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [1]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.master.Images_1 [1][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.master.Images_1 [1][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

 
class Fr_fox_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [1]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.master.Images_1 [1][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.master.Images_1 [1][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Fr_fox_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [1]
     pass

################################   F R A M E  " B O O M E R "  ################################
################################   F R A M E  " B O O M E R "  ################################ 


class Fr_boomer_left (Frame, Interface):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [2]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.master.Images_1 [2][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.master.Images_1 [2][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

  
class Fr_boomer_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [2]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.master.Images_1 [2][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.master.Images_1 [2][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Fr_boomer_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [2]
     pass

################################  F R A M E  " I C E "  ################################
################################  F R A M E  " I C E "  ################################


class Fr_ice_left (Frame, Interface):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [3]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.master.Images_1 [3][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.master.Images_1 [3][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

  
class Fr_ice_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [3]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.master.Images_1 [3][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.master.Images_1 [3][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Fr_ice_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [3]
     pass

################################  F R A M E  " J D "  ################################
################################  F R A M E  " J D "  ################################


class Fr_jd_left (Frame, Interface):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [4]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.master.Images_1 [4][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.master.Images_1 [4][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

  
class Fr_jd_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [4]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.master.Images_1 [4][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.master.Images_1 [4][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Fr_jd_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [4]
     pass


################################  F R A M E  " G R U B "  ################################
################################  F R A M E  " G R U B "  ################################


class Fr_grub_left (Frame, Interface):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [5]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.master.Images_1 [5][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.master.Images_1 [5][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

  
class Fr_grub_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [5]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.master.Images_1 [5][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.master.Images_1 [5][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Fr_grub_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [5]
     pass


################################  F R A M E  " L I G H T "  ################################
################################  F R A M E  " L I G H T "  ################################


class Fr_light_left (Frame, Interface):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [6]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.master.Images_1 [6][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.master.Images_1 [6][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

  
class Fr_light_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [6]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.master.Images_1 [6][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.master.Images_1 [6][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Fr_light_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [6]
     pass


################################  F R A M E  " A D U K A "  ################################
################################  F R A M E  " A D U K A "  ################################


class Fr_aduka_left (Frame, Interface):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [7]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.master.Images_1 [7][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.master.Images_1 [7][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

  
class Fr_aduka_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [7]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.master.Images_1 [7][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.master.Images_1 [7][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Fr_aduka_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [7]
     pass


################################  F R A M E  " K N I G H T "  ################################
################################  F R A M E  " K N I G H T "  ################################


class Fr_knight_left (Frame, Interface):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [8]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.master.Images_1 [8][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.master.Images_1 [8][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

  
class Fr_knight_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [8]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.master.Images_1 [8][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.master.Images_1 [8][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Fr_knight_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [8]
     pass


################################  F R A M E  " C A L Z I D D O N "  ################################
################################  F R A M E  " C A L Z I D D O N "  ################################


class Fr_calziddon_left (Frame, Interface):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [9]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.master.Images_1 [9][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.master.Images_1 [9][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

  
class Fr_calziddon_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [9]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.master.Images_1 [9][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.master.Images_1 [9][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Fr_calziddon_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [9]
     pass


################################  F R A M E  " M A G E "  ################################
################################  F R A M E  " M A G E "  ################################


class Fr_mage_left (Frame, Interface):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [10]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.master.Images_1 [10][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.master.Images_1 [10][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

  
class Fr_mage_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [10]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.master.Images_1 [10][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.master.Images_1 [10][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Fr_mage_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [10]
     pass


################################  F R A M E  " R A N D O M I Z E R "  ################################
################################  F R A M E  " R A N D O M I Z E R "  ################################


class Fr_randomizer_left (Frame, Interface):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [11]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.master.Images_1 [11][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.master.Images_1 [11][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

  
class Fr_randomizer_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [11]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.master.Images_1 [11][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.master.Images_1 [11][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Fr_randomizer_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [11]
     pass


################################  F R A M E  " J O L T E O N "  ################################
################################  F R A M E  " J O L T E O N "  ################################


class Fr_jolteon_left (Frame, Interface):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [12]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.master.Images_1 [12][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.master.Images_1 [12][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

  
class Fr_jolteon_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [12]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.master.Images_1 [12][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.master.Images_1 [12][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Fr_jolteon_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [12]
     pass


################################  F R A M E  " T U R T L E "  ################################
################################  F R A M E  " T U R T L E "  ################################

class Fr_turtle_left (Frame, Interface):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [13]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.master.Images_1 [13][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.master.Images_1 [13][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

  
class Fr_turtle_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [13]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.master.Images_1 [13][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.master.Images_1 [13][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Fr_turtle_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [13]
     pass


################################  F R A M E  " A R M O R "  ################################
################################  F R A M E  " A R M O R "  ################################


class Fr_armor_left (Frame, Interface):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [14]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.master.Images_1 [14][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.master.Images_1 [14][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

  
class Fr_armor_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [14]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.master.Images_1 [14][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.master.Images_1 [14][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Fr_armor_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [14]
     pass


################################  F R A M E  " A S A T E "  ################################
################################  F R A M E  " A S A T E "  ################################


class Fr_asate_left (Frame, Interface):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [15]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.master.Images_1 [15][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.master.Images_1 [15][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

  
class Fr_asate_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [15]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.master.Images_1 [15][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.master.Images_1 [15][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Fr_asate_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [15]
     pass


################################  F R A M E  " R A O N "  ################################
################################  F R A M E  " R A O N "  ################################


class Fr_raon_left (Frame, Interface):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [16]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.master.Images_1 [16][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.master.Images_1 [16][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

  
class Fr_raon_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [16]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.master.Images_1 [16][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.master.Images_1 [16][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Fr_raon_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [16]
     pass


################################  F R A M E  " T R I C O "  ################################
################################  F R A M E  " T R I C O "  ################################


class Fr_trico_left (Frame, Interface):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [17]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.master.Images_1 [17][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.master.Images_1 [17][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

  
class Fr_trico_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [17]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.master.Images_1 [17][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.master.Images_1 [17][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Fr_trico_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [17]
     pass


################################  F R A M E  " N A K "  ################################
################################  F R A M E  " N A K "  ################################


class Fr_nak_left (Frame, Interface):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [18]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.master.Images_1 [18][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.master.Images_1 [18][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

  
class Fr_nak_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [18]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.master.Images_1 [18][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.master.Images_1 [18][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Fr_nak_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [18]
     pass


################################  F R A M E  " B I G "  ################################
################################  F R A M E  " B I G "  ################################


class Fr_big_left (Frame, Interface):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [19]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.master.Images_1 [19][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.master.Images_1 [19][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

  
class Fr_big_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [19]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.master.Images_1 [19][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.master.Images_1 [19][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Fr_big_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [19]
     pass


################################  F R A M E  " D R A G O N '1' "  ################################
################################  F R A M E  " D R A G O N '1' "  ################################


class Fr_dragon1_left (Frame, Interface):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [20]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.master.Images_1 [20][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.master.Images_1 [20][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

  
class Fr_dragon1_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [20]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.master.Images_1 [20][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.master.Images_1 [20][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Fr_dragon1_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [20]
     pass


################################  F R A M E  " D R A G O N '2' "  ################################
################################  F R A M E  " D R A G O N '2' "  ################################


class Fr_dragon2_left (Frame, Interface):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [21]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.master.Images_1 [21][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.master.Images_1 [21][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)
        self.lbl_guia . place(x= 2, y= 48)    
 

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()

  
class Fr_dragon2_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [21]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.master.Images_1 [21][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.master.Images_1 [21][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Fr_dragon2_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [21]
     pass


################################            EL             ################################ 
################################            FIN            ################################

def main (): #--------------------------------------------------------------------NO TOCAR 
    app = Interface()    
    app .mainloop()

if __name__=="__main__":  #-------------------------------------------------------NO TOCAR 
    main()
   