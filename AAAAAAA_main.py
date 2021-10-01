from A_importaciones import *
from A_frames import *



class Move_class():
    def __init__(self):
        self._x = 0
        self._y = 0
   
        self.go = None

    def on_press(self):
        self.go = time.time()

    def on_release(self):
        if self.go is None: return
        if time.time() - self.go > 1:
            pass # root.destroy() #aqyu
        self.go = None


    def start_move2(self, event):        
        self._x = event.x
        self._y = event.y

    def stop_move2(self, event):
        self._x = None
        self._y = None

    def on_move2(self, event):
        deltax = event.x - self._x
        deltay = event.y - self._y
        new_position = "+{}+{}".format(self.master.master.winfo_x() + deltax, self.master.master.winfo_y() + deltay)
        self.master.master.geometry(new_position) #AQUI PUEDE HABER CONFLICTO
        self.master.master.master.geometry(new_position) 

 
################################
################################
################################
################################
################################
class Interface(Frame):  #--------------------------> FRAME CONTROLADOR PRINCIPAL
    def __init__(self, master=None, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #_____Variables de control para las ventanas:  [ 1,2,3 ]
        self._frame_1 = None
        self._frame_2 = None
        self._frame_3 = None

        self._open_1 = False  
        self._open_2 = False 
        self._open_3 = False

        #_____Variables de Control Secundarias:
        self._gear = True
        self._minimize = True
        
        #_____Métodos Llamados:
        self. configure_interface()
        self. widgets()


    def configure_interface(self):   # CONFIGURA TOPLEVEL PRINCIPA + FALTAA POSICIONAR LA VENTANA EN INICIACION
        
        # MASTER REFIERE A TOPLEVEL: PRINCIPAL
        self.master.title ('_AshmanBot_')
        self.master.geometry ('830x65+200+300')                           # TAMAÑO DE LA VENTANA + FALTA UNA POSICION AUTOMATICA BNA
        self.master.resizable (1,1)                                       # OTORGA PERMISO PARA CAMBIAR DE TAMANIO ALA VENTANA
        self.master.config (bg='magenta2')                                # CONFIGURA EL FONDO DE LA VENTANA, etc
        self.master.attributes ('-topmost', True)                         # SUPERPONE LA VENTANA A OTRAS APLICACIONES ABIERTAS
        self.master.wm_attributes ('-transparentcolor', 'magenta2')       # BORRA EL COLOR SELECCIONADO DE LA VENTANA

    def generate_list(self, file, option):   # INICIALIZA IMAGENES + NO SE SABE DONDE POSICIONAR ESTA FUNCION

        ouput = os.listdir (file)
        empty = []                    
        if option == 'I': 
            _lst = [[] for x in range(22)]
            _str = ['Fro','Fox','Boo','Ice','JD','Gru','Lig','Adu','Kni','Kal','Mag','Ran','Jol','Tur','Arm','Asa','Rao','Tri','Nak','Big','Dr1','Dr2']
            for i in ouput:               
                for index,iter in enumerate(_str):
                    if iter in i: 
                        full = file + '/' + i
                        open = cv2.imread (full)
                        RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB) 
                        _lst[index].append(RGB)               
            return _lst        
       
    def widgets(self):

        #____I N S T A N C I A S:  [ 4 ]
        self.frame_controller = A1_class (self, bg='#11161d', width=60, height=65)   # POSICIONADO      # Color: Azul         --- Frame contenedor de ash y gear
        self.frame_botones = B1_class (self, bg='#31343a', width=756, height=65)     # POSICIONADO      # Color: Plomo        --- Frame contenedor de botones
        self.frame_configurer = B2_class (self, bg='#31343a', width=756, height=65)  # NO POSICIONADO   # Color: Plomo        --- Frame contenedor de checkbuttons y labels
        self.frame_listmode = B3_class (self)                                        # NO POSICIONADO   # Color: Azul y Plomo --- Frame Contenedor de Spinbox y Listbox
         
        #____P A C K ():
        self.frame_controller .pack (side=LEFT, fill=BOTH)
        self.frame_botones .pack (side=LEFT, fill=BOTH) 

        #____P A C K___P R O P A G A T E ():
        self.frame_controller .pack_propagate (False)
        self.frame_botones .pack_propagate (False)

    def gear_stacking(self):   # ON: CON CLICK IZQUIERDO EN LA RUEDA DE CONFIGURACION - QUITA Y PONE WIDGET, REDIMENSIONA LA VENTANA PRINCIPAL,ETC

        if  self._gear == True:                                                  # PREDETERMINADO: TRUE
            self.frame_botones .pack_forget()                                    # BOTONES
            self.frame_listmode .pack_forget()                                   # MODO LISTA

            self.frame_configurer .focus_set()                                   # MODO CONFIGURACION
            self.frame_configurer .pack (side=LEFT, fill=BOTH, expand=True)
            self.master.geometry ('830x65')

            self._gear = False
 

        else:
            self.frame_configurer .pack_forget()

            if self.frame_configurer .ckbutton5.variable.get() == True:
                self.frame_listmode .pack (side=LEFT, fill=BOTH)
                self.frame_listmode .spinboxx .focus_set()
                self.master.geometry ('250x65')
            else:
                self.frame_botones .pack (side=LEFT, fill=BOTH) 
                self.frame_listmode .forget()

            self._gear = True 
   

