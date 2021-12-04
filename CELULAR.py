from A_import import *
#from A_frames import *
#from B_Frames import *


# INDICE:  NOMBRE:              TAREA:                                    : HEREDA DE:

# [ 1 ]  : LogotipoCls        : Botones: Ash y Gear                       : ( Frame )
# [ 2 ]  : DefaultButtonCls   : Opciones default para los 22 botones      : ( Button )
# [ 3 ]  : ModeButtonsCls     : Botones: 22                               : ( Frame )
# [ 4 ]  : ModeConfigurerCls  : Labels y Checkbuttons                     : ( Frame )
# [ 5 ]  : ModeListCls        : Spinbox y Listbox                         : ( Frame )
# [ 6 ]  : Checkbutton_class  : Sin uso eficiente                         : ( Checkbutton )
# [ 7 ]  : ResizeCls          : Redimensiona Imagenes                     : ( Frame )
# [ 8 ]  : TopIzqCls          : Ventana Izquierda                         : ( Frame )
# [ 9 ]  : TopDerCls          : Ventana Derecha                           : ( Frame )
# [ 10 ] : TopStufCls         : Ventana Stuff                             : ( Frame )
# [ 11 ] : MoveAllCls         : Mover Ventanas Globalmente                :
# [ 12 ] : FrameManagerCls    : Gestor de Ventanas                        : ( Frame )
# [ 13 ] : ToplevelCls        : Controla y mueve todas las Ventanas       : ( Toplevel )
# [ 14 ] : RootCls            : Inicializa la aplicacion                  : ( Tk )
# [ 15 ] : InterfazCls        : Gestiona la aplicacion                    : ( Frame, MoveAllCls )

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

# TAREAS:
#_______1- Gestiona la Interface Inamovible: (Logo y Engranaje)

