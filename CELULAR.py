from A_import import *


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
#_______1- Gestiona la Interface Inamovible: (Logo y Engranaje)

class LogotipoCls(Frame):
    def __init__(self, master, path_lst=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        #____Colección de Imágenes:
        self.Icons = path_lst

        #____Variables de Seguimiento de las Ventanas:
        self._minimize = False

        #____Métodos Llamados:
        self.create_buttons()


    def create_buttons(self):
        # [self.btn_logotipo] : Logo
        # [self.btn_settings] : Engranaje

        #____BOTONES: 2 ( Logotipo - Settings )
        self.btn_logotipo = Button(self, image=self.Icons[0], bg='#11161d', bd=0, activebackground='#11161d',
                                   command=self.minimize_all)
        self.btn_settings = Button(self, image=self.Icons[1], bg='#11161d', bd=0, activebackground='#11161d',
                                   command=self.master.configure_app)
                         
        #____Posicionamiento:
        self.btn_logotipo .grid(column=0, row=0, padx=(6,6))
        self.btn_settings .grid(column=0, row=1)

        #____Eventos:
        self.btn_logotipo .bind('<Double-Button-3>', self.close_all)  # Cierra Toplevel Secundarias
        self.btn_settings .bind('<Enter>', self.enter_mouse_settings)
        self.btn_settings .bind('<Leave>', self.leave_mouse_settings)


    # Tarea: - Destruye todas las ventanas secundarias:
    def close_all(self, event):
        # Evento: Doble clik derecho

        for indice in range(len(self.master._open)):
            # Dice: Si hay alguna ventana abierta.
            if self.master._open[indice] == True:
                self.master._windows[indice] .destroy()

                # Description: Actualiza la lista de ventanas cerradas 
                #self.master._open[indice] = False                         # Desactivado:(razón) El metodo update_window(InterfazCls) lo hace

            
    # Tarea: - Oculta y muestra todas las ventanas secundarias:
    def minimize_all(self):    
        visibility = self.check_visible_windows()

        for i in range(len(self.master._open)):

            # Dice: Si hay alguna ventana abierta:
            if self.master._open[i]:
                
                # OCULTA LAS VENNTANAS:
                if not self._minimize == True and visibility:
                    self._minimize = True if i == 2 else False

                    # Dice: Si alguna ventana esta abierta:
                    if self.master._open[i] == True:
                        self.master._windows[i] .frame_manager .minimize()
                        #self.master.all_minimize[i] = True

                # MUESTRA LAS VENTANAS:
                else:
                    self._minimize = False if i == 2 else True

                    # Dice: Si alguna ventana esta abierta:
                    if self.master._open[i] == True:
                        self.master._windows[i] .frame_manager .window_manager_off()
                        self.update_position(self.master._windows[i])                      # Solucion temporal: Evita que la ventana al minimizar se expanda

   
    def enter_mouse_settings(self, event):
        # Evento: Entrada del mouse sobre el boton (Imagen: change)
        event.widget.config(image=self.Icons[2])

    def leave_mouse_settings(self, event):
        # Evento: Salida del mouse sobre el boton (Imagen: default)
        event.widget.config(image=self.Icons[1])


    # Tarea: - Devuelve verdadero si hay alguna ventana visible.
    def check_visible_windows(self):
        for i in range(len(self.master._open)):
            # Dice: Si hay alguna ventana abierta:
            if self.master._open[i]:
                # Dice: Si hay alguna ventana visible:  
                if self.master._windows[i].winfo_ismapped():
                    return True                                         # Devuelve True y detiene el bucle

    # Tarea: - Actualiza la posicion de la ventana.
    def update_position(self, window):
        x, y = window.winfo_x(), window.winfo_y()                       # Solucion temporal: Evita que la ventana al minimizar se expanda
        window.geometry('+{}+{}'.format(x,y))


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

        #____CONTENEDORES INTERNOS: ( 1 )
        self.frame_1 = Frame (self, bg='#11161d')          # Color(fondo): Azulino
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
                lambda top1: TopIzqCls  (top1, indice, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, self.master.main_lst, self.master.ico2_lst),
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

                btn = DefaultButtonCls (self.frame_1, text=texto, command= self.indices(index2 + number))
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
            event.widget .config(bg="#24364a")                    # Color(fondo): Azul Celeste

       
    def leave_mouse(self, event):
        # Evento: Salida del mouse sobre el boton.
        # Dice: Si el color del boton no es verde:
        if not event.widget .cget('bg') == '#bdfe04':             # Color(fondo): Verde
            event.widget.config(bg='#11161d')                     # Color(fondo): Azulino


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
#********************************                ██████

# Frame contenedor de checkbuttons y labels
class ModeConfigurerCls(Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, kwargs)

        #____Métodos Llamados:
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
                lambda top1: TopIzqCls  (top1, index, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, self.master.main_lst, self.master.ico2_lst),
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




class IconsCls(Frame):
    def __init__(self, master, main_lst=None, path_lst=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        #____Colección de Imágenes:
        self.Images = main_lst
        self.Icons = path_lst

        #____Metodos Llamados:
        self.create_containers()


        master.bind('<Motion>',self.open1)



        self.grip = ttk.Sizegrip(self, style='TSizegrip')
        self.grip .place (relx=1.0, rely=1.0, anchor='center')
        ttk.Style().configure('TSizegrip', bg='black')

    
    def create_containers(self):
        #____CONTENEDORES PRINCIPALES: ( 2 )
        self.container1 = Frame(self, bg="#1b1d22",)
        self.container1 .pack(side='left', fill='y', expand=False)

        self.container2 = Frame(self, bg='#2b313c')
        self.container2 .pack(side='right', fill='both', expand=True)

        #____Ocultando:
        self.container1 .pack_forget()
        #____Enlaces:

        #________Metodos Llamados:
        self.create_icons()
        self.create_logotipo()



    def create_icons(self):
        #____ICONOS: ( 4 )
        self.button_icon1 = Button(self.container1, image=self.Icons[4], command=self.open, bg='black',  bd=0)
        self.button_icon2 = Button(self.container1, image=self.Icons[4], command=self.open, bg='black',  bd=0)
        self.button_icon3 = Button(self.container1, image=self.Icons[4], command=self.open, bg='black',  bd=0)
        self.button_icon4 = Button(self.container1, image=self.Icons[4], command=self.open, bg='black',  bd=0)

        #____Posicionamiento:
        self.button_icon1 .grid(column=0, row=0, padx=5, pady=5) # sticky='ew', para que el color de relleno del label ocupe todo
        self.button_icon2 .grid(column=0, row=1, padx=5, pady=5)
        self.button_icon3 .grid(column=0, row=2, padx=5, pady=5)
        self.button_icon4 .grid(column=0, row=3, padx=5, pady=5)


        #____Enlaces:
        self.button_icon1 .bind()
    
    def create_logotipo(self):
        #____LOGOTIPO CENTRAL:
        pass
        #self.label_icon1 = Label(self.container2, image=self.Icons[3], bg='black', cursor="hand2", bd=0)
        #self.label_icon1 .place(relx=.5, rely=.5, anchor="center")
    

    def open(self):
        pass
        #self.label_icon1 .place_forget()
        self.frame_image_mobil_tutorial = ResizeCls(self.container2, self.Images[0][1], bd=0)
        self.frame_image_mobil_tutorial       .pack(side='right', expand=True)



    def open1(self, event=None):

        x = self.master.winfo_pointerx() - self.master.winfo_rootx()
        print(x) 
        
        if 0 <= (x) < 37:
            self.container1 .pack(side='left', fill='y', expand=False)

        else:
            self.container1 .pack_forget()
  
  

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
    def __init__(self, master, indice, arg_0=None, arg_1=None, arg_2=None, arg_3=None, arg_4=None, arg_5=None, arg_6=None, arg_7=None, main_lst=None, icon_lst=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        #____Colección de Imágenes:
        self.Images = main_lst
        self.Icons = icon_lst

        #____Variables de Control: Indice de la sublista.
        self.indice = indice

        #____Lista de imagenes:
        self._0 = arg_0
        self._1 = arg_1
        self._2 = arg_2
        self._3 = arg_3
        self._4 = arg_4
        self._5 = arg_5
        self._6 = arg_6
        self._7 = arg_7

        #____Metodos Llamados:
        self.create_instances()
        #self.create_frame_container()



        #--------------------------------------------------------------------------------------------

        # Variables de Control y Seguimiento:
        self._motion_1 = False

        self.x1 = 0
        self.x2 = 100
        self.y1 = 0
        self.y2 = 7

        # INTERFACE DE CONTROL: Para cambiar las imagenes

        

        # Enlaces: 
        #self.master.bind('<Motion>',self.open_frame_container_icons)
        #self.bind('<Leave>', self.remove_frame_container_icons)


        # Configuracion de columnas y filas de la clase :
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)

        # Configuracion principal :
        """ self.frame_image_delay_complete .columnconfigure(0, weight=1)
        self.frame_image_delay_complete .rowconfigure(0, weight=1) """



    # Tarea: - Crea las imagenes 
    def create_instances(self):

        # Imagen: Delay completo del mobil
        self.frame_image_delay_complete = ResizeCls(self, self.Images[self.indice][self._0], bd=0)
        self.frame_image_delay_complete       .grid(column=0, row=1, sticky='news')

        # Imagen: Miniatura del mobil para ayudar a medir las distancias
        self.frame_image_mobil_tutorial = ResizeCls(self, self.Images[self.indice][self._1], bd=0)
        self.frame_image_mobil_tutorial       .grid(column=0, row=1, sticky='news')

        #self.frame_image_mobil_tutorial .grid_remove()



    """ def create_frame_container(self):

        self.frame_container_icons = Cls(self, self.Icons )
        self.frame_container_icons .grid(column=0, row=1, sticky='nsw') """



    # Tarea: Abrir la minuatura del mobil:  [ B U T T O N - 1 ]
    def open_image_miniature(self, event): 

        if self.frame_image_mobil_tutorial .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.frame_image_mobil_tutorial .grid()
        else:
            self.frame_image_mobil_tutorial .grid_remove()



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

        #____Colección de Imágenes:
        self.Images = main_lst

        # Variables de Control para mostrar la imagen del angulo 77:
        self.x1 = 0
        self.x2 = 100
        self.y1 = 67
        self.y2 = 100

        # Imagen: Base inicial del mobil:
        self.frame_image_base_initial = ResizeCls (self, self.Images [indice][arg_2], bd=0)
        self.frame_image_base_initial       .grid (column=0, row=0, sticky='news')
        self.frame_image_base_initial       .grid_propagate(0)

        # Imagen: Base 77 del mobil:
        self.frame_image_base_77      = ResizeCls (self, self.Images [indice][arg_3], bd=0)
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
        self.master.destroy()                        # Destruye la ventana a excepcion de root

        if isinstance(self.master.master.winfo_toplevel(), Tk):
            self.master.master.destroy()             # Destruye root
            self.master.quit()                       # SIGO INVESTIGANDO...
        

    # Tarea: - Oculta la ventana:
    def minimize(self):
        if isinstance(self.master.master.winfo_toplevel(), Tk):
            self.master.withdraw()                   # Oculta la Ventana Principal( Desaparece )
            self.master.master.iconify()             # Oculta la Ventana Root
        else:
            self.master.update_idletasks()               # Termina Tareas Pendientes y Actualiza la Aplicacion
            self.master.wm_attributes("-alpha", 0.0 )
            self.master.overrideredirect(False)          # Muestra el Gestor de Ventanas
            self.master.state('iconic')
            self.master.wm_attributes("-alpha", 1.0 )


    # Tarea: - Muestra la ventana
    def window_manager_off(self, event=None):
        # Evento: Widget visible

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
    def __init__(self, master=None, frames=None, main_lst=None, path_lst=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.overrideredirect(True)

        #____Coleccion de Imagenes:
        self.Images = main_lst
        self.Icons = path_lst               # Imagenes-Iconos: Menu de opciones

        #____Variable de Control: 
        self.frames = frames
        self.cascade = False

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
        self.frame_manager .bind("<Map>",self.frame_manager .window_manager_off)


    def create_container_icons(self):
        #____GESTOR DE ICONOS: ( 1 instancia )
        self.container_icons = IconsCls(self, self.Images, self.Icons)
        self.container_icons .pack(fill=BOTH, expand=True)
        self.container_icons .pack_forget()


    def create_label_title(self, **kwargs):
        #____TITULO DE LA VENTANA:
        self.label_title = Label(self.frame_manager, font=('Ghotam',8,'bold'), fg="white", bg="#1b1d22", bd=0, **kwargs)
        self.label_title .pack(side=LEFT, padx=10, pady=0)

        #____Enlaces: Mueven la ventana
        self.label_title .bind("<ButtonPress-1>", self.start_move)
        self.label_title .bind("<ButtonRelease-1>", self.stop_move)
        self.label_title .bind("<B1-Motion>", self.on_move)


    def create_button_menu(self):
        #____BOTONES: ( 1 )
        self.button_menu = Button(self.frame_manager, image=self.Icons[0], command=self.open_container_icons, bg="#1b1d22", activebackground='#4ca6ff', bd=0)   
        self.button_menu .pack(side=LEFT)

        #____Enlaces: Cambian la imagen del boton menu
        self.button_menu .bind("<Enter>", self.enter_mouse_menu)
        self.button_menu .bind("<Leave>", self.leave_mouse_menu)
        self.button_menu .bind("<ButtonPress-1>", self.press_mouse_menu)
        self.button_menu .bind("<ButtonRelease-1>", self.release_mouse_menu)
        

    def enter_mouse_menu(self, event):
        # Evento: Entrada del mouse sobre el boton (Imagen: change)
        event.widget .config(image=self.Icons[1], bg='#252b34')

    def leave_mouse_menu(self, event):
        # Evento: Salida del mouse sobre el boton (Imagen: default)
        event.widget .config(image=self.Icons[0], bg='#1b1d22')

    def press_mouse_menu(self, event):
        # Evento: Botón presionado (Imagen: change)
        event.widget .config(image=self.Icons[2])

    def release_mouse_menu(self, event):
        # Evento: Botón soltado (Imagen: default)
        event.widget .config(image=self.Icons[1], bg='#252b34')


    def open_container_icons(self, event=None):
        relation = self.winfo_children()

        # MOSTRAR INTERFACE:
        if not self.cascade:
            self.cascade = True
            # Description (for): Encuentra el frame hijo de la ventana y lo oculta.
            for i in range(len(self.frames)):
                if self.frames[i] in relation:
                    self.frames[i]. pack_forget()

            self.container_icons .pack(fill=BOTH, expand=True)
            #self.container_icons .bind('<Leave>', self.forget_container_icons)
            

        # OCULTAR INTERFACE:
        else:
            self.cascade = False
            # Description (for): Encuentra el frame hijo de la ventana y lo muestra.
            for i in range(len(self.frames)):
                if self.frames[i] in relation:
                    self.frames[i] .pack(fill=BOTH, expand=True)

            self.container_icons .pack_forget()


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
        self.ico1_lst, self.ico2_lst, self.ico3_lst = self.generate_list (path, 3)

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
        
        #____Variables de Control: ( Ventanas Secundarias )
        # [ 1 ] : self._open     : Número de ventanas abiertas o cerradas
        # [ 2 ] : self._windows  : Número de ventanas creadas
        # [ 3 ] : self._frame    : Número de contenedores de los frames

        self._open = [False] * 3
        self._windows = [None] * 3
        self._frame = [None] * 3

        #____Variable de Seguimiento: Boton Seleccionado en la Interface de Botones:
        self.mobil_selected = None

        #____Variables de Control: Boton  Secundarias:
        self._gear = False

        #____Variables de Seguimiento del Frame Contenedor de los Iconos en las Ventanas Secundarias:
        self.resize_1 = False

        self.mobiles = ['Frog', 'Fox', 'Boomer', 'Ice', 'J.d', 'Grub', 'Lightning', 'Aduka', 'Knight', 'Kalsiddon', 'Mage',
                        'Randomizer', 'Jolteon', 'Turtle', 'Armor','A.sate', 'Raon', 'Trico', 'Nak', 'Bigfoot', 'Barney', 'Dragon']

        #____Enlaces: Mueven las Ventanas Globalmente:
        self.bind_all("<ButtonPress-1>", self.start_move_all)             # Punto inicial    
        self.bind_all("<ButtonRelease-1>", self.stop_move_all)            # Punto final
        self.off_move = self.bind_all("<B1-Motion>", self.on_move_all)    # Puntos de movimiento

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
        self.frame_botones    = ModeButtonsCls(self, bg='#31343a', width=756, height=67)               # Posicionado     # Color: Plomo
        self.frame_configurer = ModeConfigurerCls(self, bg='#31343a', width=756, height=67)            # No posicionado  # Color: Plomo
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

    def create_windows(self, var_1, var_2, var_3, mobil=None):

        #____Lista de argumentos de la funcion: ( 3 instancias(Frame) )
        args = [var_1, var_2, var_3]

        #____Lista de contenedores de los frames:
        container = [None] * 3

        #____Lista de argumentos de los metodos de la ventana:
        title = ['Hoja Izquierda', 'Hoja Derecha', 'Game Stuff']
        text  = ['AshmanBot:  1', 'AshmanBot:  2', 'AshmanBot:  3']
        size  = [self.geo_izq.get(), self.geo_der.get(), self.geo_stuf.get()]
        

    #----------------------------------------APERTURA DE VENTANAS------------------------------------------------------- 

        for i in range(len(self._open)):
            # Dice: Si la ventana esta cerrada:
            if not self._open[i] == True:

                #____VENTANAS:  ( 3 instancias )         
                window = ToplevelCls (self.master, self._frame, self.main_lst, self.ico2_lst)
                #____Métodos Llamados:
                window .configure_toplevel(title[i], size[i])
                window .create_frame_manager(self.ico1_lst, side=TOP, fill=BOTH)
                window .create_container_icons()
                window .create_button_menu()
                window .create_label_title(text=text[i])

                #____Enlace: Actualiza la lista (self._open):
                window .bind('<Destroy>', lambda event, number=i: self.update_open(number, event))
                window .bind('<Leave>', lambda event, number=i: self.forget_container_icons(number, event))

                # Description: Actualiza la lista de ventanas y booleanos
                self._windows[i] = window
                self._open[i] = True


            # Description: Reemplaza los elementos de la lista (container)
            container[i] = args[i] (self._windows[i])

            if self._frame[i] is not None:
                self._frame[i] .destroy()
            self._frame[i] = container[i]
            self._frame[i] .pack(fill='both', expand=True)
            # Description: Oculta el frame si la interface de iconos es visible.
            if self._windows[i].container_icons .winfo_ismapped():
                self._frame[i] .pack_forget()


            # Description: Widget para redimensionar el frame.
            self.grip = ttk.Sizegrip(self._frame[i], style='TSizegrip')
            self.grip .place (relx=1.0, rely=1.0, anchor='center')
            ttk.Style().configure('TSizegrip', bg='black')


    #-----------------------------------------------------------------------------------------------------------------

        # Descripcion: Reemplaza el indice que recibe la funcion por el nombre del boton presionado en el modo botones o lista.
        for index, name in enumerate(self.mobiles):
            if mobil == index:
                # Descripcion: Almacena el nombre del boton presionado en el modo botones o lista.
                self.mobil_selected = name
                break
        

    # Tarea: - Actualizar las ventanas cerradas
    def update_open(self, number, event=None):

        if isinstance(event.widget, Toplevel):
            # Descripcion: Actualiza la lista de booleanos para volver abrir la ventana.
            self._open[number] = False
            #self._windows[number] .destroy()

            # Dice: Si todas las ventanas secundarias están cerradas:
            if self._open == [False] * 3:
                try:
                    # Descripcion: Quita la seleccion del boton presionado en el modo botones.
                    self.frame_botones .uncheck_selection()
                    # Descripcion: Actualiza el mobil seleccionado
                    self.mobil_selected = None
                except: pass


    # Tarea: - Ocultar la interface de iconos y mostrar la interface visual.
    def forget_container_icons(self, number, event=None):
        # Dice: Si el widget que desencadeno el evento es la ventana:
        if event.widget == self._windows[number]:
            self._windows[number] .cascade = False
            self._windows[number] .container_icons .pack_forget()
            self._frame[number] .pack(fill='both', expand=True)






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