############   G E S T I O N   DE  V E N T A N A S   S U P E R I O R E S  
############   G E S T I O N   DE  V E N T A N A S   S U P E R I O R E S  
############   G E S T I O N   DE  V E N T A N A S   S U P E R I O R E S  

    def windows_123 (self, var_1, var_2, var_3):
        
        #________________________V E N T A N A:   1________________________________________________________________
        if self._open_1 == False: 
            self.toplevel_LEFT = Toplevel_class (self, type=False)
            self.toplevel_LEFT .configure_toplevel ('Hoja Izquierda', '220x690') #  metodo  ('izq', '220x690')
                                
        container_frame_left = var_1 (self.toplevel_LEFT)  #  var_1 es un frame

        if self._frame_1 is not None:  
            self._frame_1 .destroy()
        self._frame_1 = container_frame_left
        self._frame_1 .pack()

        self.grip = ttk.Sizegrip(self._frame_1, style='TSizegrip')
        self.grip .place (relx=1.0, rely=1.0, anchor='center')
        ttk.Style().configure('TSizegrip', bg='black')
              
        #self.toplevel_LEFT .protocol ('WM_DELETE_WINDOW', lambda: self.close_windows(1))
        #self.toplevel_LEFT.bind('<Destroy>',lambda f: self.close_windows(1) )    

        #________________________V E N T A N A:   2________________________________________________________________
        if self._open_2 == False:
            self.toplevel_RIGHT = Toplevel_class (self, type=False)
            self.toplevel_RIGHT .configure_toplevel ('Hoja Derecha', '220x690')  # ('der', '220x690')

        container_frame_right = var_2 (self.toplevel_RIGHT) 

        if self._frame_2 is not None:
            self._frame_2 .destroy()
        self._frame_2 = container_frame_right
        self._frame_2 .pack()


        self.grip = ttk.Sizegrip(self._frame_2, style='TSizegrip')
        self.grip .place (relx=1.0, rely=1.0, anchor='center')
        ttk.Style().configure('TSizegrip', bg='black')

        #self.toplevel_RIGHT.protocol ('WM_DELETE_WINDOW', lambda: self.close_windows(2))
        #self.toplevel_RIGHT.bind('<Destroy>',lambda f: self.close_windows(2) )
        #_______ desde aqui falta completar este if


        #________________________V E N T A N A:   3________________________________________________________________
        if self._open_3 == False:
            self.toplevel_STUF = Toplevel_class (self, type=False) 
            self.toplevel_STUF .configure_toplevel ('Game Stuff', '620x190')     # ('stuf', '620x190')  

        container_frame_stuf = var_3 (self.toplevel_STUF) 

        if self._frame_3 is not None:
            self._frame_3 .destroy()
        self._frame_3 = container_frame_stuf
        self._frame_3 .pack()


        """ self.grip = ttk.Sizegrip(self._frame_3, style='TSizegrip')
        self.grip .place (relx=1.0, rely=1.0, anchor='center')
        ttk.Style().configure('TSizegrip', bg='black') """  # NO TIENE FRAME O IMAGEN TODAVIA

        #self.toplevel_STUF.protocol ('WM_DELETE_WINDOW', lambda: self.close_windows(3))
        self.toplevel_STUF.bind('<Destroy>',lambda f: self.close_windows(3) )

        #___________________________________________________________________________________________________________
        self._open_1 = True
        self._open_2 = True
        self._open_3 = True

        self.toplevel_LEFT .mainloop()
        self.toplevel_RIGHT .mainloop()
        self.toplevel_STUF .mainloop()
        #___________________________________________________________________________________________________________

    def close_windows(self,  number, event=None):
        print('afueraaaaaaaaa')
        if number == 1:
            self.toplevel_LEFT. destroy()
            self._open_1 = False
            print(11)

        if number == 2:
            self.toplevel_RIGHT. destroy()
            self._open_2 = False
            print(22)
        if number == 3:
            a = event.widget.master.destroy()
            #self.toplevel_STUF. destroy()
            self._open_3 = False
            print(33)



