
from Importaciones import *
#from A_frames import *
#from B_Frames import *


# INDICE:  NOMBRE:              TAREA:                                    : HEREDA DE:

# [ 1 ]  : A1FrameCls         : Botones: Ash y Gear                       : ( Frame )
# [ 2 ]  : DefaultButtonCls   : Opciones default para los 22 botones      : ( Button )
# [ 3 ]  : B1FrameCl          : Botones: 22                               : ( Frame )
# [ 4 ]  : B2FrameCls         : Labels y Checkbuttons                     : ( Frame )
# [ 5 ]  : B3FrameCls         : Spinbox y Listbox                         : ( Frame )
# [ 6 ]  : Checkbutton_class  : Sin uso eficiente                         : ( Checkbutton )
# [ 7 ]  : ResizeCls          : Redimensiona Imagenes                     : ( Frame )
# [ 8 ]  : TopIzqCls          : Ventana Izquierda                         : ( Frame )
# [ 9 ]  : TopDerCls          : Ventana Derecha                           : ( Frame )
# [ 10 ] : TopStufCls         : Ventana Stuff                             : ( Frame )
# [ 11 ] : MoveAllCls         : Mover Ventanas Globalmente                :
# [ 12 ] : FrameManagerCls    : Gestor de Ventanas                        : ( Frame )
# [ 13 ] : ToplevelCls        : Controla y mueve todas las Ventanas       : ( Toplevel )
# [ 14 ] : RootCls            : Inicializa la aplicacion                  : ( Tk )
# [ 15 ] : Interface          : Gestiona la aplicacion                    : ( Frame, MoveAllCls )

#********************************            ███████
#********************************        ██████   ██
#********************************        ██       ██
#********************************        ██████   ██
#********************************            ██   ██
#********************************            ██   ██
#********************************            ██   ██
#********************************            ██   ██
#********************************            ██   ██
#********************************            ██   ██
#********************************            ███████

