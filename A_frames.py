from Importaciones import *

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
        #self.xx, self.yy = self.
        
        self.image2 = self.image_copy .resize ((self.master .winfo_width(), self.master .winfo_height()))
        
        self.background2 = ImageTk.PhotoImage (self.image2)
        self.img .config (image= self.background2)
        #self.img .image = self.backgroundd



################################                           ################################
################################            EL             ################################ 
################################          INICIO           ################################ 
################################   F R A M E  " F R O G "  ################################  
################################                           ################################


class Frog_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [0] 

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [0][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [0][1], bd=0)  

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

    
class Frog_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [0] 

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [0][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [0][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event):

        winfo_x, winfo_y = self.master.winfo_width(), self.master.winfo_height() 
        event_x, event_y = event.x, event.y
        h = event_x / winfo_x * 100 
        v = event_y / winfo_y * 100
    
        if int(h) >=0 and int(v) >=68 :  
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()
    

class Frog_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [0]
     pass

################################   F R A M E  " F O X "  ################################
################################   F R A M E  " F O X "  ################################


class Fox_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [1]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [1][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [1][1], bd=0)  

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

 
class Fox_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [1]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [1][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [1][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        winfo_x, winfo_y = self.master.winfo_width(), self.master.winfo_height() 
        event_x, event_y = event.x, event.y
        h = event_x / winfo_x * 100 
        v = event_y / winfo_y * 100
    
        if int(h) >=0 and int(v) >=68 :  
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Fox_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [1]
     pass

################################   F R A M E  " B O O M E R "  ################################
################################   F R A M E  " B O O M E R "  ################################ 





class Boomer_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [2]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs) 

        self.bind ('<Configure>', self.a)    # Ver si cambiar a self.master.bind
                
        self.fr_img_delay = Example (self, self.master.Images_1 [2][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [2][1], bd=0)  

        self.lbl_guia = Label (self, text= 'Guia', font=('Calibri',8,'bold'), bg= 'black' , fg= 'white', bd= 0)  
        self.lbl_guia . bind('<Button-1>', self.position_img)   #self.lbl_guia . place(x= 2, y= 48)  

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)


    def position_img(self, event): 

        if self.fr_img_movil .grid_info() == {}:   # Metodo que devuelve un    {...} con toda la info de su ubicacion, contrariamente un {}     
            self.fr_img_movil .grid (column= 0, row= 0)
        else:
            self.fr_img_movil .grid_forget()
    
    def a(self, event):

        var_x = IntVar()  # Aqui lo puedo camvbiar a IntVar para que no  de un cero de mas 23.0 54.0 
        var_y = IntVar()
        width = self.master.winfo_width() / 35
        height = self.master.winfo_height() / 14
        w = int(width)
        h = int(height)
 
        var_x .set(w)    # aqui hay el 10% del ancho total
        getx = var_x .get()

        var_y .set(h)
        gety = var_y .get()       
        
        self.lbl_guia.place(x= getx, y= gety)
                
  
class Boomer_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [2]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.fr_img_base = Example (self, self.master.Images_1 [2][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [2][3], bd=0)  
 
        self.flecha = Label (self, text= '↑', font=('Calibri',30,'bold'), bg=  '#2f3337',fg='green2', width=1, height=1)
        self.alert_77 = Label (self, text= "Haga ' Click ' para mostrar:\nAngulo ' 77 '", font=('Bickham Script Pro',8  ,'bold'), bg=  '#2f3337',fg='white', width=50, height=2)
        
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)


        self.master.bind("<Button-1>", self.button1)      
        self.bind_motion = self.master.bind('<Motion>',self.motion)
        self.bind_leave = self.bind('<Leave>', lambda e: self.alert_77 .grid_forget())

        #______V A R I A B L E S  de  C O N T R O L  para los B I N D
        self.test = 'closed'
        self.motion = StringVar()
        self.motion.set('on')
        

    #_______M E T O D O   < B U T T O N - 1 >
    def button1(self, event): 

        self.pointer_width = event.x / self.master.winfo_width() * 100
        self.pointer_height = event.y / self.master.winfo_height() * 100
        x1, x2 = 0, 100
        y1, y2 = 68, 100  
                
        if x1 < (self.pointer_width) < x2  and  y1 < (self.pointer_height) < y2: 
            if self.test == 'closed':               
                self.fr_img_77 . grid(column=0, row=0)   # == {} (no mapeado)               
                self.test = 'open'
                self.motion.set('of')
                #print('se cambio de --ON-- a --OF-- ')
                
                self.flecha .grid(column=0, row=0, sticky=SE, ipadx=5) # VER SI ACEPTA VARIABLES
                
            else:
                self.fr_img_77 .grid_forget()
                self.test = 'closed'
                self.after(0, lambda e = self.motion: self.motion.set('on'))  ## analizae
                #print('se cambio de --OF-- a --ON-- ')
                
                self.flecha.grid_forget()


    #_______M E T O D O   < M O T I O N >
    def motion(self, event):      
 
        self.pointer_width_2 = event.x / self.master.winfo_width() * 100
        self.pointer_height_2 = event.y / self.master.winfo_height() * 100
        x1, x2 = 0, 100
        y1, y2 = 68, 100
        if self.motion.get()=='on':    
            if x1 < (self.pointer_width_2) < x2  and  y1 < (self.pointer_height_2) < y2:        
                self.alert_77 .grid (column=0, row=0, sticky=N, ipadx=5, ipady=5)
                #print(self.pointer_width_2)

            else:
                self.alert_77 .grid_forget() 
                #print('entre ala sala motion') 

        if self.fr_img_77 . grid_info() != {}:
            self.alert_77 .grid_forget() 

 
class Boomer_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [2]
     pass

################################  F R A M E  " I C E "  ################################
################################  F R A M E  " I C E "  ################################


class Ice_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [3]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [3][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [3][1], bd=0)  

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

  
class Ice_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [3]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [3][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [3][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        winfo_x, winfo_y = self.master.winfo_width(), self.master.winfo_height() 
        event_x, event_y = event.x, event.y
        h = event_x / winfo_x * 100 
        v = event_y / winfo_y * 100
    
        if int(h) >=0 and int(v) >=68 :  
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Ice_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [3]
     pass

################################  F R A M E  " J D "  ################################
################################  F R A M E  " J D "  ################################


class Jd_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [4]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [4][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [4][1], bd=0)  

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

  
class Jd_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [4]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [4][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [4][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        winfo_x, winfo_y = self.master.winfo_width(), self.master.winfo_height() 
        event_x, event_y = event.x, event.y
        h = event_x / winfo_x * 100 
        v = event_y / winfo_y * 100
    
        if int(h) >=0 and int(v) >=68 :  
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Jd_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [4]
     pass


################################  F R A M E  " G R U B "  ################################
################################  F R A M E  " G R U B "  ################################


class Grub_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [5]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [5][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [5][1], bd=0)  

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

  
class Grub_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [5]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [5][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [5][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        winfo_x, winfo_y = self.master.winfo_width(), self.master.winfo_height() 
        event_x, event_y = event.x, event.y
        h = event_x / winfo_x * 100 
        v = event_y / winfo_y * 100
    
        if int(h) >=0 and int(v) >=68 :  
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Grub_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [5]
     pass


################################  F R A M E  " L I G H T "  ################################
################################  F R A M E  " L I G H T "  ################################


class Lightning_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [6]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [6][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [6][1], bd=0)  

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

  
class Lightning_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [6]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [6][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [6][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Lightning_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [6]
     pass


################################  F R A M E  " A D U K A "  ################################
################################  F R A M E  " A D U K A "  ################################


class Aduka_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [7]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [7][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [7][1], bd=0)  

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

  
class Aduka_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [7]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [7][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [7][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Aduka_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [7]
     pass


################################  F R A M E  " K N I G H T "  ################################
################################  F R A M E  " K N I G H T "  ################################


class Knight_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [8]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [8][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [8][1], bd=0)  

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

  
class Knight_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [8]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [8][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [8][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Knight_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [8]
     pass


################################  F R A M E  " C A L Z I D D O N "  ################################
################################  F R A M E  " C A L Z I D D O N "  ################################


class Kalsiddon_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [9]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [9][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [9][1], bd=0)  

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

  
class Kalsiddon_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [9]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [9][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [9][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Kalsiddon_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [9]
     pass


################################  F R A M E  " M A G E "  ################################
################################  F R A M E  " M A G E "  ################################


class Mage_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [10]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [10][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [10][1], bd=0)  

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

  
class Mage_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [10]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [10][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [10][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Mage_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [10]
     pass


################################  F R A M E  " R A N D O M I Z E R "  ################################
################################  F R A M E  " R A N D O M I Z E R "  ################################


class Randomizer_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [11]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [11][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [11][1], bd=0)  

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

  
class Randomizer_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [11]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [11][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [11][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Randomizer_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [11]
     pass


################################  F R A M E  " J O L T E O N "  ################################
################################  F R A M E  " J O L T E O N "  ################################


class Jolteon_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [12]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [12][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [12][1], bd=0)  

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

  
class Jolteon_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [12]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [12][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [12][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Jolteon_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [12]
     pass


################################  F R A M E  " T U R T L E "  ################################
################################  F R A M E  " T U R T L E "  ################################

class Turtle_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [13]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [13][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [13][1], bd=0)  

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

  
class Turtle_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [13]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [13][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [13][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Turtle_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [13]
     pass


################################  F R A M E  " A R M O R "  ################################
################################  F R A M E  " A R M O R "  ################################


class Armor_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [14]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [14][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [14][1], bd=0)  

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

  
class Armor_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [14]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [14][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [14][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Armor_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [14]
     pass


################################  F R A M E  " A S A T E "  ################################
################################  F R A M E  " A S A T E "  ################################


class Asate_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [15]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [15][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [15][1], bd=0)  

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

  
class Asate_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [15]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [15][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [15][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Asate_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [15]
     pass


################################  F R A M E  " R A O N "  ################################
################################  F R A M E  " R A O N "  ################################


class Raon_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [16]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [16][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [16][1], bd=0)  

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

  
class Raon_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [16]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [16][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [16][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Raon_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [16]
     pass


################################  F R A M E  " T R I C O "  ################################
################################  F R A M E  " T R I C O "  ################################


class Trico_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [17]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [17][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [17][1], bd=0)  

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

  
class Trico_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [17]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [17][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [17][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Trico_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [17]
     pass


################################  F R A M E  " N A K "  ################################
################################  F R A M E  " N A K "  ################################


class Nak_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [18]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [18][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [18][1], bd=0)  

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

  
class Nak_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [18]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [18][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [18][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Nak_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [18]
     pass


################################  F R A M E  " B I G "  ################################
################################  F R A M E  " B I G "  ################################


class Bigfoot_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [19]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [19][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [19][1], bd=0)  

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

  
class Bigfoot_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [19]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [19][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [19][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Bigfoot_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [19]
     pass


################################  F R A M E  " D R A G O N '1' "  ################################
################################  F R A M E  " D R A G O N '1' "  ################################


class Barney_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [20]

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [20][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [20][1], bd=0)  

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

  
class Barney_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [20]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [20][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [20][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Barney_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [20]
     pass


################################  F R A M E  " D R A G O N '2' "  ################################
################################  F R A M E  " D R A G O N '2' "  ################################


class Dragon_left_off (Frame):  #------------------------------ IZQUIERDA :  DELAY  /  MEDIR  _____________ SUBINDICE DEL MOVIL = [21] 

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)   

        self.fr_img_delay = Example (self, self.master.Images_1 [21][0], bd=0)
        self.fr_img_delay .grid(column=0,row=0)

        self.fr_img_movil= Example (self, self.master.Images_1 [21][1], bd=0)  

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

  
class Dragon_right (Frame):  #------------------------------- DERECHA :  BASE  /  77  _____________ SUBINDICE DEL MOVIL = [21]

    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master.bind("<Button-1>", self.position_img)
 
        self.fr_img_base = Example (self, self.master.Images_1 [21][2], bd=0)
        self.fr_img_base . grid (column=0, row=0)
        self.fr_img_base . grid_propagate(0)

        self.fr_img_77 = Example (self, self.master.Images_1 [21][3], bd=0)       
 
        self.grid_columnconfigure (0,weight=1)
        self.grid_rowconfigure (0,weight=1)

    def position_img(self, event): 

        width, height = event.x, event.y
    
        if width >=115 :   #  Este evento se llama siempre que X sea mayor de 115
            if self.fr_img_77 . grid_info() == {}:
                self.fr_img_77 . grid(column=0, row=0)                            
            else:
                self.fr_img_77 . grid_forget()


class Dragon_stuf (Frame):  #-------------------------------- REGLA: GAME STUF  _____________ SUBINDICE DEL MOVIL = [21]
     pass


################################            EL             ################################ 
################################            FIN            ################################
################################
################################
################################
################################
################################
################################
################################
################################
################################
################################