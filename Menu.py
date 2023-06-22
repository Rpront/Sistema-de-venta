from tkinter import *
from PIL import ImageTk, Image 
#===========================#  Ajuste de ancho y largo de pantalla  #================================#
ventana =Tk()                                       # inicializar la variable de Ventana con tkinder incluido
ventana.geometry("720x500")                         # Tamaño de la pantalla
ventana.configure(bg='black')                       # Color del fondo

        #======================# Imagen del Titulo #===========================#  

img =  PhotoImage(file="Titulo.png")
img = img.subsample(3)
lblImagen = Label(ventana,image=img,border=0,bg="black").place(x=100,y=100)
        #===========================# Botones #================================#  

#===# Definiendo la funcion para animacion #===#
def bttn(x,y,text,bcolor,fcolor,cmd):
    def on_enter(e):
        mybutton['background']=bcolor
        mybutton['foreground']=fcolor
    def on_leave(e):
        mybutton['background']=fcolor
        mybutton['foreground']=bcolor
    

    mybutton=Button(ventana,width=42,height=2,text=text,
                    fg=bcolor,
                    bg=fcolor,
                    border=0,
                    activeforeground=fcolor,
                    activebackground=bcolor,
                    command=cmd,)                 # Salida
    mybutton.bind("<Enter>",on_enter)
    mybutton.bind("<Leave>", on_leave)
    
    mybutton.place(x=x,y=y)

#===# Definiendo la funciones de salida de las opciones #===#
def cmd():
    print("Goku")

def cmd1():
    print("Goku")

def cmd2():
    print("Goku")

def cmd3():
    print("Goku")

#===# Llamada de botones con la funcion anterior #===#


bttn(216,250,"VENTAS","#DFDFDF","black",cmd)                    # Boton de Ventas
bttn(216,290,"INVENTARIO","#DFDFDF","black",cmd1)              # Boton de Inventario
bttn(216,330,"MOVIMIENTOS","#DFDFDF","black",cmd2)             # Boton de Movimientos
bttn(216,370,"ESTADISTICAS","#DFDFDF","black",cmd3)           # Boton de Estadisticas


ventana.mainloop()