# Frame Contenedor de los botones: Ash y Gear
class A1FrameCls(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        #_____C O N T E N E D O R E S:  [ 0 ]

        self.initializer_images()
        self.controllers()
        
    def controllers(self):  # Botones
        #____B U T T O N S:  [2]:  Logo y rueda
        self.btn_ash = Button (self, image=self.image_ash, bg='#11161d', bd=0, activebackground='#11161d' ,
                               command=self.minimize_windows)
        self.btn_gear = Button (self, image=self.image_gear1, bg='#11161d', bd=0, activebackground='#11161d',
                               command=self.master.gear_stacking)                               

        self.btn_ash .grid (column=0, row=0, padx=(6,6), pady=0)
        self.btn_gear .grid (column=0, row=1)

        #____B I N D ():
        self.btn_ash .bind ('<Double-Button-3>', self.close_windows)  # Cierra Toplevel Secundarias
        self.btn_gear.bind("<Enter>", self.change_image_gear1)
        self.btn_gear.bind("<Leave>", self.change_image_gear2)


    # Cierra las ventanas secundarias:
    def close_windows(self, event):   # ACTIVA: CON DOBLE CLICK DERECHO EN EL LOGO 
    
        try:
            self.master.toplevel_LEFT .destroy() 
            self.master._open_1 = False

            self.master.toplevel_RIGHT .destroy()
            self.master._open_2 = False

            self.master.toplevel_STUF .destroy()
            self.master._open_3 = False
        except: 
            pass
            
    # Minimiza las ventanas secundarias:
    def minimize_windows(self):   # ACTIVA: CON CLICK IZQUIERDO AL LOGO 
 
        if self.master._open_1 == True or self.master._open_2 == True or self.master._open_3 == True:

            # OCULTAR VENTANAS
            if not self.master._minimize:
                if self.master._open_1:  
                    #self.master.toplevel_LEFT .withdraw()                            # Esto distorciona el tamaño del icono en la barra de tareas, cuando el mouse se posiciona encima
                    self.master.toplevel_LEFT .frame_manager .minimize()              # Metodo de Toplevel_class

                if self.master._open_2:
                    self.master.toplevel_RIGHT .frame_manager .minimize()

                if self.master._open_3:
                    self.master.toplevel_STUF .frame_manager .minimize()

                self.master._minimize = True

            # MOSTRAR VENTANAS
            else:
                if self.master._open_1:
                    self.master.toplevel_LEFT .mapped_manager()                         # Metodo de Toplevel_class

                    x = self.master.toplevel_LEFT .winfo_x()                            # Aqui se pide la posicion x  de la ventana, evita que la ventana al minimizar se expanda : solucion temporal
                    y = self.master.toplevel_LEFT .winfo_y()
                    self.master.toplevel_LEFT .geometry('+{}+{}'.format(x,y))           # Remarcando la posicion , soluciona el redimensionamiento automatico interior

                if self.master._open_2:
                    self.master.toplevel_RIGHT .mapped_manager()

                    x = self.master.toplevel_RIGHT .winfo_x()
                    y = self.master.toplevel_RIGHT .winfo_y()
                    self.master.toplevel_RIGHT .geometry('+{}+{}'.format(x,y))

                if self.master._open_3:
                    self.master.toplevel_STUF .mapped_manager()

                    x = self.master.toplevel_STUF .winfo_x()
                    y = self.master.toplevel_STUF .winfo_y()
                    self.master.toplevel_STUF .geometry('+{}+{}'.format(x,y))

                self.master._minimize = False
   

    # Cambia la imagen al pasar el mouse sobre el boton:
    def change_image_gear1(self, event):   
        event.widget.config(image=self.image_gear2) 

    # Deja la imagen que estaba por defecto:
    def change_image_gear2(self, event):
        event.widget.config(image=self.image_gear1)

    
    def initializer_images(self):
        ash = Image.open('E:/1-RICHI/MovilesDB/SubList__00.jpg')
        gear1 = Image.open('E:/1-RICHI/MovilesDB/SubList__01.jpg')
        gear2 = Image.open('E:/1-RICHI/MovilesDB/SubList__03.jpg')
        
        self.image_ash = ImageTk.PhotoImage(ash)
        self.image_gear1 = ImageTk.PhotoImage(gear1)
        self.image_gear2 = ImageTk.PhotoImage(gear2)


#********************************        ██████████████
#********************************        ██          ██
#********************************        ██████████  ██
#********************************                ██  ██
#********************************        ██████████  ██
#********************************        ██          ██
#********************************        ██  ██████████
#********************************        ██  ██
#********************************        ██  ██████████
#********************************        ██          ██
#********************************        ██████████████

# Se encarga de:
# 1- Servir de molde para crear los botones con la configuacion que se desea
class DefaultButtonCls(Button):
    def __init__(self, master, *args, **kwargs):
        kwargs = {"font":('Calibri',9,'bold'), 'bg': '#11161d', 'fg':'white', 'activebackground':'#bdfe04', 'width':10, 'bd':0, **kwargs}
        super().__init__(master, *args, **kwargs)


#********************************        ██████████████
#********************************        ██          ██
#********************************        ██████████  ██
#********************************                ██  ██
#********************************        ██████████  ██
#********************************        ██          ██
#********************************        ██████████  ██
#********************************                ██  ██
#********************************        ██████████  ██
#********************************        ██          ██
#********************************        ██████████████

# Se encarga de:
# 1- Crear los 22 botones
# 2- Abrir las Ventanas Secundarias con los indices que se indican
class B1FrameCls(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        #_____C O N T E N E D O R E S:   [ 1 ]
        self.frame_1 = Frame (self, bg='#11161d')          # Color: Azul '#11161d'
        self.frame_1 .grid (padx=(10,10), pady=(6,6))

        #_____Métodos Llamados:
        self.creator_buttons()

        #_____Variables de Control para los Botones
        self.container1 = None


    # Manda los indices para abrir las imagenes en las ventanas:
    def indices(self, indice):
        # I N D I C E S :
        arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, = 0, 1, 2, 3, 4, 5, 6, 7 

        return  lambda: self.master.windows_123(
                lambda top1: TopIzqCls  (top1, indice, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, self.master.path_lst, self.master.path_mini),
                lambda top2: TopDerCls  (top2, indice, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, self.master.path_lst, self.master.path_mini),
                lambda top3: TopStufCls (top3, indice, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, self.master.path_lst, self.master.path_mini), indice)

        
    # Crea los 22 botones y las posiciona:
    def creator_buttons(self):  
        mobiles = [['Frog', 'Fox', 'Boomer', 'Ice', 'J.d', 'Grub', 'Lightning', 'Aduka', 'Knight', 'Kalsiddon', 'Mage'],
                   ['Randomizer', 'Jolteon', 'Turtle', 'Armor', 'A.sate', 'Raon', 'Trico', 'Nak', 'Bigfoot', 'Barney', 'Dragon']]                  
        self.mobiles2 = ['Fox','Knight','Jolteon','Barney','Dragon'] 

        self.buttons22 = []                                     # Lista: Sirve para condicionar las funciones vinculadas a eventos: bind -->  mouse_move, mouse_stop, mouse_clic  
        for index1, mobil in enumerate(mobiles):                # Iterador: (mobil) = 11 elementos: 1 sublistasssss
            for index2, texto in enumerate(mobil):              # Iterador: (texto) = 1  elemento:  'Frog'
                number = 11 if index1 == 1 else 0               # number: cambie su valor de 0 a 11 si su condicion se cumple

                btn = DefaultButtonCls (self.frame_1, text=texto, command= self.indices(index2 + number))             
                n1 = 5 if index2 == 0 else 0        
                n2 = 5 if index2 == 10 else 0
                btn .grid(column=index2 , row=index1 , pady=3, padx=(n1,n2))

                btn.bind("<Enter>", self.enter_mouse)
                btn.bind("<Leave>", self.leave_mouse)
                btn.bind("<ButtonPress-1>", self.press_mouse)
                btn.bind("<ButtonRelease-1>", self.release_mouse)            

                if texto in self.mobiles2: btn.config(fg='yellow')
                self.buttons22.append(btn)   # Examinar si borrar porque no tiene uso la lista



    # TAREA:
    #   1- Cambia el color del boton al pasar el mouse sobre el
    def enter_mouse(self, event):
        if not event.widget .cget('bg') == '#bdfe04':           # -1  
            event.widget .config(bg="#24364a")                   # >>>>
        
        # 1-  Si el color del boton sobre el que se posa el mouse, NO ES VERDE :▼▼▼▼
            # >>>>   Cambia el color del boton a un --> [ CELESTE APAGADO ]

    
    # TAREA:
    #   1- Cambia el color del boton al salir el mouse de el
    def leave_mouse(self, event):
        if not event.widget .cget('bg') == '#bdfe04':            # -1
            event.widget.config(bg='#11161d')                     # >>>>

        # 1-  Si el color de fondo del boton desde donde sale el mouse, NO ES VERDE :▼▼▼▼
            # >>>>   Cambia el color del boton a un --> [ AZULINO DEFAULT ]


    # TAREA:
    #   1- Cambia el color del boton presionado actual a [VERDE-NEGRO]
    def press_mouse(self, event):
        widget_press = event.widget                                            # -1
        widget_press .config(bg='#bdfe04', fg='black')                         # -2
                     
        for btn in (self.buttons22):
            if btn != widget_press:
                if btn .cget('text') in self.mobiles2:
                    btn .config (bg='#11161d', fg='yellow')
                else:
                    btn .config (bg='#11161d', fg='white') 

        self.container1 = widget_press                                         # -4

        # 1-  Atrapa al boton clickeado [ Nombre ]
        # 2-  Cambia el background y foreground del boton clikeado a un --> [ VERDE - NEGRO ]

        # 3-  Si [self.container1 = boton clickeado anterior] deja de ser [None] y es diferente al boton clickeado actual :▼▼▼▼
            # 3.1-  [self.container1 = boton clickeado anterior] tiene de texto algunas de las cadenas de la lista, self.mobiles2 :▼▼▼▼
                # >>>>  Cambia el background y foreground del boton clikeado anterior a un --> [ AZULINO - AMARILLO ]
            # 3.2-  Entonces :▼▼▼▼
                # >>>>  Cambia el background y foreground del boton clikeado anterior a un --> [ AZULINO - BLANCO ]
        
        # 4-  Almacena el boton actual en una variable   


    # TAREA:
    #   1- Cambia el color del boton presionado actual a DEFAULT, si no coincide con el mismo boton presionado
    def release_mouse(self, event):
        widget_press = event.widget                                                 # -1
        widget_release = event.widget.winfo_containing(event.x_root, event.y_root)  # -2

        if widget_press != widget_release:                                          # -3

            if widget_press .cget('text') in self.mobiles2:                          # -3.1
                widget_press .config (bg='#11161d', fg='yellow')                      # >>>>
            else:                                                                    # -3.2
                widget_press .config (bg='#11161d', fg='white')                       # >>>>

        # 1-  Boton clikeado actual, [event.widget lo atrapa x alguna razon que no es muy clara]
        # 2-  Atrapa al widget sobre el que se solto el clic izquierdo [ Nombre del widget ]
        # 3-  Si boton clikeado actual, es diferente al widget sobre el que se solto el clic :▼▼▼▼

            # 3.1-  Si el boton clikeado tiene de texto algunas de las cadenas de la lista; self.mobiles2 :▼▼▼▼
                # >>>>  Cambia el background y foreground del boton clikeado actual a un --> [ AZULINO - AMARILLO ]
            # 3.2-  Entonces :▼▼▼▼
                # >>>>  Cambia el background y foreground del boton clikeado actual a un --> [ AZULINO - BLANCO ]


    # Deja el color como estaba por defecto
    def uncheck_selection(self):
        if self.container1 is not None:
            if self.container1 .cget('text') in self.mobiles2:
                self.container1 .config (bg='#11161d', fg='yellow')         # Cambia el color del boton: (bg y fg) que tenian por defecto
            else:
                self.container1 .config (bg='#11161d', fg='white')          # Cambia el color del boton: (bg y fg) que tenian por defecto
        self.container1 = None


#********************************        ██████  ██████
#********************************        ██  ██  ██  ██
#********************************        ██  ██  ██  ██
#********************************        ██  ██  ██  ██
#********************************        ██  ██████  ██
#********************************        ██          ██
#********************************        ██████████  ██
#********************************                ██  ██
#********************************                ██  ██
#********************************                ██  ██
#********************************                ██████

# Frame contenedor de checkbuttons y labels
class B2FrameCls(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, kwargs)

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
        label_option2 = Label (self, text= 'Modo Lista :', font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)
        label_option3 = Label (self, text= 'Activar ddd ', font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)
        label_option4 = Label (self, text= 'Activar Modo On :', font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)
        label_option5 = Label (self, text= 'Activar Modo Lista :', font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)
        label_option6 = Label (self, text= 'Activar Modo Guía :', font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)
        label_option7 = Label (self, text= 'Desactivar Movimiento :', font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)
        label_option8 = Label (self, text= 'Guargar Configuracion :', font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)

        label_option1 .grid (column=0, row=0, padx= (30,5), pady=(10,0), sticky=W)
        label_option2 .grid (column=0, row=1, padx= (30,5), pady=(0,0), sticky=W)
        label_option3 .grid (column=2, row=0, padx= (30,5), pady=(10,0), sticky=W)
        label_option4 .grid (column=2, row=1, padx= (30,5), pady=(0,0), sticky=W)
        label_option5 .grid (column=4, row=0, padx= (30,5), pady=(10,0), sticky=W)
        label_option6 .grid (column=4, row=1, padx= (30,5), pady=(0,0), sticky=W)   
        label_option7 .grid (column=6, row=0, padx= (30,5), pady=(10,0), sticky=W)
        label_option8 .grid (column=6, row=1, padx= (30,5), pady=(0,0), sticky=W)
        
    
    def create_checkbutton(self):

        self.ckbutton1 = Checkbutton_class (self, bg='#31343a', activebackground= '#31343a', bd=0, borderwidth=0,)
        self.ckbutton2 = Checkbutton_class (self, bg='#31343a', activebackground= '#31343a', bd=0, borderwidth=0,)
        self.ckbutton3 = Checkbutton_class (self, bg='#31343a', activebackground= '#31343a', bd=0, borderwidth=0,)
        self.ckbutton4 = Checkbutton_class (self, bg='#31343a', activebackground= '#31343a', bd=0, borderwidth=0,)
        self.ckbutton5 = Checkbutton_class (self, bg='#31343a', activebackground= '#31343a', bd=0, borderwidth=0,)
        self.ckbutton6 = Checkbutton_class (self, bg='#31343a', activebackground= '#31343a', bd=0, borderwidth=0,)
        self.ckbutton7 = Checkbutton_class (self, bg='#31343a', activebackground= '#31343a', bd=0, borderwidth=0,)
        self.ckbutton8 = Checkbutton_class (self, bg='#31343a', activebackground= '#31343a', bd=0, borderwidth=0,)
    
        self.ckbutton1 .grid (column=1, row=0, pady=(10,0))
        self.ckbutton2 .grid (column=1, row=1, pady=(0,0))
        self.ckbutton3 .grid (column=3, row=0, pady=(10,0))
        self.ckbutton4 .grid (column=3, row=1, pady=(0,0))
        self.ckbutton5 .grid (column=5, row=0, pady=(10,0))
        self.ckbutton6 .grid (column=5, row=1, pady=(0,0))
        self.ckbutton7 .grid (column=7, row=0, padx=(0,200), pady=(10,0),)
        self.ckbutton8 .grid (column=7, row=1, padx=(0,200), pady=(0,0),)


#********************************        ██████████████
#********************************        ██          ██
#********************************        ██  ██████████
#********************************        ██  ██        
#********************************        ██  ██████████
#********************************        ██          ██
#********************************        ██████████  ██
#********************************                ██  ██
#********************************        ██████████  ██
#********************************        ██          ██
#********************************        ██████████████

# Frame Contenedor de Spinbox y Listbox
class B3FrameCls(Frame):
    def __init__(self, master, path_lst,  *args, **kwargs):
        super().__init__(master, *args, kwargs)

        #_____Coleccion de imagenes  
        self.Miniatures = path_lst

        #_____C O N T E N E D O R E S:   [ 2 ]
        self.frame_1 = Frame (self, bg='#31343a', width=116, height=67)    # Color: Plomo       
        self.frame_2 = Frame (self, bg='#11161d', width=60, height=67)     # Color: Azul  

        self.container_2w = Frame (self.frame_1, width=116, height=20, bg='#11161d')
        self.select_mobil = Label (self.frame_1, text='Seleccione  Mobil :', font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)
        self.miniature_mobil = Label (self.frame_2, image=self.Miniatures[0], bd= 0)

        self.create_listbox (width=11, height=1)
        self.create_spinbox (width=13)

        #_____G R I D ():
        self.frame_1 .grid (column=0, row=0)                                            # MASTER A
        self.frame_2 .grid (column=1, row=0)                                            # MASTER B

        self.container_2w .grid (column=0, row=0, padx=0, pady=(0,2), sticky=N)         # SUB A.1
        self.select_mobil .grid (column=0, row=1, padx=11, pady=0)                      # SUB A.2
        self.spinboxx .grid (column=0, row=2, padx=13, pady=(3,3))                      # SUB A.3

        self.lbl_toggle .grid (column=0, row=0, padx=0, pady=0)                          # SUB.SUB A.1 .1 
        self.listboxx .grid (column=1, row=0, padx=12, pady=(1,0))                      # SUB.SUB A.1 .2

        self.miniature_mobil .grid (padx=2, pady=3)                                     # SUB B.1

        #_____G R I D___P R O P A G A T E ():
        self.frame_1 .grid_propagate(False)
        self.frame_2 .grid_propagate(False)
        self.container_2w .grid_propagate(False)
        
        #_____V A R I A B L E S  DE  C O N T R O L: 
        self._toggle_switch = False
   

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

        self.open_windows()


    def listbox_enter(self, event):  # ACTIVA: CON TECLA ENTER - INSERTA EL VALOR DE LISTBOX A SPINBOX, MANDA LLAMAR A OPEN_WINDOWS  Y ABREN LAS VENTANAS 
        listbx = self.listboxx.get(0)
        spinbx = self.spinboxx.get()

        if listbx != spinbx and listbx != '':
            self.spinboxx.delete(0, END)
            self.spinboxx.insert(0, listbx)
   
        self.open_windows() 
         
    def open_windows(self, event=None):  # ACTIVA: ** SI ES LLAMADO POR LISTBOX_SELECT ** - ABRE LAS VENTANAS
        # I N D I C E S :
        arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, = 0, 1, 2, 3, 4, 5, 6, 7 

        for index, i in enumerate(self.spinbox_values):     
            if self.spinbox_variable.get() == i:            # ANTES DABA ERROR CON: self.spinboxx .!toplvel.!frame,etc
                self.master.windows_123(
                lambda top1: TopIzqCls  (top1, index, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, self.master.path_lst, self.master.path_mini),
                lambda top2: TopDerCls  (top2, index, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, self.master.path_lst, self.master.path_mini),
                lambda top3: TopStufCls (top3, index, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, self.master.path_lst, self.master.path_mini), index)
                break                                       # Sin breack el programa seguiria buscando coincidencias despues del enter, y guardaria un error
        


        #self.after_cancel(self.fter)            
        if self._toggle_switch == True:  # almacena todas las llamadas si se da enter
            print(4444)
           
            #self.fter = self.after(4000, self.automatic_deletion) 
            #print(self.master.master.master.a)

    def automatic_deletion(self):  # ACTIVA: ** SI ES LLAMADO POR OPEN_WINDOWS ** Y SI LA VARIABLE DE CONTROL NO ES NONE - LIMPIA SPINBOX
        self.spinboxx .delete(0, END)





    def change_toggle(self, event=None):  # ACTIVA: CLICK IZQUIERDO EN RED_GREEN - CAMBIA IMAGEN ROJO-VERDE Y VICEVERSA
        if not self._toggle_switch == True:                                                     # -1
            self._toggle_switch = True                                                          # >>>>
            self.lbl_toggle .config(image=self.Miniatures[24])                                  # >>>>
            self.unbind('',self.master.off_move)                                                # >>>>
            
            # 1- Si self._switch es False :▼▼▼▼   [ Predeterminado False ]
                # 1.1-  Asiga self._switch = True
                # 1.2-  Cambia la imagen en el label por el color verde
                # 1.3-  Desactiva el enlace self.on_move_all
   
        else:                                                                                   # -1
            self._toggle_switch = False                                                         # >>>>
            self.lbl_toggle .config (image=self.Miniatures[23])                                 # >>>>
            self.master.off_move = self.bind_all("<B1-Motion>", self.master.on_move_all)        # >>>>

            # 1- Entonces si self._switch es True :▼▼▼▼
                # >>>>  Asiga self._switch = False
                # >>>>  Cambia la imagen en el label por el color rojo
                # >>>>  Activa el enlace self.on_move_all


    def validate_text(self, text, arg): # SIEMPRE QUE INSERTE TEXTO EN SPINBOX - NO PERMITE NUMEROS,SIMBOLOS,ESPACIOS Y CONTROLA LA CANTIDAD
        if all (i not in "0123456789[{!¡¿?<>(|#$%&),_-°'´}] +-*/=" for i in text) and len(text) < 14:   
                return True                                                 
        return False  

    def create_spinbox(self, **args):        
        self.spinboxx = Spinbox (self.frame_1, **args)
        
        self.spinbox_variable = StringVar()
        self.spinbox_values = ['Frog', 'Fox', 'Boomer', 'Ice', 'J.d', 'Grub', 'Lightning', 'Aduka', 'Knight', 'Kalsiddon', 'Mage',
                               'Randomizer', 'Jolteon', 'Turtle', 'Armor','A.sate', 'Raon', 'Trico', 'Nak', 'Bigfoot', 'Barney', 'Dragon']
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
        self.lbl_toggle = Label (self.container_2w, image= self.Miniatures[23], width=11, bd=0, cursor="hand2") 

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

        self.lbl_toggle .bind ("<Button-1>", self.change_toggle)
        self.listboxx .bind ('<<ListboxSelect>>', self.listbox_select)   # ACTIVA: CON CLICK IZQUIERDO EN EL LISTBOX - SELECCIONA 1 ITEM


#********************************        ██████████████
#********************************        ██          ██
#********************************        ██  ██████████
#********************************        ██  ██        
#********************************        ██  ██████████
#********************************        ██          ██
#********************************        ██  ██████  ██
#********************************        ██  ██  ██  ██
#********************************        ██  ██████  ██
#********************************        ██          ██
#********************************        ██████████████

# Frame Contenedor de Checkbutton
class Checkbutton_class(Checkbutton):   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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
 

#********************************        ██████████████
#********************************        ██          ██
#********************************        ██████████  ██
#********************************                ██  ██
#********************************                ██  ██
#********************************                ██  ██
#********************************                ██  ██
#********************************                ██  ██
#********************************                ██  ██
#********************************                ██  ██
#********************************                ██████

# Se encarga de:
# 1- Redimensionar las imagenes que le pasan:
class ResizeCls(Frame):
    def __init__(self, master, index, *args, **kwargs):
        super().__init__(master, *args, kwargs)
        
        #self.image = Image.fromarray(index)
        self.image = Image.open(index)
        self.image_copy = self.image .copy()

        self.background = ImageTk.PhotoImage(self.image)

        self.img = Label(self, image=self.background)

        # Opciones de empaquetamiento:
        self.img .pack(fill='both', expand=True)
        #self.img .grid(sticky='nwse')
        #self.img .grid_propagate(0)

        self.img .bind('<Configure>', self.resize)

    def resize(self, event):
        
        self.image2 = self.image_copy .resize((self.master.winfo_width(), self.master.winfo_height()))
        
        self.background2 = ImageTk.PhotoImage(self.image2)
        self.img .config(image=self.background2)
        #self.img .image = self.background


#********************************        ██████████████        *********************************
#********************************        ██          ██        *********************************
#********************************        ██  ██████  ██        *********************************
#********************************        ██  ██  ██  ██        *********************************
#********************************        ██  ██████  ██        *********************************
#********************************        ██          ██        *********************************
#********************************        ██  ██████  ██        *********************************
#********************************        ██  ██  ██  ██        *********************************
#********************************        ██  ██████  ██        *********************************
#********************************        ██          ██        *********************************
#********************************        ██████████████        *********************************

# index1 = Minilista de imagenes, cada mobil tiene su propia lista

#____V E N T A N A___I Z Q U I E R D A:
class TopIzqCls(Frame):
    def __init__(self, master, indice, arg_0=None, arg_1=None, arg_2=None, arg_3=None, arg_4=None, arg_5=None, arg_6=None, arg_7=None, path_lst=None, path_mini=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.x1 = 0
        self.x2 = 100
        self.y1 = 0
        self.y2 = 7

        self.frame_controller               = Frame(self.master.frame_control, bg='#2f3337')
        self.frame_controller                 .grid (column=0, row=0)

        # Imagen: Delay completo del mobil
        self.frame_image_delay_complete = ResizeCls(self, path_lst[indice][arg_0], bd=0)
        self.frame_image_delay_complete       .grid (column=0, row=0)

        # Imagen: Miniatura del mobil para ayudar a medir las distancias
        self.frame_image_mobil_tutorial = ResizeCls(self, path_lst[indice][arg_1], bd=0)
        self.frame_image_mobil_tutorial       .grid (column=0, row=0)                            # [ NO POSICIONADO ]

    # Texto: "Guia", para abrir la Miniatura del mobil 
        #self.master.frame_control.pack()

        """ self.frame_controller               = Frame(self, bg='#2f3337')
        self.frame_controller                 .pack ()  """ 

        self.lbl_change1 = Label(self.frame_controller, image=path_mini[26], width=00,height=0, bg='black', cursor="hand2")
        self.lbl_change1   .grid( column=0, row=0, padx=10)
        self.lbl_change1   .bind('<Button-1>', self.open_image_miniature)

        self.lbl_change2 = Label(self.frame_controller, image=path_mini[25], width=00,height=0, bg='black', cursor="hand2")
        self.lbl_change2   .grid( column=1, row=0, padx=10)
        self.lbl_change2   .bind('<Button-1>', self.open_image_miniature)
        

        if indice == 17:

            self.lbl_change3 = Label (self.frame_controller, text='33', bg='green', height=1, cursor="hand2")
            self.lbl_change3 .grid( column=2, row=0, padx=10)
            self.lbl_change3 .bind('<Button-1>', self.open_image_miniature)

            self.lbl_change4 = Label (self.frame_controller, text='44', bg='green', cursor="hand2")
            self.lbl_change4 .grid( column=3, row=0, padx=10)
            self.lbl_change4 .bind('<Button-1>', self.open_image_miniature)


        # Widgets No Posicionados:
        self.frame_image_mobil_tutorial .grid_remove()
        #self.frame_controller .pack_forget()

        # Evento: Para posicionar el label[text= Guia]
        #self.bind ('<Configure>', self.new_position_text_guia)


        self.bind_motion = self.master.bind('<Motion>',self.open_text_mostrar_77)
        self.bind_leave = self.bind('<Leave>', lambda arg: self.frame_controller .grid_remove())
        



        self._motion_1 = False


        # Configuracion de la Ventana:
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        """ self.frame_controller.columnconfigure(0, weight=0)
        self.frame_controller.rowconfigure(0, weight=0) """

        """ self.frame_image_delay_complete .columnconfigure(0, weight=1)

        #self.frame_image_delay_complete .rowconfigure(0, weight=0)
        self.frame_image_delay_complete .rowconfigure(1, weight=1) """


    #___< C O N F I G U R E > :
    # Tarea: Posicionar el label[text= Guia] que abre la miniatura del mobil
    def new_position_text_guia(self, event):  
        #self.a=1.17
        toplevel_width  = self.master.winfo_width() / 1.17        # winfo_width() : Devuelve el ancho actual del widget(Toplevel) en pixeles, podria usar _reqwidth() que siempre esta actualizado.
        toplevel_height = self.master.winfo_height() / 13.5
        x = int (toplevel_width)
        y = int (toplevel_height)    

        self.lbl_text_guia .place(x=x, y=y)

        if y < 49:
            self.lbl_text_guia .config(font=('Calibri',7,'bold'))
        #elif y < 40:
        #    self.self.lbl_text_guia .config(font=('Calibri',6,'bold'))  # NO FUNCIONA
        else:
            self.lbl_text_guia .config(font=('Calibri',8,'bold'))


    #___< B U T T O N - 1 > :
    # Tarea: Abrir la minuatura del mobil 
    def open_image_miniature(self, event): 

        if self.frame_image_mobil_tutorial .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.frame_image_mobil_tutorial .grid()
        else:
            self.frame_image_mobil_tutorial .grid_remove()



    #___< M O T I O N > :
    def open_text_mostrar_77(self, event):
 
        self.pointer_width_2  = event.x / self.master.winfo_width() * 100
        self.pointer_height_2 = event.y / self.master.winfo_height() * 100
        
        if not self._motion_1 == True:

            if self.x1 <(self.pointer_width_2)< self.x2  and  self.y1 <(self.pointer_height_2)< self.y2: 
                #self.master.frame_control .config(bg='red', width=0, height=0)   
                self.frame_controller .grid()
                #self.grid_rowconfigure(0, weight=0)
            else:
                self.frame_controller .grid_remove()
                #self.grid_rowconfigure(0, weight=1)

        """ if self.frame_image_base_77 .grid_info() != {}:   # == {} (no mapeado) 
            self.lbl_text_mostrar_77     .grid_remove() """


#********************************        ██████████████        *********************************
#********************************        ██          ██        *********************************
#********************************        ██  ██████  ██        *********************************
#********************************        ██  ██  ██  ██        *********************************
#********************************        ██  ██████  ██        *********************************
#********************************        ██          ██        *********************************
#********************************        ██████████  ██        *********************************
#********************************                ██  ██        *********************************
#********************************        ██████████  ██        *********************************
#********************************        ██          ██        *********************************
#********************************        ██████████████        *********************************

#____V E N T A N A___D E R E C H A:
class TopDerCls(Frame):
    def __init__(self, master, indice, arg_0=None, arg_1=None, arg_2=None, arg_3=None, arg_4=None, arg_5=None, arg_6=None, arg_7=None, path_lst=None, path_mine=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        # Variables de Control para mostrar la imagen del angulo 77:
        self.x1 = 0
        self.x2 = 100
        self.y1 = 67
        self.y2 = 100

        # Imagen: Base inicial del mobil:
        self.frame_image_base_initial = ResizeCls (self, path_lst [indice][arg_2], bd=0)
        self.frame_image_base_initial       .grid (column=0, row=0, sticky='news')
        self.frame_image_base_initial       .grid_propagate(0)

        # Imagen: Base 77 del mobil:
        self.frame_image_base_77      = ResizeCls (self, path_lst [indice][arg_3], bd=0)
        self.frame_image_base_77            .grid(column=0, row=0, sticky='news')                  # [ NO POSICIONADO ]

        # Texto: "Haga click" para mostrar el angulo 77" :  -->  Cambia la imagen a la base 77 del mobil:
        self.lbl_text_mostrar_77          = Label (self, text="Haga ' Click ' para mostrar:\nAngulo ' 77 '", font=('Bickham Script Pro',8,'bold'), bg='#2f3337', fg='white', width=50, height=2)
        self.lbl_text_mostrar_77            .grid (column=0, row=0, ipadx=5, ipady=5, sticky=N,)   # [ NO POSICIONADO ]

        # Texto: "↑":  -->  Se dibuja si aparece la imagen [base 77] del mobil:
        self.lbl_text_flecha              = Label (self, text='↑', font=('Calibri',30,'bold'), bg='#2f3337', fg='green2', width=1, height=1)
        self.lbl_text_flecha                .grid (column=0, row=0, ipadx=5, sticky=SE)            # [ NO POSICIONADO ]

        # Widget No Posicionados:
        self.frame_image_base_77 .grid_remove() 
        self.lbl_text_mostrar_77 .grid_remove()
        self.lbl_text_flecha     .grid_remove()

        # Eventos Enlazados:
            # Enlace: Posiciona/Quita   el Label [texto: "↑"]
        self.master.bind("<Button-1>", self.open_text_flecha)
        
            # Enlace:      
        self.bind_motion = self.master.bind('<Motion>',self.open_text_mostrar_77)

            # Enlace: Quita el Label [texto: "Haga click" para mostrar el angulo 77"]:
        self.bind_leave = self.bind('<Leave>', lambda arg: self.lbl_text_mostrar_77 .grid_remove())   


        #____Variables de Control para los Eventos Enlazados:
        self._button_1 = False  # Creado para el evento: Button-1
        self._motion_1 = False  # Creado para el evento: Motion
        

        # Configuración de la ventana:    
        #self.columnconfigure (0,weight=1)
        #self.rowconfigure    (0,weight=1)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_image_base_initial. columnconfigure(0, weight=1)
        self.frame_image_base_initial. rowconfigure(0, weight=1)

        self.frame_image_base_77. columnconfigure(0, weight=1)
        self.frame_image_base_77. rowconfigure(0, weight=1)
        
    
    #___< B U T T O N - 1 > :
    def open_text_flecha(self, event): 

        # Convierte el tamaño total de la ventana en porcentaje:  100 %
        self.porcentage_total_x = event.x / self.master.winfo_width() * 100              # ---> winfo_width() : Devuelve el ancho actual del widget(Toplevel) en pixeles
        self.porcentage_total_y = event.y / self.master.winfo_height() * 100             # ---> event.x/y     : Devuelve la posicion del mouse en pixeles (click/movimiento)
      
        if self.x1 <(self.porcentage_total_x)< self.x2  and  self.y1 <(self.porcentage_total_y)< self.y2: 

            if not self._button_1 == True:    # Si es Falso:   ---> Predeterminado: False
                self._button_1 = True
                self._motion_1 = True

                self.frame_image_base_77 .grid()                     # Posiciona
                self.lbl_text_mostrar_77 .grid_remove()
                self.lbl_text_flecha     .grid()                     # VER SI ACEPTA VARIABLES

            else:
                self._button_1 = False
                self._motion_1 = False

                self.frame_image_base_77 .grid_remove()
                self.lbl_text_mostrar_77 .grid()
                self.lbl_text_flecha     .grid_remove()



    #___< M O T I O N > :
    def open_text_mostrar_77(self, event):      
 
        self.pointer_width_2  = event.x / self.master.winfo_width() * 100
        self.pointer_height_2 = event.y / self.master.winfo_height() * 100
        
        if not self._motion_1 == True: 

            if self.x1 <(self.pointer_width_2)< self.x2  and  self.y1 <(self.pointer_height_2)< self.y2:    
                self.lbl_text_mostrar_77 .grid()

            else:
                self.lbl_text_mostrar_77 .grid_remove()

        if self.frame_image_base_77 .grid_info() != {}:   # == {} (no mapeado) 
            self.lbl_text_mostrar_77     .grid_remove()



#************************            ███████    ██████████████        *************************
#************************        ██████   ██    ██          ██        *************************
#************************        ██       ██    ██  ██████  ██        *************************
#************************        ██████   ██    ██  ██  ██  ██        *************************
#************************            ██   ██    ██  ██  ██  ██        *************************
#************************            ██   ██    ██  ██  ██  ██        *************************
#************************            ██   ██    ██  ██  ██  ██        *************************
#************************            ██   ██    ██  ██  ██  ██        *************************
#************************            ██   ██    ██  ██████  ██        *************************
#************************            ██   ██    ██          ██        *************************
#************************            ███████    ██████████████        *************************

#____V E N T A N A___S T U F:
class TopStufCls(Frame):
    def __init__(self, master, indice, arg_0=None, arg_1=None, arg_2=None, arg_3=None, arg_4=None, arg_5=None, arg_6=None, arg_7=None, path_lst=None, path_mine=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        pass
        
        """ if len(path_lst) > index_1:
            self.img = ResizeCls (self, path_lst [index_1])
            self.img.grid(column=0, row=0, sticky='news')
        
        if len(path_lst) > index_2:
            self.img2 = ResizeCls (self, path_lst [index_2])
            self.img2.grid(column=0, row=1, sticky='news') """

        # column 0 will use full width
        ##self.grid_columnconfigure(0, weight=1)
        # row 0 will use 1/2 height AND row 1 will use 1/2 height
        ##self.grid_rowconfigure(0, weight=1)     
        ##elf.grid_rowconfigure(1, weight=1)


#************************            ███████          ███████
#************************        ██████   ██      ██████   ██
#************************        ██       ██      ██       ██
#************************        ██████   ██      ██████   ██
#************************            ██   ██          ██   ██
#************************            ██   ██          ██   ██
#************************            ██   ██          ██   ██
#************************            ██   ██          ██   ██
#************************            ██   ██          ██   ██
#************************            ██   ██          ██   ██
#************************            ███████          ███████

# TAREAS:
#_______1- Mover todas las ventanas a excepcion de root, sin importar donde se de clic, existen algunas excepciones
class MoveAllCls():
    def __init__(self):
        self._x = 0
        self._y = 0
        self.movable = []
          
    def make_movable(self, *widgets):
        self.movable.extend(widgets)
        
    def is_movable(self, widget):
        return widget in self.movable
    
    def start_move_all(self, event):        
        self._x = event.x
        self._y = event.y
   
    def stop_move_all(self, event):
        self._x = None
        self._y = None

    def on_move_all(self, event):
        deltax = event.x - self._x
        deltay = event.y - self._y     
        _event = event.widget
        _tops = event.widget.winfo_toplevel()

        new_position = "+{}+{}".format (_tops.winfo_x() + deltax, _tops.winfo_y() + deltay)
        
        if not isinstance(_event, (Button, ttk.Sizegrip, Spinbox)) == True or self.is_movable(_event):                 # NOTA: self._is_movable(_event): Devuelve True 
            _tops.geometry(new_position)                                                                      # Mueve todas las ventanas en general menos root 

        if isinstance(_tops.master, Tk)== True and not isinstance(_event, (Button, ttk.Sizegrip, Spinbox)) or self.is_movable(_event):                                                           # otro: if _tops.master == RootCls:
            _tops.master.geometry(new_position)                                                               # Mueve la ventana root


#************************            ███████    ██████████████
#************************        ██████   ██    ██          ██
#************************        ██       ██    ██████████  ██
#************************        ██████   ██            ██  ██
#************************            ██   ██    ██████████  ██
#************************            ██   ██    ██          ██
#************************            ██   ██    ██  ██████████
#************************            ██   ██    ██  ██        
#************************            ██   ██    ██  ██████████
#************************            ██   ██    ██          ██
#************************            ███████    ██████████████

class FrameManagerCls(Frame):
    def __init__(self, master=None, listmode=None, **kwargs):
        super().__init__(master, **kwargs)
        self.listmode = listmode

        #___Métodos Llamados:
        self.initializer_images()
        self.creator_buttons()


    def creator_buttons(self):
        #___Botones: [Cerrar - Minimizar]
        self.button_close = Button(self, image=self.image_close1, command=self.close, bd=0, bg='black', activebackground='black')
        self.button_minimize = Button(self, image=self.image_minimize1, command=self.minimize, bd=0, bg='black', activebackground='black')

        self.button_close .pack(self.listmode [0])       # Orientacion del boton en el frame: Principal: (side=TOP, pady=7)    Secundario: (side=RIGHT) 
        self.button_minimize .pack(self.listmode [1])    # Orientacion del boton en el frame: Principal: (side=BOTTOM, pady=7) Secundario: (side=RIGHT, padx=10)            

        #___Enlaces: Cambian la imagen de los botones
        self.button_close.bind("<Enter>", self.change_image_close1)
        self.button_close.bind("<Leave>", self.change_image_close2)

        self.button_minimize.bind("<Enter>", self.change_image_mini1)
        self.button_minimize.bind("<Leave>", self.change_image_mini2)


    def change_image_close1(self, event):   # Cambia el color al pasar el mouse sobre el      # Color: Celeste apagado
        event.widget.config(image=self.image_close2)

    def change_image_close2(self, event):   # Deja el color como estaba por defecto           # Color: Azul oscuro
        event.widget.config(image=self.image_close1)
   
    def change_image_mini1(self, event):    # Deja el color como estaba por defecto           # Color: Azul oscuro
        event.widget.config(image=self.image_minimize2)

    def change_image_mini2(self, event):    # Deja el color como estaba por defecto           # Color: Azul oscuro
        event.widget.config(image=self.image_minimize1)


    def close(self):     # SOLUCIONAR SI QUEDAN PROCESOS ABIERTOS POR USO INADECUADO DE QUIT()
        # Cerrar:    Toplevel Principal [ Default ]
        if len(self.listmode) < 3:
            self.master.quit()                       # YO LO PUSE , utilidad por informarse todavia
            self.master.destroy()                    # Destruye Toplevel Principal
            self.master.master.destroy()             # Destruye root

        # Cerrar:    Toplevel Secundarios
        else:
            self.master.destroy()                    # Destruye Toplevel Secundarios
            #self.master.quit()                      # Elimina toda la aplicacion cuando hay 1 sola mainlopp()

    def minimize(self):
        # Minimiza:  Toplevel Principal [ Default ]
        if len(self.listmode) < 3:
            self.master.withdraw()                   # Oculta Toplevel Principal
            self.master.master .iconify()            # Iconiza root
        
        # Minimiza:  Toplevel Secundarios
        else:
            self.master.update_idletasks()           # Termina Tareas Pendientes (dibujo,etc)
            self.master.overrideredirect(False)      # Dibuja el Gestor de Ventanas a Toplevel Secundarias
            self.master.state('iconic')              # Iconiza Toplevel Secundarias


    def initializer_images(self):
        self.image_close1 = PhotoImage(file= 'E:/1-RICHI/MovilesDB/B_01.png')
        self.image_minimize1 = PhotoImage(file= 'E:/1-RICHI/MovilesDB/B_02.png')
        self.image_minimize2 = PhotoImage(file= 'E:/1-RICHI/MovilesDB/B_03.png')
        self.image_close2 = PhotoImage(file= 'E:/1-RICHI/MovilesDB/B_04.png')
  

#************************            ███████    ██████████████
#************************        ██████   ██    ██          ██
#************************        ██       ██    ██████████  ██
#************************        ██████   ██            ██  ██
#************************            ██   ██    ██████████  ██
#************************            ██   ██    ██          ██
#************************            ██   ██    ██████████  ██
#************************            ██   ██            ██  ██
#************************            ██   ██    ██████████  ██
#************************            ██   ██    ██          ██
#************************            ███████    ██████████████

class ToplevelCls(Toplevel):
    def __init__(self, master=None, arg1=None, arg2=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.overrideredirect(True)
        
        self.arg1 = arg1
        self._x = 0
        self._y = 0

        #___Frame contenedor de los botones "X" y "-"
        self.frame_manager = FrameManagerCls (self, bg="black",  listmode = arg1)       # Frame: Gestor de Ventanas
        #___Opciones de empaquetamiento:
        #self.frame_manager .pack(arg2)
        self.frame_manager .grid(arg2)

        self.frame_manager .bind("<ButtonPress-1>", self.start_move)       # Desactivado: Razon: Metodo global lo hace   /  # Intercepta los puntos x,y 
        self.frame_manager .bind("<ButtonRelease-1>", self.stop_move)      # Desactivado: Razon: Metodo global lo hace   /  # Asigna un estado de inicio o stop
        self.frame_manager .bind("<B1-Motion>", self.on_move)              # Desactivado: Razon: Metodo global lo hace   /  # Mueve la ventana 

        #___Frame contenedor de los labels
        self.frame_control = Frame(self, bg='blue')
        self.frame_control .grid(column=0, row=1, sticky='news')
        #____



        #Esto se quito...new
        """ self.label_title = Label(self.frame_manager, text='', fg="white", bg="green")   
        self.label_title .pack(side=RIGHT, padx=0, pady=0)                                          # Derecha 

        self.label_title .bind("<ButtonPress-1>", self.start_move)     # Desactivado: Razon: Metodo global lo hace   /  # Intercepta los puntos x,y 
        self.label_title .bind("<ButtonRelease-1>", self.stop_move)    # Desactivado: Razon: Metodo global lo hace   /  # Asigna un estado de inicio o stop
        self.label_title .bind("<B1-Motion>", self.on_move) """            # Desactivado: Razon: Metodo global lo hace   /  # Mueve la ventana 
        #hasta aqui...

        #self.master .bind("<Map>", self.deiconify_1)                       # Estado: Inactivo, esta definido en Root_class: (Solo sirve para root)
        #self.master .bind("<Unmap>", self.iconify_1)                       # Estado: Inactivo, esta definido en Root_class: (Solo sirve para root)

        # GLOSARIO:
            # _exception1: Es el argumento de la clase: Frame_manager_class que valida que tipo de funcion se va ejecutar en el Instancia creada
                # None:         Default / para Toplevel Principal
                # not is None:          / para Toplevel Secundarias
            # value_exception1: Es el valor de _exception1, puede ser 'cualquier valor' y 'None'

            # _exception1: Es el argumento de la clase: Toplevel_class que valida que tipo de funcion se va ejecutar en el Instancia creada,

        if len(self.arg1) < 3:  # Toplevel Secundarias            
            self.frame_manager .bind("<Map>",self.mapped_manager)


    def iconify_1(self, event):   # SOLO SE EJECUTA SI SE INSTANCIA INTERFACE SI NO NO SIRVE PORQUE ESTA INSTANCIADO EN TK
        self.withdraw()

    def deiconify_1(self, event): # SOLO SE EJECUTA SI SE INSTANCIA INTERFACE SI NO NO SIRVE PORQUE ESTA INSTANCIADO EN TK
        self.deiconify()


    def start_move(self, event=None):   # Activado temporalmente:  Razon: Arriba lo dice  
        self._x = event.x
        self._y = event.y

    def stop_move(self, event=None):    # Activado temporalmente:  Razon: Arriba lo dice
        self._x = None
        self._y = None

    def on_move(self, event=None):      # Activado temporalmente:  Razon: Arriba lo dice
        deltax = event.x - self._x
        deltay = event.y - self._y
        new_position = "+{}+{}".format(self.winfo_x() + deltax, self.winfo_y() + deltay)
        self.geometry(new_position)                 # Mueve todas las ventanas en general menos root

        if len(self.arg1) < 3:                      # Default
            self.master.geometry(new_position)      # Mueve la ventana root


    def configure_toplevel(self, title, size):  # Opciones de las Ventanas Secundarias
        self.title (title)
        self.geometry (size)
        self.resizable (1,1)
        self.wm_attributes ('-topmost', True)                     # FUNCIONA BIEN pero molesta para editar 
        #self.config (bg = 'magenta2')                            # FUNCIONA BIEN pero tiene mal aspecto
        #self.wm_attributes ('-transparentcolor', 'magenta2')     # FUNCIONA BIEN pero tiene mal aspecto

    def mapped_manager(self, event=None):       # / SOLO SE EJECUTA PARA VENTANAS 1,2,3   
        self.update_idletasks()
        self.overrideredirect(True)
        self.state('normal')


#************************            ███████    ██████  ██████
#************************        ██████   ██    ██  ██  ██  ██
#************************        ██       ██    ██  ██  ██  ██
#************************        ██████   ██    ██  ██  ██  ██
#************************            ██   ██    ██  ██████  ██
#************************            ██   ██    ██          ██
#************************            ██   ██    ██████████  ██
#************************            ██   ██            ██  ██
#************************            ██   ██            ██  ██
#************************            ██   ██            ██  ██
#************************            ███████            ██████

class RootCls(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Posicion de los botones "X" y "-"
        arg1 = ({'side':TOP, 'pady':6},{'side':BOTTOM, 'pady':6})       
        # Posicion del frame contenedor de los botones "X" y "-"

        # Opciones de empaquetamiento:
        #arg2 = {'side':RIGHT, 'fill':BOTH}
        arg2 = {'column':1, 'row':0, 'sticky':'news'}


        #self.resizable(0, 0)                     # Deja un rastro de root en pantalla, no solucionado
        self.geometry('0x0+350+0')                # Tamaño de Root

        # (Instancia) Toplevel Principal  y  (Instancia) Frame Manager:
        self.toplevel_principal = ToplevelCls(self, arg1, arg2)

        # (Instancia) Frame Principal: 
        self.frame_principal = Interface(self.toplevel_principal)

        # Opciones de empaquetamiento:
        #self.frame_principal .pack(side=RIGHT, fill=BOTH)
        self.frame_principal .grid(column=0, row=0, sticky='news')     #sticky puede causar errores de dibujo

        self.bind("<Map>", self.deiconify_on)  # Deiconiza Toplevel Principal
        self.bind("<Unmap>", self.iconify_on)  # Iconiza Toplevel Principal

    def iconify_on(self, event):
        self.toplevel_principal.withdraw()

    def deiconify_on(self, event):
        self.toplevel_principal.deiconify()


#************************            ███████    ██████████████
#************************        ██████   ██    ██          ██
#************************        ██       ██    ██  ██████████
#************************        ██████   ██    ██  ██        
#************************            ██   ██    ██  ██████████
#************************            ██   ██    ██          ██
#************************            ██   ██    ██████████  ██
#************************            ██   ██            ██  ██
#************************            ██   ██    ██████████  ██
#************************            ██   ██    ██          ██
#************************            ███████    ██████████████

# TAREAS:
#_______1- Asignar el tamaño y posicion a todas las ventanas a excepcion de root
#_______2- Gestiona toda la aplicacion

class Interface(Frame, MoveAllCls):
    def __init__(self, master=None, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        MoveAllCls.__init__(self)   # Inicializando las variables de control

        path = 'E:/1-RICHI/MovilesDB'
        #_____Coleccion de Imagenes:
        self.path_lst = self.generate_list (path, 'I')
        self.path_mini = self.generate_list (path, 'M')
        
        #_____Variables de control para las ventanas:  [ 1,2,3 ]
        self._frame_1 = None
        self._frame_2 = None
        self._frame_3 = None

        self._open_1 = False  
        self._open_2 = False 
        self._open_3 = False

        #_____Variables de Seguimiento del Boton Seleccionado en la Interface de Botones:
        self.mobil_selected = None

        #_____Variables de Control Secundarias:
        self._gear = False
        self._minimize = False

        #_____Variables de Control de Tamaño y Posición de Todas las Ventanas:
        self.geo_principal = StringVar()
        self.geo_izq = StringVar()
        self.geo_der = StringVar()
        self.geo_stuf = StringVar()
        
        #_____Métodos Llamados:
        self.size_position()
        self.configure_interface()
        self.widgets()

        #_____Enlaces para Mover las Ventanas Globalmente:
        self.bind_all("<ButtonPress-1>", self.start_move_all)             # Punto inicial    
        self.bind_all("<ButtonRelease-1>", self.stop_move_all)            # Punto final
        self.off_move = self.bind_all("<B1-Motion>", self.on_move_all)    # Puntos de movimiento

        #_____Enlaces para Pintar al Boton que Abrio las Ventanas:
        self.master.bind('<FocusIn>', self.focus_in)
        self.master.bind('<FocusOut>', self.focus_out)

        #_____Métodos Llamados de Otras Clases:
        self.make_movable(self.frame_controller.btn_ash)                  # Metodo de MoveAllCls: añade a la lista de widget, que permiten mover la ventana


    # Tareas:
    #   1- Asignar el tamaño y posicion de todas las ventanas a excepción de root 
    def size_position(self):
        screen_x = self.master.winfo_screenwidth()      # 1280
        screen_y = self.master.winfo_screenheight()     # 768
        #print('    ancho total:', screen_x,'    alto total:', screen_y )

        #____V E N T A N A___P R I N C I P A L:
        width_0 = 830                                   # Ancho
        height_0 = 67                                   # Alto
        posx_0 = screen_x // 2 - width_0 // 2           # Posicion  eje X : horizontal    ----> 1280 / 2 - 830 / 2
        posy_0 = 0                                      # Posición  eje Y : vertical
        window_0 = '{}x{}+{}+{}'.format(width_0, height_0, posx_0, posy_0)  
        self.geo_principal .set(window_0)


        #____V E N T A N A___I Z Q U I E R D A:
        width_1 = int(screen_x * 15.6 / 100)            # Ancho   Aprox: 199
        height_1 = screen_y - 74                        # Alto    Aprox: 694
        posx_1 = 0                                      # Posición  eje X : horizontal 
        posy_1 = 35                                     # Posición  eje Y : vertical
        window_1 = '{}x{}+{}+{}'.format(width_1, height_1, posx_1, posy_1)
        self.geo_izq .set(window_1)


        #____V E N T A N A___D E R E C H A:
        posx_2 = screen_x - width_1                     # Posición  eje X : horizontal    ----> 1280 - 199
        window_2 = '{}x{}+{}+{}'.format(width_1, height_1, posx_2, posy_1)
        self.geo_der .set(window_2)


        #____V E N T A N A___S T U F:
        width_3 = 860                                   # Ancho   Aprox: 860
        height_3 = 75                                   # Alto    Aprox: 75
        posx_3 = screen_x // 2 - width_3 // 2           # Posicion  eje X : horizontal    ----> 1280 / 2 - 860 / 2
        posy_3 = screen_y - height_3 - 40               # Posición  eje Y : vertical      ----> 768 - 75 - 40
        window_3 = '{}x{}+{}+{}'.format(width_3, height_3, posx_3, posy_3)
        self.geo_stuf .set(window_3)

    # Tareas:
    #   1- Configurar la ventana principal
    def configure_interface(self):
        
        # MASTER REFIERE A TOPLEVEL: PRINCIPAL
        self.master.title ('_AshmanBot_')
        self.master.geometry (self.geo_principal.get())                   # TAMAÑO DE LA VENTANA
        self.master.resizable (1,1)                                       # OTORGA PERMISO PARA CAMBIAR DE TAMANIO ALA VENTANA
        self.master.config (bg='magenta2')                                # CONFIGURA EL FONDO DE LA VENTANA, etc
        self.master.transient()                                             # No funciona
        self.master.attributes ('-topmost', True)                         # SUPERPONE LA VENTANA A OTRAS APLICACIONES ABIERTAS
        self.master.wm_attributes ('-transparentcolor', 'magenta2')       # BORRA EL COLOR SELECCIONADO DE LA VENTANA

    # Tareas:
    #   1- Inicializa las imagenes que se mandan a las ventanas
    def generate_list(self, file, option):

        ouput = os.listdir (file)
        empty = []   

        if option == 'I': 
            _lst = [[] for x in range(22)]
            _str = ['Fro','Fox','Boo','Ice','JD','Gru','Lig','Adu','Kni','Kal','Mag','Ran','Jol','Tur','Arm','Asa','Rao','Tri','Nak','Big','Bar','Dra']

            for i in ouput:               
                for index, iter in enumerate(_str):
                    if iter in i: 
                        full = file + '/' + i
                        #open = cv2.imread (full)
                        #RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB) 
                        #_lst[index].append(RGB)
                        _lst[index].append(full)               
            return _lst    

           
        if option == 'M':
            for i in ouput:  
                if 'Mini' in i :      
                    full = file + '/' + i
                    #open = cv2.imread (full)
                    #RGB = cv2.cvtColor (open, cv2.COLOR_BGR2RGB)
                    #array = Image.fromarray (RGB)
                    #img = ImageTk.PhotoImage (array)
                    #empty. append (img)
                    open = Image.open(full)
                    img  = ImageTk.PhotoImage(open)
                    empty. append (img)
            return empty    

    # Tareas:
    #   1- Crea las interfaces de control: (4 instancias de clase)
    #      1.1- self.frame_controller : Frame contenedor de 2 botones, logo y la rueda de configuracion
    #      1.2- self.frame_botones    : Frame contenedor de 22 botones
    #      1.3- self.frame_configurer : Frame contenedor de checkbuttons y labels
    #      1.4- self.frame_listmode   : Frame Contenedor de Spinbox y Listbox   
    def widgets(self):
        #____I N S T A N C I A S:  [ 4 ]
        self.frame_controller = A1FrameCls (self, bg='#11161d', width=60, height=67)   # Posicionado     # Color: Azul
        self.frame_botones =    B1FrameCls (self, bg='#31343a', width=756, height=67)     # Posicionado     # Color: Plomo
        self.frame_configurer = B2FrameCls (self, bg='#31343a', width=756, height=67)  # No posicionado  # Color: Plomo
        self.frame_listmode =   B3FrameCls (self, self.path_mini)                                        # No posicionado  # Color: Azul y Plomo
         
        #____P A C K ():
        self.frame_controller .pack (side=LEFT, fill=BOTH)
        self.frame_botones .pack (side=LEFT, fill=BOTH) 

        #____P A C K___P R O P A G A T E ():
        self.frame_controller .pack_propagate (False)
        self.frame_botones .pack_propagate (False)

    # Tareas:
    #   1- Posiciona y quita las instancias de clase
    def gear_stacking(self):   # ON: CON CLICK IZQUIERDO EN LA RUEDA DE CONFIGURACION - QUITA Y PONE WIDGET, REDIMENSIONA LA VENTANA PRINCIPAL,ETC

        if  not self._gear:                                                            # -1
            self._gear = True                                                             # -1.1
            self.frame_botones .pack_forget()                                             # -1.2
            self.frame_listmode .pack_forget()                                            # -1.3

            self.frame_configurer .pack (side=LEFT, fill=BOTH, expand=True)               # -1.4
            self.frame_configurer .focus_set()                                            # -1.5
            self.master.geometry ('830x67')                                               # -1.6

            self.off_move = self.bind_all("<B1-Motion>", self.on_move_all)                # -1.7
            
            
            # 1- Si self._gear es False:  [ Predeterminado False ]
                # 1.1-  Asigna self._gear = True
                # 1.2-  Quita la interface de botones
                # 1.3-  Quita la interface de lista
                # 1.4-  Posiciona la interface de configuracion
                # 1.5-  Le da el foco a la interfaces de configuracion
                # 1.6-  Ajusta el tamaño de la ventana principal
                # 1.7-  Activa el enlace self.on_move_all
        else:                                                                          # -1
            self._gear = False                                                            # -1.1
            self.frame_configurer .pack_forget()                                          # -1.2

            if self.frame_configurer .ckbutton5.variable.get() == True:                   # -1.3

                self.frame_listmode .pack (side=LEFT, fill=BOTH)                             # -1.3.2
                self.frame_listmode .spinboxx .focus_set()                                   # -1.3.3
                self.frame_listmode .spinboxx .delete(0, END)
                if self.mobil_selected is not None:
                    self.frame_listmode .spinboxx .insert(0, self.mobil_selected)  
                self.master.geometry ('250x67')                                              # -1.3.4


                if not self.frame_listmode. _toggle_switch == True:                          # -1.3.5
                    self.off_move = self.bind_all("<B1-Motion>", self.on_move_all)              # -1.3.5.1
                else:                                                                        # -1.3.6
                    self.unbind("",self.off_move)                                               # -1.3.6.1

            else:                                                                         # -1.4
                self.frame_listmode .pack_forget()                                           # -1.4.1
                self.frame_botones .pack (side=LEFT, fill=BOTH)                              # -1.4.2
                self.frame_botones .focus_set()                                             # nuevo

                if not self.frame_configurer .ckbutton7.variable.get() == True:              # -1.4.3
                    self.off_move = self.bind_all("<B1-Motion>", self.on_move_all)              # -1.4.3.1
                else:                                                                        # -1.4.4
                    self.unbind("",self.off_move)                                               # -1.4.4.1

            # 1- Entonces si self._gear es True:
                # 1.1-  Asigna self._gear = False
                # 1.2-  Quita la interface de configuracion

                # 1.3-  Si (ckbutton5.variable.get) es True:
                    # 1.3.1-  Desmarca el boton seleccionado en la interface de botones
                    # 1.3.2-  Posiciona la interface de lista
                    # 1.3.3-  Le da el foco a spinbox, widget de la interface de lista
                    # 1.3.4-  Ajusta el tamaño de la ventana principal

                    # 1.3.5-  Si self._switch es False:  [ Predeterminado False ]
                        # 1.3.5.1-  Activa el enlace self.on_move_all
                    # 1.3.6-  Entonces si self._switch es True:
                        # 1.3.6.1-  Desactiva el enlace self.on_move_all

                # 1.4-  Entonces si (ckbutton5.variable.get) es False:     
                    # 1.4.1-  Quita la interface de lista
                    # 1.4.2-  Posiciona la interface de botones

                    # 1.4.3-  Si (ckbutton7.variable.get) es False:
                        # 1.4.3.1-  Activa el enlace self.on_move_all
                    # 1.4.4-  Entonces (ckbutton7.variable.get) es True:
                        # 1.4.4.1-  Desactiva el enlace self.on_move_all

            # NOTAS:
            # 1. self._switch es una variable de control de la interface de lista
  
    
    def focus_in(self, event):

        if self.focus_get() == self.frame_botones:                            #
            for btn in (self.frame_botones. buttons22):                       #
                if self.mobil_selected == btn.cget('text'):                #
                    btn .config(bg='#bdfe04', fg='black')                     #
                else:                                                         #
                    if btn .cget('text') in self.frame_botones .mobiles2:     #
                        btn .config (bg='#11161d', fg='yellow')               #
                    else:                                                     #
                        btn .config (bg='#11161d', fg='white')

            
    def focus_out(self, event):

        if self.focus_get() == None and self.mobil_selected is not None:
            for btn in (self.frame_botones. buttons22):                       #
                if self.mobil_selected == btn.cget('text'):                #
                    btn .config(bg='#bdfe04', fg='black')                     #


    #############################################################
    #############################################################
    #############################################################
    #############################################################
    # G E S T I O N   DE  V E N T A N A S   S U P E R I O R E S :

    def windows_123 (self, var_1, var_2, var_3, mobil=None):

        # (self.mobil_selected) : almacena el nombre del boton presionado    
        for index,i in enumerate(self.frame_listmode .spinbox_values):
            if mobil == index:
                self.mobil_selected = i
                break

        #_____________________________________________________________________

        # Posicion de los botones "X" y "-":                             ( None: diferencia los metodos )
        arg1 = ({'side':RIGHT, 'padx':2, 'pady':(3,2)},{'side':RIGHT, 'padx':(2,10), 'pady':(3,2)}, None)   
        # Posicion del frame contenedor de los botones "X" y "-"

        # Opciones de empaquetamiento:
        #arg2 = {'side':TOP, 'fill':BOTH}
        arg2 = {'column':0, 'row':0, 'sticky':'news'}




        #                                  V E N T A N A:   1
        #__________________________________________________________________________________________________________
        if not self._open_1:   # ----> Si open_1 es False:
            self.toplevel_LEFT = ToplevelCls (self, arg1, arg2)  # AQUI no se sabe quien es el padre correcto : self o self.master
            self.toplevel_LEFT .configure_toplevel ('Hoja Izquierda', self.geo_izq.get())
                                
        container_frame_left = var_1 (self.toplevel_LEFT)  #  var_1 es un frame

        if self._frame_1 is not None:  
            self._frame_1 .destroy()
            #self._frame_1 .frame_controller .destroy() #new
        self._frame_1 = container_frame_left

        # Opciones de empaquetamiento:
        #self._frame_1 .pack(fill='both', expand=True)
        self._frame_1 .grid(column=0, row=2, sticky='news')
        """ self.a = Frame(self.toplevel_LEFT, bg='green2')
        self.a .pack(fill='both', expand=True) """




        self.toplevel_LEFT .grid_columnconfigure(0, weight=1)

        self.toplevel_LEFT .grid_rowconfigure(0, weight=0)
        self.toplevel_LEFT .grid_rowconfigure(1, weight=0)
        self.toplevel_LEFT .grid_rowconfigure(2, weight=1)


        #                                  V E N T A N A:   2
        #__________________________________________________________________________________________________________
        if not self._open_2:
            self.toplevel_RIGHT = ToplevelCls (self, arg1, arg2)
            self.toplevel_RIGHT .configure_toplevel ('Hoja Derecha', self.geo_der.get())

        container_frame_right = var_2 (self.toplevel_RIGHT) 

        if self._frame_2 is not None:
            self._frame_2 .destroy()
        self._frame_2 = container_frame_right

        # Opciones de empaquetamiento:
        #self._frame_2 .pack(fill='both', expand=True)
        self._frame_2 .grid(column=0, row=1, sticky='news')

        

        #                                  V E N T A N A:   3
        #__________________________________________________________________________________________________________
        if not self._open_3:
            self.toplevel_STUF = ToplevelCls (self, arg1, arg2)
            self.toplevel_STUF .configure_toplevel ('Game Stuff', self.geo_stuf.get())

        container_frame_stuf = var_3 (self.toplevel_STUF) 

        if self._frame_3 is not None:
            self._frame_3 .destroy()
        self._frame_3 = container_frame_stuf

        # Opciones de empaquetamiento:
        #self._frame_3 .pack(fill='both', expand=True)
        self._frame_3 .grid(column=0, row=1, sticky='news')



        #____S I Z E G R I P ():  Inquierda
        self.grip = ttk.Sizegrip(self._frame_1, style='TSizegrip')
        self.grip .place (relx=1.0, rely=1.0, anchor='center')
        ttk.Style().configure('TSizegrip', bg='black')  

        #____S I Z E G R I P ():  Derecha
        self.grip = ttk.Sizegrip(self._frame_2, style='TSizegrip')
        self.grip .place (relx=1.0, rely=1.0, anchor='center')
        ttk.Style().configure('TSizegrip', bg='black')

        #____S I Z E G R I P ():  Stuff
        """ self.grip = ttk.Sizegrip(self._frame_3, style='TSizegrip')
        self.grip .place (relx=1.0, rely=1.0, anchor='center')
        ttk.Style().configure('TSizegrip', bg='black') """  # NO TIENE FRAME O IMAGEN TODAVIA

        # Este destroy no se ejecuta en la primera llamada o la primera vex que se da clic a un boton es lo mismo
        self.toplevel_LEFT.bind('<Destroy>', lambda event: self.closing_toplevel(1, event))  
        self.toplevel_RIGHT.bind('<Destroy>', lambda event: self.closing_toplevel(2, event))
        self.toplevel_STUF.bind('<Destroy>', lambda event: self.closing_toplevel(3, event))
        #___________________________________________________________________________________________________________
        self._open_1 = True
        self._open_2 = True
        self._open_3 = True
        #_______________________________
        #self.toplevel_LEFT .mainloop()   # Funcionaba el principio
        #self.toplevel_RIGHT .mainloop()
        #self.toplevel_STUF .mainloop()
        #___________________________________________________________________________________________________________
        

    # Tareas:
    #    1- Permitir la apertura de las ventanas secundarias en la siguiente llamada
    #    2- Desactiva la seleccion del boton en la interface de botones
    def closing_toplevel(self,  number, event):
        
        if isinstance(event.widget, Toplevel):
            if number == 1:
                self._open_1 = False
            if number == 2:
                self._open_2 = False
            if number == 3: 
                self._open_3 = False

            if not self._open_1 == True and not self._open_2 == True and not self._open_3:
                try:  # Esto se ejecuta ademas de la condicion, cuando cierra de emproviso la aplicacion con ventanas secundarias. abiertas
                    self.frame_botones .uncheck_selection()
                    self.mobil_selected = None
                except: pass
            


def main (): #-----------------------------------------------

    root = RootCls()
    root .title('AshmanBot')
    #root .wm_attributes("-alpha", 0.0 )
    root .mainloop()

if __name__=="__main__":  #----------------------------------
    main()
