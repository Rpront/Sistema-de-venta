from tkinter import *
from os import sys    
#===========================#  Ajuste de ancho y largo de pantalla  #================================#
ventana =Tk()                           # inicializar la variable de Ventana con tkinder incluido
ventana.geometry("720x500")             # Tamaño de la pantalla
ventana.configure(bg='black')           # Color del fondo

        #===========================# Botones #================================#  

btn = Button(ventana,text="Ventas")
btn.pack()
btn1 = Button(ventana,text="Inventario")
btn1.pack()
btn2 = Button(ventana,text="Movimientos")
btn2.pack()
btn3 = Button(ventana,text="Estadisticas")
btn3.pack()


ventana.mainloop()
#===========================#                Menu                   #================================#
print("Inventario")
print("Ventas")
print("Proveedores")
print("Mercancia Faltante")

num = input("Seleccione una opcion: ")