################################
class A1_class(Frame):   # Frame contenedor de ash y gear
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

        path = 'E:/1-RICHI/MovilesDB'
        #_____Coleccion de Imágenes         
        self.Sublist= self.generate_list(path, 'S') 
        #_____C O N T E N E D O R E S:  [ 0 ]

        self.ash_controller()
        self.gear_controller()
        
    def ash_controller(self):  # IMAGE
        self.btn_ash = Button (self, image=self.Sublist[0], bg='#11161d', bd=0, activebackground='#11161d' , command=self.ash_minimize_windows)
        self.btn_ash .grid (column=0, row=0, padx=(6,6), pady=0)
        self.btn_ash .bind ('<Double-3>', self.ash_close_windows)
          
    def gear_controller(self):  # IMAGE
        self.btn_gear = Button (self, image=self.Sublist[1], bg='#11161d', bd=0, activebackground='#11161d', command=self.master.gear_stacking) 
        self.btn_gear .grid (column=0, row=1)
        #self.btn_gear .bind ('<Double-3>', self.master.otros)

    def ash_close_windows(self, event):   # ACTIVA: CON DOBLE CLICK DERECHO EN EL LOGO - CIERRA LAS VENTANAS 
    
        try:
            self.master.toplevel_LEFT .destroy() 
            self.master._open_1 = False
            print('desde adentro')

            self.master.toplevel_RIGHT .destroy()
            self.master._open_2 = False

            self.master.toplevel_STUF .destroy()
            self.master._open_3 = False
        except:
            pass

    def ash_minimize_windows(self):   # ACTIVA: CON CLICK IZQUIERDO AL LOGO - MINIMIZA LAS VENTANAS
 
        if self.master._open_1 == True or self.master._open_2 == True or self.master._open_3 == True:

            # MOSTRAR VENTANAS
            if self.master._minimize == False:
                if self.master._open_1 == True:
                    self.master.toplevel_LEFT .mapped_manager()                         # Metodo de Toplevel_class
                    x = self.master.toplevel_LEFT .winfo_x()               
                    y = self.master.toplevel_LEFT .winfo_y()
                    self.master.toplevel_LEFT .geometry('+{}+{}'.format(x,y))           # Remarcando la posicion , soluciona el redimensionamiento automatico interior

                if self.master._open_2 == True:
                    self.master.toplevel_RIGHT .mapped_manager()
                    x = self.master.toplevel_RIGHT .winfo_x()
                    y = self.master.toplevel_RIGHT .winfo_y()
                    self.master.toplevel_RIGHT .geometry('+{}+{}'.format(x,y))

                if self.master._open_3 == True:
                    self.master.toplevel_STUF .mapped_manager()
                    x = self.master.toplevel_STUF .winfo_x()
                    y = self.master.toplevel_STUF .winfo_y()
                    self.master.toplevel_STUF .geometry('+{}+{}'.format(x,y))

                self.master._minimize = True

            # OCULTAR VENTANAS
            else:   
                if self.master._open_1 == True:  
                    #self.master.toplevel_LEFT .withdraw()                              # Esto distorciona el tamaño del icono, cuando el mouse se posiciona encima
                    self.master.toplevel_LEFT .frame_manager .minimize()              # Metodo de Toplevel_class
                if self.master._open_2 == True:
                    self.master.toplevel_RIGHT .frame_manager .minimize()
                if self.master._open_3 == True:
                    self.master.toplevel_STUF .frame_manager .minimize()

                self.master._minimize = False
   

    def generate_list(self, file, option):   # INICIALIZA IMAGENES

        ouput = os.listdir(file)
        empty = []              
        if option == 'S':
            for i in ouput: 
                if 'SubList' in i :      
                    full = file + '/' + i
                    open = cv2.imread (full)
                    RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB)
                    array = Image.fromarray (RGB)
                    img = ImageTk.PhotoImage (array)
                    empty. append (img)
            return empty

################################
class B1_class(Frame):   # Frame contenedor de botones
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

        #_____C O N T E N E D O R E S:  [ 1 ]
        self.frame_1 = Frame (self, bg='#11161d')          # Color: Azul
        self.frame_1 .grid (padx=(10,10), pady=(6,6))

        self.mobile_button()

    def mobile_button(self):   # Metodo que crea -22- Botones (moviles)  #command = lambda:images(1))
        
        self.Frog_1 = Button (self.frame_1, text='Frog', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.windows_123 (Frog_left_off, Frog_right, Frog_stuf)) 
        self.Fox_2 = Button (self.frame_1, text='Fox', font=('Calibri',9,'bold'), bg='#11161d', fg='yellow', width= 10, bd=0, command= lambda: self.master.windows_123 (Fox_left_off, Fox_right, Fox_stuf))         
        self.Boomer_3 = Button (self.frame_1, text='Boomer', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.windows_123 (Boomer_left_off, Boomer_right, Boomer_stuf))             
        self.Ice_4 = Button (self.frame_1, text='Ice', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.windows_123 (Ice_left_off, Ice_right, Ice_stuf))
        self.JD_5 = Button (self.frame_1, text='J.D', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.windows_123 (Jd_left_off, Jd_right, Jd_stuf))
        self.Grub_6 = Button (self.frame_1, text='Grub', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.windows_123 (Grub_left_off, Grub_right, Grub_stuf))   
        self.Lightning_7 = Button (self.frame_1, text='Lightning', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width=10, bd=0, command= lambda: self.master.windows_123 (Lightning_left_off, Lightning_right, Lightning_stuf))       
        self.Aduka_8 = Button (self.frame_1, text='Aduka', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.windows_123 (Aduka_left_off, Aduka_right, Aduka_stuf))      
        self.Knight_9 = Button (self.frame_1, text='Knight', font=('Calibri',9,'bold'), bg='#11161d', fg='yellow', width= 10, bd=0, command= lambda: self.master.windows_123 (Knight_left_off, Knight_right, Knight_stuf))     
        self.Kalsiddon_10 = Button (self.frame_1, text='Kalsiddon', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.windows_123 (Kalsiddon_left_off, Kalsiddon_right, Kalsiddon_stuf))
        self.Mage_11 = Button (self.frame_1, text='Mage', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.windows_123 (Mage_left_off, Mage_right, Mage_stuf))     

        self.Randomizer_12 = Button (self.frame_1, text='Randomizer', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.windows_123 (Randomizer_left_off, Randomizer_right, Randomizer_stuf)) 
        self.Jolteon_13 = Button (self.frame_1, text='Jolteon', font=('Calibri',9,'bold'), bg='#11161d', fg='yellow', width= 10, bd=0, command= lambda: self.master.windows_123 (Jolteon_left_off, Jolteon_right, Jolteon_stuf)) 
        self.Turtle_14 = Button (self.frame_1, text='Turtle', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.windows_123 (Turtle_left_off, Turtle_right, Turtle_stuf))
        self.Armor_15 = Button (self.frame_1, text='Armor', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.windows_123 (Armor_left_off, Armor_right, Armor_stuf))
        self.Asate_16 = Button (self.frame_1, text='A.Sate', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.windows_123 (Asate_left_off, Asate_right, Asate_stuf))
        self.Raon_17 = Button (self.frame_1, text='Raon', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.windows_123 (Raon_left_off, Raon_right, Raon_stuf)) 
        self.Trico_18 = Button (self.frame_1, text='Trico', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.windows_123 (Trico_left_off, Trico_right, Trico_stuf))
        self.Nak_19 = Button (self.frame_1, text='Nak', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.windows_123 (Nak_left_off, Nak_right, Nak_stuf)) 
        self.Bigfoot_20 = Button (self.frame_1, text='Bigfoot', font=('Calibri',9,'bold'), bg='#11161d', fg='white', width= 10, bd=0, command= lambda: self.master.windows_123 (Bigfoot_left_off, Bigfoot_right, Bigfoot_stuf)) 
        self.Barney_21 = Button (self.frame_1, text='Barney', font=('Calibri',9,'bold'), bg='#11161d', fg='yellow', width= 10, bd=0, command= lambda: self.master.windows_123 (Barney_left_off, Barney_right, Barney_stuf)) 
        self.Dragon_22 = Button (self.frame_1, text='Dragon', font=('Calibri',9,'bold'), bg='#11161d', fg='yellow', width= 10, bd=0, command= lambda: self.master.windows_123 (Dragon_left_off, Dragon_right, Dragon_stuf))
                
        self.Frog_1 .grid (column= 1, row= 1, pady= 3, padx= (5,0))
        self.Fox_2 .grid (column= 2, row= 1, pady= 3, padx= (0,0))       
        self.Boomer_3 .grid (column= 3, row= 1, pady= 3, padx= (0,0))           
        self.Ice_4 .grid (column= 4, row= 1, pady= 3, padx= (0,0))
        self.JD_5 .grid (column= 5, row= 1, pady= 3, padx= (0,0))
        self.Grub_6 .grid (column= 6, row= 1, pady= 3, padx= (0,0))
        self.Lightning_7 .grid (column= 7, row= 1, pady= 3, padx= (0,0))
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
        self.Bigfoot_20 .grid (column= 9, row= 2, pady= 2, padx= (0,0))
        self.Barney_21 .grid (column= 10, row= 2, pady= 2, padx= (0,0))
        self.Dragon_22 .grid (column= 11, row= 2, pady= 2, padx= (0,5))