class LogotipoCls(Frame):
    def __init__(self, master, ico3_lst=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        #____Colección de Imágenes:
        self.ico3_lst = ico3_lst

        #____Métodos Llamados:
        self.create_buttons()


    def create_buttons(self):
        # [self.btn_logotipo] : Logo
        # [self.btn_settings] : Engranaje

        #____BOTONES: 2 ( Logotipo - Settings )
        self.btn_logotipo = Button(self, image=self.ico3_lst[0], bg='#11161d', bd=0, activebackground='#11161d',
                                   command=self.minimize_windows)
        self.btn_settings = Button(self, image=self.ico3_lst[1], bg='#11161d', bd=0, activebackground='#11161d',
                                   command=self.master.gear_stacking)
                         
        #____Posicionamiento:
        self.btn_logotipo .grid(column=0, row=0, padx=(6,6))
        self.btn_settings .grid(column=0, row=1)

        #____Eventos:
        self.btn_logotipo .bind('<Double-Button-3>', self.close_windows)  # Cierra Toplevel Secundarias
        self.btn_settings .bind('<Enter>', self.enter_mouse_settings)
        self.btn_settings .bind('<Leave>', self.leave_mouse_settings)


    # Tarea: 1- Cierra las ventanas secundarias:
    def close_windows(self, event):   # ACTIVA: CON DOBLE CLICK DERECHO EN EL LOGO 
        """for index in range(len(self.master._open))
            if self.master._open[index] == True:
                self.master._open[index] = False
                self.master._window[index] .destroy()"""


        for index, window in enumerate(self.master.windows):
            window.destroy()
            #self.master._windows[index].destroy()
            #self.master._open[index] = False

            
    # Minimiza las ventanas secundarias:
    def minimize_windows(self):   # ACTIVA: CON CLICK IZQUIERDO AL LOGO 
 
        if self.master._open[0] == True or self.master._open[1] == True or self.master._open[2] == True:

            # OCULTAR VENTANAS
            if not self.master._minimize:
                self.master._minimize = True

                if self.master._open[0]:  
                    #self.master.toplevel_LEFT .withdraw()                            # Esto distorciona el tamaño del icono en la barra de tareas, cuando el mouse se posiciona encima
                    self.master.toplevel_LEFT .frame_manager .minimize()              # Metodo de Toplevel_class

                if self.master._open[1]:
                    self.master.toplevel_RIGHT .frame_manager .minimize()

                if self.master._open[2]:
                    self.master.toplevel_STUF .frame_manager .minimize()


            # MOSTRAR VENTANAS
            else:
                self.master._minimize = False

                if self.master._open[0]:
                    self.master.toplevel_LEFT .frame_manager .window_manager_off()                         # Metodo de Toplevel_class

                    x = self.master.toplevel_LEFT .winfo_x()                            # Aqui se pide la posicion x  de la ventana, evita que la ventana al minimizar se expanda : solucion temporal
                    y = self.master.toplevel_LEFT .winfo_y()
                    self.master.toplevel_LEFT .geometry('+{}+{}'.format(x,y))           # Remarcando la posicion , soluciona el redimensionamiento automatico interior

                if self.master._open[1]:
                    self.master.toplevel_RIGHT .frame_manager .window_manager_off()

                    x = self.master.toplevel_RIGHT .winfo_x()
                    y = self.master.toplevel_RIGHT .winfo_y()
                    self.master.toplevel_RIGHT .geometry('+{}+{}'.format(x,y))

                if self.master._open[2]:
                    self.master.toplevel_STUF .frame_manager .window_manager_off()

                    x = self.master.toplevel_STUF .winfo_x()
                    y = self.master.toplevel_STUF .winfo_y()
                    self.master.toplevel_STUF .geometry('+{}+{}'.format(x,y))

   

    def enter_mouse_settings(self, event):
        # Entrada del mouse sobre el boton (Imagen: change)
        event.widget.config(image=self.ico3_lst[2]) 

    def leave_mouse_settings(self, event):
        # Salida del mouse sobre el boton (Imagen: default)
        event.widget.config(image=self.ico3_lst[1])


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

# TAREAS:
#_______1- Crea Botones con una configuracion ya establecida: (22 Botones)

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

# TAREAS:
#_______1- Crear los 22 botones
#_______2- Abrir las Ventanas Secundarias

class ModeButtonsCls(Frame):
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
                lambda top1: TopIzqCls  (top1, indice, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, self.master.main_lst, self.master.mini_lst),
                lambda top2: TopDerCls  (top2, indice, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, self.master.main_lst, self.master.mini_lst),
                lambda top3: TopStufCls (top3, indice, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, self.master.main_lst, self.master.mini_lst), indice)

        
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
class ModeConfigurerCls(Frame):
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

        self.checkbutton1 = CheckbuttonCls (self, bg='#31343a', activebackground= '#31343a', bd=0, borderwidth=0,)
        self.checkbutton2 = CheckbuttonCls (self, bg='#31343a', activebackground= '#31343a', bd=0, borderwidth=0,)
        self.checkbutton3 = CheckbuttonCls (self, bg='#31343a', activebackground= '#31343a', bd=0, borderwidth=0,)
        self.checkbutton4 = CheckbuttonCls (self, bg='#31343a', activebackground= '#31343a', bd=0, borderwidth=0,)
        self.checkbutton5 = CheckbuttonCls (self, bg='#31343a', activebackground= '#31343a', bd=0, borderwidth=0,)
        self.checkbutton6 = CheckbuttonCls (self, bg='#31343a', activebackground= '#31343a', bd=0, borderwidth=0,)
        self.checkbutton7 = CheckbuttonCls (self, bg='#31343a', activebackground= '#31343a', bd=0, borderwidth=0,)
        self.checkbutton8 = CheckbuttonCls (self, bg='#31343a', activebackground= '#31343a', bd=0, borderwidth=0,)
    
        self.checkbutton1 .grid (column=1, row=0, pady=(10,0))
        self.checkbutton2 .grid (column=1, row=1, pady=(0,0))
        self.checkbutton3 .grid (column=3, row=0, pady=(10,0))
        self.checkbutton4 .grid (column=3, row=1, pady=(0,0))
        self.checkbutton5 .grid (column=5, row=0, pady=(10,0))
        self.checkbutton6 .grid (column=5, row=1, pady=(0,0))
        self.checkbutton7 .grid (column=7, row=0, padx=(0,200), pady=(10,0),)
        self.checkbutton8 .grid (column=7, row=1, padx=(0,200), pady=(0,0),)


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
class ModeListCls(Frame):
    def __init__(self, master, mini_lst,  *args, **kwargs):
        super().__init__(master, *args, kwargs)

        #_____Coleccion de imagenes  
        self.Miniatures = mini_lst

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
                lambda top1: TopIzqCls  (top1, index, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, self.master.main_lst, self.master.mini_lst),
                lambda top2: TopDerCls  (top2, index, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, self.master.main_lst, self.master.mini_lst),
                lambda top3: TopStufCls (top3, index, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, self.master.main_lst, self.master.mini_lst), index)
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
class CheckbuttonCls(Checkbutton):   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.variable = BooleanVar()
        self.configure(variable=self.variable) # ver si acepta config en vez de configure
    
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
        super().__init__(master, bg='black', *args, **kwargs)
        
        self.image = Image.open(index)
        self.image_copy = self.image .copy()

        self.photo_image = ImageTk.PhotoImage(self.image)

        self.img = Label(self, image=self.photo_image, bg='black')
        self.img .pack(fill='both', expand=True)
        self.img .bind('<Configure>', self.resize)

    def resize(self, event):
        self.image = self.image_copy .resize((self.master.winfo_width(), self.master.winfo_height()))
        self.photo_image = ImageTk.PhotoImage(self.image)
        self.img .config(image=self.photo_image)


