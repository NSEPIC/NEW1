from Importaciones import *

# INDICE:  NOMBRE:              TAREA:                                    : HEREDA DE:

# [ 1 ]  : LogotipoCls        : Botones: Logotipo y Settings              : ( Frame )
# [ 2 ]  : DefaultButtonCls   : Opciones default para los 22 botones      : ( Button )
# [ 3 ]  : ModeButtonsCls     : Botones: 22                               : ( Frame )
# [ 4 ]  : ModeConfigurerCls  : Labels y Checkbuttons                     : ( Frame )
# [ 5 ]  : ModeListCls        : Spinbox y Listbox                         : ( Frame )
# [ 6 ]  : Checkbutton_cls  : Sin uso eficiente                         : ( Checkbutton )
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
#______ 1- Gestiona la Interface Inamovible: (Logo y Engranaje)

class LogotipoCls(Frame):
    def __init__(self, master, path_lst=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        #____Colección de Imágenes:
        self.Icons = path_lst

        #____Variables de seguimiento: [ self.btn_logotipo ]
        self.logotipo = 'default'

        #____Métodos Llamados:
        self.create_buttons()


    def create_buttons(self):
        # [self.btn_logotipo] : Logo
        # [self.btn_settings] : Engranaje

        #____BOTONES: 2 ( Logotipo - Settings )
        self.btn_logotipo = Button(self, image=self.Icons[0],
                                   command=self.minimize_all,
                                   bg='#11161d',                                # Color(fondo)       : Azulino oscuro
                                   activebackground='#11161d',                  # Color(fondo/active): Azulino oscuro
                                   bd=0,
                                   )

        self.btn_settings = Button(self, image=self.Icons[3],
                                   command=self.master.configure_app,
                                   bg='#11161d',                                # Color(fondo)       : Azulino oscuro
                                   activebackground='#11161d',                  # Color(fondo/active): Azulino oscuro
                                   bd=0,
                                   )
                         
        #____Posicionamiento:
        self.btn_logotipo .grid(column=0, row=0, padx=(6,6))
        self.btn_settings .grid(column=0, row=1)

        #____Eventos:
        # [ 1 ] : Cierra todas las ventanas secundarias abiertas y devuelve la imagen por defecto al boton logotipo
        self.btn_logotipo .bind('<Double-Button-3>', self.close_all)
        self.off_enter = self.btn_settings .bind('<Enter>', self.enter_mouse_settings)
        self.off_leave = self.btn_settings .bind('<Leave>', self.leave_mouse_settings)


    # Tarea: - Destruye todas las ventanas secundarias:
    def close_all(self, event):
        # Evento: Doble clik derecho

        for indice in range(len(self.master._open)):
            # Dice: Si hay alguna ventana abierta.
            if self.master._open[indice]:
                self.master._windows[indice] .destroy()

                # Description: Actualiza la lista de ventanas cerradas 
                #self.master._open[indice] = False                         # Desactivado:(razón) El metodo update_window(InterfazCls) lo hace

        #--------------------------------------------------------------------------------------------------
        # Description: Actualiza la variable de seguimiento y devuelve la imagen por defecto del boton
        self.logotipo = 'default'
        self.btn_logotipo .config(image=self.Icons[0])

            
    # Tarea: - Oculta y muestra todas las ventanas secundarias:
    def minimize_all(self):
        # Description: Devuelve True(hay alguna ventana visible) o None(ninguna es visible)
        visibility = self.check_visible_windows()

        for i in range(len(self.master._open)):
            # Dice: Si hay alguna ventana abierta:
            if self.master._open[i]:
                # OCULTA LAS VENNTANAS:
                if visibility:
                    # Dice: Si alguna ventana esta abierta:
                    if self.master._open[i] == True:
                        self.master._windows[i] .frame_manager .minimize()
                        
                        #--------------------------------------------------------------------------------------------------
                        # Description: Cambia la imagen del boton a celeste apagado
                        self.btn_logotipo .config(image=self.Icons[2],)
                       

                # MUESTRA LAS VENTANAS:
                else:
                    # Dice: Si alguna ventana esta abierta:
                    if self.master._open[i] == True:
                        self.master._windows[i] .frame_manager .window_manager_off()
                        self.update_position(self.master._windows[i])                      # Solucion temporal: Evita que la ventana al minimizar se expanda

                        #--------------------------------------------------------------------------------------------------
                        # Description: Cambia la imagen del boton a celeste encendido
                        self.btn_logotipo .config(image=self.Icons[1],)



    def enter_mouse_settings(self, event):
        # Evento: Entrada del mouse sobre el boton (Imagen: change)
        event.widget.config(image=self.Icons[4])

    def leave_mouse_settings(self, event):
        # Evento: Salida del mouse sobre el boton (Imagen: default)
        event.widget.config(image=self.Icons[3])


    # Tarea: - Devuelve verdadero si hay alguna ventana visible.
    def check_visible_windows(self, release=None):
        for i in range(len(self.master._open)):
            # Dice: Si hay alguna ventana abierta:
            if self.master._open[i]:
                # Description: Detiene el bucle y devuelve True, si hay alguna ventana abierta y si se le pasa un argumento al metodo
                if release is not None:
                    return True
                # Dice: Detiene el bucle y devuelve True,  si hay alguna ventana visible
                if self.master._windows[i].winfo_ismapped():
                    return True

    # Tarea: - Actualiza la posicion de la ventana.
    def update_position(self, window):
        x, y = window.winfo_x(), window.winfo_y()                       # Solucion temporal: Evita que la ventana al minimizar se expanda
        window.geometry('+{}+{}'.format(x,y))



    #################################################################################################################################
    ######################################   M E T O D O S  DE  A C C E S O  E X T E R N O   ########################################
    #################################################################################################################################

    #--------------------------------------------------------------------------------------
    # Tarea: - Desactivar el evento y cambiar la imagen del boton settings a dark
    def settings_enter_deactivate(self, event=None):
        # Description: Desactiva el evento
        self.btn_settings.unbind('<Enter>', self.off_enter)
        self.btn_settings.config(image=self.Icons[3])
    
    # Tarea: - Activar el evento y cambiar la imagen del boton settings a light
    def settings_enter_activate(self, event=None):
        # Description: Activa el evento
        self.off_enter = self.btn_settings .bind('<Enter>', self.enter_mouse_settings)
        self.btn_settings.config(image=self.Icons[4])


    #--------------------------------------------------------------------------------------
    # Tarea - Cambiar la imagen del boton logotipo a celeste encendido
    def logotipo_off(self):
        # Dice: Si hay alguna ventana visible:
        if self.logotipo != 'off':
            self.btn_logotipo .config(image=self.Icons[1])

    # Tarea - Devolver la imagen del boton a default
    def logotipo_default(self):
        self.btn_logotipo .config(image=self.Icons[0])

    
    #--------------------------------------------------------------------------------------
    # Tarea - Cambiar la imagen del boton logotipo a celeste encendido
    def map_widget(self, event=None):
        n1 = 0
        n2 = self.master._open .count(True)

        for i in range(len(self.master._open)):
            # Dice: Si hay alguna ventana abierta:
            if self.master._open[i]:
                # Dice: Si hay alguna ventana visible: 
                if self.master._windows[i].winfo_ismapped():
                    n1 += 1
                    # Description: Si la cantidad de ventanas visibles es la misma cantidad de ventanas abiertas
                    if n1 == n2:
                        self.btn_logotipo .config(image=self.Icons[1],)


    #--------------------------------------------------------------------------------------
    # Tarea - Cambiar la imagen del boton logotipo a celeste apagado
    def unmap_widget(self, event=None):
        self.logotipo = 'off'
        self.btn_logotipo .config(image=self.Icons[2],)



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
#______ 1- Crea Botones con una configuracion ya establecida: (22 Botones)

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
#______ 1- Crear los 22 botones
#______ 2- Abrir las Ventanas Secundarias

class ModeButtonsCls(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        #____CONTENEDORES INTERNOS: ( 1 )
        self.frame_1 = Frame (self, bg='#11161d')                                       # Color(fondo): Azulino
        self.frame_1 .grid (padx=(10,10), pady=(6,6))

        #____Métodos Llamados:
        self.creator_buttons()

        #____Variables de Control: Contenedor del ultimo boton presionado
        self.container1 = None


    # Tarea: - Manda los indices para abrir las imagenes en las ventanas secundarias:
    def indices(self, indice):
        # I N D I C E S :
        arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, = 0, 1, 2, 3, 4, 5, 6, 7 

        return  lambda: self.master.create_windows(
                lambda top1: TopIzqCls  (top1, indice, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, self.master.main_lst, self.master.ico2_lst, self.master.ico4_lst),
                lambda top2: TopDerCls  (top2, indice, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, self.master.main_lst, self.master.ico2_lst),
                lambda top3: TopStufCls (top3, indice, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, self.master.main_lst, self.master.ico2_lst), indice)

        
    # Tarea: - Crea los 22 botones y las posiciona:
    def creator_buttons(self):  
        mobiles = [['Frog', 'Fox', 'Boomer', 'Ice', 'J.d', 'Grub', 'Lightning', 'Aduka', 'Knight', 'Kalsiddon', 'Mage'],
                   ['Randomizer', 'Jolteon', 'Turtle', 'Armor', 'A.sate', 'Raon', 'Trico', 'Nak', 'Bigfoot', 'Barney', 'Dragon']]                  
        self.mobiles2 = ['Fox', 'Knight', 'Jolteon', 'Barney', 'Dragon'] 

        self.buttons22 = []                                     # Lista: Sirve para condicionar las funciones vinculadas a eventos: bind -->  mouse_move, mouse_stop, mouse_clic  
        for index1, mobil in enumerate(mobiles):                # Iterador(mobil) = 11 elementos: 1 sublistasssss
            for index2, texto in enumerate(mobil):              # Iterador(texto) = 1  elemento:  'Frog'...
                number = 11 if index1 == 1 else 0               # number: cambie su valor de 0 a 11 si su condicion se cumple

                btn = DefaultButtonCls (self.frame_1, 
                                        text=texto, 
                                        command= self.indices(index2 + number)
                                        )

                n1 = 5 if index2 == 0 else 0        
                n2 = 5 if index2 == 10 else 0
                btn .grid(column=index2 , row=index1 , pady=3, padx=(n1,n2))

                # Enlaces: Cambian el color de los botones:
                btn.bind("<Enter>", self.enter_mouse)
                btn.bind("<Leave>", self.leave_mouse)
                btn.bind("<ButtonPress-1>", self.press_mouse)
                btn.bind("<ButtonRelease-1>", self.release_mouse)

                if texto in self.mobiles2: btn.config(fg='yellow')
                self.buttons22.append(btn)



    def enter_mouse(self, event):
        # Evento: Entrada del mouse sobre el boton.
        # Dice: Si el color del boton no es verde:
        if not event.widget .cget('bg') == '#bdfe04':             # Color(fondo): Verde
            event.widget .config(bg="#24364a")                    # Color(fondo): Celeste apagado

       
    def leave_mouse(self, event):
        # Evento: Salida del mouse sobre el boton.
        # Dice: Si el color del boton no es verde:
        if not event.widget .cget('bg') == '#bdfe04':             # Color(fondo): Verde
            event.widget.config(bg='#11161d')                     # Color(fondo): Azulino oscuro


    # Tarea: - Cambia el color del boton presionado actual a [VERDE-NEGRO]
    def press_mouse(self, event):
        # Evento: Botón presionado.
        event.widget .config(bg='#bdfe04', fg='black')            # Color(fondo): Verde  /  Color(texto): Negro
                     
        for btn in (self.buttons22):
            # Dice: Si cualquiera de los 22 botones no tiene esta configuracion (fondo: Verde - texto: Negro)
            if btn != event.widget:
                # Description (if-else): Configura los botones a sus colores por default.
                if btn .cget('text') in self.mobiles2:
                    btn .config (bg='#11161d', fg='yellow')       # Color(fondo): Azulino  /  Color(texto): Amarillo 
                else:
                    btn .config (bg='#11161d', fg='white')        # Color(fondo): Azulino  /  Color(texto): Blanco

        # Description: Ultimo boton presionado.
        self.container1 = event.widget


    # Tarea: - Cambia el color del boton presionado actual a default, si no coincide con el mismo boton presionado
    def release_mouse(self, event):
        # Evento: Botón soltado.
        
        # Description: Ultimo boton en dejar de ser presionado.
        widget_press = event.widget 
        # Description: Ultimo widget en dejar de ser presionado
        widget_release = event.widget.winfo_containing(event.x_root, event.y_root)

        if widget_press != widget_release:
            # Description (if-else): Configura el ultimo boton en dejar de ser presionado a sus colores por default.
            if widget_press .cget('text') in self.mobiles2:
                widget_press .config (bg='#11161d', fg='yellow')
            else:
                widget_press .config (bg='#11161d', fg='white')


    # Tarea: - Quita la seleccion del boton presionado
    def uncheck_selection(self):
        # Dice: Si se presiono un boton.
        if self.container1 is not None:
            # Description (if-else): Configura el ultimo boton presionado a sus colores por default.
            if self.container1 .cget('text') in self.mobiles2:
                self.container1 .config (bg='#11161d', fg='yellow')
            else:
                self.container1 .config (bg='#11161d', fg='white')
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
#********************************                ██████             aqui me quedo

# Frame contenedor de checkbuttons y labels
class ModeConfigurerCls(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, kwargs)

        #____Métodos Llamados:
        self.create_label()
        self.create_checkbutton()
        self.check_checkbox()

    def cheeck(self): # ES UN EVENTP QUE ´PASA CUANDO CHECKBUTON 5 CAMBIOA DE VALOR 
        pass
        """ if self.variable.get() == False:
            self.variable.set(True)
        if self.variable.get() == True:
            self.variable.set(False)
        """

    def create_label(self):

        label_option1 = Label (self, text= 'Mover ventana :' , font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)
        label_option2 = Label (self, text= 'Modo Lista :', font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)
        label_option3 = Label (self, text= 'Mover ventanas ', font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)
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

        self.checkbutton1 = CheckbuttonCls (self, command=lambda :self.seleccionar(1), bg='#2b313c', activebackground= '#2b313c', bd=0, borderwidth=0,)
        self.checkbutton2 = CheckbuttonCls (self, bg='#2b313c', activebackground= '#2b313c', bd=0, borderwidth=0,)
        self.checkbutton3 = CheckbuttonCls (self, command=lambda :self.seleccionar(3), bg='#2b313c', activebackground= '#2b313c', bd=0, borderwidth=0,)
        self.checkbutton4 = CheckbuttonCls (self, command=lambda :self.seleccionar(4), bg='#2b313c', activebackground= '#2b313c', bd=0, borderwidth=0,)
        self.checkbutton5 = CheckbuttonCls (self, command=lambda :self.seleccionar(5), bg='#2b313c', activebackground= '#2b313c', bd=0, borderwidth=0,)
        self.checkbutton6 = CheckbuttonCls (self, command=lambda :self.seleccionar(6), bg='#2b313c', activebackground= '#2b313c', bd=0, borderwidth=0,)
        self.checkbutton7 = CheckbuttonCls (self, command=lambda :self.seleccionar(7), bg='#2b313c', activebackground= '#2b313c', bd=0, borderwidth=0,)
        self.checkbutton8 = CheckbuttonCls (self, command=lambda :self.seleccionar(8), bg='#2b313c', activebackground= '#2b313c', bd=0, borderwidth=0,)
    
        self.checkbutton1 .grid (column=1, row=0, pady=(10,0))
        self.checkbutton2 .grid (column=1, row=1, pady=(0,0))
        self.checkbutton3 .grid (column=3, row=0, pady=(10,0))
        self.checkbutton4 .grid (column=3, row=1, pady=(0,0))
        self.checkbutton5 .grid (column=5, row=0, pady=(10,0))
        self.checkbutton6 .grid (column=5, row=1, pady=(0,0))
        self.checkbutton7 .grid (column=7, row=0, padx=(0,200), pady=(10,0),)
        self.checkbutton8 .grid (column=7, row=1, padx=(0,200), pady=(0,0),)


    # Tarea: - Marca las casillas por defecto
    def check_checkbox(self):
        self.checkbutton1 .check()
        self.checkbutton3 .check()


    def seleccionar(self, number=None):

        if number == 1:
            if self.checkbutton1 .variable.get():
                self.master._boolean = True
            else:
                self.master._boolean = False


        if number == 3:
            if self.checkbutton3 .variable.get():
                for i in range(3):
                    self.master._booleans[i] = True
            else:
                for i in range(3):
                    self.master._booleans[i] = False
        

        if number == 4:
            if self.checkbutton4 .variable.get():
                self.master.deactivate_forget_icons()
            else:
                self.master.activate_forget_icons()


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
    def __init__(self, master, mobiles, path_lst,  *args, **kwargs):
        super().__init__(master, *args, kwargs)
        #____Lista de mobiles:
        self.mobiles = mobiles

        #____Coleccion de imagenes  
        self.Miniatures = path_lst

        #____Variables de Control: 
        self._toggle_switch = False

        #____CONTENEDORES INTERNOS: ( 2 )
        self.frame_1 = Frame (self, bg='#31343a', width=116, height=67)    # Color: Plomo       
        self.frame_2 = Frame (self, bg='#11161d', width=60, height=67)     # Color: Azul  

        self.container_2w = Frame (self.frame_1, width=116, height=20, bg='#11161d')
        self.select_mobil = Label (self.frame_1, text='Seleccione  Mobil :', font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)
        self.miniature_mobil = Label (self.frame_2, image=self.Miniatures[0], bd= 0)

        self.create_listbox (width=11, height=1)
        self.create_spinbox (width=13)

        #____Posicionamiento:
        self.frame_1 .grid (column=0, row=0)                                            # MASTER A
        self.frame_2 .grid (column=1, row=0)                                            # MASTER B

        self.container_2w .grid (column=0, row=0, padx=0, pady=(0,2), sticky=N)         # SUB A.1
        self.select_mobil .grid (column=0, row=1, padx=11, pady=0)                      # SUB A.2
        self.spinboxx .grid (column=0, row=2, padx=13, pady=(3,3))                      # SUB A.3

        self.lbl_toggle .grid (column=0, row=0, padx=0, pady=0)                          # SUB.SUB A.1 .1 
        self.listboxx .grid (column=1, row=0, padx=12, pady=(1,0))                      # SUB.SUB A.1 .2

        self.miniature_mobil .grid (padx=2, pady=3)                                     # SUB B.1

        #____Propagacion:
        self.frame_1 .grid_propagate(False)
        self.frame_2 .grid_propagate(False)
        self.container_2w .grid_propagate(False)
        
   

    def change_variable(self, *args):  # ACTIVA: SI SPINBOX_VARIABLE CAMBIA DE VALOR - BORRA LA LISTA DE LISTBOX, MANDA A LLAMAR A UPDATE Y CAMBIA LAS MINIATURAS
        spin = self.spinboxx.get().capitalize()

        if spin == '':
            self.listboxx .delete(0, END)
        else:    
            list_new = []
            for index, i in enumerate(self.mobiles):
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

        for index, i in enumerate(self.mobiles):     
            if self.spinbox_variable.get() == i:            # ANTES DABA ERROR CON: self.spinboxx .!toplvel.!frame,etc
                self.master.create_windows(
                lambda top1: TopIzqCls  (top1, index, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, self.master.main_lst, self.master.ico2_lst, self.master.ico4_lst),
                lambda top2: TopDerCls  (top2, index, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, self.master.main_lst, self.master.ico2_lst),
                lambda top3: TopStufCls (top3, index, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, self.master.main_lst, self.master.ico2_lst), index)
                break                                       # Sin breack el programa seguiria buscando coincidencias despues del enter, y guardaria un error
        


        #self.after_cancel(self.fter)            
        if self._toggle_switch == True:  # almacena todas las llamadas si se da enter
            print(4444)
           
            #self.fter = self.after(4000, self.automatic_deletion) 
            #print(self.master.master.master.a)

    def automatic_deletion(self):  # ACTIVA: ** SI ES LLAMADO POR OPEN_WINDOWS ** Y SI LA VARIABLE DE CONTROL NO ES NONE - LIMPIA SPINBOX
        self.spinboxx .delete(0, END)





    def change_toggle(self, event=None):# CAMBIA IMAGEN ROJO-VERDE Y VICEVERSA
        # Evento: Click izquierdo.
        if not self._toggle_switch == True:                                                     # -1
            self._toggle_switch = True                                                          # >>>>
            self.lbl_toggle .config(image=self.Miniatures[24])                                  # >>>>
            #self.unbind('',self.master.off_move)                                                # >>>>
            
            # 1- Si self._switch es False :▼▼▼▼   [ Predeterminado False ]
                # 1.1-  Asiga self._switch = True
                # 1.2-  Cambia la imagen en el label por el color verde
                # 1.3-  Desactiva el enlace self.on_move_all
   
        else:                                                                                   # -1
            self._toggle_switch = False                                                         # >>>>
            self.lbl_toggle .config (image=self.Miniatures[23])                                 # >>>>
            #self.master.off_move = self.bind_all("<B1-Motion>", self.master.on_move_all)        # >>>>

            # 1- Entonces si self._switch es True :▼▼▼▼
                # >>>>  Asiga self._switch = False
                # >>>>  Cambia la imagen en el label por el color rojo
                # >>>>  Activa el enlace self.on_move_all


    def validate_text(self, text, arg): # SIEMPRE QUE INSERTE TEXTO EN SPINBOX - NO PERMITE NUMEROS,SIMBOLOS,ESPACIOS Y CONTROLA LA CANTIDAD
        if all (i not in "0123456789ñ[{!¡¿?<>(|#$%&),_-°'}] +-*/=" for i in text) and len(text) < 14:   
                return True                                                 
        return False  

    def create_spinbox(self, **args):        
        self.spinboxx = Spinbox (self.frame_1, **args)
        
        self.spinbox_variable = StringVar()

        self.all_register = (self.register(self.validate_text), '%P', '%S')
        self.spinboxx.config (values=self.mobiles,
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
    def __init__(self, master, index, value1=1, value2=0, *args, **kwargs):
        super().__init__(master, bg='black', *args, **kwargs)
        self.value1 = value1
        self.value2 = value2

        self.image = Image.open(index)
        self.image_copy = self.image .copy()

        self.photo_image = ImageTk.PhotoImage(self.image)

        self.img = Label(self, image=self.photo_image, bg='black')
        self.img .pack(fill='both', expand=True)
        self.img .bind('<Configure>', self.resize)

    def resize(self, event=None):
        self.image = self.image_copy .resize((self.master.winfo_width(), self.master.winfo_height() // self.value1 - self.value2))
        self.photo_image = ImageTk.PhotoImage(self.image)
        self.img .config(image=self.photo_image)
    
#********************************        ██████████████
#********************************        ██          ██
#********************************        ██  ██████  ██
#********************************        ██  ██  ██  ██
#********************************        ██  ██████  ██
#********************************        ██          ██
#********************************        ██  ██████  ██
#********************************        ██  ██  ██  ██
#********************************        ██  ██████  ██
#********************************        ██          ██
#********************************        ██████████████

class IconsCls(Frame):
    def __init__(self, master, path_lst1=None, path_lst2=None, indice1=None, indice2=None, frames=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        #____Variables de control: 
        self.indice1 = indice1                       # Type: entero           - Caracteres: 0 - 21              Funcion: Rastrear el botón presionado 

        self.var1 = False                            # Type: booleano         - Caracteres: False - True        Funcion: Alternar la ejecucion (if - else)
        self.var2 = False                            # Type: booleano         - Caracteres: False - True        Funcion: Alternar la ejecucion (if - else)

        self.option = None                           # Type: entero           - Caracteres: 0 - 4               Funcion: Rastrear el botón presionado

        self.variable = False                        # Type: booleano         - Caracteres: False - True        Funcion: Permitir o denegar la ejecucion del metodo que muestra la interface vertical de 5 botones

        self.indice2 = indice2                       # Type: entero           - Caracteres:                     Funcion:
        self.frames = frames                         # Sin uso   

        self.off_after = None                        # Type: None - string    - Caracteres: String              Funcion: Guardar la funcion after para cancelarla despues

        self.off_motion = None                       # Type: None - string    - Caracteres: String              Funcion: Guardar la funcion after para cancelarla despues


        #____Colección de Imágenes:
        self.Images  = path_lst1        # Coleccion: Imagenes principales para las ventanas
        self.Icons_1 = path_lst2        # Coleccion: Iconos N°2   [ Destino: Class.IconsCls ]

        

        #____Enlaces: 
        self.master.bind("<ButtonRelease-1>", self._release)
        self.bind('<Map>', self.activate_motion)
        self.bind('<Unmap>', self.deactivate_motion)


        #____Metodos Llamados:_
        self.create_container_1()
        self.create_container_2()
        self.create_list_interfaces()
        self.create_sizegrip()


    ###########################################################################################################################################
    ################################  ENLACES EXTERIORES  #####################################################################################


    # Tarea: - Ejecutar el metodo: [ open_interface_buttons ] no se bien
    def _release(self, event=None):
        self.variable = False


    # Tarea: - Activar el evento motion, cuando se mapea la interface global
    def activate_motion(self, event=None):
        self.off_b1_motion = self.master.bind('<B1-Motion>', self._deactivate_motion)
        #print('error 1')
        self.off_motion = self.master.bind("<Motion>", self.motion_open_interface_vertical)

        #self.off_leave = self.master.master.bind

        # Description: Ejecuta la funcion enlazada al evento movimiento de raton que no se ejecuto despues de mapearse su contenedor
        self.motion_open_interface_vertical()
        # Description: (Solucion temporal): Abre la interface vertical de botones que no se visualiza al segundo intento de abrir la interface total
        self.motion_open_interface_vertical()
        

    # Tarea: - Desactivar el evento motion
    def deactivate_motion(self, event=None):
        #self.master.unbind("<B1-Motion>", self.off_b1_motion)
        #print('error 2')
        self.master.unbind("<Motion>", self.off_motion)


    def _deactivate_motion(self, event=None):
        print(3333333333333333333333333333333333333333333333333)
        pass
        #self.master.unbind("<Motion>", self.off_motion)

        """ e= event.x
        #print(111111111) # hacer que cusndo se presione b1 motion se pare la secuencia para borrar la interface verticsl y si no esta visible que no aparezca y lo contrario
        #self.master.unbind("<Motion>", self.off_motion)
        if self.frame_container_global_1.winfo_ismapped():
            #print('______ismaped_______________', e)
            self.frame_container_global_2 .pack_forget()
            self.frame_container_global_2 .pack(side='right', fill='both', expand=True)

            # Description: Muestra la interface de botones.
            self.frame_container_global_1 .pack(side='left', fill='y', expand=False)
        else:
            self.frame_container_global_1 .pack_forget() """

    # Tarea: - Crear el sizegrip     
    def create_sizegrip(self):
        self.grip = ttk.Sizegrip(self, style='TSizegrip')
        self.grip .place (relx=1.0, rely=1.0, anchor='center')
        ttk.Style().configure('TSizegrip', bg='black')

    ###########################################################################################################################################
    ################################                                 ##########################################################################
    ################################  INTERFACE VERTICAL DE BOTONES  ##########################################################################
    ################################                                 ##########################################################################
    ###########################################################################################################################################

    #---------------------- CONTENEDOR GLOBAL 1 -------------------------------

    # Tarea: - Crear la interface izquierda vertical de botones
    def create_container_1(self):
        # [ 1 ] self.frame_container_global_1             : Interface izquierda vertical de botones                : NO POSICIONADO

        #____CONTENEDOR EXTERIOR 1:
        self.frame_container_global_1 = Frame(self, bg="#1b1d22",)                      # Color(fondo): Gris oscuro
        self.frame_container_global_1 .pack(side='left', fill='y', expand=False)

        #____Peso de distribucion:
        self.frame_container_global_1 .columnconfigure(0, weight=1)
        self.frame_container_global_1 .rowconfigure(0, weight=0)
        self.frame_container_global_1 .rowconfigure(1, weight=0)
        self.frame_container_global_1 .rowconfigure(2, weight=0)
        self.frame_container_global_1 .rowconfigure(3, weight=0)
        self.frame_container_global_1 .rowconfigure(4, weight=1)

        #________Metodos Llamados:
        self.create_buttons_manager()
    

    #-------------------- BOTONES ADMINISTRADORES ---------------------------


    # Tarea: - Crea los botones de la interface vertical de botones
    def create_buttons_manager(self):
        # [ 1 ] self.button_1 ( 0 )              Abre [imagen     :  Ayuda para medir el mobil ]    : POSICIONADO
        # [ 2 ] self.button_2 ( 1 )              Abre [Interface 1:  Delay general             ]    : POSICIONADO
        # [ 3 ] self.button_3 ( 2 )              Abre [Sin uso                                 ]    : POSICIONADO
        # [ 4 ] self.button_4 ( 3 )              Abre [Sin uso                                 ]    : POSICIONADO
        # [ 5 ] self.button_5 ( 2 )              Abre [Interface 2:  Ajustes                   ]    : POSICIONADO

        #____BOTONES: ( 5 ) 
        self.button_1 = Button(self.frame_container_global_1, image=self.Icons_1[8], command=lambda:self.open_interface(0), bg='black',  bd=0)
        self.button_2 = Button(self.frame_container_global_1, image=self.Icons_1[8], command=lambda:self.open_interface(1), bg='black',  bd=0)
        self.button_3 = Button(self.frame_container_global_1, image=self.Icons_1[8], command=lambda:self.open_interface(2), bg='black',  bd=0)
        self.button_4 = Button(self.frame_container_global_1, image=self.Icons_1[8], command=lambda:self.open_interface(3), bg='black',  bd=0)
        self.button_5 = Button(self.frame_container_global_1, image=self.Icons_1[4], command=lambda:self.open_interface(2), bg='#1b1d22', activebackground='#1b1d22', bd=0)    # Color(fondo): Gris oscuro

        #____Posicionamiento:
        self.button_1 .grid(column=0, row=0, padx=5, pady=5)
        self.button_2 .grid(column=0, row=1, padx=5, pady=5)
        self.button_3 .grid(column=0, row=2, padx=5, pady=5)
        self.button_4 .grid(column=0, row=3, padx=5, pady=5)
        self.button_5 .grid(column=0, row=4, padx=5, pady=30, sticky='s')


        #____Eventos(Callback):
        #________________________________________________________
        self.button_1 .bind('<ButtonPress>',   self.iniciar_test)                           # Reiniciar el cronometro y mostrar la interface de botones
        self.button_1 .bind('<ButtonRelease>', self.iniciar_test)                           # Reiniciar el cronometro y mostrar la interface de botones
        #________________________________________________________
        self.button_2 .bind('<ButtonPress>',   self.iniciar_test)                           # Reiniciar el cronometro y mostrar la interface de botones
        self.button_2 .bind('<ButtonRelease>', self.iniciar_test)                           # Reiniciar el cronometro y mostrar la interface de botones
        #________________________________________________________
        self.button_3 .bind('<ButtonPress>',   self.iniciar_test)                           # Reiniciar el cronometro y mostrar la interface de botones
        self.button_3 .bind('<ButtonRelease>', self.iniciar_test)                           # Reiniciar el cronometro y mostrar la interface de botones
        #________________________________________________________
        self.button_4 .bind('<ButtonPress>',   self.iniciar_test)                           # Reiniciar el cronometro y mostrar la interface de botones
        self.button_4 .bind('<ButtonRelease>', self.iniciar_test)                           # Reiniciar el cronometro y mostrar la interface de botones
        #________________________________________________________
        self.button_5 .bind('<ButtonPress>',   self.iniciar_test)                           # Reiniciar el cronometro y mostrar la interface de botones
        self.button_5 .bind('<ButtonRelease>', self.iniciar_test)                           # Reiniciar el cronometro y mostrar la interface de botones
        self.off_enter = self.button_5 .bind("<Enter>", self.enter_mouse_settings)          # Reiniciar el cronometro y mostrar la interface de botones
        self.button_5                  .bind("<Leave>", self.leave_mouse_settings)          # Reiniciar el cronometro y mostrar la interface de botones
        #________________________________________________________


    ###########################################################################################################################################
    ###########################  MÉTODOS COMMAND: GLOBAL 1  ###################################################################################
    ###########################################################################################################################################

    #------------------------------------- 1 ------------------------------------------

    # Tarea: - Muestra y oculta las imagenes del boton presionado
    def open_interface(self, number=None):

        # Si presionas un boton diferente
        if self.option != number and self.option is not None:
            self.var1 = False
        # Entonces. Si presionas el mismo boton
        else:
            self.option = number


        # Description: Muestra la imagen del boton presionado
        if not self.var1:
            self.var1 = True

            # Description: Oculta el logo
            self.label_logo .grid_remove()
            # Description: Oculta la imagen del boton presionado anteriormente
            self.list_interfaces[self.option] .grid_remove()
            # Description: Muestra la imagen del boton presionado
            self.list_interfaces[number]. grid(sticky='news')


        # Description: Muestra el logo
        else:
            self.var1 = False

            #----------------------------------------ACTIVA EL EVENTO------------------------------------------------
            if number == 2:
                # Description 1: Activa el evento para cambiar la imagen del boton setting a encendido
                # Description 2: Si se llama al metodo con el argumento 1 cambia la imagen del boton setting a encendido
                self.activate_enter_settings(1)
            #--------------------------------------------------------------------------------------------------------

            # Description: Oculta la imagen
            self.list_interfaces[number] .grid_remove()
            # Description: Posiciona el logo
            self.label_logo .grid()

        self.option = number


    ###########################################################################################################################################
    ##########################  MÉTODOS BIND: GLOBAL 1  #######################################################################################
    ###########################################################################################################################################

    #------------------------------------- 1 ------------------------------------------

    # Tarea: -  Reiniciar el conometro y mostrar la interface de botones
    def iniciar_test(self, event=None):
         # Description: Actualiza la posicion del contenedor 2 para que sea visible el contenedor 1. [fraccion: para visualizar la interface de botones ]
        self.frame_container_global_2 .pack_forget()
        self.frame_container_global_2 .pack(side='right', fill='both', expand=True)

        # Description: Muestra la interface de botones.
        self.frame_container_global_1 .pack(side='left', fill='y', expand=False)

        # Description: Variable asignada en el método "timer" para cancelar la funcion after                Prederminado: None
        if self.off_after is not None:
            self.after_cancel(self.off_after)
        self.conteo = 1.5

        # Metodo llamado:
        self.timer()

    #____________________________________ 1.1 _________________________________________
    # Tarea: -  Iniciar el conometro para ocultar la interface de botones
    def timer(self):
        # Metodo llamado:
        self.run_timer()

        if self.conteo >= 0:
            self.off_after = self.after(1000, self.timer)

        # Entonces si "self.conteo" es menor a 0:
        else:
            self.off_after = None
            # Description: Oculta la interface de botones.
            self.frame_container_global_1 .pack_forget()       

    #____________________________________ 1.2 _________________________________________
    # Tarea: -  Servir de conometro
    def run_timer(self):
        if self.conteo >= 0:
            self.conteo -= 1


    #------------------------------------- 2 ------------------------------------------

    # Tarea: -  Cambiar la imagen del boton setting a encendido
    def enter_mouse_settings(self, event=None):
        # Evento: Entrada del mouse sobre el boton.
        event.widget.config(image=self.Icons_1[5])

    #------------------------------------- 3 ------------------------------------------

    # Tarea: -  Cambiar la imagen del boton setting a apagado    
    def leave_mouse_settings(self, event=None):
        # Evento: Salida del mouse sobre el boton.
        event.widget.config(image=self.Icons_1[4])


    ###########################################################################################################################################
    ################################                                   ########################################################################
    ################################  INTERFACE DERECHA DE DESARROLLO  ########################################################################
    ################################                                   ########################################################################
    ###########################################################################################################################################

    
    #---------------------- CONTENEDOR GLOBAL 2 -------------------------------
    
    # Tarea: -  Crear la interface derecha de desarrollo
    def create_container_2(self):
        # [ 1 ] self.frame_container_global_2         : Interface global derecha                     : POSICIONADO

        #____CONTENEDOR EXTERIOR 2:
        self.frame_container_global_2  = Frame(self, bg='#2b313c')                            # Color(fondo): Gris claro
        self.frame_container_global_2 .pack(side='right', fill='both', expand=True)

        #____Peso de distribucion:
        self.frame_container_global_2 .columnconfigure(0, weight=1)
        self.frame_container_global_2 .rowconfigure(0, weight=1)

        #________Metodos Llamados:
        self.create_image_logo()
        self.create_subcontainer_1()
        self.create_subcontainer_2()


    # Tarea: - Crea las imagenes que se posicionan directamente en la ventana sin contenedor adicional
    def create_image_logo(self):
        # [ 1 ] self.label_logo                       : Imagen: Logo "ASH"                                     : POSICIONADO
        # [ 2 ] self.frame_image_guiadetiro           : Imagen: Ayuda para medir el mobil                      : NO POSICIONADO

        #____IMAGEN: ( 1 widget)
        self.label_logo = Label(self.frame_container_global_2, image=self.Icons_1[3], bg='black', bd=0)
        self.label_logo .grid(column=0, row=0)

        #____IMAGEN: ( 1 instancia )
        self.frame_image_guiadetiro = ResizeCls(self.frame_container_global_2, self.Images[self.indice1][1], bd=0)


    ###########################################################################################################################################
    ################################                               ############################################################################
    ################################  SUBCONTENEDOR '1': GLOBAL 2  ############################################################################
    ################################                               ############################################################################
    ###########################################################################################################################################

    # Tarea: - Crear el "PRIMER" subcontenedor interno del contenedor global 2     
    def create_subcontainer_1(self):
        # [ 1 ] glb2_frame_subcontainer_1            Funcion: AImagenes para mostrar el delay general        : NO POSICIONADO

        self.glb2_frame_subcontainer_1 = Frame(self.frame_container_global_2)
        
        #____Peso de distribucion:
        self.glb2_frame_subcontainer_1 .columnconfigure(0, weight=1)
        self.glb2_frame_subcontainer_1 .rowconfigure(0, weight=1)
        self.glb2_frame_subcontainer_1 .rowconfigure(1, weight=0)
        self.glb2_frame_subcontainer_1 .rowconfigure(2, weight=1)

        #________Metodos Llamados:
        self.create_images_sub1()
        self.create_mini_interface_sub1()

    
    # Tarea: - Crea las imagenes que se posicionan en el primer subcontenedor del contenedor global 2
    def create_images_sub1(self):
        # [ 1 ] self.image_delay1  : Imagen: Delay General (F8, S1, S2, DD1, DD2)                                  : POSICIONADO
        # [ 2 ] self.image_delay2  : Imagen: Delay General (1+, 2+, SS, Ang-Maximo)                                : POSICIONADO 
        # [ 3 ] self.image_delay3  : Imagen: Delay General (TP, Vida, Ang-Recto, Ang-Maximo)                       : POSICIONADO 
        
        #____IMAGENES: ( 3 instancias )
        self.image_delay1 = ResizeCls(self.glb2_frame_subcontainer_1, self.Images[22][0], 2, 10, bd=0)
        self.image_delay2 = ResizeCls(self.glb2_frame_subcontainer_1, self.Images[22][1], 2, 10, bd=0)
        self.image_delay3 = ResizeCls(self.glb2_frame_subcontainer_1, self.Images[22][2], 2, 10, bd=0)

        #____Orden de apilamiento de imagenes:
        self.image_delay3 .lower()

        #____Posicionamiento:
        self.image_delay1 .grid(column=0, row=0, sticky='news')
        self.image_delay2 .grid(column=0, row=2, sticky='news')
        self.image_delay3 .grid(column=0, row=2, sticky='news')

    
    # Tarea: - Crear una mini interface con un único botón para cambiar el orden de apilamiento de las imagenes que estan en el subcontenedor 1
    def create_mini_interface_sub1(self):
        # [ 1 ] self.frame_manager_button            : Interface del boton para cambiar de imagen             : POSICIONADO
        # [ 2 ] self.button_next                     : Boton para cambiar de imagen                           : POSICIONADO
        # [ 3 ] self.button_next                     : Boton para cambiar de imagen                           : POSICIONADO

        #____INTEFACE DE CONTROL: ( 1 )
        self.frame_manager_button = Frame(self.glb2_frame_subcontainer_1, bg='#1b1d22', bd=0, height=20)
        self.frame_manager_button .grid(column=0, row=1, sticky='ew')

        #____BOTONES: ( 1 )
        self.button_next = Button(self.frame_manager_button, image=self.Icons_1[6], command=self.change_image, bg='#1b1d22', activebackground='#1b1d22', bd=0, cursor='hand2')
        self.button_next .pack()

        #____Eventos(Callback):
        self.button_next .bind("<Enter>", self.enter_mouse_next)
        self.button_next .bind("<Leave>", self.leave_mouse_next)


    ###########################################################################################################################################
    ###########################  MÉTODOS COMMAND: GLOBAL 2  ###################################################################################
    ###########################################################################################################################################
    
    #------------------------------------- 1 ------------------------------------------

    # Tarea: - Cambia el orden de apilamiento de las imagenes que estan en el subcontenedor 1
    def change_image(self):
        if not self.var2:
            self.var2 = True
            self.image_delay2 .lower()
        else:
            self.var2 = False
            self.image_delay2 .lift()


    ###########################################################################################################################################
    #########################  MÉTODOS BIND: GLOBAL 2  ########################################################################################
    ###########################################################################################################################################

    #------------------------------------- 1 ------------------------------------------

    # Tarea: -  Cambiar la flecha de la imagen del boton next a celeste
    def enter_mouse_next(self, event=None):
        # Evento: Entrada del mouse sobre el boton.
        event.widget.config(image=self.Icons_1[7])
    
    #------------------------------------- 2 ------------------------------------------

    # Tarea: -  Cambiar la flecha de la imagen del boton next a blanco
    def leave_mouse_next(self, event=None):
        # Evento: Salida del mouse sobre el boton.
        event.widget.config(image=self.Icons_1[6])


    ###########################################################################################################################################
    ################################                               ############################################################################
    ################################  SUBCONTENEDOR '2': GLOBAL 2  ############################################################################
    ################################                               ############################################################################
    ###########################################################################################################################################
 
    # Tarea: - Crear el "SEGUNDO" subcontenedor interno del contenedor global 2     
    def create_subcontainer_2(self):
        # [ 2 ] glb2_frame_subcontainer_2_settings          : Interface de ajustes        : NO POSICIONADO

        self.glb2_frame_subcontainer_2_settings = Frame(self.frame_container_global_2, bg='#2b313c')    # Color(fondo): Gris claro
        #self.glb2_frame_subcontainer_2_settings .grid()
        
        #____Peso de distribucion:
        """ self.frame_container_settings .columnconfigure(0, weight=1)
        self.frame_container_settings .columnconfigure(1, weight=1)
        self.frame_container_settings .rowconfigure(0, weight=1)
        self.frame_container_settings .rowconfigure(1, weight=1)
        self.frame_container_settings .rowconfigure(2, weight=1) """

        #____Eventos(Callback):
        self.glb2_frame_subcontainer_2_settings .bind('<Map>', self.deactivate_enter_settings) 
        self.glb2_frame_subcontainer_2_settings .bind('<Unmap>', self.activate_enter_settings) 

        #________Metodos Llamados:
        self.create_mini_interface_sub2()


    ###########################################################################################################################################
    #########################  MÉTODOS BIND: GLOBAL 2  ########################################################################################
    ###########################################################################################################################################

    #------------------------------------- 1 ------------------------------------------

    # Tarea: - Desactiva el evento y cambia la imagen a dark
    def deactivate_enter_settings(self, event=None):
        # Description: Desactiva el evento para cambiar la imagen del boton setting a encendido
        self.button_5 .unbind('<Enter>', self.off_enter)
        
        # Description: Cambia la imagen del boton setting a apagado
        self.button_5 .config(image=self.Icons_1[4])

    #------------------------------------- 2 ------------------------------------------

    # Tarea: - Activa el evento y cambia la imagen a light
    def activate_enter_settings(self, var=None, event=None):
        # Description: Activa el evento para cambiar la imagen del boton setting a encendido
        self.off_enter = self.button_5 .bind('<Enter>', self.enter_mouse_settings)

        # Description: Si se llama al metodo con el argumento 1 cambia la imagen del boton setting a encendido
        if var == 1:
            self.button_5 .config(image=self.Icons_1[5])


    ###########################################################################################################################################
    ###########################  MÉTODOS S: GLOBAL 2  ###########################################################################################
    ###########################################################################################################################################

    #------------------------------------- 1 ------------------------------------------

    # Tarea: - Crea los widget internos para los ajustes de la ventana 
    def create_mini_interface_sub2(self):

        #____ETIQUETAS:
        label_1 = Label (self.glb2_frame_subcontainer_2_settings, text='Deshabilitar \nde ventana :' ,font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)
        label_2 = Label (self.glb2_frame_subcontainer_2_settings, text='Bloquear ventana :'          ,font=('Calibri',9,'bold'), bg='#31343a', fg='white', bd=0)

        #____Posicionamiento:
        label_1 .grid(column=0, row=0, padx=(20,5), pady=(10,0), )
        label_2 .grid(column=0, row=1, padx=(20,5), pady=(0,0), )

        #____CASILLAS:
        self.checkbutton1 = CheckbuttonCls(self.glb2_frame_subcontainer_2_settings, command=lambda *arg:self.seleccionar(1, self.indice2), bg='#2b313c', activebackground= '#2b313c', bd=0, borderwidth=0,)
        self.checkbutton2 = CheckbuttonCls(self.glb2_frame_subcontainer_2_settings, command=lambda *arg:self.seleccionar(2, self.indice2), bg='#2b313c', activebackground= '#2b313c', bd=0, borderwidth=0,)
       
        #____Posicionamiento:
        self.checkbutton1 .grid(column=1, row=0, padx=(0,0), pady=(10,0))
        self.checkbutton2 .grid(column=1, row=1, padx=(0,0), pady=(0,0))


    def seleccionar(self, indice_button=None, indice_ventana=None):
        if indice_button == 1:
            if self.checkbutton1 .variable.get():
                self.master.master._disabled[indice_ventana] = True
            else:
                self.master.master._disabled[indice_ventana] = False

                

    # Tarea: -  Muestra y oculta la interface vertical de botones.
    def motion_open_interface_vertical(self, event=None):
        if not self.variable:
            self.iniciar_test()




    # Tarea: - Crear una lista que almacene todas las interfaces o imagenes que abran los botones de la interface de botones
    def create_list_interfaces(self):
        # [ 1 ] : self.frame_image_guiadetiro            : Imagen: Ayuda para medir el mobil                        active: [Boton 1]
        # [ 2 ] : self.frame_container_album_2           : Contenedor: Imagenes para mostrar el delay general       active: [Boton 2]
        self.list_interfaces = [self.frame_image_guiadetiro, self.glb2_frame_subcontainer_1, self.glb2_frame_subcontainer_2_settings]



    def checked(self):
        self.checkbutton1 .check()

    
   


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
    def __init__(self, master, indice, arg_0=None, arg_1=None, arg_2=None, arg_3=None, arg_4=None, arg_5=None, arg_6=None, arg_7=None, main_lst=None, icon_lst1=None, icon_lst2=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        #____Colección de Imágenes:
        self.Images = main_lst
        self.Icons = icon_lst1
        self.Mobiles = icon_lst2

        #____Variables de Control: Indice de la sublista de b
        self.indice = indice

        #____Lista de indices de las imagenes:
        self._0 = arg_0
        self._1 = arg_1
        self._2 = arg_2
        self._3 = arg_3
        self._4 = arg_4
        self._5 = arg_5
        self._6 = arg_6
        self._7 = arg_7


        self._start = None
        self._btn = None

        #____Peso de distribucion principal:
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure   (0, weight=1)
        self.grid_rowconfigure   (1, weight=1)

        #____Metodos Llamados:
        self.open_interface()


    # Tarea: - Abrir la interface del mobil
    def open_interface(self):
        if self.indice == 17:
            #____Metodos Llamados:
            self.create_container_2()
        else:
            #____Metodos Llamados:
            self.create_container_1()
            #self.button1 .config(state='disabled', cursor='arrow')


    # Tarea: - Crea los contenedores Parte 1  [ INTERFACE: STANDAR ]
    def create_container_1(self):
        # [ 1 ] self.frame_container_global_1       : Interface global N° 1, para mostrar el delay completo del mobil                    : POSICIONADO
        # [ 2 ] self.frame_container_widgets_1      : Interface subglobal de la interface global N°1, para mostrar la mini interface     : POSICIONADO
        # [ 3 ] frame_image_delay_complete          : Imagen: Delay completo del mobil                                                   : POSICIONADO

        #____CONTENEDOR EXTERIOR 1:
        self.frame_container_global_1 = Frame(self)
        self.frame_container_global_1 .grid(sticky='news')

        #____CONTENEDOR INTERIOR:
        self.frame_container_widgets_1 = Frame(self.frame_container_global_1, bg='#1b1d22', bd=0, height=42)
        self.frame_container_widgets_1 .grid(column=0, row=0, sticky='news')

        #____IMAGEN: Delay completo del mobil
        self.frame_image_delay_complete = ResizeCls(self.frame_container_global_1, self.Images[self.indice][self._0], value2=42 ,bd=0)
        self.frame_image_delay_complete .grid(column=0, row=1, sticky='news')

        #____Peso de distribucion:
        self.frame_container_global_1 .columnconfigure(0, weight=1)     
        self.frame_container_global_1 .rowconfigure   (0, weight=0)
        self.frame_container_global_1 .rowconfigure   (1, weight=1)

        #____Peso de distribucion:
        variable = 0 if self.indice != 17 else 1 
        self.frame_container_widgets_1 .columnconfigure(0, weight=variable)
        self.frame_container_widgets_1 .columnconfigure(1, weight=1) 
        self.frame_container_widgets_1 .columnconfigure(2, weight=0)
        self.frame_container_widgets_1 .columnconfigure(3, weight=0) 
        self.frame_container_widgets_1 .rowconfigure   (0, weight=1) 

        #________Metodos Llamados:
        self.create_items_1()

    
    def create_items_1(self):
        # [ 1 ] self.button1                              : Boton "Wind\n00"                                       : NO POSICIONADO
        # [ 2 ] self.button2                              : Boton "Wind\nChart"                                    : POSICIONADO
        # [ 3 ] self.label_switch                         : Label "OFF"                                            : POSICIONADO
        # [ 3 ] self.label_mobil                          : Imagen: Miniatura del mobil                            : POSICIONADO

        self.button1 = Button(self.frame_container_widgets_1, text='Base\nTrico', font=('Calibri',8,'bold'), command=lambda:self.change_interfaces(0), bg='#2b313c', fg='white', activebackground='#4ca6ff', activeforeground='white', bd=0, cursor='hand2')
        self.button2 = Button(self.frame_container_widgets_1, text='Wind\nChart', font=('Calibri',8,'bold'), command=lambda:self.change_interfaces(1), bg='#2b313c', fg='white', activebackground='#4ca6ff', activeforeground='white', bd=0, cursor='hand2')
        self.label_switch = Label(self.frame_container_widgets_1, text='O\nF\nF', font=('Arial',7,'bold'), bg='#1b1d22', fg='white')
        self.label_mobil = Label(self.frame_container_widgets_1, image=self.Mobiles[self.indice], bg='green', bd=0)

        #____Posicionamiento:
        if self.indice == 17:
            self.button1 .grid(column=0, row=0, padx=(0,1), sticky='news')
        self.button2 .grid(column=1, row=0, padx=(1,0), sticky='news')
        self.label_switch .grid(column=2, row=0, sticky='nes')
        self.label_mobil .grid(column=3, row=0, sticky='nes')

        #____Eventos:
        self.button1 .bind("<Enter>", self.enter_mouse)
        self.button1 .bind("<Leave>", self.leave_mouse)

        self.button2 .bind("<Enter>", self.enter_mouse)
        self.button2 .bind("<Leave>", self.leave_mouse)

    
    def change_interfaces(self, number):
        if number == 0:
            self.frame_container_global_1 .grid_remove()
            self.frame_container_global_2 .pack(fill='both', expand=True)


    ###############################################                       ###############################################  
    ###############################################   I N T E R F A C E   ############################################### 
    ###############################################       T R I C O       ###############################################
    ###############################################                       ###############################################

    # Tarea: - Crea los contenedores - Parte 2  [INTERFACE: TRICO]
    def create_container_2(self):
        # [ 1 ] frame_container_global_2            : Interface global N° 2, muestra la interface del trico                              : POSICIONADO
        # [ 2 ] self.frame_container_widgets_1      : Interface subglobal de la interface global N°2, para mostrar la mini interface     : POSICIONADO

        #____CONTENEDOR EXTERIOR 2:
        self.frame_container_global_2 = Frame(self)
        self.frame_container_global_2 .pack(fill='both', expand=True)

        #____CONTENEDOR INTERIOR:
        self.frame_container_widgets_2 = Frame(self.frame_container_global_2, bg='#1b1d22', bd=0, height=42)
        self.frame_container_widgets_2 .pack(fill='both')


        #____Peso de distribucion: Contenedor Interior
        self.frame_container_widgets_2 .columnconfigure(0, weight=1)
        self.frame_container_widgets_2 .columnconfigure(1, weight=1)
        self.frame_container_widgets_2 .columnconfigure(2, weight=1)
        self.frame_container_widgets_2 .rowconfigure   (0, weight=1)
        self.frame_container_widgets_2 .rowconfigure   (1, weight=1)

        #________Metodos Llamados:
        self.create_items_2()


    def create_items_2(self):
        #____BOTONES: ( 4 )
        self.button_1 = Button(self.frame_container_widgets_2, text='Atrás', font=('Calibri',8,'bold'), command=lambda:self.start_test(1), bg='#2b313c', fg='white', activebackground='#4ca6ff', activeforeground='white', bd=0, cursor='hand2')
        self.button_2 = Button(self.frame_container_widgets_2, text='Chart', font=('Calibri',8,'bold'), command=lambda:self.start_test(2), bg='#2b313c', fg='white', activebackground='#4ca6ff', activeforeground='white', bd=0, cursor='hand2', state='disabled')
        self.button_3 = Button(self.frame_container_widgets_2, text='Otros', font=('Calibri',8,'bold'), command=lambda:self.start_test(3), bg='#2b313c', fg='white', activebackground='#4ca6ff', activeforeground='white', bd=0, cursor='hand2', state='disabled')
        self.button_4 = Button(self.frame_container_widgets_2, text='Extra', font=('Calibri',8,'bold'), command=lambda:self.start_test(4), bg='#2b313c', fg='white', activebackground='#4ca6ff', activeforeground='white', bd=0, cursor='hand2')
        self.button_5 = Button(self.frame_container_widgets_2, text='Laser', font=('Calibri',8,'bold'), command=lambda:self.start_test(5), bg='#2b313c', fg='white', activebackground='#4ca6ff', activeforeground='white', bd=0, cursor='hand2')
        self.button_6 = Button(self.frame_container_widgets_2, text='Más',   font=('Calibri',8,'bold'), command=lambda:self.start_test(6), bg='#2b313c', fg='white', activebackground='#4ca6ff', activeforeground='white', bd=0, cursor='hand2')

        #____Posicionamiento:
        self.button_1 .grid(column=0, row=0, pady=(0,1), padx=(2), sticky='news')
        self.button_2 .grid(column=1, row=0, pady=(0,1), sticky='news' )
        self.button_3 .grid(column=2, row=0, pady=(0,1), padx=(2), sticky='news')
        self.button_4 .grid(column=0, row=1, pady=(1,2), padx=(2), sticky='news')
        self.button_5 .grid(column=1, row=1, pady=(1,2), sticky='news')
        self.button_6 .grid(column=2, row=1, pady=(1,2), padx=(2), sticky='news')

        #____Enlaces:
        self.button_1 .bind("<Enter>", self.enter_mouse)
        self.button_1 .bind("<Leave>", self.leave_mouse)

        self.button_2 .bind("<Enter>", self.enter_mouse)
        self.button_2 .bind("<Leave>", self.leave_mouse)

        self.button_3 .bind("<Enter>", self.enter_mouse)
        self.button_3 .bind("<Leave>", self.leave_mouse)
        
        self.button_4 .bind("<Enter>", self.enter_mouse)
        self.button_4 .bind("<Leave>", self.leave_mouse)

        self.button_5 .bind("<Enter>", self.enter_mouse)
        self.button_5 .bind("<Leave>", self.leave_mouse)

        self.button_6 .bind("<Enter>", self.enter_mouse)
        self.button_6 .bind("<Leave>", self.leave_mouse)

        #------------------------------------------------------------------------------------------------------
        # [ 1 ] self.frame_image_delay_trico  : Imagen -->  Base por defecto + delay trico
        # [ 2 ] self.frame_image_delay_raon   : Imagen -->  Base por defecto + delay raon
        # [ 3 ] self.frame_image_1forma       : Imagen -->  Base por defecto + 1 Forma
        # [ 4 ] self.frame_image_laser        : Imagen -->  Base por defecto + Laser

        #____IMAGENES: ( 4 )
        self.frame_image_delay_trico = ResizeCls(self.frame_container_global_2, self.Images[17][2], value2=42, bd=0)
        self.frame_image_delay_raon = ResizeCls(self.frame_container_global_2, self.Images[17][3], value2=42, bd=0)
        self.frame_image_1forma = ResizeCls(self.frame_container_global_2, self.Images[17][4], value2=42, bd=0)
        self.frame_image_laser = ResizeCls(self.frame_container_global_2, self.Images[17][5], value2=42, bd=0)

        #____Posicionamiento:
        self.frame_image_delay_trico .pack(fill='both', expand=True)
        #self.frame_image_delay_raon .pack(fill='both', expand=True)
        #self.frame_image_1forma .pack(fill='both', expand=True)
        #self.frame_image_laser .pack(fill='both', expand=True)

        self.collection = [None, self.frame_image_delay_trico, None, None, self.frame_image_1forma, self.frame_image_laser, self.frame_image_delay_raon]


    def start_test(self, number):
        # [ 1 ] : number           : Número asignado al botón presionado
        # [ 2 ] : self._start      : Controla la direccion de ejecucion
        # [ 3 ] : self._indice     : Indice de la lista de imagenes actualmente visible


        # Description(if): Solo se ejecuta 1 vez cuando es creado el contenedor global
        if self._start is None:
            self._start = number                     # Guarda el numero del boton
            self._indice = 1                         # Asigna el indice de la imagen por default

            # Description: Metodo Interno llamado
            self.change_image(number)


        # Description(elif): Si se presiona el mismo boton anterior, quita la imagen visible actual + posiciona la imagen por default
        elif self._start == number and number != 1:
            # Description: Hace de controlador (if/else)
            self._start = '...'

            # Description: Quita la imagen actualmente visible
            self.collection[self._indice] .pack_forget()

            # Description: Posiciona la imagen por default
            self.collection[1] .pack(fill='both', expand=True)

            # Description: Llama al metodo de la ventana derecha y posiciona la imagen por default
            self.master.frames[1].change_image(1, self._indice)

            # Description: Actualiza el indice actualmente posisionado
            self._indice = 1


        else:
            self.change_image(number)



    def change_image(self, number):

        #--------------------------------- ATRAS --------------------------------------
        if number == 1:
            # Description: Quita la interface del trico
            self.frame_container_global_2 .pack_forget()
            # Description: Crea la interface standar del mobil y el sizegrip
            self.create_container_1()
            self.create_sizegrip()

            
        #--------------------------- (CHART) DISABLED ---------------------------------
        elif number == 2:
            pass


        #--------------------------- (OTROS) DISABLED ---------------------------------
        elif number == 3:
            pass


        #-------------------------------- EXTRA ---------------------------------------
        elif number == 4:
            # Description: Quita la imagen actual + Posiciona la nueva imagen
            self.collection[self._indice] .pack_forget()
            self.collection[number] .pack(fill='both', expand=True)
            
            # Description: Llama al metodo de la ventana derecha para cambiar el orden de apilamiento de las imagenes
            self.master.frames[1].change_image(number, self._indice)

            # Description: Almacenan el numero del boton presionado
            self._indice = number
            self._start = self._indice


        #-------------------------------- LASER ---------------------------------------
        elif number == 5:
            # Description: Quita la imagen actual y posiciona la nueva imagen
            self.collection[self._indice] .pack_forget()
            self.collection[number] .pack(fill='both', expand=True)
            
            # Description: Llama al metodo de la ventana derecha para cambiar el orden de apilamiento de las imagenes
            self.master.frames[1].change_image(number, self._indice)

            # Description: Almacenan el numero del boton presionado
            self._indice = number
            self._start = self._indice
        

        #---------------------------------- MÁS ---------------------------------------
        elif number == 6:
            # Description: Quita la imagen actual y posiciona la nueva imagen
            self.collection[self._indice] .pack_forget()
            self.collection[number] .pack(fill='both', expand=True)
            
            # Description: Llama al metodo de la ventana derecha para cambiar el orden de apilamiento de las imagenes
            self.master.frames[1].change_image(number, self._indice)

            # Description: Almacenan el numero del boton presionado
            self._indice = number
            self._start = self._indice


    def create_sizegrip(self):
        self.grip = ttk.Sizegrip(self, style='TSizegrip')
        self.grip .place (relx=1.0, rely=1.0, anchor='center')
        ttk.Style().configure('TSizegrip', bg='black')


    ######################################################################################################################  
    ###################################################################################################################### 
    ######################################################################################################################
    ######################################################################################################################


    def enter_mouse(self, event):
        # Entrada del mouse sobre el boton (Imagen: change)
        event.widget.config(bg='#4ca6ff')

    def leave_mouse(self, event):
        # Salida del mouse sobre el boton (Imagen: default)
        event.widget.config(bg='#2b313c')

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

        #____Indice del boton:
        self.indice = indice

        #____Colección de Imágenes:
        self.Images = main_lst

        #____Lista de indices de las imagenes:
        self._0 = arg_0
        self._1 = arg_1
        self._2 = arg_2
        self._3 = arg_3
        self._4 = arg_4
        self._5 = arg_5
        self._6 = arg_6
        self._7 = arg_7

        #____Variables de Control:
        self.x1 = 0
        self.x2 = 100
        self.y1 = 67
        self.y2 = 100

        #____Variables de Control para los Eventos:
        self._button_1 = False  # Creado para el evento: Button-1
        self._motion_1 = False  # Creado para el evento: Motion

        #____Peso de distribucion:
        self.columnconfigure(0, weight=1)
        self.rowconfigure   (0, weight=1)

        #____Eventos:
        # [ 1 ]  :  Activa todas las opciones de imagenes que se pueden mostrar
        # [ 2 ]  :  Quita el Label-texto: "Haga click" para mostrar el angulo 77"
        # [ 3 ]  :  Posiciona y Quita los widgets:   [ Label-texto"Haga click" para mostrar el angulo 77" ], [ Label-texto: "↑" ]
        # [ 4 ]  :  Posiciona y Quita el widget:     [ Label-texto"Haga click" para mostrar el angulo 77" ]
        # [ 5 ]  :  Soluciona error: Reactiva el evento motion que se desactiva por algun motivo cuando se desactiva el evento motion de la interface de iconos
        
        self.master.bind("ash", lambda _: self.activate_version())                                          # 1 - SIN CONFLICTO
        self.off_leave  = self.bind ('<Leave>', lambda arg:self.label_text_mostrar_77 .grid_remove())       # 2
        self.off_button = self.master.bind("<Button-1>",   self.open_text_flecha)                           # 3
        self.off_motion = self.master.bind("<Motion>",     self.open_text_mostrar_77)                       # 4
        self.master.bind("<Map>", self.reactivate_motion)                                                          # 5 - DESACT

        #____Metodos Llamados:
        self.open_interface()



    # Tarea: - Abrir la interface del mobil
    def open_interface(self):

        if self.indice == 17:

            # Description: [ DESACTIVA LOS EVENTOS ]
            self.unbind("", self.off_leave)  # Puede crear errores, falta poner <Leave>
            self.master.unbind("<Button-1>", self.off_button)
            self.master.unbind("<Motion>", self.off_motion)

            #____Metodos Llamados:
            self.create_container_2()

        else:
            #____Metodos Llamados:
            self.create_container_1()




    # Tarea: - Crea el primer contenedor global  [ INTERFACE: STANDAR]
    def create_container_1(self):
        # [ 1 ] self.frame_container_global_1       : Contenedor global N° 1, muestra la imagen base standar del mobil           : POSICIONADO

        #____CONTENEDOR EXTERIOR 1:
        self.frame_container_global_1 = Frame(self)
        self.frame_container_global_1 .grid(sticky='news')

        #____Peso de distribucion:
        self.frame_container_global_1 .columnconfigure(0, weight=1)
        self.frame_container_global_1 .rowconfigure   (0, weight=1)

        #________Metodos Llamados:
        self.create_items_1()


    def create_items_1(self):
        # [ 1 ] self.frame_image_base_initial        : Imagen: Base inicial del mobil                                        : POSICIONADO
        # [ 1 ] self.frame_image_base_77             : Imagen: Base 77 del mobil                                             : NO POSICIONADO
        # [ 1 ] self.label_text_mostrar_77           : Label-Texto: "Haga click" para mostrar el angulo 77"                  : NO POSICIONADO
        # [ 1 ] self.label_text_flecha               : Label-Texto: "↑"                                                      : NO POSICIONADO

        #____IMAGENES:  ( 2 instancias )
        self.frame_image_base_initial = ResizeCls(self.frame_container_global_1, self.Images[self.indice][self._2], bd=0)
        self.frame_image_base_77      = ResizeCls(self.frame_container_global_1, self.Images [self.indice][self._3], bd=0)

        #____WIDGETS:  ( 2 widgets )
        self.label_text_mostrar_77        = Label(self.frame_container_global_1, text="Haga ' Click ' para mostrar:\nAngulo ' 77 '", font=('Bickham Script Pro',8,'bold'), bg='#2f3337', fg='white', width=50, height=2)
        self.label_text_flecha            = Label(self.frame_container_global_1, text='↑', font=('Calibri',30,'bold'), bg='#2f3337', fg='green2', width=1, height=1)

        #____Posicionamiento:
        self.frame_image_base_initial .grid(column=0, row=0, sticky='news')
        self.frame_image_base_77      .grid(column=0, row=0, sticky='news')
        self.label_text_mostrar_77    .grid(column=0, row=0, ipadx=5, ipady=5, sticky='n',)
        self.label_text_flecha        .grid(column=0, row=0, ipadx=5, sticky=SE)

        #____Desposicionados: o #____Orden de apilamiento de imagenes:
        self.frame_image_base_77   .grid_remove()
        self.label_text_mostrar_77 .grid_remove()
        self.label_text_flecha     .grid_remove()





    # Tarea: - Crea el segundo contenedor global  [ INTERFACE: TRICO]
    def create_container_2(self):
        # [ 1 ] frame_container_global_2            : Contenedor global N° 2, muestra las imagenes base del trico                : POSICIONADO

        #____CONTENEDOR EXTERIOR 2:
        self.frame_container_global_2 = Frame(self)
        self.frame_container_global_2 .grid(column=0, row=0, sticky='news')

        #____Peso de distribucion:
        self.frame_container_global_2 .columnconfigure(0, weight=1)
        self.frame_container_global_2 .rowconfigure   (0, weight=1)


        #________Metodos Llamados:
        self.create_items_2()


    def create_items_2(self):
        # [ 1 ] self.frame_image_delay_trico  : Imagen -->  Base por defecto + delay trico
        # [ 2 ] self.frame_image_delay_raon   : Imagen -->  Base por defecto + delay raon
        # [ 3 ] self.frame_image_1forma       : Imagen -->  Base por defecto + 1 Forma

        #____IMAGENES: ( 4 )
        self.frame_image_delay_trico = ResizeCls(self.frame_container_global_2, self.Images[17][6], bd=0)
        self.frame_image_laser       = ResizeCls(self.frame_container_global_2, self.Images[17][7], bd=0)
        self.frame_image_raon        = ResizeCls(self.frame_container_global_2, self.Images[17][8], bd=0)

        #____Orden de apilamiento de imagenes:
        self.frame_image_delay_trico .lift()

        #____Posicionamiento:
        self.frame_image_delay_trico .pack(fill='both', expand=True)
        #self.frame_image_laser       .grid(column=0, row=0, sticky='news')
        #self.frame_image_raon        .grid(column=0, row=0, sticky='news')

        self.collection2 = [None, self.frame_image_delay_trico, self.frame_image_delay_trico, self.frame_image_delay_trico, self.frame_image_delay_trico, self.frame_image_laser, self.frame_image_raon]

    
    # Tarea: - Cambia el orden de apilamiento de las imagenes en la interface del trico
    def change_image(self, number=None, prenumber=None):
        # [ 1 ] : number        -->  [number]     -->   : Botón presionado
        # [ 2 ] : self._indice  -->  [prenumber]  -->   : Boton anterior

        # Description: Si la imagen por defecto es visible:
        if self.frame_image_delay_trico.winfo_ismapped():
            prenumber = 1

        if number == 1: 
            self.collection2[prenumber] .pack_forget()
            self.collection2[1] .pack(fill='both', expand=True)

        elif number == 2:
            pass

        elif number == 3:
            pass

        elif number == 4:
            self.collection2[prenumber] .pack_forget()
            self.collection2[1] .pack(fill='both', expand=True)

        elif number == 5:
            self.collection2[prenumber] .pack_forget()
            self.collection2[number] .pack(fill='both', expand=True)
        
        elif number == 6:
            if self.master.version == 'activado':
                self.collection2[prenumber] .pack_forget()
                self.collection2[number] .pack(fill='both', expand=True)
            else:
                self.collection2[prenumber] .pack_forget()
                self.collection2[1] .pack(fill='both', expand=True)
            


    # Tarea: - Activar todas las opciones de imagenes que se pueden mostrar       
    def activate_version(self, event=None):
        if not self.master.check_version:
            self.master.check_version = True
            self.master.version = 'activado'
        else:
            self.master.check_version = False
            self.master.version = 'desactivado'

    # Tarea: - [ Soluciona error ] Reactiva el evento motion
    def reactivate_motion(self, event=None):
        print('reactivando motion')
        if self.indice != 17:
            self.off_motion = self.master.bind("<Motion>", self.open_text_mostrar_77)


    #___< B U T T O N - 1 > :
    def open_text_flecha(self, event):

        # Description: Convierte el tamaño total de la ventana en porcentaje:  100 %
        x = event.x / self.master.winfo_width() * 100
        y = event.y / self.master.winfo_height() * 100
      
        if self.x1 <(x)< self.x2  and  self.y1 <(y)< self.y2: 

            if not self._button_1:       # Predeterminado: False
                self._button_1 = True
                self._motion_1 = True
                
                # Description: Posiciona
                self.frame_image_base_77   .grid()
                self.label_text_mostrar_77 .grid_remove()
                self.label_text_flecha     .grid()
            else:
                self._button_1 = False
                self._motion_1 = False

                # Description: Oculta
                self.frame_image_base_77   .grid_remove()
                self.label_text_mostrar_77 .grid()
                self.label_text_flecha     .grid_remove()


    #___< M O T I O N > :
    def open_text_mostrar_77(self, event=None):
        x  = event.x / self.master.winfo_width() * 100
        y = event.y / self.master.winfo_height() * 100

        if self.indice != 17:
            if not self._motion_1:    # Predeterminado: False

                if self.x1 <(x)< self.x2  and  self.y1 <(y)< self.y2:  
                    print('motion if')  
                    self.label_text_mostrar_77 .grid()

                else:
                    print('motion else')  

                    self.label_text_mostrar_77 .grid_remove()

            if self.frame_image_base_77 .grid_info() != {}:   # == {} (no mapeado) 
                self.label_text_mostrar_77     .grid_remove()

 

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
            self.img = ResizeCls (self, self.Images [index_1])
            self.img.grid(column=0, row=0, sticky='news')
        
        if len(path_lst) > index_2:
            self.img2 = ResizeCls (self, self.Images [index_2])
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
    def __init__(self, window=None, windows=None, disabled=None):
        self._x = 0
        self._y = 0
        #---------------------------DESCRIPCION DE TAREAS------------------------------------------------

        # [ 1 ] : Lista de widgets que permiten mover su ventana o sus ventanas
        # [ 2 ] : Lista de widgets que no se les permite mover su ventana o sus ventanas
        # [ 3 ] : Boleano de estado de la ventana principal                                 : Predeterminado: True(Permitir)
        # [ 4 ] : Boleanos de estado de las ventanas secundarias                            : Predeterminado: Trues(Permitir)
            # Indice:
                # Índice 0 : Controla la ventana secundaria izquierda
                # Índice 1 : Controla la ventana secundaria derecha
                # Índice 2 : Controla la ventana secundaria central
        # [ 5 ] : Bloquea el movimiento de su ventana secundaria                            : Predeterminado; Falses(Desactivado)

        self.movable = []
        self.immovable = []
        self._boolean = True
        self._booleans = [True] * 3
        #self._disabled = [False] * 3

        #---------------------------ARGUMENTOS RECIBIDOS-------------------------------------------------

        # [ 1 ] : Ventana principal
        # [ 2 ] : Ventanas secundarias
        # [ 3 ] : 

        self.principal   = window
        self.secundarias = windows      
        self._disabled   = disabled

          
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

        #self._displace = None

        #print('____stop___', self._displace)

    def access_move_all(self, event):
        # [self.movable]   : Lista que permite mover su ventana
        # [self.immovable] : Lista que no permite mover su ventana

        deltax = event.x - self._x
        deltay = event.y - self._y

        self.widget = event.widget
        self.window = event.widget.winfo_toplevel()
        #____Nueva Posición:
        self.new_position = "+{}+{}".format (self.window.winfo_x() + deltax, self.window.winfo_y() + deltay)


        #----------------------------------CONTROLADOR DE MOVIMIENTO----------------------------------------------------

        # Description: Mueve la ventana principal
        if self.window == self.principal and self._boolean:
                self.on_move_all()

        # Description: Mueve la ventana secundaria
        for i in range(3):
            if self.window == self.secundarias[i] and self._booleans[i]:
                if not self._disabled[i]:
                    #self._displace = 'desplazando ventana'
                    self.on_move_all()
                    #print('___access move____', self._displace)
        
        

    def on_move_all(self):
        # Dice: [ Si no es una instancia de... ] and [ No está en la lista (self.immovable) ] or [ Esta en la lista (self.movable) ]
            if not isinstance(self.widget, (Button, ttk.Sizegrip, Spinbox)) == True and not self.is_immovable(self.widget) == True or self.is_movable(self.widget):     #self._is_movable(widget): Devuelve True
                # Descripción: Mueve la ventana a excepción de root
                self.window.geometry(self.new_position)
            #------------------------------------------------------------------------------------------------------------------------------------------

            # Dice: [ Si es una instancia de... ] and [ No es una instancia de... ] or [  Esta en la lista (self.movable) ]
            if isinstance(self.window.master, Tk) == True and not isinstance(self.widget, (Button, ttk.Sizegrip, Spinbox)) == True and not self.is_immovable(self.widget) == True or self.is_movable(self.widget):               
                # Descripción: Mueve root                                        # otro: if _tops.master == RootCls:
                self.window.master.geometry(self.new_position)
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

        #____Eventos:
        # 
        #self.frame_manager .bind("<Map>", self.frame_manager .window_manager_off)


    def create_buttons(self):
        #----------------------------------------------ARGUMENTOS---------------------------------------------------------

        # Description: Posicion de los botones: ( PRINCIPAL )
        close1, minimize1 = {'side':TOP}, {'side':BOTTOM}                 
        # Description: Posicion de los botones: ( SECUNDARIA )
        close2, minimize2 = {'side':RIGHT}, {'side':RIGHT, 'padx':(0,3)}

        #-----------------------------------------------------------------------------------------------------------------

        # Description: Actualiza la geometria de la ventana:
        self.update_idletasks()

        # Description: Solicita el ancho y alto de la ventana:
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
        event.widget.config(image=self.Icons[3], bg='#2b313c')

    def leave_mouse_minimize(self, event):
        # Salida del mouse sobre el boton (Imagen: default)
        event.widget.config(image=self.Icons[1], bg='#1b1d22')


    # Tarea: - Destruye la ventana:
    def close(self):
        self.master.destroy()                                   # Destruye la ventana a excepcion de root

        if isinstance(self.master.master.winfo_toplevel(), Tk):
            self.master.master.destroy()                        # Destruye root
            self.master.quit()                                  # SIGO INVESTIGANDO...
        

    # Tarea: - Oculta la ventana:
    def minimize(self):
        if isinstance(self.master.master.winfo_toplevel(), Tk):
            self.master.withdraw()                              # Oculta la Ventana Principal( Desaparece )
            self.master.master.iconify()                        # Oculta la Ventana Root
        else:
            self.master.update_idletasks()                      # Termina Tareas Pendientes y Actualiza la Aplicacion
            self.master.wm_attributes("-alpha", 0.0 )
            self.master.overrideredirect(False)                 # Muestra el Gestor de Ventanas
            self.master.state('iconic')
            self.master.wm_attributes("-alpha", 1.0 )


    # Tarea: - Muestra la ventana
    def window_manager_off(self, event=None):
        # Evento: Widget visible

        if not isinstance(self.master.master.winfo_toplevel(), Tk):
            self.master.update_idletasks()
            self.master.overrideredirect(True)                  # Oculta el Gestor de Ventanas
            self.master.state('normal')                         # SIGO INVESTIGANDO SI ES NECESARIO...



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

class ToplevelCls(Toplevel, MoveAllCls):
    def __init__(self, master=None, path_lst1=None, path_lst2=None, frames=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        #____Inicializando las variables de control
        MoveAllCls.__init__(self)

        self.overrideredirect(True)

        self.indice = None

        #____Coleccion de Imagenes:
        self.Images  = path_lst1               # Imagenes-Iconos: Menu de opciones
        self.Icons_1 = path_lst2

        #____Variable de Control: 
        self.frames = frames
        self.cascade = False

        #____Variable de Control: Controla las opciones de imagenes que se pueden mostrar
        self.check_version = False
        self.version = None

        #____Variables de Reposo: Coordenadas de la Ventana.
        self._x = 0
        self._y = 0

        #____Enlaces:
        #self.bind('<Map>',self.visibility_on)
        #self.bind('<Unmap>',self.visibility_off)


    def create_frame_manager(self, path_lst, **position):
        # [ 1 ] self.frame_manager  : Frame(contenedor):  Botones: [X] [-]

        #____GESTOR DE VENTANA: ( 1 instancia )
        self.frame_manager = FrameManagerCls(self, path_lst, bg="#1b1d22")
        self.frame_manager .pack(position)

        #____Enlaces: Mueven la ventana
        self.frame_manager .bind("<ButtonPress-1>", self.start_move)
        self.frame_manager .bind("<ButtonRelease-1>", self.stop_move)
        self.frame_manager .bind("<B1-Motion>", self.on_move)
        #____Enlaces: Oculta el gestor de ventanas
        self.frame_manager .bind("<Map>", self.frame_manager .window_manager_off)


    def create_container_icons(self, indice1=None, indice2=None, boolean=None):
        # indice1: 

        #____GESTOR DE ICONOS: ( 1 instancia )
        self.icons_interface = IconsCls(self, self.Images, self.Icons_1, indice1, indice2, self.frames)
        self.icons_interface .pack(fill=BOTH, expand=True)
        self.icons_interface .pack_forget()

        if boolean:
            self.icons_interface.checked()


    def create_label_title(self, **kwargs):
        #____TITULO DE LA VENTANA:
        self.label_title = Label(self.frame_manager, font=('Ghotam',8,'bold'), fg="green2", bg="#1b1d22", bd=0, **kwargs)
        self.label_title .pack(side=BOTTOM, padx=10, pady=0)

        #____Enlaces: Mueven la ventana
        self.label_title .bind("<ButtonPress-1>", self.start_move)
        self.label_title .bind("<ButtonRelease-1>", self.stop_move)
        self.label_title .bind("<B1-Motion>", self.on_move)


    def create_button_menu(self):
        #____BOTONES: ( 1 )
        self.button_menu = Button(self.frame_manager, image=self.Icons_1[0], command=self.open_container_icons, bg="#1b1d22", activebackground='#4ca6ff', bd=0)   
        self.button_menu .pack(side=LEFT)

        #____Enlaces: Cambian la imagen del boton menu
        self.button_menu .bind("<Enter>", self.enter_mouse_menu)
        self.button_menu .bind("<Leave>", self.leave_mouse_menu)
        self.button_menu .bind("<ButtonPress-1>", self.press_mouse_menu)
        self.button_menu .bind("<ButtonRelease-1>", self.release_mouse_menu)
        

    def enter_mouse_menu(self, event):
        # Evento: Entrada del mouse sobre el boton (Imagen: change)
        event.widget .config(image=self.Icons_1[1], bg='#202429')

    def leave_mouse_menu(self, event):
        # Evento: Salida del mouse sobre el boton (Imagen: default)
        event.widget .config(image=self.Icons_1[0], bg='#1b1d22')

    def press_mouse_menu(self, event):
        # Evento: Botón presionado (Imagen: change)
        event.widget .config(image=self.Icons_1[2])

    def release_mouse_menu(self, event):
        # Evento: Botón soltado (Imagen: default)
        event.widget .config(image=self.Icons_1[1], bg='#202429')


    def open_container_icons(self, event=None):
        relation = self.winfo_children()

        # MOSTRAR INTERFACE:
        if not self.cascade:
            self.cascade = True
            # Description (for): Encuentra el frame hijo de la ventana y lo oculta.
            for i in range(len(self.frames)):
                if self.frames[i] in relation:
                    self.frames[i]. pack_forget()

            # Description: Muestra la interface del menu
            self.icons_interface .pack(fill=BOTH, expand=True)

        # OCULTAR INTERFACE:
        else:
            self.cascade = False
            # Description (for): Encuentra el frame hijo de la ventana y lo muestra.
            for i in range(len(self.frames)):
                if self.frames[i] in relation:
                    self.frames[i] .pack(fill=BOTH, expand=True)

            # Description: Oculta la interface del menu
            self.icons_interface .pack_forget()


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
            #print('moveee')
            self.master.geometry(new_position)                    # Mueve la ventana root
        else:
            self.icons_interface.variable = True

    def configure_toplevel(self, title, size):  # Opciones de las Ventanas Secundarias
        self.title (title)
        self.geometry (size)
        self.resizable (1,1)
        self.wm_attributes ('-topmost', True)                     # FUNCIONA BIEN pero molesta para editar 
        self.config (bg = 'magenta2')                            # FUNCIONA BIEN pero tiene mal aspecto
        #self.wm_attributes ('-transparentcolor', 'magenta2')     # FUNCIONA BIEN pero tiene mal aspecto


    """ def visibility_on(self, event=None):
        print(44)
        # Visibilidad del widget:

        #for i in self.master._window
        #print(self.master._windows)

        self.update()
        for i in (self._windows):
            if i is None:
                print(11111)

        widget = event.widget
        if isinstance(widget, Toplevel) and widget.winfo_viewable():
            if not isinstance(self.master.winfo_toplevel(), Tk):
                print('visible')
            

    def visibility_off(self, event=None):
        # Sin visibilidad del widget:

        widget = event.widget
        if isinstance(widget, Toplevel) and not widget.winfo_viewable():
            print('not visible') """


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
        self.ico1_lst, self.ico2_lst, self.ico3_lst, self.ico4_lst = self.generate_list (path, 3)

        #print('eee', len(self.main_lst[22]))

        #____Enlaces para Ocultar y Mostrar la Ventana Principal: ( 1 forma )
        self.bind("<Unmap>", self.iconify_on)    # Activacion: Click en el icono de la barra de tareas
        self.bind("<Map>", self.deiconify_on)    # Activacion: Click en el icono de la barra de tareas

        #____Métodos Llamados:
        self.configure_root()
        self.create_window()


    def configure_root(self):
        #self.resizable(0, 0)                     # Deja un rastro de root en pantalla, no solucionado
        self.geometry('0x0+300+0')                # Tamaño de Root


    def create_window(self):
        # [ 1 ] self.toplevel_principal  : Toplevel: Ventana principal
        # [ 2 ] self.frame_interface     : Frame: Interface de control

        #____VENTANA PRINCIPAL: ( 2 instancias )
        self.toplevel_principal = ToplevelCls(self, path_lst1=self.ico2_lst)
        self.frame_interface    = InterfazCls(self.toplevel_principal, self.main_lst, self.mini_lst, self.ico1_lst, self.ico2_lst, self.ico3_lst, self.ico4_lst)

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
            multilist = [[] for x in range(23)]  # antes 22
            mobiles = ['Fro','Fox','Boo','Ice','JD','Gru','Lig','Adu','Kni','Kal','Mag','Ran','Jol','Tur','Arm','Asa','Rao','Tri','Nak','Big','Bar','Dra',  'Otros'] # antes sin Otros

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
            empty1, empty2, empty3, empty4 = [],[],[],[]
            icons = ['Ico1', 'Ico2', 'Ico3', 'Mobile']

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
                        if icon in 'Mobile':
                            empty4 .append(img) 
            return empty1, empty2, empty3, empty4

    
        

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
    def __init__(self, master=None, main_lst=None, mini_lst=None, ico1_lst=None, ico2_lst=None, ico3_lst=None, ico4_lst=None, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        #MoveAllCls.__init__(self)   # Inicializando las variables de control

        #____Coleccion de Imagenes:
        self.main_lst = main_lst
        self.mini_lst = mini_lst
        self.ico1_lst = ico1_lst
        self.ico2_lst = ico2_lst
        self.ico3_lst = ico3_lst
        self.ico4_lst = ico4_lst

        #____Variables de Control de Tamaño y Posición de Todas las Ventanas:
        self.geo_principal = StringVar()
        self.geo_izq = StringVar()
        self.geo_der = StringVar()
        self.geo_stuf = StringVar()
        
        #____Variables de Control: ( Ventanas Secundarias )
        # [ 1 ] : self._open      : Número de ventanas abiertas o cerradas
        # [ 2 ] : self._windows   : Número de ventanas creadas
        # [ 3 ] : self._frame     : Número de contenedores de los frames

        self._open = [False] * 3
        self._windows = [None] * 3
        self._frame = [None] * 3

        #____Variables de Control: ( Ventanas Secundarias )
        # [ 1 ] : self._disabled  : Número de ventanas bloqueadas              : predeterminado: Falses(Desactivado)

        self._disabled = [False] * 3

        #____Inicializando las variables de control
        MoveAllCls.__init__(self, self.master, self._windows, self._disabled)


        #____Variable de Seguimiento: Boton Seleccionado en la Interface de Botones:
        self.mobil_selected = None

        #____Variables de Control: Boton Secundarias:
        self._gear = False

        #____Variables de Seguimiento del Frame Contenedor de los Iconos en las Ventanas Secundarias:
        self.resize_1 = False

        self.mobiles = ['Frog', 'Fox', 'Boomer', 'Ice', 'J.d', 'Grub', 'Lightning', 'Aduka', 'Knight', 'Kalsiddon', 'Mage',
                        'Randomizer', 'Jolteon', 'Turtle', 'Armor','A.sate', 'Raon', 'Trico', 'Nak', 'Bigfoot', 'Barney', 'Dragon']

        self._deactivate = False


        #____Enlaces: Mueven las Ventanas Globalmente:
        self.bind_all("<ButtonPress-1>", self.start_move_all)             # Punto inicial    
        self.bind_all("<ButtonRelease-1>", self.stop_move_all)            # Punto final
        self.off_move = self.bind_all("<B1-Motion>", self.access_move_all)    # Puntos de movimiento

        #____Enlaces: Marca el Boton que Abrio las Ventanas:
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
        self.frame_botones    = ModeButtonsCls(self, bg='#2b313c', width=756, height=67)               # Posicionado     # Color: Plomo
        self.frame_configurer = ModeConfigurerCls(self, bg='#2b313c', width=756, height=67)            # No posicionado  # Color: Plomo
        self.frame_listmode   = ModeListCls(self, self.mobiles, self.mini_lst)                                       # No posicionado  # Color: Azul y Plomo
         
        #____Posicionamiento:
        self.frame_static .pack(side=LEFT, fill=BOTH)
        self.frame_botones .pack(side=LEFT, fill=BOTH)

        #____Propagación:
        self.frame_static .pack_propagate(False)
        self.frame_botones .pack_propagate(False)


    # Tarea: 1- Gestiona los widgets de la ventana principal
    def configure_app(self):

        # Dice: Si [self._gear] es falso: ( Predeterminado False )
        if not self._gear:
            self._gear = True
            self.master.geometry('834x67')

            # Description: Desactiva el evento y cambia la imagen a default
            self.frame_static .settings_enter_deactivate()

            self.frame_botones .pack_forget()
            self.frame_listmode .pack_forget()

            self.frame_configurer .pack(side=LEFT, fill=BOTH, expand=True)
            self.frame_configurer .focus_set()

        else:
            self._gear = False
            self.frame_configurer .pack_forget()

            # Description: Desactiva en evento y cambia la imagen a light
            self.frame_static .settings_enter_activate()

            # Dice: Si la casilla N°5 está marcada:
            if self.frame_configurer .checkbutton2 .variable.get():
                self.master.geometry('254x67')
                # Description: Posiciona la interface de lista
                self.frame_listmode .pack(side=LEFT, fill=BOTH)
                self.frame_listmode .spinboxx .focus_set()
                self.frame_listmode .spinboxx .delete(0, END)

                # Dice: Si se asignó el nombre de un móvil a la variable de seguimiento:
                if self.mobil_selected is not None:
                    self.frame_listmode .spinboxx .insert(0, self.mobil_selected)


            # Dice: Si la casilla N°5 no está marcada:
            else:
                # Description: Posiciona la interface de botones
                self.frame_listmode .pack_forget()
                self.frame_botones .pack (side=LEFT, fill=BOTH)
                self.frame_botones .focus_set()

    
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

    def create_windows(self, var_1, var_2, var_3, indice_mobil=None):

        #---------------------------------------------ARGUMENTOS------------------------------------------------------------

        #____Lista de argumentos de la funcion: ( 3 instancias(Frames) )
        args = [var_1, var_2, var_3]

        #____Lista de contenedores de los frames:
        container = [None] * 3

        #____Lista de argumentos de los metodos de la ventana:
        title = ['Hoja Izquierda', 'Hoja Derecha', 'Game Stuff']
        text  = ['1', '2', '3']
        size  = [self.geo_izq.get(), self.geo_der.get(), self.geo_stuf.get()]
        

        #----------------------------------------APERTURA DE VENTANAS------------------------------------------------------- 

        for i in range(len(self._open)):
            # Dice: Si la ventana esta cerrada:
            if not self._open[i] == True:

                #____VENTANAS:  ( 3 instancias )         
                window = ToplevelCls (self, self.main_lst, self.ico2_lst, self._frame)
                #____Métodos Llamados:
                window .configure_toplevel(title[i], size[i])
                window .create_frame_manager(self.ico1_lst, side=TOP, fill=BOTH)
                window .create_container_icons(indice_mobil, i)
                window .create_button_menu()
                window .create_label_title(text=text[i])

                #____Eventos:
                # [ 1 ]  :  Actualiza las ventanas cerradas para volver a abrirlas
                # [ 2 ]  :  Oculta la interface de menu y vuelve a mostrar la interface por default cuando el mouse sale de la ventana
                
                window .bind('<Destroy>', lambda event, number=i: self.update_open(number, event))
                self.off_leave1 = window .bind('<Leave>', lambda event, number=i: self.leave_windows(number, event))


                # Description: Desactiva el evento que quita la interface vertical de botones

                # Description: Actualiza la lista de ventanas y booleanos
                self._windows[i] = window
                self._open[i] = True

                # Description: Desactiva el evento que quita la interface vertical de botones
                if self._deactivate:
                    self._windows[i] .unbind('<Leave>', self.off_leave1)


            # Description: Reemplaza los elementos[None] de la lista *container*
            container[i] = args[i] (self._windows[i])

            # Description: Destruye las instancias(frames) de las ventanas abiertas
            if self._frame[i] is not None:
                self._frame[i] .destroy()
                # Description: Recrea la interface al destruirse su contenedor
                self._windows[i] .icons_interface .destroy()
                self._windows[i] .create_container_icons(indice_mobil, i, self._disabled[i])

                self._windows[i] .icons_interface .deactivate_motion()

            self._frame[i] = container[i]
            # Description: Posiciona las instancias(frames) de las ventanas abiertas
            self._frame[i] .pack(fill='both', expand=True)

            """ # Description: Oculta el frame si la interface de iconos es visible.
            if self._windows[i] .icons_interface .winfo_ismapped():pass
                #self._frame[i] .pack_forget() # sin uso """

            # Description: Widget para redimensionar el frame.
            self.grip = ttk.Sizegrip(self._frame[i], style='TSizegrip')
            self.grip .place (relx=1.0, rely=1.0, anchor='center')
            ttk.Style().configure('TSizegrip', bg='black')

        
            #--------------------------------CONFIGURACION DEL LOGOTIPO-------------------------------------------

            #____Eventos:
            # [ 1 ]  :  Actualiza las ventanas cerradas para volver a abrirlas
            # [ 2 ]  :  Oculta la interface de menu y vuelve a mostrar la interface por default
            self._frame[i].bind("<Map>", self.frame_static .map_widget)
            self._windows[i].frame_manager.bind("<Unmap>", self.frame_static .unmap_widget)

            # Description: Cambia la imagen del boton a celeste encendido
            self.frame_static .logotipo_off()
            


        #------------------------------------NOMBRE DEL BOTON PRESIONADO-----------------------------------------------------

        # Descripcion: Reemplaza el indice que recibe la funcion por el nombre del boton presionado en el modo botones o lista.
        for index, name in enumerate(self.mobiles):
            if indice_mobil == index:
                # Descripcion: Almacena el nombre del boton presionado en el modo botones o lista.
                self.mobil_selected = name
                break
    

    # Tarea: - Actualizar las ventanas cerradas para volver a abrirlas
    def update_open(self, number, event=None):
        if isinstance(event.widget, Toplevel):
            # Descripcion: Actualiza la lista de booleanos para volver abrir la ventana.
            self._open[number] = False
            #self._windows[number] .destroy()

            #-----------------------------------------------------------------------------------
            try:
                self.frame_static .map_widget()
            except: pass

            #-----------------------------------------------------------------------------------
            # Dice: Si todas las ventanas secundarias están cerradas:
            if self._open == [False] * 3:
                try:
                    # Descripcion: Quita la seleccion del boton presionado en el modo botones.
                    self.frame_botones .uncheck_selection()
                    # Descripcion: Actualiza el mobil seleccionado
                    self.mobil_selected = None

                    #---------------------------------------------------------------------------
                    # Description: Devuelve la imagen del boton a default 
                    self.frame_static .logotipo_default()
                except: pass


    # Tarea: - Ocultar la interface que abre el menu y volver a mostrar la interface por default.
    def leave_windows(self, number, event=None):

        #print('FOTGET CONTAINER ICONS')
        # Dice: Si el widget que desencadeno el evento es una instancia de Toplevel                   : self._deactivate: predeterminado(False)
        if isinstance(event.widget, Toplevel):
            if not self._deactivate:
                # Dice: Si el widget que desencadeno el evento es la ventana:        
                if event.widget == self._windows[number]:
                    self._windows[number] .cascade = False
                    self._windows[number] .icons_interface .pack_forget()
                    self._frame[number] .pack(fill='both', expand=True)
                    #print('Event.widget toplevel')
        
    
    # Tarea: - Desactiva el evento
    def deactivate_forget_icons(self, event=None):
        self._deactivate = True
        #--------------------------------------------------- DESACTIVAR EVENTO " A " -------------------------------------------------------------------
        # Description: Desactiva el evento que quita la interface vertical de botones
        """ for i in range(len(self._open)):
            if self._windows[i] is not None:
                self._windows[i] .unbind('<Leave>', self.off_leave1)

            else:
                self._deactivate = True """

        #----------------------------------------------------- ACTIVAR EVENTO " B " --------------------------------------------------------------------
        # Description: Activa el evento que quita la interface vertical de botones
        #self.off_leave2 = self._windows[0] .bind('<Leave>', lambda arg:self._windows[0].icons_interface.frame_container_global_1 .pack_forget())

        
    # Tarea: - Activa el evento y cambia la imagen a light
    def activate_forget_icons(self, event=None):
        self._deactivate = False
        #--------------------------------------------------- DESACTIVAR EVENTO " B " -------------------------------------------------------------------
        # Description: Desactiva el evento que quita la inte
        """ for i in range(len(self._open)):
            self._windows[0] .unbind('<Leave>', self.off_leave2) """

        #----------------------------------------------------- ACTIVAR EVENTO " A " --------------------------------------------------------------------
        # Description: Activa el evento que quita la interface vertical de botones
        """ for i in range(len(self._open)):
            self.off_leave1 = self._windows[i] .bind('<Leave>', lambda event, number=i: self.forget_container_icons(number, event))
        """


def main (): #-----------------------------------------------
    if len(sys.argv) > 1:
        folder = sys.argv[1]
    else:
        folder = os.getcwd()


    root = RootCls(folder)
    root .title('AshmanBot')
    #root .wm_attributes("-alpha", 0.0 )
    root .mainloop()

if __name__=="__main__":  #------------------------------
    main()