################################
class B2_class(Frame):   # Frame contenedor de checkbuttons y labels
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, kwargs)

        #_____C O N T E N E D O R E S:  [ 0 ]
 
        self.create_label()
        self.create_checkbutton()

    def cheeck(self): # ES UN EVENTP QUE ´PASA CUANDO CHECKBUTON 5 CAMBIOA DE VALOR 
        pass
        """ if self.variable.get() == False:
            self.variable.set(True)
        if self.variable.get() == True:
            self.variable.set(False)
        """

    def create_label(self):

        label_option1 = Label (self, text= 'Activar Aimbot :' , font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)
        label_option2 = Label (self, text= 'Activar aimbot :', font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)
        label_option3 = Label (self, text= 'Activar ddd ', font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)
        label_option4 = Label (self, text= 'Activar Modo On :', font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)
        label_option5 = Label (self, text= 'Activar Modo Lista :', font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)
        label_option6 = Label (self, text= 'Activar Modo Guía :', font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)
        label_option7 = Label (self, text= 'Recordar Configuracion :', font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)

        label_option1 .grid (column=0, row=0, padx= (30,10), pady=(10,0), sticky=W)
        label_option2 .grid (column=0, row=1, padx= (30,10), pady=(0,0), sticky=W)
        label_option3 .grid (column=2, row=0, padx= (30,10), pady=(10,0), sticky=W)
        label_option4 .grid (column=2, row=1, padx= (30,10), pady=(0,0), sticky=W)
        label_option5 .grid (column=4, row=0, padx= (30,10), pady=(10,0), sticky=W)
        label_option6 .grid (column=4, row=1, padx= (30,10), pady=(0,0), sticky=W)   
        label_option7 .grid (column=6, row=0, padx= (30,10), pady=(10,0), sticky=W)
    
    def create_checkbutton(self):

        self.ckbutton1 = Checkbutton_class (self, bg='#31343a', activebackground= '#31343a', bd=0, borderwidth=0,)
        self.ckbutton2 = Checkbutton_class (self, bg='#31343a', activebackground= '#31343a', bd=0, borderwidth=0,)
        self.ckbutton3 = Checkbutton_class (self, bg='#31343a', activebackground= '#31343a', bd=0, borderwidth=0,)
        self.ckbutton4 = Checkbutton_class (self, bg='#31343a', activebackground= '#31343a', bd=0, borderwidth=0,)
        self.ckbutton5 = Checkbutton_class (self, bg='#31343a', activebackground= '#31343a', bd=0, borderwidth=0,)
        self.ckbutton6 = Checkbutton_class (self, bg='#31343a', activebackground= '#31343a', bd=0, borderwidth=0,)
        self.ckbutton7 = Checkbutton_class (self, bg='#31343a', activebackground= '#31343a', bd=0, borderwidth=0,)
    
        self.ckbutton1 .grid (column=1, row=0, pady=(10,0))
        self.ckbutton2 .grid (column=1, row=1, pady=(0,0))
        self.ckbutton3 .grid (column=3, row=0, pady=(10,0))
        self.ckbutton4 .grid (column=3, row=1, pady=(0,0))
        self.ckbutton5 .grid (column=5, row=0, pady=(10,0))
        self.ckbutton6 .grid (column=5, row=1, pady=(0,0))
        self.ckbutton7 .grid (column=7, row=0, padx=(0,200), pady=(10,0),)