""" class IconsIzqCls(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        

        # INTERFACE DE CONTROL: Para cambiar las imagenes

        # Frame: Contenedor de todos los iconos: 
        self.frame_container_icons               = Frame(self, bg='#2f3337')
        self.frame_container_icons                 .grid(column=0, row=0, sticky='new')

        # Label: Iconos:
        self.lbl_icon1 = Label(self.frame_container_icons, image=path_mini[26], bg='black', cursor="hand2", bd=0)
        self.lbl_icon1   .grid(column=0, row=0, padx=0) # sticky='ew', para que el color de relleno del label ocupe todo

        self.lbl_icon2 = Label(self.frame_container_icons, image=path_mini[25], bg='black', cursor="hand2", bd=0)
        self.lbl_icon2   .grid(column=1, row=0, padx=0)

        # Eventos: Para cambiar las imagenes 1
        self.lbl_icon1   .bind('<Button-1>', self.open_image_miniature)
        self.lbl_icon2   .bind('<Button-1>', self.open_image_miniature)

        if indice == 17:

            # Label: Iconos:    
            self.lbl_icon3 = Label(self.frame_container_icons, text='33', bg='green', height=1, cursor="hand2")
            self.lbl_icon3   .grid(column=2, row=0, padx=0)

            self.lbl_icon4 = Label(self.frame_container_icons, text='44', bg='green', cursor="hand2")
            self.lbl_icon4   .grid(column=3, row=0, padx=0)

            # Eventos: Para cambiar las imagenes 2
            self.lbl_icon3   .bind('<Button-1>', self.open_image_miniature)
            self.lbl_icon4   .bind('<Button-1>', self.open_image_miniature)

            self.frame_container_icons.columnconfigure((2,3), weight=1)
          
        
    def controllers(self):  
        pass """
        

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
    def __init__(self, master, indice, arg_0=None, arg_1=None, arg_2=None, arg_3=None, arg_4=None, arg_5=None, arg_6=None, arg_7=None, main_lst=None, path_mini=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        # Variables de Control y Seguimiento:
        self._motion_1 = False

        self.x1 = 0
        self.x2 = 100
        self.y1 = 0
        self.y2 = 7

        # INTERFACE DE CONTROL: Para cambiar las imagenes

        # Frame: Contenedor de todos los iconos: 
        self.frame_container_icons               = Frame(self, bg='#2f3337')
        self.frame_container_icons                 .grid(column=0, row=0, sticky='new')

        
          
        # POSICIONAMIENTO DE IMAGENES:    

        # Imagen: Delay completo del mobil
        self.frame_image_delay_complete = ResizeCls(self, main_lst[indice][arg_0], bd=0)
        self.frame_image_delay_complete       .grid(column=0, row=1, sticky='news')

        # Imagen: Miniatura del mobil para ayudar a medir las distancias
        self.frame_image_mobil_tutorial = ResizeCls(self, main_lst[indice][arg_1], bd=0)
        self.frame_image_mobil_tutorial       .grid(column=0, row=1, sticky='news')


        # Widgets No Posicionados:
        self.frame_image_mobil_tutorial .grid_remove()
        self.frame_container_icons .grid_remove()

        self.master.bind('<Motion>',self.open_frame_container_icons)
        self.bind('<Leave>', self.remove_frame_container_icons)


        # Configuracion principal :
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)

        # Configuracion principal :
        """ self.frame_image_delay_complete .columnconfigure(0, weight=1)
        self.frame_image_delay_complete .rowconfigure(0, weight=1) """

        # Configuracion del contenedor de iconos :
        self.frame_container_icons.columnconfigure((0,1), weight=1)
        self.frame_container_icons.rowconfigure(0, weight=1)


    # Tarea: Abrir la minuatura del mobil:  [ B U T T O N - 1 ]
    def open_image_miniature(self, event): 

        if self.frame_image_mobil_tutorial .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.frame_image_mobil_tutorial .grid()
        else:
            self.frame_image_mobil_tutorial .grid_remove()


    # Tarea: Ocultar y mostrar el frame contenedor de los iconos: [ M O T I O N ]
    def open_frame_container_icons(self, event):
        """ self.porcentage_x  = event.x / self.master.winfo_width() * 100
        self.porcentage_y = event.y / self.master.winfo_height() * 100
        
        if not self._motion_1 == True:
        
            if self.x1 <(self.porcentage_x)< self.x2  and  self.y1 <(self.porcentage_y)< self.y2: """
        self.master.master.resize_1 = True    # Variable de seguimiento

        self.frame_container_icons .grid()
        """ else:
        self.master.master.resize_1 = True     # Variable de seguimiento
        self.frame_container_icons .grid_remove() """

        """ if self.frame_image_base_77 .grid_info() != {}:   # == {} (no mapeado) 
            self.lbl_text_mostrar_77     .grid_remove() """

    # Tarea: Ocultar y mostrar el frame contenedor de los iconos: [ M O T I O N ]
    def remove_frame_container_icons(self, event):
        self.master.master.resize_1 = False
        self.frame_container_icons .grid_remove()



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
    def __init__(self, master, indice, arg_0=None, arg_1=None, arg_2=None, arg_3=None, arg_4=None, arg_5=None, arg_6=None, arg_7=None, main_lst=None, path_mine=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        # Variables de Control para mostrar la imagen del angulo 77:
        self.x1 = 0
        self.x2 = 100
        self.y1 = 67
        self.y2 = 100

        # Imagen: Base inicial del mobil:
        self.frame_image_base_initial = ResizeCls (self, main_lst [indice][arg_2], bd=0)
        self.frame_image_base_initial       .grid (column=0, row=0, sticky='news')
        self.frame_image_base_initial       .grid_propagate(0)

        # Imagen: Base 77 del mobil:
        self.frame_image_base_77      = ResizeCls (self, main_lst [indice][arg_3], bd=0)
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
    def __init__(self, master, indice, arg_0=None, arg_1=None, arg_2=None, arg_3=None, arg_4=None, arg_5=None, arg_6=None, arg_7=None, main_lst=None, path_mine=None, *args, **kwargs):
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
        self.immovable = []
          
    def make_movable(self, *widgets):
        self.movable.extend(widgets)

    def make_immovable(self, *widgets):
        self.immovable.extend(widgets)
        
    def is_movable(self, widget):
        return widget in self.movable

    def is_immovable(self, widget):
        return widget in self.immovable

    
    def start_move_all(self, event):        
        self._x = event.x
        self._y = event.y
   
    def stop_move_all(self, event):
        self._x = None
        self._y = None

    def on_move_all(self, event):
        # [self.movable]   : Lista que permite mover su ventana
        # [self.immovable] : Lista que no permite mover su ventana

        deltax = event.x - self._x
        deltay = event.y - self._y

        widget = event.widget
        window = event.widget.winfo_toplevel()
        #____Nueva Posición:
        new_position = "+{}+{}".format (window.winfo_x() + deltax, window.winfo_y() + deltay)


        # Dice: [ Si no es una instancia de... ] and [ No está en la lista (self.immovable) ] or [ Esta en la lista (self.movable) ]
        if not isinstance(widget, (Button, ttk.Sizegrip, Spinbox)) == True and not self.is_immovable(widget) == True or self.is_movable(widget):     #self._is_movable(widget): Devuelve True
            # Descripción: Mueve la ventana a excepción de root
            window.geometry(new_position)
        #------------------------------------------------------------------------------------------------------------------------------------------

        # Dice: [ Si es una instancia de... ] and [ No es una instancia de... ] or [  Esta en la lista (self.movable) ]
        if isinstance(window.master, Tk)== True and not isinstance(widget, (Button, ttk.Sizegrip, Spinbox)) == True and not self.is_immovable(widget) == True or self.is_movable(widget):               
            # Descripción: Mueve root                                        # otro: if _tops.master == RootCls:
            window.master.geometry(new_position)
        #------------------------------------------------------------------------------------------------------------------------------------------


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
    def __init__(self, master=None, path_lst=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        #____Coleccion de Imagenes:
        self.Icons = path_lst         # Iconos: cerrar y minimizar las ventanas

        #____Métodos Llamados:
        self.create_buttons()


    def create_buttons(self):
        #____Posicion de los botones: ( PRINCIPAL )
        close1, minimize1 = {'side':TOP}, {'side':BOTTOM}                 
        #____Posicion de los botones: ( SECUNDARIA )
        close2, minimize2 = {'side':RIGHT}, {'side':RIGHT, 'padx':(0,10)}

        #____Actualiza la geometria de la ventana:
        self.update_idletasks()

        #____Solicita el ancho y alto de la ventana:
        x = self.winfo_toplevel().winfo_width()
        y = self.winfo_toplevel().winfo_height()
        

        #____BOTONES: 2 ( Cerrar - Minimizar )
        self.button_close = Button(self, image=self.Icons[0], command=self.close, bd=0, bg='#1b1d22', activebackground='red')
        self.button_minimize = Button(self, image=self.Icons[1], command=self.minimize, bd=0, bg='#1b1d22', activebackground='#4ca6ff')

        #____Posicionamiento:
        self.button_close .pack(close1 if x > y  else close2)
        self.button_minimize .pack(minimize1 if x > y else minimize2)

        #____Enlaces: Cambian la imagen de los botones
        self.button_close.bind("<Enter>", self.enter_mouse_close)
        self.button_close.bind("<Leave>", self.leave_mouse_close)

        self.button_minimize.bind("<Enter>", self.enter_mouse_minimize)
        self.button_minimize.bind("<Leave>", self.leave_mouse_minimize)


    def enter_mouse_close(self, event):
        # Entrada del mouse sobre el boton (Imagen: change)
        event.widget.config(image=self.Icons[2], bg='red')

    def leave_mouse_close(self, event):
        # Salida del mouse sobre el boton (Imagen: default)
        event.widget.config(image=self.Icons[0], bg='#1b1d22')

    def enter_mouse_minimize(self, event):
        # Entrada del mouse sobre el boton (Imagen: change)
        event.widget.config(image=self.Icons[3], bg='#4ca6ff')

    def leave_mouse_minimize(self, event):
        # Salida del mouse sobre el boton (Imagen: default)
        event.widget.config(image=self.Icons[1], bg='#1b1d22')


    # Tarea: - Destruye la ventana:
    def close(self):
        self.master.destroy()                        # Destruye la Ventana

        if isinstance(self.master.master.winfo_toplevel(), Tk):
            self.master.master.destroy()             # Destruye la Ventana Root
            self.master.quit()                       # SIGO INVESTIGANDO...

    # Tarea: - Oculta la ventana:
    def minimize(self):
        if isinstance(self.master.master.winfo_toplevel(), Tk):
            self.master.withdraw()                   # Oculta la Ventana Principal( Desaparece )
            self.master.master.iconify()             # Oculta la Ventana Root
        else:
            self.window_manager_on()                 # Oculta la Ventana Secundaria( No desaparece )


    # Tarea: - Muestra el gestor de ventanas
    def window_manager_on(self, event=None):
        self.master.update_idletasks()               # Termina Tareas Pendientes y Actualiza la Aplicacion
        self.master.overrideredirect(False)          # Muestra el Gestor de Ventanas
        self.master.state('iconic')                  # Oculta la Ventana Secundaria en la Barra de Tareas
    
    # Tarea: - Oculta el gestor de ventanas
    def window_manager_off(self, event=None):
        if not isinstance(self.master.master.winfo_toplevel(), Tk):
            self.master.update_idletasks()
            self.master.overrideredirect(True)       # Oculta el Gestor de Ventanas
            self.master.state('normal')              # SIGO INVESTIGANDO SI ES NECESARIO...


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
    def __init__(self, master=None, path_lst=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.overrideredirect(True)

        #____Coleccion de Imagenes:
        self.Icons = path_lst        # Iconos: menu de opciones

        #____Variables de Reposo de las Coordenadas de la Ventana:
        self._x = 0
        self._y = 0


    def create_frame_manager(self, lst, **position):
        # [ 1 ] self.frame_manager  : Frame(contenedor):  Botones: [X] [-]

        #____GESTOR DE VENTANA: ( 1 instancia )
        self.frame_manager = FrameManagerCls(self, lst, bg="#1b1d22")
        self.frame_manager .pack(position)

        #____Enlaces: Mueven la ventana
        self.frame_manager .bind("<ButtonPress-1>", self.start_move)
        self.frame_manager .bind("<ButtonRelease-1>", self.stop_move)
        self.frame_manager .bind("<B1-Motion>", self.on_move)
        #____Enlaces: Oculta el gestor de ventanas
        self.frame_manager .bind("<Map>",self.frame_manager .window_manager_off)


    def create_label_title(self, **kwargs):
        #____TITULO DE LA VENTANA:
        self.label_title = Label(self.frame_manager, font=('Ghotam',8,'bold'), fg="white", bg="#1b1d22", bd=0, **kwargs)
        self.label_title .pack(side=LEFT, padx=10, pady=0)

        #____Enlaces: Mueven la ventana
        self.label_title .bind("<ButtonPress-1>", self.start_move)
        self.label_title .bind("<ButtonRelease-1>", self.stop_move)
        self.label_title .bind("<B1-Motion>", self.on_move)


    def create_button_menu(self, metodo=None):
        #____BOTONES: ( 1 )
        self.button_menu = Button(self.frame_manager, image=self.Icons[0], command=metodo, bg="#1b1d22", activebackground='#4ca6ff', bd=0)   
        self.button_menu .pack(side=LEFT)

        #____Enlaces: Cambian la imagen del boton menu
        self.button_menu .bind("<Enter>", self.enter_mouse_menu)
        self.button_menu .bind("<Leave>", self.leave_mouse_menu)
        self.button_menu .bind("<ButtonPress-1>", self.press_mouse_menu)
        self.button_menu .bind("<ButtonRelease-1>", self.release_mouse_menu)


    def enter_mouse_menu(self, event):
        # Entrada del mouse sobre el boton (Imagen: change)
        event.widget .config(image=self.Icons[1], bg='#252b34')

    def leave_mouse_menu(self, event):
        # Salida del mouse sobre el boton (Imagen: default)
        event.widget .config(image=self.Icons[0], bg='#1b1d22')

    def press_mouse_menu(self, event):
        # Botón presionado (Imagen: change)
        self.button_press = event.widget
        self.button_press .config(image=self.Icons[2])

    def release_mouse_menu(self, event):
        # Botón soltado (Imagen: default) $$-$$$
        self.button_press .config(image=self.Icons[1], bg='#252b34')


    #def open_



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

        #Dice: Si el padre de la ventana es una instancia de Tk():
        if isinstance(self.master.winfo_toplevel(), Tk):
            self.master.geometry(new_position)                    # Mueve la ventana root


    def configure_toplevel(self, title, size):  # Opciones de las Ventanas Secundarias
        self.title (title)
        self.geometry (size)
        self.resizable (1,1)
        self.wm_attributes ('-topmost', True)                     # FUNCIONA BIEN pero molesta para editar 
        self.config (bg = 'magenta2')                            # FUNCIONA BIEN pero tiene mal aspecto
        #self.wm_attributes ('-transparentcolor', 'magenta2')     # FUNCIONA BIEN pero tiene mal aspecto


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
    def __init__(self, folder, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #path = folder  # c:\Users\Usuario\Desktop\proyecto
        path = 'E:/1-RICHI/MovilesDB'

        #____Coleccion de Imagenes:
        self.main_lst = self.generate_list (path, 1)
        self.mini_lst = self.generate_list (path, 2)
        self.ico1_lst, self.ico2_lst, self.ico3_lst = self.generate_list (path, 3)

        #____Enlaces para Ocultar y Mostrar la Ventana Principal: ( 1 forma )
        self.bind("<Unmap>", self.iconify_on)    # Activacion: Click en el icono de la barra de tareas
        self.bind("<Map>", self.deiconify_on)    # Activacion: Click en el icono de la barra de tareas

        #____Métodos Llamados:
        self.configure_root()
        self.create_window()


    def configure_root(self):
        #self.resizable(0, 0)                     # Deja un rastro de root en pantalla, no solucionado
        self.geometry('0x0+350+0')                # Tamaño de Root


    def create_window(self):
        # [ 1 ] self.toplevel_principal  : Toplevel: Ventana principal
        # [ 2 ] self.frame_interface     : Frame: Interface de control

        #____VENTANA PRINCIPAL: ( 2 instancias )
        self.toplevel_principal = ToplevelCls(self, self.ico2_lst)
        self.frame_interface    = InterfazCls(self.toplevel_principal, self.main_lst, self.mini_lst, self.ico1_lst, self.ico2_lst, self.ico3_lst)

        #____SubMétodos Llamados: ( 1 )
        self.toplevel_principal .create_frame_manager(self.ico1_lst, side=RIGHT, fill=BOTH)     # Frame Manager

        #____Posicionamiento:
        self.frame_interface .pack(side=RIGHT, fill=BOTH)


    # Tarea: 1- Oculta la ventana principal
    def iconify_on(self, event=None):
        self.toplevel_principal.withdraw()

    # Tarea: 1- Muestra la ventana principal
    def deiconify_on(self, event=None):
        self.toplevel_principal.deiconify()


    # Tarea: 1- Inicializa las imagenes
    def generate_list(self, file, option):

        ouput = os.listdir(file)

        # Descripción: (1) Genera la lista principal de imagenes sin ininicializarlas
        if option == 1:
            multilist = [[] for x in range(22)]
            mobiles = ['Fro','Fox','Boo','Ice','JD','Gru','Lig','Adu','Kni','Kal','Mag','Ran','Jol','Tur','Arm','Asa','Rao','Tri','Nak','Big','Bar','Dra']

            for i in ouput:
                for index, mobil in enumerate(mobiles):
                    if mobil in i:
                        full = file + '/' + i
                        multilist[index] .append(full)
            return multilist


        # Descripción: (2) Genera la lista de imagenes de miniatura inicializadas
        if option == 2:
            empty = []

            for i in ouput:
                if 'Mini' in i :
                    full = file + '/' + i
                    open = Image.open(full)
                    img  = ImageTk.PhotoImage(open)
                    empty. append(img)
            return empty


        # Descripción: (3) Genera la lista de imagenes de iconos inicializadas ddd
        if option == 3:
            empty1, empty2, empty3 = [],[],[]
            icons = ['Ico1', 'Ico2', 'Ico3']

            for i in ouput:
                for index, icon in enumerate(icons):
                    if icon in i:
                        full = file + '/' + i
                        open = Image.open(full)
                        img  = ImageTk.PhotoImage(open)
                        if icon in 'Ico1':
                            empty1 .append(img)
                        if icon in 'Ico2':
                            empty2 .append(img)
                        if icon in 'Ico3':
                            empty3 .append(img) 
            return empty1, empty2, empty3
        
        

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

class InterfazCls(Frame, MoveAllCls):
    def __init__(self, master=None, main_lst=None, mini_lst=None, ico1_lst=None, ico2_lst=None, ico3_lst=None, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        MoveAllCls.__init__(self)   # Inicializando las variables de control

        #____Coleccion de Imagenes:
        self.main_lst = main_lst
        self.mini_lst = mini_lst
        self.ico1_lst = ico1_lst
        self.ico2_lst = ico2_lst
        self.ico3_lst = ico3_lst

        #____Variables de Control de Tamaño y Posición de Todas las Ventanas:
        self.geo_principal = StringVar()
        self.geo_izq = StringVar()
        self.geo_der = StringVar()
        self.geo_stuf = StringVar()
        
        #____Variables de Control de los Frames de las Ventanas Secundarias: [ 1,2,3 ]
        """ self._frame_1 = None
        self._frame_2 = None
        self._frame_3 = None """
        self._frame = [None] * 3
        self._open = [False] * 3
        self.windows = [None] * 3

        #self.container = [None] *3

        #____Variables de Seguimiento del Boton Seleccionado en la Interface de Botones:
        self.mobil_selected = None

        #____Variables de Control Secundarias:
        self._gear = False
        self._minimize = False

        #____Variables de Seguimiento del Frame Contenedor de los Iconos en las Ventanas Secundarias:
        self.resize_1 = False

        #____Enlaces para Mover las Ventanas Globalmente:
        self.bind_all("<ButtonPress-1>", self.start_move_all)             # Punto inicial    
        self.bind_all("<ButtonRelease-1>", self.stop_move_all)            # Punto final
        self.off_move = self.bind_all("<B1-Motion>", self.on_move_all)    # Puntos de movimiento

        #____Enlaces para Marcar el Boton que Inicio las Ventanas:
        self.master.bind('<FocusIn>', self.focus_in)
        self.master.bind('<FocusOut>', self.focus_out)

        #____Métodos Llamados:
        self.size_position_windows()
        self.configure_interface()
        self.widgets()

        #____Métodos Heredados Llamados:
        self.make_movable(self.frame_static.btn_logotipo)                  # Class MoveAllCls: Añade a la lista de widget que permite mover la ventana
        self.make_immovable(self.frame_botones.frame_1)


    # Tarea: 1- Asignar el tamaño y posicion de todas las ventanas a excepción de root:
    def size_position_windows(self):
        # Mi monitor: (1280 x 768)

        #____Tamaño del Monitor del Usuario:
        screen_x = self.master.winfo_screenwidth()      # Tamaño Ancho
        screen_y = self.master.winfo_screenheight()     # Tamaño Alto
        #print('Ancho Pantalla ---> ', screen_x, '\nAlto Pantalla ---> ', screen_y )


        #____VENTANA PRINCIPAL:                         # Redimensionable : No
        width = 834                                     # Tamaño Ancho
        height = 67                                     # Tamaño Alto
        posx = screen_x // 2 - width // 2               # Posicion (x)    : (1280 / 2) - (830 / 2)
        posy = 0                                        # Posición (y)
        #____Tamaño y Posición: 
        window = '{}x{}+{}+{}'.format(width, height, posx, posy)
        self.geo_principal .set(window)
        #---------------------------------------------------------------------------------------------------------

        #____VENTANA IZQUIERDA:                         # Redimensionable : Si
        width_1 = int(screen_x * 15.6 / 100)            # Tamaño Ancho    : 199
        height_1 = screen_y - 74                        # Tamaño Alto     : 694
        posx_1 = 0                                      # Posición (x)
        posy_1 = 35                                     # Posición (y)
        #____Tamaño y Posición:
        window_1 = '{}x{}+{}+{}'.format(width_1, height_1, posx_1, posy_1)
        self.geo_izq .set(window_1)
        #---------------------------------------------------------------------------------------------------------

        #____VENTANA DERECHA:
        posx_2 = screen_x - width_1                     # Posición (x)    : (1280 - 199)
        #____Tamaño y Posición:
        window_2 = '{}x{}+{}+{}'.format(width_1, height_1, posx_2, posy_1)
        self.geo_der .set(window_2)
        #---------------------------------------------------------------------------------------------------------

        #____VENTANA STUFF:                             # Redimensionable : Si
        width_3 = 860                                   # Tamaño Ancho    : 860
        height_3 = 75                                   # Tamaño Alto     : 75
        posx_3 = screen_x // 2 - width_3 // 2           # Posicion (x)    : (1280 / 2) - (860 / 2)
        posy_3 = screen_y - height_3 - 40               # Posición (y)    : (768 - 75) - 40
        #____Tamaño y Posición:
        window_3 = '{}x{}+{}+{}'.format(width_3, height_3, posx_3, posy_3)
        self.geo_stuf .set(window_3)
        #---------------------------------------------------------------------------------------------------------

   
    # Tarea: 1- Configura la ventana principal:
    def configure_interface(self):      
        # [self.master] Refiere a ventana principal

        self.master.title('_AshmanBot_')
        self.master.geometry(self.geo_principal.get())                   # TAMAÑO DE LA VENTANA
        self.master.resizable(1,1)                                       # OTORGA PERMISO PARA CAMBIAR DE TAMANIO ALA VENTANA
        self.master.config(bg='magenta2')                                # CONFIGURA EL FONDO DE LA VENTANA, etc
        self.master.transient()                                          # No funciona bien
        self.master.attributes('-topmost', True)                         # SUPERPONE LA VENTANA A OTRAS APLICACIONES ABIERTAS
        self.master.wm_attributes('-transparentcolor', 'magenta2')       # BORRA EL COLOR SELECCIONADO DE LA VENTANA


    # Tarea: 1- Crea las interfaces de control:
    def widgets(self):
        # [ 1 ] self.frame_static     : Botones: Ash y Gear
        # [ 2 ] self.frame_botones    : Botones: 22
        # [ 3 ] self.frame_configurer : Labels y Checkbuttons
        # [ 4 ] self.frame_listmode   : Spinbox y Listbox

        #____INTERFACES DE CONTROL: ( 4 instancias )
        self.frame_static     = LogotipoCls(self, self.ico3_lst, bg='#11161d', width=60, height=67)    # Posicionado     # Color: Azul
        self.frame_botones    = ModeButtonsCls(self, bg='#31343a', width=756, height=67)               # Posicionado     # Color: Plomo
        self.frame_configurer = ModeConfigurerCls(self, bg='#31343a', width=756, height=67)            # No posicionado  # Color: Plomo
        self.frame_listmode   = ModeListCls(self, self.mini_lst)                                       # No posicionado  # Color: Azul y Plomo
         
        #____Posicionamiento:
        self.frame_static .pack(side=LEFT, fill=BOTH)
        self.frame_botones .pack(side=LEFT, fill=BOTH)

        #____Propagación:
        self.frame_static .pack_propagate(False)
        self.frame_botones .pack_propagate(False)


    # Tarea: 1- Gestiona los widgets de la ventana principal
    def gear_stacking(self):

        # Dice: Si [self._gear] es falso: ( Predeterminado False )
        if not self._gear:
            self._gear = True
            self.frame_botones .pack_forget()
            self.frame_listmode .pack_forget()

            self.master.geometry('834x67')
            self.frame_configurer .pack(side=LEFT, fill=BOTH, expand=True)
            self.frame_configurer .focus_set()

            # Descripcion: Activa el método para mover las ventanas globalmente
            self.off_move = self.bind_all("<B1-Motion>", self.on_move_all)


        else:
            self._gear = False
            self.frame_configurer .pack_forget()

            # Dice: Si la casilla N°5 está marcada:
            if self.frame_configurer .checkbutton5 .variable.get() == True:
                self.master.geometry('254x67')
                self.frame_listmode .pack(side=LEFT, fill=BOTH)
                self.frame_listmode .spinboxx .focus_set()
                self.frame_listmode .spinboxx .delete(0, END)

                # Dice: Si se asignó el nombre de un móvil a la variable de seguimiento:
                if self.mobil_selected is not None:
                    self.frame_listmode .spinboxx .insert(0, self.mobil_selected)

                if not self.frame_listmode. _toggle_switch == True:
                    self.off_move = self.bind_all("<B1-Motion>", self.on_move_all)
                else:
                    self.unbind("", self.off_move)

            # Dice: Si la casilla N°5 no está marcada:
            else:
                self.frame_listmode .pack_forget()
                self.frame_botones .pack (side=LEFT, fill=BOTH)
                self.frame_botones .focus_set()

                # Dice: Si la casilla N°7 está marcada:
                if self.frame_configurer .checkbutton7 .variable.get() == True:
                    self.unbind("", self.off_move)  # Desactiva

                # Dice: Si la casilla N°7 no está marcada:
                else:
                    self.off_move = self.bind_all("<B1-Motion>", self.on_move_all)  # Activa


    # Tarea: 1- [Busca y Marca] el boton que inició las ventanas secundarias:
    def focus_in(self, event):
        # Entrada del foco a la ventana principal:

        if self.focus_get() == self.frame_botones:
            for btn in (self.frame_botones. buttons22):
                if self.mobil_selected == btn.cget('text'):
                    btn .config(bg='#bdfe04', fg='black')
                else:
                    if btn .cget('text') in self.frame_botones .mobiles2:
                        btn .config (bg='#11161d', fg='yellow')
                    else:
                        btn .config (bg='#11161d', fg='white')


    # Tarea: 1- [Busca y Marca] el boton que inició las ventanas secundarias:
    def focus_out(self, event):
        # Salida del foco de la ventana principal:

        if self.focus_get() == None and self.mobil_selected is not None:
            for btn in (self.frame_botones. buttons22):
                if self.mobil_selected == btn.cget('text'):
                    btn .config(bg='#bdfe04', fg='black')


    #############################################################
    #############################################################
    #############################################################
    #############################################################

    # G E S T I O N   D E  V E N T A N A S   S U P E R I O R E S :

    def windows_123 (self, var_1, var_2, var_3, mobil=None):
        # [self.mobil_selected] Almacena el nombre del boton presionado en el modo botones o lista

        for index, name in enumerate(self.frame_listmode .spinbox_values):
            if mobil == index:
                self.mobil_selected = name
                break

        
        #___________________________________________________________________________________________________________

        #____Lista de argumentos de la funcion: ( 3 instancias(Frame) )
        args = [var_1, var_2, var_3]

        #____Lista de contenedores de frames:
        container = [None] * 3

        #____Lista de argumentos de los metodos de la ventana:
        title = ['Hoja Izquierda', 'Hoja Derecha', 'Game Stuff']
        text = ['AshmanBot:  1', 'AshmanBot:  2', 'AshmanBot:  3']
        size = [self.geo_izq.get(), self.geo_der.get(), self.geo_stuf.get()]
        
        for i in range(len(self._open)):
            if not self._open[i] == True:
                
                window = ToplevelCls (self, self.ico2_lst)
                #____Métodos Llamados:
                window .configure_toplevel(title[i], size[i])
                window .create_frame_manager(self.ico1_lst, side=TOP, fill=BOTH)
                window .create_button_menu()
                window .create_label_title(text=text[i])

                window .bind('<Destroy>', lambda event, number=i: self.closing_toplevel(number, event)) 

                #____Actualizando la lista
                self.windows[i] = window
                self._open[i] = True


            container[i] = args[i] (self.windows[i])
            print('45454', container[i])
            if self._frame[i] is not None:
                print('233333333333')
                self._frame[i] .destroy()
                print('entreeeeeeeeeeeee')
            self._frame[i] = container[i]
            self._frame[i] .pack(fill='both', expand=True)

                
            """ self.grip = ttk.Sizegrip(self._frame[i], style='TSizegrip')
            self.grip .place (relx=1.0, rely=1.0, anchor='center')
            ttk.Style().configure('TSizegrip', bg='black') """


    # Tareas:
    #    1- Permitir la apertura de las ventanas secundarias en la siguiente llamada
    #    2- Desactiva la seleccion del boton en la interface de botones
    def closing_toplevel(self,  number, event=None):
        
        """if isinstance(event.widget, Toplevel):
            if number == 0:
                self._open[0] = False
                #self.toplevel_LEFT.destroy()
            if number == 1:
                self._open[1] = False
                #self.toplevel_RIGHT.destroy()
            if number == 2: 
                self._open[2] = False
                #self.toplevel_STUF.destroy()"""

        # verifico si la ventana ya estaba cerrada
        if not self._open[number]:
            return

        #____Actualiza y cierra la ventana indicada:
        self._open[number] = False
        self.windows[number] .destroy()
        print('ventanas', len(self.windows))

        # Dice: Si todas las ventanas secundarias están cerradas:
        if self._open == [False] * len(self._open):
            try:  # Esto se ejecuta ademas de la condicion, cuando cierra de emproviso la aplicacion con ventanas secundarias. abiertas
                self.frame_botones .uncheck_selection()
                self.mobil_selected = None
            except: pass


def main (): #-----------------------------------------------
    if len(sys.argv) > 1:
        folder = sys.argv[1]
    else:
        folder = os.getcwd()


    root = RootCls(folder)
    root .title('AshmanBot')
    root .wm_attributes("-alpha", 0.0 )
    root .mainloop()

if __name__=="__main__":  #------------------------------
    main()