################################          
class B3_class(Frame, Move_class):   # Frame Contenedor de Spinbox y Listbox
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, kwargs)

        path = 'E:/1-RICHI/MovilesDB'
        #_____Coleccion de imagenes  
        self.Miniatures= self.generate_list(path, 'M')

        #_____C O N T E N E D O R E S___2:
        self.frame_1 = Frame (self, bg='#31343a', width=116, height=65)    # Color: Plomo       
        self.frame_2 = Frame (self, bg='#11161d', width=60, height=65)     # Color: Azul  

        self.container_2w = Frame (self.frame_1, width=116, height=20, bg='#11161d')
        self.select_mobil = Label (self.frame_1, text='Seleccione  Mobil :', font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)
        self.miniature_mobil = Label (self.frame_2, image=self.Miniatures[0], bd= 0)


        # ANTERIOR
        #self.select_mobil .bind("<ButtonPress-1>", self.master.master.start_move)   
        #self.select_mobil .bind("<ButtonRelease-1>", self.master.master.stop_move) 
        #self.select_mobil .bind("<B1-Motion>", self.master.master.on_move)


        self.create_listbox (width=11, height=1)
        self.create_spinbox (width=13)
        self.bind_move_3()

        #_____G R I D ():
        self.frame_1 .grid (column=0, row=0)                                            # MASTER A
        self.frame_2 .grid (column=1, row=0)                                            # MASTER B

        self.container_2w .grid (column=0, row=0, padx=0, pady=(0,2), sticky=N)         # SUB A.1
        self.select_mobil .grid (column=0, row=1, padx=11, pady=0)                      # SUB A.2
        self.spinboxx .grid (column=0, row=2, padx=13, pady=(3,3))                      # SUB A.3

        self.red_green .grid (column=0, row=0, padx=0, pady=0)                          # SUB.SUB A.1 .1 
        self.listboxx .grid (column=1, row=0, padx=12, pady=(1,0))                      # SUB.SUB A.1 .2

        self.miniature_mobil .grid (padx=2, pady=3)                                     # SUB B.1

        #_____G R I D___P R O P A G A T E ():
        self.frame_1 .grid_propagate(False)
        self.frame_2 .grid_propagate(False)
        self.container_2w .grid_propagate(False)
        
        #_____Variables de control:
        self._change = None
   

    def change_variable(self, *args):  # ACTIVA: SI SPINBOX_VARIABLE CAMBIA DE VALOR - BORRA LA LISTA DE LISTBOX, MANDA A LLAMAR A UPDATE Y CAMBIA LAS MINIATURAS

        spin = self.spinboxx.get().capitalize()

        if spin == '':
            self.listboxx .delete(0, END)
        else:    
            list_new = []
            for index, i in enumerate(self.spinbox_values):
                if spin == i:                           
                    self.miniature_mobil .config(image= self.Miniatures[index])
                    self.spinboxx .icursor(END)
                if spin in i:
                    list_new .append(i)

            if list_new != []:
                self.update(list_new)

            if spin == 'As':  
                self.listboxx.delete(0,1)

        if self.listboxx.get(0) != spin and self.listboxx.get(0) != '' or spin == '': 
            self.miniature_mobil .config(image= self.Miniatures[22])
        
    def update(self, list):  # ACTIVA: ** SI ES LLAMADO POR CHANGE_VARIABLE ** - BORRA LA LISTA DE LISTBOX EXISTENTE, AGREGA NUEVOS VALORES A LISTA Y BORRA DE NUEVO SI SE CUMPLE LA CONDICION
    
        self.listboxx .delete(0, END)                                    # 1- BORRA LA LISTA DE LISTBOX
        for i in list:                                                  # 1- ITERANDO: 'list_new'.  2- INSERTANDO ITERADOR 'i' A LISTBOX.  
            self.listboxx .insert(END, i)
        if self.listboxx.get(0) == self.spinbox_variable.get():
            self.listboxx .delete(0, END) 


    def listbox_select(self,event):  # ACTIVA: CON CLICK IZQUIERDO EN LISTBOX - 
       
        selection = self.listboxx .get(ANCHOR)                                                           # 1- BORRA EL CONTENIDO DE SPINBOX.  2- INSERTA EL ITEM SELECCIONADO DEL LISTBOX A SPINBOX                         
        
        if self.listboxx.get(0,END) != ():      
            self.spinboxx .delete(0, END) 
        self.spinboxx .insert(0, selection)
        self.listboxx .selection_clear(0,END)
 
        self.after(100, lambda: self.spinboxx.focus_set())

        #print('numero',self.listboxx.size())
          

    def listbox_enter(self, event):  # ACTIVA: CON TECLA ENTER - INSERTA EL VALOR DE LISTBOX A SPINBOX, MANDA LLAMAR A OPEN_WINDOWS  Y ABREN LAS VENTANAS
 
        listbx = self.listboxx.get(0)
        spinbx = self.spinboxx.get()

        if listbx != spinbx and listbx != '':
            self.spinboxx.delete(0, END)
            self.spinboxx.insert(0, listbx)
            
        self.open_windows(event) 
         
    def open_windows(self, event):  # ACTIVA: ** SI ES LLAMADO POR LISTBOX_SELECT ** - ABRE LAS VENTANAS
        
        left = [Frog_left_off, Fox_left_off, Boomer_left_off, Ice_left_off, Jd_left_off, Grub_left_off, Lightning_left_off, Aduka_left_off, Knight_left_off, Kalsiddon_left_off, Mage_left_off, Randomizer_left_off, Jolteon_left_off, Turtle_left_off, Armor_left_off, Asate_left_off, Raon_left_off, Trico_left_off, Nak_left_off, Bigfoot_left_off, Barney_left_off, Dragon_left_off,]
        right = [Frog_right, Fox_right, Boomer_right, Ice_right, Jd_right, Grub_right, Lightning_right, Aduka_right, Knight_right, Kalsiddon_right, Mage_right, Randomizer_right, Jolteon_right, Turtle_right, Armor_right, Asate_right, Raon_right, Trico_right, Nak_right, Bigfoot_right, Barney_right, Dragon_right]
        stuf = [Frog_stuf, Fox_stuf, Boomer_stuf, Ice_stuf, Jd_stuf, Grub_stuf, Lightning_stuf, Aduka_stuf, Knight_stuf, Kalsiddon_stuf, Mage_stuf, Randomizer_stuf, Jolteon_stuf, Turtle_stuf, Armor_stuf, Asate_stuf, Raon_stuf, Trico_stuf, Nak_stuf, Bigfoot_stuf, Barney_stuf, Dragon_stuf]

        for index, i in enumerate(self.spinbox_values):
            if self.spinboxx.get() == i:
                self.master.windows_123(left[index], right[index], stuf[index]) 
        
        if self._change is not None:
            self.after(5000, self.automatic_deletion) 

    def automatic_deletion(self):  # ACTIVA: ** SI ES LLAMADO POR OPEN_WINDOWS ** Y SI LA VARIABLE DE CONTROL NO ES NONE - LIMPIA SPINBOX

        self.spinboxx .delete(0, END)     


    def change_red_green(self, event):  # ACTIVA: CLICK IZQUIERDO EN RED_GREEN - CAMBIA IMAGEN ROJO-VERDE Y VICEVERSA

        if self._change is None:
            self.red_green .config (image=self.Miniatures[24])  
            self._change = True
        else:
            self.red_green .config (image=self.Miniatures[23])
            self._change = None

    def validate_text(self, text, arg): # SIEMPRE QUE INSERTE TEXTO EN SPINBOX - NO PERMITE NUMEROS,SIMBOLOS,ESPACIOS Y CONTROLA LA CANTIDAD

        if all (i not in "0123456789[{!¡¿?<>(|#$%&),_-°'´}] +-*/=" for i in text) and len(text) < 14:   
                return True                                                 
        return False  

    def create_spinbox(self, **args):
        
        self.spinboxx = Spinbox (self.frame_1, **args)
        
        self.spinbox_variable = StringVar()
        self.spinbox_values = ['Frog', 'Fox', 'Boomer', 'Ice', 'J.d', 'Grub', 'Lightning', 'Aduka', 'Knight', 'Kalsiddon', 'Mage', 'Randomizer', 'Jolteon', 'Turtle', 'Armor','A.sate', 'Raon', 'Trico', 'Nak', 'Bigfoot', 'Barney', 'Dragon']
        self.all_register = (self.register(self.validate_text), '%P', '%S')
        self.spinboxx.config (values=self.spinbox_values,
                             textvariable=self.spinbox_variable,
                             validate='key',
                             validatecommand=self.all_register,
                             justify='center',
                             wrap=True,
                             bd=0)

        self.spinboxx.icursor(END)

        self.spinboxx .bind ('<Double-1>', lambda *arg: self.spinboxx.delete(0, END))     # ACTIVA: CON DOBLE CLICK EN SPINBOX - LIMPIA SPINBOX
        self.spinboxx .bind ('<Return>', self.listbox_enter)                              # ACTIVA: CON TECLA ENTER - SELECCIONA EL INDICE 0 DEL LISTBOX  

        self.spinbox_variable .trace_add ('write', self.change_variable)  
        self.spinbox_variable .trace_add ('write', lambda *arg: self.spinbox_variable.set (self.spinbox_variable.get() .capitalize()))   # INSERTA EL VALOR OBTENIDO EN MAYUSCULA EL PRIMER STRING

    def create_listbox(self, **kwargs):
     
        self.red_green = Label (self.container_2w, image= self.Miniatures[23], width=11, bd=0) 

        self.listboxx = Listbox (self.container_2w, **kwargs)
        self.listboxx .config (font=('Calibri',9,'bold'),
                              bg='#11161d', fg='#00ff00',
                              borderwidth=0, bd=0,
                              highlightthickness=0,
                              highlightbackground='#11161d',  
                              highlightcolor='#11161d',  
                              selectbackground='#11161d', 
                              selectforeground='#ff8000',
                              activestyle='none',
                              justify='center',
                              selectmode=SINGLE,
                              takefocus=0)

        self.red_green .bind ("<Button-1>", self.change_red_green)
        self.listboxx .bind ('<<ListboxSelect>>', self.listbox_select)   # ACTIVA: CON CLICK IZQUIERDO EN EL LISTBOX - SELECCIONA 1 ITEM

    def generate_list (self, file, option):   # INICIALIZA IMAGENES

        ouput = os.listdir (file)
        empty = [] 
           
        if option == 'M':
            for i in ouput:  
                if 'Mini' in i :      
                    full = file + '/' + i
                    open = cv2.imread (full)
                    RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB)
                    array = Image.fromarray (RGB)
                    img = ImageTk.PhotoImage (array)
                    empty. append (img)
            return empty

    def bind_move_3(self):
        # NEW
        #Move_class.__init__(self)
        self.select_mobil .bind("<ButtonPress-1>", self.start_move2)   
        self.select_mobil .bind("<ButtonRelease-1>", self.stop_move2) 
        self.select_mobil .bind("<B1-Motion>", self.on_move2)
        
################################
################################
################################
################################
################################
class Checkbutton_class(Checkbutton):   
    def __init__(self, *args, **kwargs):
        Checkbutton.__init__(self, *args, **kwargs)

        self.variable = BooleanVar()
        self.configure(variable=self.variable)
    
    def checked(self):
        return self.variable.get()
    
    def check(self):
        self.variable.set(True)
    
    def uncheck(self):
        self.variable.set(False) 

    def value (self):
        if self.variable .get() == True: 
            pass  
   

################################
################################
################################
################################
################################
class Frame_manager_class(Frame):
    def __init__(self, master=None, _mode=None, **kwargs):
        Frame.__init__(self, master, **kwargs)
        self._mode = _mode
        self.master = master
        self.initializer_images()

    def close(self):
        if self._mode is None:
            self.master.destroy()                    # Destruye Toplevel Principal
            self.master.master.destroy()             #/Destruye root

        if self._mode is not None:
            self.master.destroy()                    # Destruye Toplevel Secundarios
            self.master.quit()                       # APRUEBAA

    def minimize(self):
        if self._mode is None:   
            self.master.withdraw()                   # Oculta Toplevel Principal
            self.master.master .iconify()            # Iconiza root

        if self._mode is not None:
            self.master.update_idletasks()           # Termina Tareas Pendientes (dibujo,etc)
            self.master.overrideredirect(False)      # Dibuja el Gestor de Ventanas a Toplevel Secundarias
            self.master.state('iconic')              # Iconiza Toplevel Secundarias

    # MODO: VERTICAL INTERFACE
    def buttons_height(self):
        self.button_close = Button(self, image=self.image_close, command=self.close, bd=0, bg='black', activebackground='black')
        self.button_minimize = Button(self, image=self.image_minimize, command=self.minimize, bd=0, bg='black', activebackground='black')

        self.button_close .pack(side=TOP, pady=7)               # modo vertical
        self.button_minimize .pack(side=BOTTOM, pady=7)         # modo vertical

    # MODO: HORIZONTAL VENTANAS      
    def buttons_width(self):
        self.button_close = Button(self, image=self.image_close, command=self.close, bd=0, bg='black', activebackground='black')
        self.button_minimize = Button(self, image=self.image_minimize, command=self.minimize, bd=0, bg='black', activebackground='black')
        self.label_title = Label(self, text='', fg="white", bg="green")

        self.button_close .pack(side=RIGHT)                     # modo horizontal
        self.button_minimize .pack(side=RIGHT, padx=10)         # modo horizontal    
        self.label_title .pack(side=RIGHT, padx=0, pady=0)      # modo horizontal

    def initializer_images(self):
        self.image_close = PhotoImage(file= '11.png')
        self.image_maximize = PhotoImage(file= 'ma.png') 
        self.image_minimize = PhotoImage(file= '22.png')
        self.image_reduce = PhotoImage(file= 'ma2.png')
  

################################
################################
################################
################################
################################
class Toplevel_class(Toplevel):
    def __init__(self, master=None, type=None, **kwargs):
        Toplevel.__init__(self, master, **kwargs)
        self.master = master
        self.overrideredirect(True)
        self._x = 0
        self._y = 0

        if type == True:         # FRAME BOTONES DE CONTROL MODO: VERTICAL
            self.mode_height()
        if type == False:        # FRAME BOTONES DE CONTROL MODO: HORIZONTAL
            self.mode_width()

        path = 'E:/1-RICHI/MovilesDB'
        #____Coleccion de imagenes:
        self.Images_1 = self.generate_list (path, 'I')

        #____self.frame_manager:  GESTOR DE VENTANAS INSTANCIA DE:          Frame_manager_class: FRAME
        self.frame_manager .bind("<ButtonPress-1>", self.start_move)        # Intercepta los puntos x,y 
        self.frame_manager .bind("<ButtonRelease-1>", self.stop_move)       # Asigna un estado de inicio o stop
        self.frame_manager .bind("<B1-Motion>", self.on_move)               # Mueve la ventana 

        self.master .bind("<Map>", self.deiconify_1)                        # SE EJECUTA CUANDO ES VISIBLE    / SOLO SE EJECUTA PARA INTERFACE
        self.master .bind("<Unmap>", self.iconify_1)                        # SE EJECUTA CUANDO ES INVISIBLE  / SOLO SE EJECUTA PARA INTERFACE   


    def iconify_1(self, event):   # SOLO SE EJECUTA SI SE INSTANCIA INTERFACE SI NO NO SIRVE PORQUE ESTA INSTANCIADO EN TK
        self.withdraw()

    def deiconify_1(self, event): # SOLO SE EJECUTA SI SE INSTANCIA INTERFACE SI NO NO SIRVE PORQUE ESTA INSTANCIADO EN TK
        self.deiconify()


    def start_move(self, event):        
        self._x = event.x
        self._y = event.y

    def stop_move(self, event):
        self._x = None
        self._y = None

    def on_move(self, event):
        deltax = event.x - self._x
        deltay = event.y - self._y
        new_position = "+{}+{}".format(self.winfo_x() + deltax, self.winfo_y() + deltay)

        self.geometry(new_position)              # Moviendo Instancias
 
        if self.move_tk == True:
            self.master.geometry(new_position)   # Moviendo Raiz   


    def configure_toplevel(self, title, size):
        self.title (title)
        self.geometry (size)
        self.resizable (1,1)
        self.wm_attributes ('-topmost', True)                     # FUNCIONA BIEN pero molesta para editar 
        #self.config (bg = 'magenta2')                            # FUNCIONA BIEN pero tiene mal aspecto
        #self.wm_attributes ('-transparentcolor', 'magenta2')     # FUNCIONA BIEN pero tiene mal aspecto
 
    def generate_list(self, file, option):   # INICIALIZA IMAGENES

        ouput = os.listdir (file)
        empty = []                    
        if option == 'I': 
            _lst = [[] for x in range(22)]
            _str = ['Fro','Fox','Boo','Ice','JD','Gru','Lig','Adu','Kni','Kal','Mag','Ran','Jol','Tur','Arm','Asa','Rao','Tri','Nak','Big','Dr1','Dr2']
            for i in ouput:               
                for index,iter in enumerate(_str):
                    if iter in i: 
                        full = file + '/' + i
                        open = cv2.imread (full)
                        RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB) 
                        _lst[index].append(RGB)               
            return _lst 


    # MODO: VERTICAL INTERFACE
    def mode_height(self):  
        #____F R A M E:
        self.frame_manager = Frame_manager_class (self, bg="black")  
        self.frame_manager .pack (side=RIGHT, fill=BOTH)
        self.frame_manager .buttons_height()

        self.move_tk = True
        # DESDE AQUI SE PUEDE BORRAR E INTANCIAR EN MAIN

    # MODO: HORIZONTAL VENTANAS
    def mode_width(self):
        #____F R A M E:
        self.frame_manager = Frame_manager_class (self, a=1, bg="black")   
        self.frame_manager .pack(side=TOP, fill=BOTH)
        self.frame_manager .buttons_width()
        self.frame_manager .bind("<Map>",self.mapped_manager)

        #____L A B E L:     
        self.frame_manager .label_title .bind("<ButtonPress-1>", self.start_move)        # Intercepta los puntos x,y 
        self.frame_manager .label_title .bind("<ButtonRelease-1>", self.stop_move)       # Asigna un estado de inicio o stop
        self.frame_manager .label_title .bind("<B1-Motion>", self.on_move)               # Mueve la ventana 

        self.move_tk = False 

    def mapped_manager(self, event=None):  # / SOLO SE EJECUTA PARA VENTANAS 1,2,3   
        self.update_idletasks()
        self.overrideredirect(True)
        self.state('normal')



################################
################################
################################
################################
################################
class Root_class(Tk):  # SIN FUNCIONAMIENTO
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        #self.resizable(0, 0)
        self.geometry('0x0')

        self.toplevel_principal = Toplevel_class(self, type=True)  # MODO VERTICAL
        self.toplevel_principal .geometry('830x65')
        self.frame_principal = Interface(self.toplevel_principal)
        self.frame_principal .pack(side=RIGHT, fill=BOTH)

        self.bind("<Map>", self.on_deiconify)
        self.bind("<Unmap>", self.on_iconify)

        #self.bind_all_root()

    def on_iconify(self, event):
        self.toplevel_principal.withdraw()

    def on_deiconify(self, event):
        self.toplevel_principal.deiconify()

    def bind_all_root(self):

        print(77777)
        self.frame_principal .frame_botones .bind("<ButtonPress-1>", self.start_move)   
        self.frame_principal .frame_botones .bind("<ButtonRelease-1>", self.stop_move) 
        self.frame_principal .frame_botones .bind("<B1-Motion>", self.on_move)

        """ self.frame_ashmanbot .frame_controller .bind("<ButtonPress-1>", self.start_move)   
        self.frame_ashmanbot .frame_controller .bind("<ButtonRelease-1>", self.stop_move) 
        self.frame_ashmanbot .frame_controller .bind("<B1-Motion>", self.on_move)

        self.frame_ashmanbot .frame_controller .btn_ash .bind("<ButtonPress-1>", self.start_move)   
        self.frame_ashmanbot .frame_controller .btn_ash .bind("<ButtonRelease-1>", self.stop_move) 
        self.frame_ashmanbot .frame_controller .btn_ash .bind("<B1-Motion>", self.on_move)

        self.frame_ashmanbot .frame_controller .btn_gear .bind("<ButtonPress-1>", self.start_move)   
        self.frame_ashmanbot .frame_controller .btn_gear .bind("<ButtonRelease-1>", self.stop_move) 
        self.frame_ashmanbot .frame_controller .btn_gear .bind("<B1-Motion>", self.on_move)

        self.frame_ashmanbot .frame_config .bind("<ButtonPress-1>", self.start_move)   
        self.frame_ashmanbot .frame_config .bind("<ButtonRelease-1>", self.stop_move) 
        self.frame_ashmanbot .frame_config .bind("<B1-Motion>", self.on_move)

        self.frame_ashmanbot .frame_listmode .bind("<ButtonPress-1>", self.start_move)   
        self.frame_ashmanbot .frame_listmode .bind("<ButtonRelease-1>", self.stop_move) 
        self.frame_ashmanbot .frame_listmode .bind("<B1-Motion>", self.on_move)

        self.frame_ashmanbot .frame_listmode.frame_1 .bind("<ButtonPress-1>", self.start_move)   
        self.frame_ashmanbot .frame_listmode.frame_1 .bind("<ButtonRelease-1>", self.stop_move) 
        self.frame_ashmanbot .frame_listmode.frame_1 .bind("<B1-Motion>", self.on_move)

        self.frame_ashmanbot .frame_listmode.frame_2 .bind("<ButtonPress-1>", self.start_move)   
        self.frame_ashmanbot .frame_listmode.frame_2 .bind("<ButtonRelease-1>", self.stop_move) 
        self.frame_ashmanbot .frame_listmode.frame_2 .bind("<B1-Motion>", self.on_move) """

 

def main (): #------------------------------------------------------------NO TOCAR

    root = Root_class()
    root .title('AshmanBot')
    #root .geometry('0x0')
    #root .wm_attributes("-alpha", 0.0 )
    #app = Interface(root)
    #app .pack()    
    root .mainloop()

if __name__=="__main__":  #-------------------------------------------------------NO TOCAR 
    main()